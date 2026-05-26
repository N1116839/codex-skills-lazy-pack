---
name: shutdown-sync
description: Shutdown synchronization helper from lazy-pack #07. Use when the user says 收工, 先收工, 結束了, 結束工作, 準備換電腦, 我要換電腦, 該同步的同步, 先到這裡, 收尾同步, shutdown sync, or asks Codex to wrap up and perform three-way sync: update Obsidian working note, commit, and push.
---

# Shutdown Sync

Use this workflow at the end of a project session. It is the writing counterpart to 開工: 收工 writes the working note, preserves pitfalls, and syncs GitHub when the current project is a Git repo.

## #07 Shutdown SOP

1. Inventory today's work from the conversation and filesystem:
   - Completed files and decisions.
   - Unfinished tasks.
   - New pitfalls and root causes.
   - Validation performed or skipped.
2. Determine the working directory and read the nearest project `AGENTS.md`.
3. Locate the Obsidian working note:
   - Prefer the explicit Obsidian note path in `AGENTS.md`.
   - Otherwise try `G:\我的雲端硬碟\我的第二大腦\<REPO_NAME>\工作筆記.md`.
   - If missing, report the blocker and still continue Git sync when appropriate.
4. Update the Obsidian working note:
   - Refresh `上次做到哪`.
   - Add or update `下一步` when there are unfinished tasks.
   - Append one row to `最近更動紀錄`.
   - Add new `踩坑筆記` when relevant.
5. Persist cross-project pitfalls to `G:\我的雲端硬碟\我的第二大腦\踩坑紀錄.md`.
6. When new reusable knowledge is created, update:
   - `G:\我的雲端硬碟\我的第二大腦\知識庫\index.md`.
   - `G:\我的雲端硬碟\我的第二大腦\知識庫\log.md`.
7. Check Git status.
8. Stage only relevant files. Never stage `.claude/`, secrets, credentials, large raw media, unrelated screenshots, dependencies, or unrelated untracked files.
9. Commit with a concise message that says what changed and why.
10. Push the current branch to the configured remote.
11. Report the three-way sync status: GDrive, Obsidian, GitHub.

## 本專案沉澱規則：換電腦前收工

當使用者說「先收工」、「我要換電腦」、「收尾同步」時，必須用精準繁體中文完成下列事項：

1. 先檢查 Git 狀態，分清楚已追蹤修改、未追蹤檔案、已領先遠端的 commit。
2. 將本輪完成事項、未完成事項、踩坑點、驗證結果寫入專案接續紀錄與第二大腦。
3. 未完成事項不可只口頭回報；要納入版本控制中的接續文件，讓換電腦後可直接接續。
4. 若使用者已要求更新 GitHub，需提交並推送相關倉庫；不要把大型原始資料、截圖或不相關未追蹤檔案誤加入 commit。
5. 若同時要求更新 skills，需執行 skills-sync：同步本機、Google Drive 備份、GitHub lazy-pack repo、第二大腦與 lazy-pack note。
6. 收工回報需列出：已完成、已提交、已推送、未納入版本控制、未驗證或阻擋原因。

## 第二大腦固定寫入規則

固定第二大腦位置：

`G:\我的雲端硬碟\我的第二大腦`

每次收工至少要判斷是否需要更新：

- `G:\我的雲端硬碟\我的第二大腦\踩坑紀錄.md`
- `G:\我的雲端硬碟\我的第二大腦\知識庫\index.md`
- `G:\我的雲端硬碟\我的第二大腦\知識庫\log.md`
- 專案自己的 Obsidian 接續紀錄或專案資料夾內接續紀錄

若本輪有使用者明確回饋「不要再犯」、「幫我記住」、「踩坑」、「回饋給 AI」，必須寫入 `踩坑紀錄.md`，不能只在最後訊息口頭總結。

## Commit Message Rules

- Title: verb + object, for example `更新開工收工同步規則`.
- Body: 3-5 bullets explaining what changed and why, when the change is non-trivial.
- If there is nothing substantive to commit, skip commit/push and report that no GitHub sync was needed.

## Do Not

- Do not run `git add .` blindly.
- Do not commit `.claude/settings.local.json`, `.claude/worktrees/`, secrets, tokens, credentials, or generated dependency folders.
- Do not run synchronization for a conversation with no substantive progress; report that there was nothing to sync.
