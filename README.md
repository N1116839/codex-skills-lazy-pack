# Codex Skills Lazy Pack

可攜的個人技能與選用環境工具。技能可供支援 SKILL.md 的代理讀取；各產品的 Hook 與設定格式需分開配置。

## 個人技能（12 個）

| Skill | 用途／觸發 |
|---|---|
| ai-dispatch | OpenCode 派工；派工、派給士兵 |
| evidence-based-content | 資料正確性與來源追溯；校對資料庫、查文獻 |
| gas-targeted-fix | 精準修程式；修正 GAS、改程式 |
| html-evidence-training-builder | 可追溯 HTML 訓練資料庫 |
| html-training-deck | HTML 教育訓練簡報 |
| project-init-sync | 依專案需要建立唯一現況入口與接續環境；初始化專案 |
| startup-sync | 開工恢復、工作中保存、交付前重核；開工、繼續專案 |
| shutdown-sync | 收工結算事件、去重並依既有授權同步；收工、換電腦 |
| skills-sync | 技能備份、打包與 GitHub 同步 |
| rdq | 需求探索與規格卡；用 RDQ、先訪談我 |
| research-content-organization | 依實際內容整理研究資料 |
| speak-human-tw | 繁體中文去 AI 味；說人話、改自然一點 |

## 安裝與換機

```powershell
git clone https://github.com/N1116839/codex-skills-lazy-pack.git
cd codex-skills-lazy-pack
.\install-all-skills.ps1
```

macOS／Linux 執行 `bash install-all-skills.sh`。腳本將技能複製至 `.codex/skills` 與 `.claude/skills`；改寫前備份有差異的同名檔案，保留本機額外檔案，不刪整個技能目錄。備份在對應工具目錄的 `backups/codex_skills_<時間>`。重新啟動技能探索後生效。

個別 ZIP 位於 `packages/`，整包為 `packages/codex-personal-skills-bundle.zip`。初始化、開工、收工三技能共用 startup-sync 的規範與程式，請一起安裝。`.system` 只列索引，不打包。

## 長任務接續（2026-10-20）

- 唯一工作筆記現行區保存任務、底稿、更正、進度與下一步；AGENTS／README 等只作入口。使用者決策在工作中即保存，收工再結算。
- 同專案同根因第 3 次提升專案重要規則，第 5 次提升全域；歷史累計不歸零。同次澄清不重算，新交付再犯另計。先保存可追溯證據，再移除活躍重複文字。
- Firebase、其他資料庫與部署按專案需要選用；保留已有配置。初始化不再強制套用班級工具。
- 專案建立 `.project-workflow.json` 才選用檢查器；沒有此檔的專案不受 Hook 影響。狀態與私人事件帳留在專案／vault，不上傳本 repo。

詳見 [共用接續協定](skills/startup-sync/references/workflow.md)。Python 3.10+，執行程式僅需標準庫。

```text
python <startup-sync>/scripts/project_workflow.py validate --project <專案>
python <startup-sync>/scripts/install_hooks.py --dry-run
python <startup-sync>/scripts/install_hooks.py
```

安裝器合併 Codex 的 SessionStart（含 compact）、UserPromptSubmit 與 Stop，保留其他 Hook，不修改模型、MCP 或資料庫。換機要重新安裝 Hook，以刷新 Python 與腳本路徑；可用 `--uninstall` 移除本工具事件。

**Codex 要求使用者在 `/hooks` 審閱並信任確切定義，安裝腳本不代為授予信任。** 尚未信任、主機不支援或未實測觸發時，以人工重讀模式運作。配置成功不等於已啟用；程式回傳的 receipt 也不證明內容理解正確。主機未提供 turn_id 時會明示無法強制本輪 receipt。實際自動壓縮效果須在使用者環境另驗。

產品來源：[Codex Hooks](https://learn.chatgpt.com/docs/hooks)。本次以 Codex 0.160.1 的功能與 hooks/list 驗證格式；行為測試含模擬壓縮事件，不冒稱已觀察真實壓縮。

## 選用 MCP 與舊工具

既有 `setup-mcp.ps1`／`setup-mcp.sh` 及 `scripts/session-cleanup.sh` 保留為獨立工具；不是本次接續 Hook 的安裝流程。它們有各自的服務、登入與 SessionEnd 預設，執行前先核對實際產品與需要，不作所有新專案的必跑步驟。Firebase、NotebookLM、Obsidian 只在需要時配置。

## 驗證與資料保護

```text
python -m unittest discover -s skills/startup-sync/tests -v
```

測試涵蓋來源與manifest變更、中文路徑、跨專案隔離、缺失來源、模擬compact、receipt與Stop有限提醒、事件3／5去重、Hook合併及錯誤輸出。工程測試與實際內容驗收分開。

暫存以 `_暫存` 結尾、下載以AI名稱如 `codex_` 開頭。不擅刪改使用者原件、唯一來源或Clippings；有授權清理須記錄絕對路徑、原因與實測。不上傳密鑰、私人原稿、現況、receipt或測試快取。來源須真實可追溯，使用者合法提供的私人材料亦可在授權範圍核讀。

細項見 [SKILLS_INDEX.md](SKILLS_INDEX.md)。歷史更新紀錄不覆蓋目前技能內容。
