---
name: project-init-sync
description: Initialize a new project folder with the #07 classroom tools working mode, including Google Drive folder, AGENTS.md blueprint, Git/GitHub, Obsidian working note, and startup/shutdown workflow references. Use when the user says 專案初始化, 初始化專案, 初始化班級工具工作模式, project init sync, 老師建專案模式, 幫我建專案, 幫我建新專案, 新增專案, 在這個資料夾初始化, or asks Codex to set up a new project from scratch in any folder.
---

# Project Init Sync

Use this workflow to initialize the #07 classroom tools working mode. This skill creates the environment; it does not preserve session notes unless the user also asks for 收工.

## #07 Initialization Workflow

1. Check environment:
   - OS.
   - `git --version`.
   - `gh auth status`.
   - `node --version`.
   - Ask for the Obsidian vault path if not already known.
   - Verify the vault path exists.
2. Ask for the classroom tools root folder name and cloud-drive parent folder. Default parent: `G:\我的雲端硬碟`.
3. Create the root folder without overwriting existing user files.
4. Create or update `AGENTS.md` as the Codex project blueprint. Include:
   - Project name and local path.
   - GitHub repo URL or intended repo name.
   - Firebase project ID when known.
   - Obsidian working note path: `<vault path>\<project folder>\工作筆記.md`.
   - Working rhythm: 開工 reads, 收工 writes.
   - Student data privacy rules.
5. Create or update `README.md` with the current setup summary and tool list.
6. Create or update `.gitignore`. It must exclude:
   - `desktop.ini`, `*.tmp`, `~$*`.
   - `.env`, `*.key`, `credentials.*`.
    - `.claude/`, `.codex/`.
    - `node_modules/`.
7. Preserve Firebase files if they already exist: `.firebaserc`, `firebase.json`, and `firestore.rules`.
8. Initialize Git if the folder is not already a repository.
9. Apply `git config windows.appendAtomically false` for Windows folders that may sync through Drive or OneDrive.
10. Create the Obsidian project folder and `工作筆記.md` after the vault path is confirmed.
11. Create a first `工作筆記.md` with:
    - `上次做到哪`.
    - `工具清單`.
    - `最近更動紀錄`.
    - `踩坑筆記`.
12. Create GitHub remote or enable GitHub Pages only when GitHub CLI authentication works and the user has confirmed repo visibility. Lazy-pack #07 assumes a public repo for free GitHub Pages.
13. Commit and push only the intended initialization files after checking status and confirming the file list.

## Required Working Note Template

Use this structure for the Obsidian working note:

```markdown
# <project-name> 工作筆記

> 進度日誌。專案藍圖請看 GDrive 端的 `AGENTS.md` 或 `README.md`。

## 上次做到哪

**最後動作：** 初始化班級工具總專案
**所在 repo：** <repo-url-or-pending>

## 工具清單

- 尚無

## 最近更動紀錄

| 日期 | 變更摘要 | GDrive | Obsidian | GitHub |
|------|----------|--------|----------|--------|
| <today> | 初始化班級工具總專案 | OK | OK | 待確認 |

## 踩坑筆記

- 尚無
```

## Safety Rules

- Never commit `.claude/`, `.codex/`, secrets, API keys, tokens, credentials, or local permission files.
- Do not run `git add .` blindly. Stage only intended files.
- If GitHub authentication or Pages setup is blocked, still finish local and Obsidian setup, then report the blocker.
