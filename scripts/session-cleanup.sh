#!/bin/bash
# SessionEnd safety net: auto-commit+push if GDrive repo has uncommitted changes when session ends

LOG_FILE="$HOME/.claude/scripts/session-cleanup.log"
log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"; }

INPUT=$(cat 2>/dev/null || echo "")
WORKDIR=$(echo "$INPUT" | python -c "import sys, json; d=json.load(sys.stdin); print(d.get('cwd', ''))" 2>/dev/null)
[ -z "$WORKDIR" ] && WORKDIR="$PWD"

log "========== SessionEnd triggered =========="
log "Working dir: $WORKDIR"

case "$WORKDIR" in
    *雲端硬碟*) ;;
    *"My Drive"*) ;;
    *) log "  -> Not a GDrive dir, skipping"; exit 0 ;;
esac

cd "$WORKDIR" || exit 0
[ -d ".git" ] || exit 0

git config windows.appendAtomically false 2>/dev/null
git add -u 2>/dev/null

if git diff --cached --quiet; then
    log "  -> No modified tracked files, skipping"
    exit 0
fi

REPO_NAME=$(basename "$WORKDIR")
git commit -m "[SessionEnd auto-save] $(date +'%Y-%m-%d %H:%M')

Auto-save by SessionEnd hook. See Obsidian working note: $REPO_NAME/工作筆記.md" >/dev/null 2>&1

git push origin HEAD >/dev/null 2>&1
log "  -> Committed and pushed"
