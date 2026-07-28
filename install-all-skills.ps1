# install-all-skills.ps1
# Installs all personal skills to Codex and Claude Code.
# Works on any Windows computer. Run from the folder this script is in.
# Usage: .\install-all-skills.ps1

$ErrorActionPreference = 'Stop'

$source = Join-Path $PSScriptRoot 'skills'
$targets = @(
    (Join-Path $env:USERPROFILE '.codex\skills'),
    (Join-Path $env:USERPROFILE '.claude\skills')
)

if (!(Test-Path -LiteralPath $source)) {
    throw "Cannot find bundled skills folder: $source"
}

$installed = @()
Get-ChildItem -LiteralPath $source -Directory | Where-Object { $_.Name -ne '.system' } | ForEach-Object {
    foreach ($target in $targets) {
        New-Item -ItemType Directory -Force -Path $target | Out-Null
        $dest = Join-Path $target $_.Name
        if (Test-Path -LiteralPath $dest) { Remove-Item -LiteralPath $dest -Recurse -Force }
        Copy-Item -LiteralPath $_.FullName -Destination $dest -Recurse -Force
    }
    $installed += $_.Name
    Write-Host "  [OK] Installed skill: $($_.Name)"
}

Write-Host ""
Write-Host "Done. Installed $($installed.Count) skills to Codex and Claude Code."
Write-Host "Restart the agent so newly installed skills are detected."
