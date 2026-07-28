#!/bin/bash
# install-all-skills.sh
# Installs all personal skills to Codex and Claude Code.
# Works on macOS and Linux.
# Usage: bash install-all-skills.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE="$SCRIPT_DIR/skills"
TARGETS=("$HOME/.codex/skills" "$HOME/.claude/skills")

if [ ! -d "$SOURCE" ]; then
    echo "ERROR: Cannot find bundled skills folder: $SOURCE"
    exit 1
fi

count=0
for skill_dir in "$SOURCE"/*/; do
    name=$(basename "$skill_dir")
    [ "$name" = ".system" ] && continue
    for target in "${TARGETS[@]}"; do
        mkdir -p "$target"
        dest="$target/$name"
        rm -rf "$dest"
        cp -r "$skill_dir" "$dest"
    done
    echo "  [OK] Installed skill: $name"
    count=$((count + 1))
done

echo ""
echo "Done. Installed $count skills to Codex and Claude Code."
echo "Restart the agent so newly installed skills are detected."
