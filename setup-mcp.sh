#!/bin/bash
# setup-mcp.sh
# Configures MCP servers for Claude Code on macOS / Linux.
# Requires: Node.js, npm (or npx), uv already installed.
# Usage: bash setup-mcp.sh
#        bash setup-mcp.sh --vault "/Users/me/my-vault"

set -e

VAULT_PATH=""
while [[ $# -gt 0 ]]; do
    case "$1" in
        --vault) VAULT_PATH="$2"; shift 2 ;;
        *) shift ;;
    esac
done

SETTINGS="$HOME/.claude/settings.json"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

log()    { echo "$1"; }
log_ok() { echo "  [OK] $1"; }
log_w()  { echo "  [!!] $1"; }

# --- Step 1: Prerequisites ---
log "=== Step 1: Checking prerequisites ==="
node --version &>/dev/null && log_ok "Node.js: $(node --version)" || { log_w "Node.js not found. Install from https://nodejs.org"; exit 1; }
npm --version &>/dev/null && log_ok "npm: $(npm --version)" || { log_w "npm not found"; exit 1; }

# --- Step 2: mcpvault ---
log ""
log "=== Step 2: Installing mcpvault (Obsidian MCP) ==="
if command -v mcpvault &>/dev/null; then
    log_ok "mcpvault already installed: $(mcpvault --version 2>/dev/null || echo 'ok')"
else
    npm install -g "@bitbonsai/mcpvault" && log_ok "mcpvault installed" || log_w "mcpvault install failed"
fi
MCPVAULT_PATH=$(command -v mcpvault 2>/dev/null || echo "mcpvault")

# --- Step 3: firebase-tools ---
log ""
log "=== Step 3: firebase-tools (Firebase MCP) ==="
log_ok "firebase-tools available via npx (no global install needed)"

# --- Step 4: nlm ---
log ""
log "=== Step 4: Installing nlm (NotebookLM MCP) ==="
if command -v nlm &>/dev/null; then
    log_ok "nlm already installed: $(nlm --version 2>/dev/null)"
else
    if command -v uv &>/dev/null; then
        uv tool install notebooklm-mcp-cli && log_ok "nlm installed" || log_w "nlm install failed"
    else
        log_w "uv not found. Install: curl -LsSf https://astral.sh/uv/install.sh | sh"
    fi
fi
NLM_PATH=$(command -v nlm 2>/dev/null || echo "")

# --- Step 5: Vault path ---
log ""
log "=== Step 5: Obsidian vault path ==="
if [ -z "$VAULT_PATH" ]; then
    read -r -p "Enter your Obsidian vault path (e.g. ~/Documents/my-vault): " VAULT_PATH
    VAULT_PATH="${VAULT_PATH/#\~/$HOME}"
fi
[ -d "$VAULT_PATH" ] && log_ok "Vault found: $VAULT_PATH" || log_w "Vault not found at $VAULT_PATH - configure manually later"

# --- Step 6: Write settings.json ---
log ""
log "=== Step 6: Writing ~/.claude/settings.json ==="
mkdir -p "$(dirname "$SETTINGS")"

# Read existing settings (preserve other keys)
if [ -f "$SETTINGS" ]; then
    EXISTING=$(cat "$SETTINGS")
else
    EXISTING="{}"
fi

# Use python to merge (available on macOS/Linux)
python3 - <<PYEOF
import json, sys

settings_path = "$SETTINGS"
vault_path = "$VAULT_PATH"
mcpvault_path = "$MCPVAULT_PATH"
nlm_path = "$NLM_PATH"

try:
    with open(settings_path) as f:
        d = json.load(f)
except:
    d = {}

mcp = {
    "obsidian": {"command": mcpvault_path, "args": [vault_path]},
    "firebase": {"command": "npx", "args": ["-y", "firebase-tools@latest", "mcp"]}
}
if nlm_path:
    mcp["notebooklm"] = {"command": nlm_path}

d["mcpServers"] = mcp
d["hooks"] = {
    "SessionEnd": [{"hooks": [{"type": "command", "command": "bash ~/.claude/scripts/session-cleanup.sh"}]}]
}

with open(settings_path, "w") as f:
    json.dump(d, f, indent=2, ensure_ascii=False)
print("  [OK] settings.json written")
PYEOF

# --- Step 7: session-cleanup.sh ---
log ""
log "=== Step 7: Installing SessionEnd hook ==="
SCRIPTS_DIR="$HOME/.claude/scripts"
mkdir -p "$SCRIPTS_DIR"
HOOK_SRC="$SCRIPT_DIR/scripts/session-cleanup.sh"
if [ -f "$HOOK_SRC" ]; then
    cp "$HOOK_SRC" "$SCRIPTS_DIR/session-cleanup.sh"
    chmod +x "$SCRIPTS_DIR/session-cleanup.sh"
    log_ok "session-cleanup.sh installed"
else
    log_w "scripts/session-cleanup.sh not found in this repo - skipping"
fi

log ""
log "=============================================="
log "MCP setup complete!"
log "Next steps:"
log "  1. Run 'nlm login' to authenticate NotebookLM"
log "  2. Run 'npx firebase-tools login' to authenticate Firebase"
log "  3. Restart Claude Code completely"
log "  4. Test: ask Claude to list your Obsidian vault or Firebase projects"
log "=============================================="
