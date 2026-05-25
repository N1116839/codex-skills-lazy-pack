# Codex Skills Index

更新時間：2026-05-25 16:45

## 個人 skills

| Skill | 類型 | GitHub 資料夾 | ZIP 懶人包 | 用途 |
|---|---|---|---|---|
| gas-targeted-fix | personal | `skills/gas-targeted-fix` | `packages/gas-targeted-fix.zip` | 精準修正 Google Apps Script 與一般程式碼。Use when the user asks in Traditional Chinese to fix code, such as "幫我修正程式碼", "修正程式", "改程式", "幫我改 GAS", "修正 Apps Script", "Google Sheets 自動化壞了", or asks for minimal, non-refactoring code changes. Preserve original logic, naming, comments, structure, and style unless the user explicitly requests broader changes. |
| html-training-deck | personal | `skills/html-training-deck` | `packages/html-training-deck.zip` | 建立或修訂 HTML 內部教育訓練簡報、內部稽核教材、SOP 學習平台、稽查重點頁、Q&A 學習頁、互動式年度行事曆與 image2 視覺化教材。Use when the user asks for HTML簡報、內部教育訓練、內部稽核、稽查重點、SOP學習、Q&A、年度資料收件行事曆、部門訓練、互動式教材、GitHub Pages 發佈前檢查。 |
| project-init-sync | personal | `skills/project-init-sync` | `packages/project-init-sync.zip` | Initialize a classroom tools project workspace with Codex working files, Git, Firebase references, and optional GitHub or Obsidian integration. Use when the user says 初始化班級工具工作模式, 專案初始化, project init sync, or asks Codex to set up a new classroom tools project from the #07 workflow. |
| shutdown-sync | personal | `skills/shutdown-sync` | `packages/shutdown-sync.zip` | Review and preserve project work at the end of a Codex session. Use when the user says 收尾同步, 結束工作, shutdown sync, or asks Codex to wrap up, summarize changes, prepare commits, or sync project notes. |
| skills-sync | personal | `skills/skills-sync` | `packages/skills-sync.zip` | 同步、備份、打包與上傳 Codex skills。Use when the user says 更新skills、同步skills、備份skills、上傳skills到GitHub、建立skills懶人包、換電腦恢復skills、把skills放入第二大腦，或要求 Codex 同步本機 skills、第二大腦、Google Drive 懶人包與 GitHub skills repo. |
| startup-sync | personal | `skills/startup-sync` | `packages/startup-sync.zip` | Load project context and check workspace state at the start of a Codex session. Use when the user says 啟動同步, 開始工作, startup sync, or asks Codex to prepare the current project workspace before making changes. |

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
