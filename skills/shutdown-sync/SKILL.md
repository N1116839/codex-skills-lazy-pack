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

## 本專案沉澱規則：換電腦前收工

當使用者說「先收工」、「我要換電腦」、「收尾同步」時，必須用精準繁體中文完成下列事項：

1. 先檢查 Git 狀態，分清楚已追蹤修改、未追蹤檔案、已領先遠端的 commit。
2. 將本輪完成事項、未完成事項、踩坑點、驗證結果寫入專案接續紀錄與第二大腦。
3. 未完成事項不可只口頭回報；要納入版本控制中的接續文件，讓換電腦後可直接接續。
4. 若使用者已要求更新 GitHub，需提交並推送相關倉庫；不要把大型原始資料、截圖或不相關未追蹤檔案誤加入 commit。
5. 若同時要求更新 skills，需執行 skills-sync：同步本機、Google Drive 備份、GitHub lazy-pack repo、第二大腦與 lazy-pack note。
6. 收工回報需列出：已完成、已提交、已推送、未納入版本控制、未驗證或阻擋原因。
