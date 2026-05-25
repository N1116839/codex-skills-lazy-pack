---
name: project-init-sync
description: Initialize a classroom tools project workspace with Codex working files, Git, Firebase references, and optional GitHub or Obsidian integration. Use when the user says 初始化班級工具工作模式, 專案初始化, project init sync, or asks Codex to set up a new classroom tools project from the #07 workflow.
---

# Project Init Sync

Use this workflow to initialize a classroom tools workspace.

1. Confirm the project root and avoid overwriting existing user files.
2. Create or update `AGENTS.md` with project name, local path, Firebase project, GitHub remote, Obsidian note path, and working rules.
3. Create or update `README.md` with the current setup summary.
4. Create or update `.gitignore` to exclude OS files, secrets, local agent settings, dependencies, and build output.
5. Preserve Firebase files if they already exist: `.firebaserc`, `firebase.json`, and `firestore.rules`.
6. Initialize Git if the folder is not already a repository.
7. Apply `git config windows.appendAtomically false` for Windows folders that may sync through Drive or OneDrive.
8. Commit only after checking status and confirming the intended files.
9. Create GitHub remotes or enable GitHub Pages only when GitHub CLI authentication works and the user has confirmed repo visibility.
10. Create Obsidian notes only after the vault path and vault-relative note path are confirmed.
