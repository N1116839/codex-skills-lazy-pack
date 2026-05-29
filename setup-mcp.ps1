# setup-mcp.ps1
# Configures MCP servers for Claude Code on Windows.
# Requires: Node.js, npm, uv already installed.
# Usage: .\setup-mcp.ps1 -VaultPath "G:\My Drive\my-vault"

param(
    [Parameter(Mandatory=$false)]
    [string]$VaultPath = ""
)

$ErrorActionPreference = 'Stop'
$settingsPath = Join-Path $env:USERPROFILE '.claude\settings.json'

# --- Helpers ---
function Ensure-Dir($p) { New-Item -ItemType Directory -Force -Path $p | Out-Null }
function Log($msg) { Write-Host $msg }
function LogOK($msg) { Write-Host "  [OK] $msg" -ForegroundColor Green }
function LogWarn($msg) { Write-Host "  [!!] $msg" -ForegroundColor Yellow }

# --- Step 1: Check prerequisites ---
Log "=== Step 1: Checking prerequisites ==="
try { $nodeVer = (node --version 2>&1); LogOK "Node.js: $nodeVer" } catch { LogWarn "Node.js not found. Install from https://nodejs.org" ; exit 1 }
try { $npmVer = (npm --version 2>&1); LogOK "npm: $npmVer" } catch { LogWarn "npm not found" ; exit 1 }

# --- Step 2: Install mcpvault (Obsidian MCP) ---
Log ""
Log "=== Step 2: Installing mcpvault (Obsidian MCP) ==="
$mcpvaultPath = Join-Path $env:APPDATA 'npm\mcpvault.cmd'
if (Test-Path $mcpvaultPath) {
    LogOK "mcpvault already installed at $mcpvaultPath"
} else {
    Log "  Installing mcpvault globally..."
    npm install -g "@bitbonsai/mcpvault" 2>&1 | Out-Null
    if (Test-Path $mcpvaultPath) { LogOK "mcpvault installed" }
    else { LogWarn "mcpvault install may have failed - check npm output" }
}

# --- Step 3: Install firebase-tools ---
Log ""
Log "=== Step 3: firebase-tools (Firebase MCP) ==="
try {
    $fbVer = (npx -y firebase-tools@latest --version 2>&1 | Select-String '^\d')
    LogOK "firebase-tools available via npx: $fbVer"
} catch { LogWarn "npx call failed - Node.js may not be set up correctly" }

# --- Step 4: Install notebooklm-mcp-cli (nlm) ---
Log ""
Log "=== Step 4: Installing nlm (NotebookLM MCP) ==="
try { $nlmVer = (nlm --version 2>&1); LogOK "nlm already installed: $nlmVer" }
catch {
    Log "  Installing notebooklm-mcp-cli via uv..."
    try {
        uv tool install notebooklm-mcp-cli 2>&1 | Out-Null
        LogOK "nlm installed. Run 'nlm login' to authenticate."
    } catch { LogWarn "uv not found or install failed. Install uv first: https://astral.sh/uv" }
}

# --- Step 5: Ask for vault path if not provided ---
Log ""
Log "=== Step 5: Obsidian vault path ==="
if ($VaultPath -eq "") {
    $VaultPath = Read-Host "Enter your Obsidian vault path (e.g. G:\My Drive\my-vault)"
}
if (!(Test-Path -LiteralPath $VaultPath)) {
    LogWarn "Vault path not found: $VaultPath"
    LogWarn "MCP will be configured anyway - fix the path in ~/.claude/settings.json later"
}

# --- Step 6: Write/update settings.json ---
Log ""
Log "=== Step 6: Writing ~/.claude/settings.json ==="
Ensure-Dir (Join-Path $env:USERPROFILE '.claude')

$existing = @{}
if (Test-Path $settingsPath) {
    try {
        $content = Get-Content $settingsPath -Raw -Encoding UTF8
        $existing = $content | ConvertFrom-Json
    } catch { LogWarn "Could not parse existing settings.json - will overwrite MCP section only" }
}

# Build new mcpServers object
$nlmExe = Join-Path $env:USERPROFILE '.local\bin\notebooklm-mcp.exe'
$mcpServers = [PSCustomObject]@{
    obsidian = [PSCustomObject]@{
        command = $mcpvaultPath
        args    = @($VaultPath)
    }
    firebase = [PSCustomObject]@{
        command = "npx.cmd"
        args    = @("-y", "firebase-tools@latest", "mcp")
    }
}

# Add notebooklm only if the exe exists
if (Test-Path $nlmExe) {
    $mcpServers | Add-Member -NotePropertyName notebooklm -NotePropertyValue ([PSCustomObject]@{ command = $nlmExe })
}

# Merge with existing settings
if ($existing.PSObject.Properties['mcpServers']) {
    $existing.mcpServers = $mcpServers
} else {
    $existing | Add-Member -NotePropertyName mcpServers -NotePropertyValue $mcpServers
}

# Add SessionEnd hook
$sessionHook = [PSCustomObject]@{
    SessionEnd = @(
        [PSCustomObject]@{
            hooks = @(
                [PSCustomObject]@{
                    type    = "command"
                    command = "bash $($env:USERPROFILE -replace '\\','/')/.claude/scripts/session-cleanup.sh"
                }
            )
        }
    )
}

if ($existing.PSObject.Properties['hooks']) {
    $existing.hooks = $sessionHook
} else {
    $existing | Add-Member -NotePropertyName hooks -NotePropertyValue $sessionHook
}

$existing | ConvertTo-Json -Depth 10 | Out-File $settingsPath -Encoding utf8
LogOK "settings.json written to $settingsPath"

# --- Step 7: Copy session-cleanup.sh ---
Log ""
Log "=== Step 7: Installing SessionEnd hook script ==="
$scriptsDir = Join-Path $env:USERPROFILE '.claude\scripts'
$hookScript = Join-Path $PSScriptRoot 'scripts\session-cleanup.sh'
if (Test-Path $hookScript) {
    Ensure-Dir $scriptsDir
    Copy-Item $hookScript (Join-Path $scriptsDir 'session-cleanup.sh') -Force
    LogOK "session-cleanup.sh installed"
} else {
    LogWarn "session-cleanup.sh not found in scripts\ - skipping hook"
}

Log ""
Log "=============================================="
Log "MCP setup complete!"
Log "Next steps:"
Log "  1. Run 'nlm login' in a terminal to authenticate NotebookLM"
Log "  2. Run 'npx firebase-tools login' in a terminal to authenticate Firebase"
Log "  3. Restart Claude Code completely"
Log "  4. Test: ask Claude to list your Obsidian vault or Firebase projects"
Log "=============================================="
