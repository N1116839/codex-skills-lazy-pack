# Codex Skills Index

更新時間：2026-06-09

## 個人 skills

| Skill | 類型 | GitHub 資料夾 | ZIP 懶人包 | 用途 |
|---|---|---|---|---|
| ai-dispatch | personal | `skills/ai-dispatch` | `packages/ai-dispatch.zip` | 用 OpenCode CLI ＋ NVIDIA 免費模型組成「AI 大軍」派工出工，省下昂貴 Token。當使用者說「派工」「派給士兵」「叫大軍做」「用 opencode 做」「headless 派工」「平行派工」「開七個視窗」「dispatch」時觸發。軍師（Claude/Codex）規劃審查，OpenCode 士兵出工，軍師只讀 result_*.md。含換機自動裝 opencode 與引導 NVIDIA 免費金鑰。 |
| evidence-based-content | personal | `skills/evidence-based-content` | `packages/evidence-based-content.zip` | 資料正確性與可追溯標準。任何涉及 GDP 知識庫條目、內部教育訓練平台資料、論文報告時套用。當使用者說「校對資料庫」「整理 KB」「查文獻」「驗證資料」「逐筆核對」「資料要扎實」「有理有據」「不要推論」「來源在哪」時觸發。 |
| gas-targeted-fix | personal | `skills/gas-targeted-fix` | `packages/gas-targeted-fix.zip` | 精準修正 Google Apps Script 與一般程式碼。Use when the user asks in Traditional Chinese to fix code, such as "幫我修正程式碼", "修正程式", "改程式", "幫我改 GAS", "修正 Apps Script", "Google Sheets 自動化壞了", or asks for minimal, non-refactoring code changes. Preserve original logic, naming, comments, structure, and style unless the user explicitly requests broader changes. |
| html-evidence-training-builder | personal | `skills/html-evidence-training-builder` | `packages/html-evidence-training-builder.zip` | Build or revise traceable HTML training databases from user-provided SOP/WI/FR, deck, spreadsheet, and document sources; enforce source traceability, no invented company facts, Firestore sync, and image2/imagegen visual planning. |
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

## 全域 AI 檔案保護規範

所有 personal skills 同步時必須保留並傳遞下列規範：

- Agent 測試暫存檔：檔名結尾需加 `_暫存`，例如 `report_暫存.html`。
- Agent 網路下載檔：檔名前綴需加 AI 名稱與底線，例如 `codex_檔案名稱.pdf`。
- 明確違規例：`暫存.txt`、`下載.txt`、`test.txt`、`temp.docx`。這些名稱不可作為 agent 暫存或下載檔。
- 沒有 `AI名稱_` 前綴、也沒有 `_暫存` 後綴的檔案或資料夾，一律視為使用者資料。
- 使用者資料不得刪除、移動、改名、覆蓋或當成未追蹤暫存資料清理。
- 若使用者明確授權刪除未命名檔案或資料夾，必須紀錄路徑、原因、時間與授權來源。
- AI 下載或建立後作為來源依據的資料，需公開、可下載、可追溯且來源真實；例如公司公開 ESG 公文、公開財報、政府常見缺失、國際法規條文。

## 2026-06-09 新增 ai-dispatch（AI 派工大軍）

- 新增 `ai-dispatch`：用 OpenCode CLI ＋ NVIDIA 免費模型（DeepSeek V4 Flash / Kimi 2.6 / Nemotron 3 Ultra）派工出工。軍師（Claude/Codex）規劃審查，士兵出工，軍師只讀 `result_*.md` 省 Token；支援平行 7 視窗。
- 跨專案、跨機器可用；含換新機自動 bootstrap（裝 `opencode-ai`、引導 build.nvidia.com 申請免費金鑰）。
- 觸發語以「派工」為主。預設行為：軍師自己用 Bash 跑 opencode、讀 result、只回報摘要。
- 安全：NVIDIA 金鑰存 `~/.local/share/opencode/auth.json`，絕不進 repo；機敏資料（學生姓名、內部 SOP 原文）不派給免費雲端模型。已掃描確認 skill 不含祕密。
- 已同步本機 `.codex` 與 `.claude`、Google Drive 備份、第二大腦 canonical、lazy-pack `skills/ai-dispatch` 與 `packages/ai-dispatch.zip`，並重建 `codex-personal-skills-bundle.zip`。

## 2026-06-08 全域檔案保護規範

- `project-init-sync`：專案初始化時，必須把 AI 下載/暫存命名規則、可追溯來源要求、未命名使用者資料不得刪除規則寫入 `AGENTS.md` 或專案藍圖。
- `startup-sync`：開工/專案繼續時，必須重讀並提醒上述規範。
- `shutdown-sync`：收工時，必須檢查本輪是否違反命名、來源與刪除紀錄規範。
- `skills-sync`：同步 skills 時必須保留並傳遞這些規範。
- 已更新四個 skill 目錄與 zip：`project-init-sync`、`startup-sync`、`shutdown-sync`、`skills-sync`。

## 2026-06-08 補強：換電腦仍須套用

- 使用者回報換電腦後 agent 建立 `暫存.txt`、`下載.txt`，未依全域命名規則操作。
- 已將 `暫存.txt`、`下載.txt` 列為明確違規例，並要求開工/專案繼續不得反問是哪條規定；應直接依本全域規範修正。
- 已補強：使用者要求建立暫存/下載示範檔且未指定內容時，可建立最小示範內容，但檔名仍必須合規；不可先建立 `暫存.txt` / `下載.txt` 再反問內容。
- 已同步本機、第二大腦 canonical、Google Drive 備份、lazy-pack skills 與 zip。

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

## 2026-05-26 html-training-deck 補資料

- `html-training-deck` 已補入新勝 GDP HTML 內訓踩坑：文件點擊互動、部門文件閱讀地圖、GDP 智慧查詢、FAQ 點擊與輸入一致性、learner-facing HTML 不顯示使用者回饋或 `更新者：system`。
- 已補入互動定義：優先使用滑桿、拖拉、篩選、勾選、點擊解說、互動圖表等可操作學習，不把 hover/parallax 說明當作主要互動。
- 已補入資料正確性規則：第一章至第八章需盤點，時程目錄只作參考，正式內容以 SOP/WI/FR 原文為主，有出入需回報。
- 已更新 `html-training-deck.zip` 與 `codex-personal-skills-bundle.zip`。

## 2026-05-26 html-evidence-training-builder 新增

- 新增 `html-evidence-training-builder`：使用者提供資料製作 HTML 資料庫/教材時，先做來源盤點、可追溯資料庫索引、Firestore 同步，再做視覺化互動與 image2/imagegen 規劃。
- 已同步本機、Google Drive skills 備份、第二大腦 canonical、lazy-pack repo。
- 已新增 `html-evidence-training-builder.zip` 並重建 `codex-personal-skills-bundle.zip`。
