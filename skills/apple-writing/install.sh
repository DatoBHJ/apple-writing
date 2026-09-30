#!/usr/bin/env bash
# install.sh — copy this skill into an agent harness's skill directory.
#
#   ./install.sh                      # install for every detected harness
#   ./install.sh claude               # one harness: claude | codex | cursor | dsh | agents | ...
#   ./install.sh claude --project     # into ./.claude/skills instead of ~/.claude/skills
#   ./install.sh /custom/skills       # any directory
#   ./install.sh --list               # show the supported names
#
# Prefer `npx skills add <owner>/<repo>` when you have network access — it knows
# the current path for every supported agent and keeps them in sync:
#   https://github.com/vercel-labs/skills
#
# Written for bash 3.2 (the macOS default), so no associative arrays.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
NAME="$(basename "$HERE")"

HARNESSES="dsh claude codex cursor agents opencode gemini copilot windsurf continue kiro goose"

# target_paths <harness> -> prints "<global>|<project>"; non-zero if unknown.
# Paths follow the skills CLI agent table (vercel-labs/skills).
target_paths() {
  case "$1" in
    dsh)      echo "$HOME/.dsh/skills|.dsh/skills" ;;
    claude)   echo "$HOME/.claude/skills|.claude/skills" ;;
    codex)    echo "$HOME/.codex/skills|.agents/skills" ;;
    cursor)   echo "$HOME/.cursor/skills|.agents/skills" ;;
    agents)   echo "$HOME/.agents/skills|.agents/skills" ;;
    opencode) echo "$HOME/.config/opencode/skills|.agents/skills" ;;
    gemini)   echo "$HOME/.gemini/skills|.agents/skills" ;;
    copilot)  echo "$HOME/.copilot/skills|.agents/skills" ;;
    windsurf) echo "$HOME/.codeium/windsurf/skills|.windsurf/skills" ;;
    continue) echo "$HOME/.continue/skills|.continue/skills" ;;
    kiro)     echo "$HOME/.kiro/skills|.kiro/skills" ;;
    goose)    echo "$HOME/.config/goose/skills|.goose/skills" ;;
    *) return 1 ;;
  esac
}

usage() {
  echo "usage: ./install.sh [harness|path] [--project] [--list]"
  echo
  echo "harnesses: $HARNESSES"
  echo "  every name above is also a valid --agent for: npx skills add"
}

sync() {  # sync <destination>
  dest="$1"
  mkdir -p "$dest"
  if command -v rsync >/dev/null 2>&1; then
    rsync -a --delete --exclude '.git' --exclude '.tmp' --exclude '__pycache__' \
      "$HERE/" "$dest/$NAME/"
  else
    rm -rf "${dest:?}/$NAME"
    mkdir -p "$dest/$NAME"
    cp -R "$HERE/." "$dest/$NAME/"
  fi
  echo "  -> $dest/$NAME"
}

[ "${1:-}" = "--list" ] && { usage; exit 0; }

PROJECT=0
[ "${2:-}" = "--project" ] && PROJECT=1
ARG="${1:-}"

if [ -z "$ARG" ]; then
  echo "installing '$NAME' for every detected harness:"
  found=0
  for h in $HARNESSES; do
    paths="$(target_paths "$h")"
    global="${paths%%|*}"
    # only install where the harness already exists, so nothing is created blindly
    if [ -d "$(dirname "$global")" ]; then sync "$global"; found=1; fi
  done
  if [ "$found" = 0 ]; then
    echo "  (no known harness directory found — pass one explicitly)"
    usage
    exit 1
  fi
elif paths="$(target_paths "$ARG")"; then
  global="${paths%%|*}"
  project="${paths##*|}"
  if [ "$PROJECT" = 1 ]; then sync "$PWD/$project"; else sync "$global"; fi
elif [ -d "$ARG" ] || [ "${ARG#/}" != "$ARG" ]; then
  sync "$ARG"
else
  echo "error: unknown harness '$ARG'" >&2
  usage
  exit 1
fi

echo
echo "installed. the harness discovers the skill from its SKILL.md frontmatter,"
echo "so it takes effect on the next session."
echo
echo "optional: this skill does not ship Apple's style guide text. rebuild it with"
echo "  $HERE/tools/fetch-style-guide.sh"
