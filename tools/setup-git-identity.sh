#!/usr/bin/env bash
# setup-git-identity.sh — point git commits at your GitHub noreply address.
#
# Commits carry whatever `git config user.email` said when they were made, and
# they carry it forever: changing the account email later does not rewrite
# history, and GitHub's "keep my email private" setting only covers web-based
# Git operations, not commits made from a machine.
#
# Run this on every machine you commit from, BEFORE the first commit. On a fresh
# machine with no git identity, git guesses one from your account name and
# hostname — which leaks more than an email does.
#
#   ./setup-git-identity.sh             # apply
#   ./setup-git-identity.sh --dry-run   # show what would change
#
# Requires: gh CLI, signed in (gh auth login).
set -euo pipefail

DRY=0
[ "${1:-}" = "--dry-run" ] && DRY=1

command -v gh >/dev/null || { echo "error: gh CLI is required — install it and run 'gh auth login'" >&2; exit 1; }
gh auth status >/dev/null 2>&1 || { echo "error: not signed in — run 'gh auth login' first" >&2; exit 1; }

read -r LOGIN ID <<< "$(gh api user --jq '.login + " " + (.id | tostring)')"
NOREPLY="${ID}+${LOGIN}@users.noreply.github.com"

echo "GitHub account : ${LOGIN} (id ${ID})"
echo "noreply address: ${NOREPLY}"
echo

cur_name="$(git config --global user.name || echo '(unset)')"
cur_email="$(git config --global user.email || echo '(unset)')"
cur_uc="$(git config --global user.useConfigOnly || echo 'false')"

echo "current global settings:"
echo "  user.name       = ${cur_name}"
echo "  user.email      = ${cur_email}"
echo "  user.useConfigOnly = ${cur_uc}"
echo

if [ "${cur_email}" = "${NOREPLY}" ] && [ "${cur_uc}" = "true" ]; then
  echo "already correct — nothing to do."
  exit 0
fi

if [ "$DRY" = 1 ]; then
  echo "dry run — would set:"
else
  echo "setting:"
fi

apply() {
  if [ "$DRY" = 1 ]; then echo "  git config --global $1 \"$2\""; return; fi
  git config --global "$1" "$2"
  echo "  git config --global $1 \"$2\""
}

apply user.name  "${LOGIN}"
apply user.email "${NOREPLY}"
apply user.useConfigOnly true

if [ "$DRY" = 1 ]; then
  echo
  echo "(nothing was changed)"
else
  echo
  echo "done. commits made from now on carry the noreply address and stay"
  echo "attributed to @${LOGIN}. existing commits are unchanged — rewriting"
  echo "history is a separate decision and usually not worth it."
  echo
  echo "one setting to check in the browser (needs the web UI):"
  echo "  Settings → Emails → \"Keep my email addresses private\"      (should be on)"
  echo "  Settings → Emails → \"Block command line pushes that expose my email\" (should be on)"
  echo
  echo "note: this machine only. run this script again on any other machine"
  echo "you commit from — git config does not travel with clones."
fi

if [ "$DRY" = 0 ]; then
  echo
  echo "verify the next commit with:  git log -1 --format='%an <%ae>'"
fi