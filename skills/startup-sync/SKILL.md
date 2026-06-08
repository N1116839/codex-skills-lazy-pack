---
name: startup-sync
description: Startup continuation helper from lazy-pack #07. Use when the user says 開工, 開始工作, 我來了, 上次做到哪, 我們繼續, 接下來呢, 接續工作, 專案繼續, 繼續專案, 啟動同步, startup sync, or asks Codex to resume the current project.
---

# Startup Sync

Use this workflow at the start of a project session. It is the reading counterpart to 收工: 開工 reads the working note and checks state; it does not modify project notes.

## #07 Startup SOP

1. Determine the working directory from the current workspace.
2. Confirm the directory is a Git repo and is inside a cloud-synced folder when possible.
3. Read the nearest project `AGENTS.md`.
4. Determine `REPO_NAME` from the project folder name.
5. Locate the Obsidian working note:
   - Prefer the explicit Obsidian note path in `AGENTS.md`.
   - Otherwise try `G:\我的雲端硬碟\我的第二大腦\<REPO_NAME>\工作筆記.md`.
   - Also accept `專案工作流程.md` if the project uses that file name.
6. Read, but do not rewrite, the working note. Summarize only:
   - `上次做到哪`.
   - `下一步`, if present.
   - The latest relevant `踩坑筆記`.
7. Check local Git state with `git status --short`.
8. Check remote state with `git fetch` only when useful. Do not run `git pull` automatically.
9. Report:
   - Project name.
   - Last progress.
   - Local Git state.
   - Remote state if checked.
   - Recommended next steps.
10. Ask which direction to continue from instead of starting unrelated work.

## 開工 / 專案繼續規則

當使用者說「開工」、「專案繼續」、「繼續專案」、「啟動同步」時，不要只看目前資料夾。必須先讀取專案工作筆記與第二大腦紀錄，避免重犯已記錄的踩坑點。

固定第二大腦位置：

`G:\我的雲端硬碟\我的第二大腦`

至少檢查：

- `AGENTS.md`
- 專案自己的接續紀錄或 Obsidian 專案筆記
- `G:\我的雲端硬碟\我的第二大腦\踩坑紀錄.md`
- `G:\我的雲端硬碟\我的第二大腦\知識庫\log.md`

開工回報要包含：目前專案狀態、上次未完成事項、需要避免的踩坑點、是否有未提交或未同步內容。

## Global AI File Protection Rules

At every 開工 / 專案繼續, re-read and restate any project-specific version of these rules before touching files:

- Agent-created temporary files must include `_暫存` at the end of the file name before the extension.
- Files downloaded by an agent from the internet must start with the agent name and underscore, such as `codex_檔案名稱`.
- Forbidden examples: `暫存.txt`, `下載.txt`, `test.txt`, `temp.docx`. These names are non-compliant because they lack the required suffix or prefix.
- Files or folders without an `AI名稱_` prefix and without a `_暫存` suffix are user data by default.
- User data must not be deleted, moved, renamed, cleaned, overwritten, or treated as disposable untracked files.
- If the user explicitly authorizes deleting an unnamed file or folder, record the deleted path, reason, timestamp, and authorization source in the project handoff or working note.
- Source evidence used by the agent must be public, downloadable, traceable, and from a real source unless the user provides private source files for the project.

## Do Not

- Do not run `git pull` unless the user confirms.
- Do not edit the working note during 開工.
- Do not create a missing working note during 開工; report that #07 initialization or manual setup is needed.
- Do not paste the full working note unless the user explicitly asks.
