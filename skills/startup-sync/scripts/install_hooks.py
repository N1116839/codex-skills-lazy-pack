#!/usr/bin/env python3
"""Install/remove only this workflow's optional Codex hooks. Never grants trust."""
import argparse
import datetime
import json
from pathlib import Path
import shlex
import subprocess
import sys
from project_workflow import atomic_json, read

TAG = 'Project workflow v1'


def merge(config, command, windows_command, uninstall=False):
    updated = json.loads(json.dumps(config))
    events = updated.setdefault('hooks', {})
    for event in ('SessionStart', 'UserPromptSubmit', 'Stop'):
        groups = []
        for group in events.get(event, []):
            group = dict(group)
            group['hooks'] = [item for item in group.get('hooks', []) if item.get('statusMessage') != TAG]
            if group['hooks']:
                groups.append(group)
        if not uninstall:
            handler = {'type': 'command', 'command': command, 'commandWindows': windows_command,
                       'statusMessage': TAG, 'timeout': 5}
            if event != 'Stop':
                handler['additionalContextLimit'] = 20000
            group = {'hooks': [handler]}
            if event == 'SessionStart':
                group['matcher'] = '^(startup|resume|clear|compact|fork)$'
            groups.append(group)
        if groups:
            events[event] = groups
        else:
            events.pop(event, None)
    return updated


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--codex-home', type=Path, default=Path.home() / '.codex')
    p.add_argument('--python', default=sys.executable)
    p.add_argument('--dry-run', action='store_true')
    p.add_argument('--uninstall', action='store_true')
    args = p.parse_args()
    path = args.codex_home / 'hooks.json'
    script = Path(__file__).resolve().with_name('project_workflow.py')
    argv = [args.python, str(script), 'hook']
    previous = json.loads(read(path)) if path.exists() else {}
    new = merge(previous, shlex.join(argv), subprocess.list2cmdline(argv), args.uninstall)
    changed = previous != new
    backup = None
    if changed and not args.dry_run:
        if path.exists():
            backup = args.codex_home / 'backups' / ('codex_hooks_' + datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f') + '.json')
            backup.parent.mkdir(parents=True, exist_ok=True)
            backup.write_bytes(path.read_bytes())
        atomic_json(path, new)
        if json.loads(read(path)) != new:
            raise RuntimeError('Hook read-back mismatch.')
    print(json.dumps({'changed': changed, 'written': changed and not args.dry_run, 'path': str(path),
                      'backup': str(backup) if backup else None, 'trust': 'Human review required in Codex CLI /hooks; not granted by this installer.'}, ensure_ascii=False))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
