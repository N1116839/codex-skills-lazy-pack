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
- If the user asks to create a temporary file or download-file example, use a compliant name immediately, such as `命名規則示範_暫存.txt` or `codex_下載檔案示範.txt`. Asking what content to put inside does not permit creating a non-compliant file first.
- Files or folders without an `AI名稱_` prefix and without a `_暫存` suffix are user data by default.
- User data must not be deleted, moved, renamed, cleaned, overwritten, or treated as disposable untracked files.
- If the user explicitly authorizes deleting an unnamed file or folder, record the deleted path, reason, timestamp, and authorization source in the project handoff or working note.
- Source evidence used by the agent must be public, downloadable, traceable, and from a real source unless the user provides private source files for the project.

## Do Not

- Do not run `git pull` unless the user confirms.
- Do not edit the working note during 開工.
- Do not create a missing working note during 開工; report that #07 initialization or manual setup is needed.
- Do not paste the full working note unless the user explicitly asks.

## Obsidian 專案駕駛艙硬性閘門（2026-06-22）

開工 / 專案繼續不能只讀專案工作筆記。依第二大腦影片式工作流，必須先完成下列 checklist，少一項就不可宣稱開工完成，也不可進入正式 SOP 或實作：

- 已讀第二大腦 `AGENTS.md` 與 `CLAUDE.md`。
- 已讀全域 `踩坑紀錄.md`。
- 已讀 `知識庫/log.md`。
- 已讀 `專案/專案索引.md`，確認目標專案駕駛艙位置。
- 已讀目標專案的總覽與工作筆記，例如 `POE2/POE2總覽.md`、`POE2/工作筆記.md`。
- 已檢查 git status（若目前資料夾是 Git repo）。
- 開工回報明列：已查來源、未查來源、本次需要避免的踩坑點、目前專案狀態、下一步選項。

若使用者接著問專案專業問題（例如 POE2 做裝），回答前還要讀該專案的來源索引與資料庫；未查完時只能標為「暫定」或「不能正確回答」。
## Pitfall Memory Gate（2026-06-26）

開工不是只讀到踩坑紀錄，而是要把踩坑轉成可執行檢查。若任務涉及既有專案、跨 agent 接手、使用者截圖、來源整理或「不要再犯」類回饋，開工回報必須列出：

- 已查來源：本次已讀哪些專案檔、第二大腦頁面、來源索引或 Clippings。
- 未查來源：哪些應查但尚未查，原因是什麼。
- 本次要避免的踩坑：從 `踩坑紀錄.md` 與專案工作筆記抽出，不可只說「已注意」。
- 每個踩坑的檢查方式：用 Trigger / Required check / Stop condition / Write-back 表達。
- 停止條件：哪些資料未查完時必須停下來問使用者，不能自行猜測。


## 重複踩坑、目標變更與主題整併 Gate（2026-09-07）

開工前，若是大型專案或本輪目標有更新，先完成：

1. 以唯一 Pitfall ID 對照專案權威、工作筆記與全域 `踩坑紀錄.md`，讀取其聚合次數與 Required check；不得把同根因的日期日誌當成多條現行規則。
2. 比對新目標與現行入口、歷史決策、下一步及來源索引。發現衝突、歧義或會誤導新目標的舊摘要時，只能標為待封存／待更新；未確認取代位置前，不得按舊計畫執行。
3. 列出本輪要放入的功能主題與既有權威檔。HP／MP、掉落、玩家 PK、敵國 PK 等戰鬥責任預設屬同一戰鬥主題；若要拆分，先說明責任邊界與雙向回鏈。

開工回報必須說明命中的 Pitfall ID／次數、舊目標是否已封存，以及本輪主題落點。資料不足時停止宣稱已完成防錯或已完成目標轉換。
