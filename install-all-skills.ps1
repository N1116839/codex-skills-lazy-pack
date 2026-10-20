# Copy personal skills with backups; preserve unrelated local files.
param([string[]]$TargetRoots = @(
    (Join-Path $env:USERPROFILE '.codex\skills'),
    (Join-Path $env:USERPROFILE '.claude\skills')
))
$ErrorActionPreference = 'Stop'
function Get-SkillHash([string]$Path) {
    $stream = [IO.File]::OpenRead($Path)
    $algorithm = [Security.Cryptography.SHA256]::Create()
    try { return [BitConverter]::ToString($algorithm.ComputeHash($stream)) }
    finally { $stream.Dispose(); $algorithm.Dispose() }
}
$source = Join-Path $PSScriptRoot 'skills'
if (!(Test-Path -LiteralPath $source -PathType Container)) { throw "Missing skills: $source" }
$stamp = Get-Date -Format 'yyyyMMdd_HHmmss_fffffff'
$skills = @(Get-ChildItem -LiteralPath $source -Directory | Where-Object { $_.Name -ne '.system' })
foreach ($target in $TargetRoots) {
    $targetPath = [System.IO.Path]::GetFullPath($target)
    $backupRoot = Join-Path (Split-Path $targetPath -Parent) "backups\codex_skills_$stamp"
    foreach ($skill in $skills) {
        $destination = Join-Path $targetPath $skill.Name
        foreach ($file in (Get-ChildItem -LiteralPath $skill.FullName -Recurse -File)) {
            if ($file.FullName -match '[\\/]__pycache__[\\/]' -or $file.Extension -eq '.pyc') { continue }
            if ($file.Attributes -band [IO.FileAttributes]::ReparsePoint) { throw "Refusing linked source: $($file.FullName)" }
            $relative = $file.FullName.Substring($skill.FullName.Length + 1)
            $out = Join-Path $destination $relative
            $outParent = Split-Path $out -Parent
            New-Item -ItemType Directory -Force -Path $outParent | Out-Null
            $checkDir = Get-Item -LiteralPath $outParent
            while ($null -ne $checkDir) {
                if ($checkDir.Attributes -band [IO.FileAttributes]::ReparsePoint) { throw "Refusing linked destination: $outParent" }
                $checkDir = $checkDir.Parent
            }
            if (Test-Path -LiteralPath $out) {
                if ((Get-Item -LiteralPath $out).Attributes -band [IO.FileAttributes]::ReparsePoint) { throw "Refusing linked destination: $out" }
                if ((Get-SkillHash $out) -eq (Get-SkillHash $file.FullName)) { continue }
                $backup = Join-Path (Join-Path $backupRoot $skill.Name) $relative
                New-Item -ItemType Directory -Force -Path (Split-Path $backup -Parent) | Out-Null
                Copy-Item -LiteralPath $out -Destination $backup
            }
            Copy-Item -LiteralPath $file.FullName -Destination $out -Force
            if ((Get-SkillHash $out) -ne (Get-SkillHash $file.FullName)) { throw "Copy mismatch: $out" }
        }
    }
    Write-Host "Installed $($skills.Count) skills at $targetPath; changed originals backed up at $backupRoot when needed."
}
Write-Host 'Restart skill discovery. Codex continuity hooks require separate installation and user trust; see README.'
