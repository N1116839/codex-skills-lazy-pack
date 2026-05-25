---
name: shutdown-sync
description: Review and preserve project work at the end of a Codex session. Use when the user says 收尾同步, 結束工作, shutdown sync, or asks Codex to wrap up, summarize changes, prepare commits, or sync project notes.
---

# Shutdown Sync

Use this workflow at the end of a project session.

1. Check Git status and summarize changed files.
2. Review whether `AGENTS.md`, README, Firebase config, and project notes need updates.
3. Run lightweight validation relevant to the latest changes when feasible.
4. Do not commit or push unless the user has asked for it or explicitly confirms.
5. If committing, use a concise commit message and include only relevant files.
6. Report completed work, remaining blockers, and any skipped validation.
