---
name: skills-sync
description: 同步、備份、打包與上傳 Codex skills。Use when the user says 更新skills、同步skills、備份skills、上傳skills到GitHub、建立skills懶人包、換電腦恢復skills、把skills放入第二大腦，或要求 Codex 同步本機 skills、第二大腦、Google Drive 懶人包與 GitHub skills repo.
---

# Skills Sync

Use this workflow when the user asks to update, back up, package, restore, or publish Codex skills.

## Scope

- Personal skills live in `%USERPROFILE%\.codex\skills`, excluding `.system`.
- System skills under `.system` are indexed in notes but not copied to GitHub packages unless the user explicitly asks and licensing/ownership is clear.
- Google Drive backup root: `G:\我的雲端硬碟\2026codex\skills`.
- GitHub lazy-pack repo: `N1116839/codex-skills-lazy-pack`.
- Second Brain project note: `G:\我的雲端硬碟\我的第二大腦\專案\2026codex AI測試.md`.
- Lazy-pack index note: `G:\我的雲端硬碟\2026codex\01.5-Codex必裝Skills與Plugins.md`.

## Required Workflow

1. Read the current local skills list from `%USERPROFILE%\.codex\skills`.
2. Separate personal skills from `.system` skills.
3. Scan personal skills for obvious secrets before packaging: API keys, tokens, passwords, private keys.
4. Copy each personal skill to the Google Drive backup root.
5. Create or update individual zip packages for each personal skill.
6. Update the skills GitHub lazy-pack repo with `skills/<skill-name>/`, `packages/<skill-name>.zip`, `SKILLS_INDEX.md`, `README.md`, and install/update instructions.
7. Update the Second Brain with full skills inventory, local path, Google Drive backup path, GitHub repo URL, restore steps for a new computer, latest update timestamp, and unresolved risks.
8. Update the lazy-pack note with any new or changed skills.
9. Commit and push the skills repo when GitHub authentication is available. Prefer a private repo unless the user explicitly requests public.
10. Report what changed, what was uploaded, and any skipped items.

## Rules

- Do not upload `.system` skills as personal packages by default.
- Do not include secrets, tokens, credentials, `.env`, cache folders, or generated build output.
- Use UTF-8 safe reading/writing for Traditional Chinese notes.
- When the user says `更新skills`, treat it as a request to update Second Brain and GitHub together, not only local files.
- If GitHub push fails, still update local Google Drive backup and Second Brain, then report the blocker.
## 2026-05-25 Canonical Second Brain Rule

- Canonical human-readable source for personal skills: `G:\我的雲端硬碟\我的第二大腦\Codex標準\skills`.
- When the user says `建立skills`, create or update the skill in the Second Brain canonical folder first, then sync to `%USERPROFILE%\.codex\skills`, `G:\我的雲端硬碟\2026codex\skills`, and `codex-skills-lazy-pack`.
- GitHub lazy-pack must include both individual skill ZIP files and one all-in-one package: `packages/codex-personal-skills-bundle.zip`.
- The all-in-one package must contain `skills/` and `install-all-skills.ps1` so a new computer can install every personal skill in one step.
