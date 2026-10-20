#!/usr/bin/env python3
"""Opt-in project continuity, bounded hook context, and review receipts. No network."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
import time

MANIFEST = '.project-workflow.json'
START = '<!-- workflow:current:start -->'
END = '<!-- workflow:current:end -->'
VERSION = '1.0.0'


class WorkflowError(Exception):
    pass


def digest(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()


def read(path):
    try:
        return Path(path).read_text(encoding='utf-8-sig')
    except (OSError, UnicodeError) as exc:
        raise WorkflowError(f'Cannot read {path}: {exc}') from exc


def atomic_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix='codex_workflow_', suffix='_暫存', dir=path.parent)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as stream:
            json.dump(value, stream, ensure_ascii=False, indent=2)
            stream.write('\n')
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)  # Only the exact temp file created above.


def discover(cwd):
    current = Path(cwd).resolve()
    if current.is_file():
        current = current.parent
    for directory in (current, *current.parents):
        candidate = directory / MANIFEST
        if candidate.is_file():
            return candidate
        if (directory / '.git').exists():
            break
    return None


def resolve_path(spec, manifest, cfg):
    if not isinstance(spec, str) or not spec:
        raise WorkflowError('Source path must be a nonempty string.')
    if spec.startswith('${vault}/'):
        vault = os.environ.get('PROJECT_WORKFLOW_VAULT') or cfg.get('vault_root')
        if not vault:
            raise WorkflowError('vault_root or PROJECT_WORKFLOW_VAULT is required.')
        root = Path(vault).resolve()
        path = (root / spec[len('${vault}/'):]).resolve()
        if not path.is_relative_to(root):
            raise WorkflowError('Vault source escapes its root.')
        return path
    path = Path(spec)
    return path.resolve() if path.is_absolute() else (manifest.parent / path).resolve()


def section(path, start, end):
    content = read(path)
    if not start or not end or start == end:
        raise WorkflowError(f'Invalid section markers: {path}')
    if content.count(start) != 1 or content.count(end) != 1:
        raise WorkflowError(f'Section markers must each occur exactly once: {path}')
    begin, finish = content.index(start) + len(start), content.index(end)
    if finish <= begin:
        raise WorkflowError(f'Reversed or empty section: {path}')
    result = content[begin:finish].strip()
    if not result:
        raise WorkflowError(f'Empty current section: {path}')
    return result


def snapshot(manifest):
    raw = read(manifest)
    cfg = json.loads(raw)
    if not isinstance(cfg, dict):
        raise WorkflowError('Manifest must be a JSON object.')
    if cfg.get('schema_version') != 1 or not isinstance(cfg.get('project_id'), str) or not cfg['project_id']:
        raise WorkflowError('Manifest requires schema_version=1 and project_id.')
    if not isinstance(cfg.get('state'), dict) or not isinstance(cfg.get('required', []), list):
        raise WorkflowError('state must be an object; required must be an array.')
    for item in cfg.get('required', []):
        if not isinstance(item, dict) or not isinstance(item.get('id'), str) or not item['id']:
            raise WorkflowError('Each required source needs a nonempty string id.')
    sources = [('current', cfg['state'])]
    sources.extend((item['id'], item) for item in cfg.get('required', []))
    ids = [item[0] for item in sources]
    if len(ids) != len(set(ids)):
        raise WorkflowError('Duplicate source id.')
    sections, hashes = [], []
    for name, spec in sources:
        path = resolve_path(spec['path'], manifest, cfg)
        value = section(path, spec.get('start', START), spec.get('end', END))
        sha = digest(value)
        sections.append(f'[{name}] {path}\n{value}')
        hashes.append({'id': name, 'path': str(path), 'sha256': sha})
    text = '\n\n'.join(sections)
    if not isinstance(cfg.get('limits', {}), dict):
        raise WorkflowError('limits must be an object.')
    limit = cfg.get('limits', {}).get('max_chars', 12000)
    if not isinstance(limit, int) or not 100 <= limit <= 50000:
        raise WorkflowError('max_chars must be 100..50000.')
    if len(text) > limit:
        raise WorkflowError(f'Current context has {len(text)} characters, limit {limit}; consolidate, do not truncate.')
    signature = digest(json.dumps({'manifest': digest(raw), 'sources': hashes}, sort_keys=True, ensure_ascii=False))
    return {'project_id': cfg['project_id'], 'manifest': str(manifest), 'state_hash': hashes[0]['sha256'],
            'context_hash': signature, 'sources': hashes, 'text': text}


def cache_file(manifest, session, turn):
    if not session or not turn:
        raise WorkflowError('Session and turn identifiers are required.')
    root = Path(os.environ.get('PROJECT_WORKFLOW_CACHE_DIR') or (Path(tempfile.gettempdir()) / 'codex_workflow_cache_暫存'))
    return root / digest(str(manifest.resolve()))[:24] / digest(session)[:24] / (digest(turn) + '.json')


def load_cache(path):
    value = json.loads(read(path)) if path.exists() else {}
    if not isinstance(value, dict):
        raise WorkflowError('Review cache must be an object; restore from authoritative sources.')
    return value


def register(snap, session, turn, event):
    path = cache_file(Path(snap['manifest']), session, turn)
    previous = load_cache(path)
    if previous.get('context_hash') != snap['context_hash']:
        previous.pop('receipt', None)
    previous.update({'session': session, 'turn': turn, 'context_hash': snap['context_hash'],
                     'state_hash': snap['state_hash'], 'event': event, 'loaded_at': time.time()})
    atomic_json(path, previous)
    return previous


def checkpoint(snap, session, turn, expected, result, reason):
    path = cache_file(Path(snap['manifest']), session, turn)
    cached = load_cache(path)
    if expected != snap['state_hash'] or cached.get('context_hash') != snap['context_hash']:
        raise WorkflowError('State/source changed or was not loaded for this turn. Run context with the same session/turn, review, then checkpoint.')
    if not reason.strip():
        raise WorkflowError('A concrete review reason is required; receipt does not prove understanding.')
    cached['receipt'] = {'result': result, 'reason': reason.strip(), 'context_hash': snap['context_hash'], 'time': time.time()}
    atomic_json(path, cached)
    return {'ok': True, 'state_hash': snap['state_hash'], 'context_hash': snap['context_hash'], 'receipt': str(path)}


def context_text(snap, session=None, turn=None):
    prefix = ('Project continuity: saved context, not a new user request. Current user instructions may update it. '
              'Do not execute historical next steps. On a decision/correction, update the single current section; '
              'before delivery check scope, baseline, evidence, and actual output.\n')
    command = ''
    if session and turn:
        command = (f'\nSession={json.dumps(session)}, turn={json.dumps(turn)}. After reviewing/updating, run '
                   f'project_workflow.py context --project <project> --session <session> --turn <turn>, then '
                   f'checkpoint --project <project> --session <session> --turn <turn> '
                   f'--expected-state-hash <current state_hash> --result updated|unchanged --reason <specific check>. '
                   f'Use the installed startup-sync/scripts/project_workflow.py. A receipt is not a content-quality certificate.\n')
    return prefix + f'project_id={snap["project_id"]}; state_hash={snap["state_hash"]}; context_hash={snap["context_hash"]}\n' + snap['text'] + command


def hook(payload):
    if not isinstance(payload, dict):
        raise WorkflowError('Hook input must be a JSON object.')
    manifest = discover(payload.get('cwd') or os.getcwd())
    if manifest is None or payload.get('agent_id'):
        return {}
    event = payload.get('hook_event_name', '')
    if event not in ('SessionStart', 'UserPromptSubmit', 'Stop'):
        return {}
    session = str(payload.get('session_id') or '')
    # A missing turn id is explicitly unbound; never invent a supposedly real turn.
    turn = str(payload.get('turn_id') or '')
    snap = snapshot(manifest)
    if event in ('SessionStart', 'UserPromptSubmit'):
        if session and turn:
            register(snap, session, turn, event)
        extra = context_text(snap, session if turn else None, turn or None)
        if not turn:
            extra += '\nNo turn_id supplied by this host; automatic receipt enforcement for this event is unavailable. Still review before delivery.'
        return {'hookSpecificOutput': {'hookEventName': event, 'additionalContext': extra}}
    if not session or not turn:
        return {'systemMessage': 'Project workflow: host omitted session/turn id; review receipt cannot be verified.'}
    path = cache_file(manifest, session, turn)
    cached = load_cache(path)
    if cached.get('receipt', {}).get('context_hash') == snap['context_hash']:
        return {}
    if payload.get('stop_hook_active') or cached.get('stop_requested'):
        return {'systemMessage': 'Project workflow review remains unverified after one reminder; do not claim automatic validation passed.'}
    cached['stop_requested'] = True
    atomic_json(path, cached)
    return {'decision': 'block', 'reason': 'Before completing this turn, restore the current project context, persist any new decisions, and record a review checkpoint. Do not repeat the whole history.\n' + context_text(snap, session, turn)}


def ledger_report(data):
    """Validate unique incidents and compute project/global totals; never infer incidents."""
    if not isinstance(data, dict) or not isinstance(data.get('events'), list):
        raise WorkflowError('Ledger requires an events array.')
    events = data.get('events', [])
    by_id, totals, pending = {}, {}, []
    for event in events:
        if not isinstance(event, dict):
            raise WorkflowError('Ledger events must be objects.')
        for key in ('id', 'project_id', 'rule_id', 'status', 'evidence'):
            if not event.get(key):
                raise WorkflowError(f'Event missing {key}.')
        if event['id'] in by_id:
            raise WorkflowError(f'Duplicate event ID: {event["id"]}')
        by_id[event['id']] = event
        if event['status'] == 'pending':
            pending.append(event['id'])
        elif event['status'] == 'confirmed':
            count = event.get('count', 1)
            if not isinstance(count, int) or isinstance(count, bool) or count < 1:
                raise WorkflowError('Invalid event count.')
            if count != 1 and not event.get('legacy_aggregate'):
                raise WorkflowError('Only evidence-backed legacy aggregates may have count > 1.')
            key = (event['project_id'], event['rule_id'])
            totals[key] = totals.get(key, 0) + count
        elif event['status'] != 'clarification':
            raise WorkflowError('Unknown event status.')
    for event in events:
        if event['status'] == 'clarification':
            target = by_id.get(event.get('clarifies'))
            if not target or target['status'] != 'confirmed' or (target['project_id'], target['rule_id']) != (event['project_id'], event['rule_id']):
                raise WorkflowError('Clarification must refer to a confirmed event with the same project/root cause.')
    return {'rules': [{'project_id': p, 'rule_id': r, 'count': n,
                       'level': 'global' if n >= 5 else 'project-important' if n >= 3 else 'project'}
                      for (p, r), n in sorted(totals.items())], 'pending': pending}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    for name in ('context', 'validate', 'checkpoint'):
        item = sub.add_parser(name)
        item.add_argument('--project', required=True)
        item.add_argument('--session')
        item.add_argument('--turn')
        if name == 'checkpoint':
            item.add_argument('--expected-state-hash', required=True)
            item.add_argument('--result', choices=['updated', 'unchanged'], required=True)
            item.add_argument('--reason', required=True)
    sub.add_parser('hook')
    item = sub.add_parser('ledger')
    item.add_argument('path')
    args = parser.parse_args()
    payload = None
    try:
        if args.command == 'hook':
            payload = json.load(sys.stdin)
            result = hook(payload)
        elif args.command == 'ledger':
            result = ledger_report(json.loads(read(args.path)))
        else:
            manifest = discover(args.project)
            if manifest is None:
                raise WorkflowError('No opted-in project manifest found.')
            snap = snapshot(manifest)
            if args.command == 'checkpoint':
                result = checkpoint(snap, args.session, args.turn, args.expected_state_hash, args.result, args.reason)
            else:
                if bool(args.session) != bool(args.turn):
                    raise WorkflowError('Supply both --session and --turn, or neither.')
                if args.session:
                    register(snap, args.session, args.turn, 'manual-context')
                result = snap if args.command == 'context' else {k: v for k, v in snap.items() if k != 'text'}
        print(json.dumps(result, ensure_ascii=False))
        return 0
    except (WorkflowError, KeyError, ValueError, TypeError, OSError) as exc:
        if args.command == 'hook':
            # Keep a repair turn possible: a broken manifest must not lock the user out.
            message = ('Project continuity failed; saved state was NOT loaded: ' + str(exc) +
                       '. Repair or read the authoritative sources before dependent work; do not claim validation passed.')
            result = {'systemMessage': message}
            event = payload.get('hook_event_name') if isinstance(payload, dict) else None
            if event in ('SessionStart', 'UserPromptSubmit'):
                result['hookSpecificOutput'] = {'hookEventName': event, 'additionalContext': message}
            print(json.dumps(result, ensure_ascii=False))
        else:
            print(json.dumps({'error': str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 0 if args.command == 'hook' else 1


if __name__ == '__main__':
    for stream in (sys.stdin, sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(encoding='utf-8')
    raise SystemExit(main())
