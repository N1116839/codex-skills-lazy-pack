$ErrorActionPreference = 'Stop'
$source = Join-Path $PSScriptRoot 'skills'
$target = Join-Path $env:USERPROFILE '.codex\skills'
if(!(Test-Path -LiteralPath $source)){
  throw "Cannot find bundled skills folder: $source"
}
New-Item -ItemType Directory -Force -Path $target | Out-Null
Get-ChildItem -LiteralPath $source -Directory | Where-Object { $_.Name -ne '.system' } | ForEach-Object {
  $dest = Join-Path $target $_.Name
  if(Test-Path -LiteralPath $dest){ Remove-Item -LiteralPath $dest -Recurse -Force }
  Copy-Item -LiteralPath $_.FullName -Destination $dest -Recurse -Force
  Write-Host "Installed skill: $($_.Name)"
}
Write-Host "Done. Restart Codex so newly installed skills are detected."
