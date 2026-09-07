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
## Pitfall Write-back Format（2026-06-26）

收工寫踩坑時，不可只寫「已記錄」或心得。每個跨專案或會重犯的踩坑，都要整理成可執行檢查表：

- Trigger：什麼情境會觸發這個踩坑。
- Required check：動手或回答前必須查哪些來源、檔案、狀態或截圖。
- Stop condition：缺少哪些查核時必須停下來問使用者，不能自行猜測。
- Write-back：完成後要寫回哪些位置，例如專案 `工作筆記.md`、全域 `踩坑紀錄.md`、`知識庫/index.md`、`知識庫/log.md`、專案 `AGENTS.md`。

若本輪是整理資料整理專案或修正 agent 工作流程，收工回報還要明列：哪些現有 skills 已檢查、哪些有出入、哪些已更新、是否已同步到 Google Drive 備份與 GitHub/lazy-pack。

## Global AI File Protection Checkout

At every 收工, check whether the session complied with these rules and write any violation or near miss into the project handoff / working note and `踩坑紀錄.md` when relevant:

- Agent-created temporary files use the `_暫存` suffix before the extension.
- Agent-downloaded internet files use the agent-name prefix, such as `codex_檔案名稱`.
- Flag these as violations if created by an agent: `暫存.txt`, `下載.txt`, `test.txt`, `temp.docx`, or any other unprefixed/unsuffixed disposable-looking name.
- Also flag the case where an agent creates `暫存.txt` or `下載.txt` and then asks the user what content should go inside. The naming violation has already happened and must be recorded.
- Files or folders without an `AI名稱_` prefix and without a `_暫存` suffix were treated as user data and were not deleted, moved, renamed, cleaned, or overwritten.
- Any user-authorized deletion of an unnamed file or folder was recorded with exact path, reason, timestamp, and authorization.
- Agent-used source evidence was public, downloadable, traceable, and from a real source, unless it was explicitly user-provided private project material.

## Commit Message Rules

- Title: verb + object, for example `更新開工收工同步規則`.
- Body: 3-5 bullets explaining what changed and why, when the change is non-trivial.
- If there is nothing substantive to commit, skip commit/push and report that no GitHub sync was needed.

## Do Not

- Do not run `git add .` blindly.
- Do not commit `.claude/settings.local.json`, `.claude/worktrees/`, secrets, tokens, credentials, or generated dependency folders.
- Do not run synchronization for a conversation with no substantive progress; report that there was nothing to sync.

## Obsidian 每日筆記與來源整理（2026-06-22）

收工時除了更新專案工作筆記，也要依影片式第二大腦流程判斷是否更新每日筆記：

- 每日筆記位置：`G:\我的雲端硬碟\我的第二大腦\每日筆記\YYYY-MM-DD.md`。
- 每日筆記只放當天來源、問答/工作摘要、決策、踩坑、待查，並連回專案駕駛艙；不要把專案完整內容雙寫到每日筆記。
- 專案進度、決策、實際觀察、踩坑主體仍寫入該專案 `工作筆記.md` 或 `專案工作流程.md`。
- 原始來源完整保留在 `Clippings/`、專案 `assets/` 或來源檔，不改動原始剪藏。
- 若新增專案、來源索引或可復用 SOP，更新 `專案/專案索引.md`、`知識庫/index.md`、`知識庫/log.md`。
- 收工回報要列出：更新了哪些 Obsidian 筆記、哪些來源已保留、哪些待查。


## 重複踩坑升級、目標封存與主題回寫（2026-09-07）

收工發現踩坑或收到目標更新時，先找同根因 Pitfall ID，不得直接新增一則日期日誌。第 1、2 次照既有格式記錄；第 3 次合併前三次為一行可執行規則，升級到專案權威並重設專案權威計數為 1；同根因累計第 10 次才合併成第二大腦全域規範的一行，重設全域計數為 1。每次後續發生只更新該權威行的累計次數、最後日期、攔截結果與證據回鏈。

若本輪改變專案目標，必須把衝突、模糊或誤導的舊計畫封存而非刪除：保留原文，寫明取代它的新目標、日期、理由和現行權威連結，並從活躍入口移除。原始來源與歷史證據不得改動。

收工前檢查本輪新增資料是否已歸入既有主題。相依功能要有一個可發現的母題入口；不要把戰鬥的 HP／MP、掉落、玩家 PK、敵國 PK 拆成彼此無回鏈的零散檔案。若因責任邊界確需拆分，更新母題索引與雙向連結。
