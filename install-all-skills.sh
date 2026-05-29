#!/bin/bash
# install-all-skills.sh
# Installs all personal skills to Claude Code (~/.claude/skills/)
# Works on macOS and Linux.
# Usage: bash install-all-skills.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE="$SCRIPT_DIR/skills"
CLAUDE_TARGET="$HOME/.claude/skills"

if [ ! -d "$SOURCE" ]; then
    echo "ERROR: Cannot find bundled skills folder: $SOURCE"
    exit 1
fi

mkdir -p "$CLAUDE_TARGET"

count=0
for skill_dir in "$SOURCE"/*/; do
    name=$(basename "$skill_dir")
    [ "$name" = ".system" ] && continue
    dest="$CLAUDE_TARGET/$name"
    rm -rf "$dest"
    cp -r "$skill_dir" "$dest"
    echo "  [OK] Installed skill: $name"
    count=$((count + 1))
done

echo ""
echo "Done. Installed $count skills to: $CLAUDE_TARGET"
echo "Restart Claude Code so newly installed skills are detected."
