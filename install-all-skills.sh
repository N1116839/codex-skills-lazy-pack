#!/usr/bin/env bash
# Overlay personal skills; back up collisions, preserve unrelated local files.
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE="$SCRIPT_DIR/skills"
[[ -d "$SOURCE" ]] || { echo "Missing bundled skills: $SOURCE" >&2; exit 1; }
TARGETS=("$HOME/.codex/skills" "$HOME/.claude/skills")
# Optional explicit destination(s) also support isolated restore tests.
if (( $# )); then TARGETS=("$@"); fi
STAMP="$(date +%Y%m%d_%H%M%S)_$$"
for target in "${TARGETS[@]}"; do
    [[ ! -L "$target" ]] || { echo "Refusing linked target: $target" >&2; exit 1; }
    mkdir -p "$target"
    target="$(cd "$target" && pwd -P)"
    backup="$(dirname "$target")/backups/codex_skills_$STAMP"
    for skill_dir in "$SOURCE"/*/; do
        [[ -d "$skill_dir" ]] || continue
        name="$(basename "$skill_dir")"
        [[ "$name" != '.system' ]] || continue
        while IFS= read -r -d '' file; do
            relative="${file#"$SOURCE"/}"
            dest="$target/$relative"
            parent="$(dirname "$dest")"
            check="$parent"
            while [[ "$check" != "$target" && "$check" != '/' ]]; do
                [[ ! -L "$check" ]] || { echo "Refusing linked path: $check" >&2; exit 1; }
                check="$(dirname "$check")"
            done
            [[ ! -L "$dest" ]] || { echo "Refusing linked file: $dest" >&2; exit 1; }
            mkdir -p "$parent"
            if [[ -f "$dest" ]]; then
                cmp -s "$file" "$dest" && continue
                mkdir -p "$(dirname "$backup/$relative")"
                cp -p "$dest" "$backup/$relative"
            fi
            cp -p "$file" "$dest"
            cmp -s "$file" "$dest" || { echo "Copy mismatch: $dest" >&2; exit 1; }
        done < <(find "$skill_dir" -type f ! -path '*/__pycache__/*' ! -name '*.pyc' -print0)
    done
    echo "Installed skills at $target; changed originals backed up at $backup when needed."
done
echo 'Restart skill discovery. Codex continuity hooks require separate installation and user trust; see README.'
