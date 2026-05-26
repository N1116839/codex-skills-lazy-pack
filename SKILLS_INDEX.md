# Codex Skills Index

更新時間：2026-05-26

## 個人 skills

| Skill | 類型 | GitHub 資料夾 | ZIP 懶人包 | 用途 |
|---|---|---|---|---|
| gas-targeted-fix | personal | `skills/gas-targeted-fix` | `packages/gas-targeted-fix.zip` | 精準修正 Google Apps Script 與一般程式碼。Use when the user asks in Traditional Chinese to fix code, such as "幫我修正程式碼", "修正程式", "改程式", "幫我改 GAS", "修正 Apps Script", "Google Sheets 自動化壞了", or asks for minimal, non-refactoring code changes. Preserve original logic, naming, comments, structure, and style unless the user explicitly requests broader changes. |
| html-training-deck | personal | `skills/html-training-deck` | `packages/html-training-deck.zip` | 建立或修訂 HTML 內部教育訓練簡報、內部稽核教材、SOP 學習平台、稽查重點頁、Q&A 學習頁、互動式年度行事曆與 image2 視覺化教材。Use when the user asks for HTML簡報、內部教育訓練、內部稽核、稽查重點、SOP學習、Q&A、年度資料收件行事曆、部門訓練、互動式教材、GitHub Pages 發佈前檢查。 |
| project-init-sync | personal | `skills/project-init-sync` | `packages/project-init-sync.zip` | Initialize the classroom tools working mode from lazy-pack #07, including the Google Drive project folder, project blueprint, Git/GitHub, Obsidian working note, and startup/shutdown workflow references. |
| shutdown-sync | personal | `skills/shutdown-sync` | `packages/shutdown-sync.zip` | Shutdown synchronization helper from lazy-pack #07. Triggered by 收工/先收工/結束工作/換電腦 requests; updates Obsidian working note, records pitfalls, commits, and pushes relevant project changes. |
| skills-sync | personal | `skills/skills-sync` | `packages/skills-sync.zip` | 同步、備份、打包與上傳 Codex skills。Use when the user says 更新skills、同步skills、備份skills、上傳skills到GitHub、建立skills懶人包、換電腦恢復skills、把skills放入第二大腦，或要求 Codex 同步本機 skills、第二大腦、Google Drive 懶人包與 GitHub skills repo. |
| startup-sync | personal | `skills/startup-sync` | `packages/startup-sync.zip` | Startup continuation helper from lazy-pack #07. Triggered by 開工/開始工作/上次做到哪/繼續專案 requests; reads Obsidian working note, checks Git status, and recommends next steps without modifying notes. |

## 系統 skills 索引

- imagegen（系統內建，僅索引，不打包上傳）
- openai-docs（系統內建，僅索引，不打包上傳）
- plugin-creator（系統內建，僅索引，不打包上傳）
- skill-creator（系統內建，僅索引，不打包上傳）
- skill-installer（系統內建，僅索引，不打包上傳）

## 更新規則

當使用者說「更新skills」時，Codex 需同步更新：

1. 本機 %USERPROFILE%\.codex\skills。
2. Google Drive 備份 G:\我的雲端硬碟\2026codex\skills。
3. 本 repo 的 skills/ 與 packages/。
4. 第二大腦專案頁。
5. G:\我的雲端硬碟\2026codex\01.5-Codex必裝Skills與Plugins.md。

.system skills 只做索引，不預設打包。

## 2026-05-25 收工同步

- 已重新同步 6 個 personal skills 至 `skills/` 與 `packages/`。
- `shutdown-sync` 新增換電腦前收工規則：精準繁體中文、踩坑點寫入第二大腦、未完成事項納入版本控制、確認提交與推送。
- `html-training-deck` 新增年度行事曆視覺與重複資訊規則：收件核對台卡片化、來源旁放已完成/未完成、避免「本頁相關 SOP / 依頻率分組 / 來源」重複、關鍵設備行事曆使用條列式選單。
- 明顯敏感資訊掃描未發現 API key、token、password、secret 或 private key；命中項目僅為 skill 說明文字。
## 整包懶人包

| Package | 路徑 | 用途 |
|---|---|---|
| codex-personal-skills-bundle.zip | `packages/codex-personal-skills-bundle.zip` | 一次安裝所有 personal skills，內含 `skills/` 與 `install-all-skills.ps1`。 |

## 第二大腦 canonical source

- `G:\我的雲端硬碟\我的第二大腦\Codex標準\skills`
- 之後使用者說「建立skills」時，先在第二大腦建立或更新，再同步到本機、Google Drive 備份與 GitHub lazy-pack。

## 2026-05-26 #07 懶人包對齊

- `project-init-sync` 已改為對齊 #07 初始化班級工具工作模式：環境檢查、GDrive 專案資料夾、`AGENTS.md`/README/`.gitignore`、Git/GitHub、Obsidian `工作筆記.md`。
- `startup-sync` 已改為 #07 開工接續助手：讀工作筆記、查 Git 狀態、可 fetch、不可自動 pull、不可修改工作筆記。
- `shutdown-sync` 已改為 #07 收工同步助手：更新工作筆記、保存踩坑、更新第二大腦、stage 相關檔案、commit、push，並避免提交 `.claude/` 與敏感資料。
- 已更新三個 skill zip 與 `codex-personal-skills-bundle.zip`。
