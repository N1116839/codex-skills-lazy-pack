---
name: ai-dispatch
description: 用 OpenCode CLI ＋ NVIDIA 免費模型組成「AI 大軍」派工出工，省下昂貴 Token。當使用者說「派工」「派給士兵」「叫大軍做」「用 opencode 做」「headless 派工」「無頭派工」「平行派工」「開七個視窗」「dispatch」或要把大量寫程式/生成內容的工作交給便宜模型執行時觸發。軍師（Claude/Codex）負責規劃與審查，OpenCode 士兵負責出工；軍師只讀 result_*.md，不吃士兵的全程對話。可跨專案、跨機器使用。
---

# AI 派工大軍（ai-dispatch）

## 角色分工

| 角色 | 是誰 | 做什麼 |
|---|---|---|
| 軍師 / 總指揮 | Claude Code 或 Codex（你我） | 規劃、寫計畫書、派工、審查、驗收、回報 |
| 士兵 | OpenCode CLI ＋ NVIDIA 免費模型 | 出工：寫程式、生成內容、批次產出 |

核心原則：**規劃用聰明的軍師，出工用便宜的大軍。軍師只讀 `result_*.md`，不把士兵的整段對話塞進自己的 context（省 Token）。**

## 觸發後的預設行為

使用者說「派工 …」時，**軍師自己用 Bash 執行 opencode、讀 `result_*.md`、只回報摘要**。不要把士兵的完整輸出灌回對話。

- **1～2 件小任務**：直接前景或背景跑，跑完讀 result 回報。
- **大量同類任務**：拆成 `task_unit1..N.md`，可多個背景並行（或請使用者開多視窗），軍師逐一讀 `result_unitN.md`。

## 前置檢查（換新機自動 bootstrap）

派工前先確認環境，缺什麼就補：

1. **OpenCode 是否安裝**：`opencode --version`
   - 沒有 → `npm i -g opencode-ai@latest`（需 Node 18+；npm 套件名是 `opencode-ai`，不是 `opencode`）。
2. **NVIDIA 免費金鑰是否接好**：`opencode auth list`（看有沒有 `Nvidia api`）
   - 沒有 → 引導使用者：
     1. 到 https://build.nvidia.com 用**個人**信箱註冊開發者帳號（教育帳號拿不到 key）。
     2. 建立 NVIDIA 雲端帳號時，帳號名稱**只能用英數和連字號**（中文/空格會 `Invalid NCA name` 失敗）。
     3. 帳號頭像 → API Keys → Generate（名稱填 OpenCode、選 Never expire）→ 複製 `nvapi-...`。
     4. 終端機 `opencode auth login` → 選 NVIDIA → 貼 key。
   - 🔑 金鑰存在 `~/.local/share/opencode/auth.json`（使用者設定區）。**絕不可寫進任何 repo / task / result 檔。**

## 士兵模型（NVIDIA，已驗證 ID）

```
nvidia/deepseek-ai/deepseek-v4-flash       ← 主力：百萬上下文，寫程式/生成文字（預設用這個）
nvidia/moonshotai/kimi-k2.6                ← 多模態（看得懂圖片）/ 需要較強推理時
nvidia/nvidia/nemotron-3-ultra-550b-a55b   ← 大型推理備選
```

免費限制：約 40 次/分鐘、人多會排隊變慢、不保證穩定（適合開發/批次，不適合正式生產服務）。

## 標準派工流程

1. **軍師寫計畫書** → 在「當前專案」根目錄的 `dispatch/task_<名稱>.md` 寫清楚規格（越明確越好，士兵不必猜）。
   - 若當前專案沒有 `dispatch/`，先建立，並用本檔末的 task 模板起頭。
2. **派工執行**（軍師用 Bash 跑；長任務用背景）：
   ```bash
   opencode run -m nvidia/deepseek-ai/deepseek-v4-flash --dangerously-skip-permissions --dir . \
     "請讀取 dispatch/task_<名稱>.md，完成任務後把結果摘要寫進 dispatch/result_<名稱>.md"
   ```
   - `--dangerously-skip-permissions`＝無頭派工，士兵不會卡在確認對話（headless）。
   - `--dir .`＝在當前專案目錄作業。
3. **軍師只讀 result**：`dispatch/result_<名稱>.md`。**不要讀士兵的完整對話/事件流。**
4. **寫程式類驗收**：只看 `git diff`（哪些檔、改幾行、有疑慮才細看），不讀整檔全文。
5. **回報**：把 result 摘要 + 驗收結論講給使用者，不貼士兵的長輸出。

## 平行派工（最高 7 倍速）

拆成 `task_unit1.md`…`task_unitN.md`，每單元一條指令並行（軍師可開多個背景 Bash，或請使用者開多個 PowerShell 視窗）：
```bash
opencode run -m nvidia/deepseek-ai/deepseek-v4-flash --dangerously-skip-permissions \
  "讀 dispatch/task_unit1.md，結果寫 dispatch/result_unit1.md"
```
軍師逐一讀 `result_unitN.md` 驗收。Token 燃燒 = N 倍，但軍師端只付「讀結果」的成本。

## Token 節省鐵則

- 士兵執行中，軍師不需盯著看。
- 結論落地到固定小檔 `result_*.md`；中間過程不入軍師 context。
- 只取尾端結論，不要把整條事件流灌回來。
- 寫程式驗收看 git diff，不讀全文。
- 軍師 context 盡量壓在 50～60% 以下（越滿每輪重讀越燒）。

## 邊界與安全

- **機敏資料不派給免費雲端模型**：學生姓名、成績、公司內部 SOP 原文等，不可丟給 NVIDIA 免費模型（資料可能被用於改進模型）。需處理機敏資料時改用本地模型（如 Ollama Gemma），或先去識別化。呼應各專案 AGENTS.md「不存學生姓名」。
- **金鑰永不進 repo**。
- 規格不清、跨專案邊界不明、會動到權限/部署時 → 先問使用者，不自行猜。

## task_<名稱>.md 模板

```markdown
# 任務：[任務名稱]

## 目標
[一句話說明要做什麼]

## 規格
[詳細規格，越清楚越好，士兵不需要猜]

## 輸出要求
- 產出檔案：[路徑]
- 完成後把結果摘要寫進：dispatch/result_[任務名稱].md
- result 內容：完成狀態（成功/失敗）、產出了哪些檔案、有問題就列出問題點

## 注意事項
[特別提醒；機敏資料不可外流到雲端]
```

## 跨機 / 跨 Codex 同步

本 skill 同時放在 `~/.claude/skills/ai-dispatch/` 與 `~/.codex/skills/ai-dispatch/`。
使用者說「更新skills」時由 skills-sync 打包到 GitHub lazy-pack ＋ 第二大腦 ＋ Google Drive，換機可還原、Codex 也吃得到。換機後第一次派工，靠上面「前置檢查」自動補裝 opencode 與引導 NVIDIA key。
