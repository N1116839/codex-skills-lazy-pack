# install-all-skills.ps1
# Installs all personal skills to Claude Code (~/.claude/skills/)
# Works on any Windows computer. Run from the folder this script is in.
# Usage: .\install-all-skills.ps1

$ErrorActionPreference = 'Stop'

$source = Join-Path $PSScriptRoot 'skills'
$claudeTarget = Join-Path $env:USERPROFILE '.claude\skills'

if (!(Test-Path -LiteralPath $source)) {
    throw "Cannot find bundled skills folder: $source"
}

New-Item -ItemType Directory -Force -Path $claudeTarget | Out-Null

$installed = @()
Get-ChildItem -LiteralPath $source -Directory | Where-Object { $_.Name -ne '.system' } | ForEach-Object {
    $dest = Join-Path $claudeTarget $_.Name
    if (Test-Path -LiteralPath $dest) { Remove-Item -LiteralPath $dest -Recurse -Force }
    Copy-Item -LiteralPath $_.FullName -Destination $dest -Recurse -Force
    $installed += $_.Name
    Write-Host "  [OK] Installed skill: $($_.Name)"
}

Write-Host ""
Write-Host "Done. Installed $($installed.Count) skills to: $claudeTarget"
Write-Host "Restart Claude Code so newly installed skills are detected."
