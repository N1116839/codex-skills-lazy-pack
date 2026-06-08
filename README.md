# Codex Skills Lazy Pack

**一鍵安裝個人 Skills + MCP 環境設定**

> ✅ 同時支援 **OpenAI Codex**（`.codex/`）與 **Claude Code**（`.claude/`）。
> Skills 相容兩者，安裝腳本自動判斷目標環境。

換電腦？新電腦？跑完這份 lazy pack，5 分鐘恢復完整工作環境。

---

## 包含什麼？

### 個人 Skills（8 個）

| Skill | 說明 | 觸發詞 |
|-------|------|--------|
| `evidence-based-content` | 資料正確性與可追溯標準 | 校對資料庫、查文獻、驗證資料 |
| `gas-targeted-fix` | 精準修正 Google Apps Script | 幫我修正程式碼、改程式、修正 GAS |
| `html-evidence-training-builder` | 建立可追溯 HTML 訓練資料庫 | 建立訓練頁、KB、知識庫 |
| `html-training-deck` | 建立 HTML 教育訓練簡報 | HTML 簡報、內部教育訓練 |
| `project-init-sync` | 初始化班級工具工作模式 | 初始化專案、老師建專案模式 |
| `shutdown-sync` | 收工三方同步 | 收工、先收工、結束工作、換電腦 |
| `startup-sync` | 開工接續上次工作 | 開工、上次做到哪、接續工作 |
| `skills-sync` | 備份與同步 skills | 更新 skills、同步 skills、備份 skills |

> 💡 Codex 使用者：skills 安裝在 `%USERPROFILE%\.codex\skills`，觸發詞與 Claude 版共用。

### MCP 伺服器設定腳本

- Obsidian（mcpvault）：讓 AI 讀寫你的筆記庫
- Firebase：讓 AI 直接操作 Firestore 資料
- NotebookLM（nlm）：讓 AI 操控 NotebookLM
- SessionEnd hook：忘記收工時的安全網（自動備份）

---

## 快速安裝

### Windows（一次安裝 skills + MCP + hook）

```powershell
# 1. 下載本 repo（或 git clone）
git clone https://github.com/N1116839/codex-skills-lazy-pack.git
cd codex-skills-lazy-pack

# 2. 安裝所有 skills
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\install-all-skills.ps1

# 3. 設定 MCP + SessionEnd hook（會問你 vault 路徑）
.\setup-mcp.ps1
```

### macOS / Linux

```bash
git clone https://github.com/N1116839/codex-skills-lazy-pack.git
cd codex-skills-lazy-pack
bash install-all-skills.sh
bash setup-mcp.sh
```

### 只裝 skills（不動 MCP）

```powershell
# Windows
.\install-all-skills.ps1

# macOS/Linux
bash install-all-skills.sh
```

---

## 分開安裝說明

某些 MCP 需要手動登入，分開處理：

| 工具 | 安裝後要做的事 |
|------|--------------|
| Obsidian MCP | 確認 vault 路徑正確後重啟 Claude Code |
| Firebase MCP | 終端機執行 `npx firebase-tools login` |
| NotebookLM MCP | 終端機執行 `nlm login` |
| SessionEnd hook | 自動設定，無需額外操作 |

---

## 換電腦完整流程

1. 新電腦安裝 **OpenAI Codex**（[下載 Desktop app](https://developers.openai.com/codex/app)）或 **Claude Code**（Pro 方案）
2. 安裝基礎工具：Git、Node.js、uv（看[#00 環境建置](https://github.com/mathruffian-dot/codex-lazy-packs)）
3. `git clone` 本 repo
4. 執行 `install-all-skills.ps1`（Windows）或 `install-all-skills.sh`（mac）
5. 執行 `setup-mcp.ps1` / `setup-mcp.sh`，輸入 vault 路徑
6. 重啟 AI agent
7. 說「開工」驗證

---

## 跨 AI 相容性說明

Skills 的觸發描述已設計為**繁體中文 + 英文雙語**，確保：
- Claude Code（任何 Claude 模型）✅
- 其他 AI 工具若支援讀取 SKILL.md 也能觸發 ✅

Cursor / GitHub Copilot 不支援 SKILL.md 格式，需另行設定 `.cursorrules` 或 `.github/copilot-instructions.md`。

---

## 資料夾結構

```
codex-skills-lazy-pack/
├── skills/                    ← 8 個個人 skills
│   ├── evidence-based-content/
│   ├── gas-targeted-fix/
│   ├── html-evidence-training-builder/
│   ├── html-training-deck/
│   ├── project-init-sync/
│   ├── shutdown-sync/
│   ├── skills-sync/
│   └── startup-sync/
├── scripts/
│   └── session-cleanup.sh     ← SessionEnd hook script
├── packages/                  ← 個別 ZIP 包
├── install-all-skills.ps1     ← Windows 一鍵安裝 skills
├── install-all-skills.sh      ← macOS/Linux 一鍵安裝 skills
├── setup-mcp.ps1              ← Windows MCP + hook 設定
├── setup-mcp.sh               ← macOS/Linux MCP + hook 設定
└── SKILLS_INDEX.md            ← 詳細索引
```

---

## 更新紀錄

| 日期 | 更新內容 |
|------|---------|
| 2026-06-08 | 補強換電腦規則：`暫存.txt`、`下載.txt` 明確列為違規命名；開工時應直接套用全域規範，不得反問是哪條規定 |
| 2026-06-08 | 新增全域 AI 檔案保護規範：暫存檔 `_暫存`、下載檔 `AI名稱_`、未命名檔案視為使用者資料不得刪除；更新 project-init/startup/shutdown/skills-sync 與 zip |
| 2026-05-29 | 改為 public；加入跨電腦 MCP 安裝腳本、SessionEnd hook、macOS/Linux 支援 |
| 2026-05-25 | 同步 6 個 personal skills、更新 shutdown-sync 與 html-training-deck |
| 2026-05-22 | 初版建立 |

## 全域 AI 檔案保護規範

- Agent 測試暫存檔：檔名結尾需加 `_暫存`。
- Agent 網路下載檔：檔名前綴需加 AI 名稱，例如 `codex_檔案名稱`。
- `暫存.txt`、`下載.txt`、`test.txt`、`temp.docx` 都是違規例，不可作為 agent 建立的暫存或下載檔。
- 沒有 `AI名稱_` 前綴、也沒有 `_暫存` 後綴的檔案或資料夾，一律視為使用者資料，不可刪除、移動、改名、覆蓋或清理。
- 使用者授權刪除未命名檔案時，必須紀錄路徑、原因、時間與授權來源。
- AI 使用的下載來源需公開、可下載、可追溯且來源真實；例如公司公開 ESG 公文、公開財報、政府常見缺失、國際法規條文。
