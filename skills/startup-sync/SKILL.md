---
name: startup-sync
description: Load project context and check workspace state at the start of a Codex session. Use when the user says 啟動同步, 開始工作, startup sync, or asks Codex to prepare the current project workspace before making changes.
---

# Startup Sync

Use this workflow at the start of a project session.

1. Read the nearest project `AGENTS.md`.
2. Check the current working directory and list key project files.
3. Check Git status and identify uncommitted changes without reverting them.
4. Confirm configured external systems from `AGENTS.md`, especially Firebase project ID, GitHub remote, and Obsidian note path.
5. Report blockers clearly before doing any deployment, commit, push, or destructive operation.
6. Continue with the user's requested task after the workspace state is understood.
