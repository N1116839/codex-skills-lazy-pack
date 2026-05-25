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


## 不打包的內容

.system 是 Codex 內建 skill，只在 SKILLS_INDEX.md 做索引，不預設上傳為個人懶人包。

## 口令

當使用者說「更新skills」時，應同步本機、第二大腦、Google Drive 懶人包與 GitHub repo。