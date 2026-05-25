# Codex Skills Lazy Pack

這個 repo 用來備份與搬移使用者的個人 Codex skills。預設為私人 repo。

## 安裝到新電腦

1. 安裝 Codex。
2. 確認資料夾存在：

`powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.codex\skills"
`

3. 從本 repo 的 skills/ 複製需要的 skill 到：

`	ext
%USERPROFILE%\.codex\skills\<skill-name>
`

或解壓 packages/<skill-name>.zip，再把內層 skill 資料夾放到 %USERPROFILE%\.codex\skills。

## 目前包含

- gas-targeted-fix
- html-training-deck
- project-init-sync
- shutdown-sync
- skills-sync
- startup-sync

## 最新同步

2026-05-25 16:45 已重新同步本機 personal skills、Google Drive 備份、ZIP 懶人包與本 repo。

本次更新重點：

- `shutdown-sync`：補上換電腦前收工規則，要求用精準繁體中文記錄完成事項、未完成事項、踩坑點、驗證結果，並將未完成事項納入版本控制。
- `html-training-deck`：補上年度行事曆與關鍵設備行事曆的視覺規則，避免來源、依頻率分組與本頁 SOP 重複。
- 已做明顯敏感資訊掃描，未發現需排除的金鑰或 token。

## 不打包的內容

.system 是 Codex 內建 skill，只在 SKILLS_INDEX.md 做索引，不預設上傳為個人懶人包。

## 口令

當使用者說「更新skills」時，應同步本機、第二大腦、Google Drive 懶人包與 GitHub repo。
## 一次安裝全部 skills

本 repo 同時提供單一 skill ZIP 與整包懶人包。

整包檔案：`packages/codex-personal-skills-bundle.zip`

新電腦安裝方式：

1. 下載並解壓 `codex-personal-skills-bundle.zip`。
2. 在解壓後資料夾執行：

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\install-all-skills.ps1
```

3. 重新啟動 Codex，讓 skills 被偵測。

第二大腦 canonical source：`G:\我的雲端硬碟\我的第二大腦\Codex標準\skills`。
之後說「建立skills」時，先在第二大腦建立或更新，再同步到本機、Google Drive 備份與 GitHub lazy-pack。
