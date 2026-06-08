---
name: project-init-sync
description: Initialize the classroom tools working mode from lazy-pack #07, including the Google Drive project folder, project blueprint, Git/GitHub, Obsidian working note, and startup/shutdown workflow references. Use when the user says 初始化班級工具工作模式, 專案初始化, project init sync, 老師建專案模式, or asks Codex to set up a new classroom tools project from the #07 workflow.
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
   - `.claude/`.
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

- Never commit `.claude/`, secrets, API keys, tokens, credentials, or local permission files.
- Do not run `git add .` blindly. Stage only intended files.
- If GitHub authentication or Pages setup is blocked, still finish local and Obsidian setup, then report the blocker.

## Global AI File Protection Rules

Project initialization must write these rules into the new project's `AGENTS.md` or equivalent project blueprint.

- Agent-created temporary files must include `_暫存` at the end of the file name before the extension, for example `report_暫存.html`.
- Files downloaded by an agent from the internet must start with the agent name and underscore, for example `codex_source.pdf` or `claude_reference.docx`.
- Forbidden examples: `暫存.txt`, `下載.txt`, `test.txt`, `temp.docx`. These lack the required `_暫存` suffix or `AI名稱_` prefix and must be treated as user data once created.
- If the user asks to create a temporary file or a download-file example without specifying content, create a minimal compliant demonstration file. Do not create `暫存.txt` or `下載.txt`, and do not use "ask for content first" to bypass the naming rule.
- Any file or folder that does not start with `AI名稱_` and does not end with `_暫存` is user data by default. It must not be deleted, moved, renamed, cleaned, or overwritten.
- Deleting an unnamed file or folder is forbidden unless the user explicitly authorizes the exact path. The deletion must be recorded in the project handoff or working note with path, reason, time, and authorizing user instruction.
- Agent-downloaded or agent-created project materials must be public, downloadable, traceable, and from a real source when used as source evidence, such as public company ESG documents, public financial reports, government deficiency publications, or named international regulations.
- Project setup must include a cleanup rule: cleanup may only target files matching the agent prefix or `_暫存` suffix, and must list absolute paths before deletion.
