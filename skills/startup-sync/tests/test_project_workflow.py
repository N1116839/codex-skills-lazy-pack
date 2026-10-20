import json
import os
from pathlib import Path
import sys
import subprocess
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import project_workflow as w
import install_hooks as install


class ContinuityTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='codex_workflow_', suffix='_暫存')
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / '中文專案'
        self.root.mkdir()
        self.cache = Path(self.tmp.name) / 'cache_暫存'
        self.previous = os.environ.get('PROJECT_WORKFLOW_CACHE_DIR')
        os.environ['PROJECT_WORKFLOW_CACHE_DIR'] = str(self.cache)
        self.addCleanup(self.restore_env)
        (self.root / 'note.md').write_text(w.START + '\nCurrent task: preserve Firebase when used.\n' + w.END + '\nHistorical next steps are not active.', encoding='utf-8')
        (self.root / 'rules.md').write_text('<!-- start -->\nReview only; do not rewrite.\n<!-- end -->', encoding='utf-8')
        self.manifest = self.root / w.MANIFEST
        self.config = {'schema_version': 1, 'project_id': 'sample', 'state': {'path': 'note.md'},
                       'required': [{'id': 'scope', 'path': 'rules.md', 'start': '<!-- start -->', 'end': '<!-- end -->'}]}
        self.write_config()

    def restore_env(self):
        if self.previous is None:
            os.environ.pop('PROJECT_WORKFLOW_CACHE_DIR', None)
        else:
            os.environ['PROJECT_WORKFLOW_CACHE_DIR'] = self.previous

    def write_config(self):
        self.manifest.write_text(json.dumps(self.config, ensure_ascii=False), encoding='utf-8')

    def event(self, name, **extra):
        return {'hook_event_name': name, 'cwd': str(self.root), 'session_id': 's', 'turn_id': 't', **extra}

    def test_unicode_path_and_active_only(self):
        snap = w.snapshot(self.manifest)
        self.assertIn('preserve Firebase', snap['text'])
        self.assertNotIn('Historical', snap['text'])

    def test_subdirectory_and_sibling_isolation(self):
        child = self.root / 'sub'; child.mkdir()
        self.assertEqual(w.discover(child), self.manifest)
        sibling = self.root.parent / 'sibling'; sibling.mkdir()
        self.assertIsNone(w.discover(sibling))
        self.assertEqual(w.hook({'cwd': str(sibling), 'hook_event_name': 'UserPromptSubmit'}), {})

    def test_git_boundary(self):
        child = self.root / 'nested'; child.mkdir(); (child / '.git').mkdir()
        self.assertIsNone(w.discover(child))

    def test_missing_duplicate_reversed_markers(self):
        for body in ('missing', w.START + 'x' + w.START + w.END, w.END + 'x' + w.START):
            (self.root / 'note.md').write_text(body, encoding='utf-8')
            with self.assertRaises(w.WorkflowError): w.snapshot(self.manifest)

    def test_limit_does_not_truncate(self):
        self.config['limits'] = {'max_chars': 100}; self.write_config()
        with self.assertRaises(w.WorkflowError): w.snapshot(self.manifest)

    def test_vault_reference(self):
        self.config['vault_root'] = str(self.root)
        self.config['state']['path'] = '${vault}/note.md'; self.write_config()
        self.assertIn('Firebase', w.snapshot(self.manifest)['text'])
        self.config['state']['path'] = '${vault}/../elsewhere'; self.write_config()
        with self.assertRaises(w.WorkflowError): w.snapshot(self.manifest)

    def test_new_turn_load_and_receipt(self):
        result = w.hook(self.event('UserPromptSubmit'))
        self.assertIn('additionalContext', result['hookSpecificOutput'])
        snap = w.snapshot(self.manifest)
        w.checkpoint(snap, 's', 't', snap['state_hash'], 'unchanged', 'Scope and baseline checked.')
        self.assertEqual(w.hook(self.event('Stop')), {})
        w.hook(self.event('UserPromptSubmit', turn_id='t2'))
        self.assertEqual(w.hook(self.event('Stop', turn_id='t2'))['decision'], 'block')

    def test_stop_is_bounded(self):
        w.hook(self.event('UserPromptSubmit'))
        self.assertEqual(w.hook(self.event('Stop'))['decision'], 'block')
        self.assertNotIn('decision', w.hook(self.event('Stop')))
        self.assertNotIn('decision', w.hook(self.event('Stop', turn_id='other', stop_hook_active=True)))

    def test_state_or_source_change_invalidates_receipt(self):
        for filename in ('note.md', 'rules.md'):
            w.hook(self.event('UserPromptSubmit'))
            before = w.snapshot(self.manifest)
            w.checkpoint(before, 's', 't', before['state_hash'], 'unchanged', 'Checked actual scope.')
            path = self.root / filename
            path.write_text(path.read_text(encoding='utf-8').replace('Review', 'Revised review').replace('Current task', 'Updated task'), encoding='utf-8')
            after = w.snapshot(self.manifest)
            with self.assertRaises(w.WorkflowError):
                w.checkpoint(after, 's', 't', after['state_hash'], 'updated', 'Updated decision.')
            w.register(after, 's', 't', 'context')
            w.checkpoint(after, 's', 't', after['state_hash'], 'updated', 'Rechecked updated source.')
            self.assertEqual(w.hook(self.event('Stop')), {})

    def test_compaction_reload_and_missing_turn(self):
        result = w.hook(self.event('SessionStart', source='compact'))
        self.assertIn('preserve Firebase', result['hookSpecificOutput']['additionalContext'])
        missing = self.event('SessionStart', source='compact'); missing.pop('turn_id')
        result = w.hook(missing)
        self.assertIn('No turn_id', result['hookSpecificOutput']['additionalContext'])

    def test_cache_does_not_store_prompt(self):
        w.hook(self.event('UserPromptSubmit', prompt='PRIVATE PROMPT CONTENT'))
        contents = ''.join(p.read_text(encoding='utf-8') for p in self.cache.rglob('*.json'))
        self.assertNotIn('PRIVATE PROMPT', contents)
        self.assertNotIn('Firebase', contents)

    def test_duplicate_ids(self):
        self.config['required'].append(self.config['required'][0]); self.write_config()
        with self.assertRaises(w.WorkflowError): w.snapshot(self.manifest)

    def test_cli_malformed_hook_reports_failure_without_lockout(self):
        result = subprocess.run([sys.executable, w.__file__, 'hook'], input='{broken',
                                text=True, encoding='utf-8', capture_output=True, check=True)
        output = json.loads(result.stdout)
        self.assertNotIn('continue', output)
        self.assertIn('NOT loaded', output['systemMessage'])

    def test_missing_source_allows_repair_turn_with_explicit_gap(self):
        self.config['state']['path'] = 'missing.md'; self.write_config()
        result = subprocess.run([sys.executable, w.__file__, 'hook'],
                                input=json.dumps(self.event('UserPromptSubmit')),
                                text=True, encoding='utf-8', capture_output=True, check=True)
        output = json.loads(result.stdout)
        self.assertNotIn('continue', output)
        self.assertIn('NOT loaded', output['hookSpecificOutput']['additionalContext'])

    def test_invalid_input_shapes_fail_clearly(self):
        for malformed in ([], None, 'text'):
            self.manifest.write_text(json.dumps(malformed), encoding='utf-8')
            with self.assertRaises(w.WorkflowError): w.snapshot(self.manifest)
            with self.assertRaises(w.WorkflowError): w.hook(malformed)
            with self.assertRaises(w.WorkflowError): w.ledger_report(malformed)

    def test_manifest_change_invalidates_receipt(self):
        w.hook(self.event('UserPromptSubmit'))
        before = w.snapshot(self.manifest)
        w.checkpoint(before, 's', 't', before['state_hash'], 'unchanged', 'Checked scope.')
        self.config['project_id'] = 'renamed'; self.write_config()
        self.assertEqual(w.hook(self.event('Stop'))['decision'], 'block')

    def test_subagent_does_not_share_parent_receipt(self):
        self.assertEqual(w.hook(self.event('UserPromptSubmit', agent_id='child')), {})
        self.assertFalse(self.cache.exists())

    def test_hook_merge_repeat_preserves_unrelated(self):
        other = {'hooks': {'Stop': [{'hooks': [{'type': 'command', 'command': 'other'}]}]}}
        new = install.merge(other, 'python task.py', 'python task.py')
        self.assertEqual(install.merge(new, 'python task.py', 'python task.py'), new)
        self.assertEqual(install.merge(new, '', '', uninstall=True), other)

    def test_ledger_thresholds_clarification_and_projects(self):
        events = [{'id': str(n), 'project_id': 'p', 'rule_id': 'R', 'status': 'confirmed', 'evidence': 'handoff#'+str(n)} for n in range(1, 6)]
        for size, level in ((2, 'project'), (3, 'project-important'), (5, 'global')):
            self.assertEqual(w.ledger_report({'events': events[:size]})['rules'][0]['level'], level)
        events += [{'id': 'c', 'project_id': 'p', 'rule_id': 'R', 'status': 'clarification', 'clarifies': '1', 'evidence': 'note#c'},
                   {'id': 'q1', 'project_id': 'q', 'rule_id': 'R', 'status': 'confirmed', 'evidence': 'q#1'}]
        report = w.ledger_report({'events': events})
        self.assertEqual([r['count'] for r in report['rules']], [5, 1])
        self.assertEqual(report, w.ledger_report({'events': events}))
        with self.assertRaises(w.WorkflowError): w.ledger_report({'events': events + [events[0]]})


if __name__ == '__main__':
    unittest.main()
