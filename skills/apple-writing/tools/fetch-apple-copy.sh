#!/usr/bin/env bash
# fetch-apple-copy.sh — pull Apple's live writing guidance and copy for calibration.
#
# Apple's pages are JS-rendered for humans but server-rendered for curl, and
# several routes are traps. This script encodes the routes that actually work
# (verified 2026-09-30) so an agent can re-read the source instead of trusting
# memory of it.
#
# Usage:
#   ./fetch-apple-copy.sh page <apple.com-url>     # marketing copy + footnotes, deduplicated
#   ./fetch-apple-copy.sh hig <slug>               # HIG page text (writing, inclusion, ...)
#   ./fetch-apple-copy.sh asg <section-slug>       # one Apple Style Guide section
#   ./fetch-apple-copy.sh grep <pattern>           # grep the local Style Guide corpus
#   ./fetch-apple-copy.sh list                     # list known HIG pages / local corpus
#
# Examples:
#   ./fetch-apple-copy.sh page https://www.apple.com/iphone-duo/
#   ./fetch-apple-copy.sh hig writing
#   ./fetch-apple-copy.sh grep "serial comma"
set -uo pipefail

UA_CHROME="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122 Safari/537.36"
UA_SAFARI="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"

# Local research corpus, if it has been built. This repository does not ship
# Apple's text (see THIRD_PARTY_NOTICES.md) — tools/fetch-style-guide.sh downloads
# it from Apple. Walk up the tree so the lookup works from a clone or an install.
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CORPUS=""
d="$HERE"
for _ in 1 2 3 4 5; do
  d="$(dirname "$d")"
  if [ -f "$d/research/apple-style-guide.txt" ]; then CORPUS="$d/research"; break; fi
  if [ -f "$d/apple-style-guide.txt" ]; then CORPUS="$d"; break; fi
done

die() { echo "error: $*" >&2; exit 1; }
need_python() { command -v python3 >/dev/null || die "python3 is required"; }

# ---------------------------------------------------------------- marketing pages
cmd_page() {
  local url="${1:?usage: fetch-apple-copy.sh page <url>}"
  need_python
  local tmp; tmp="$(mktemp -t applepage.XXXXXX).html"
  curl -sL -m 30 -A "$UA_CHROME" "$url" -o "$tmp" || die "fetch failed: $url"
  local bytes; bytes=$(wc -c < "$tmp" | tr -d ' ')
  [ "$bytes" -gt 20000 ] || { echo "warning: only $bytes bytes — page may not be server-rendered" >&2; }

  python3 - "$tmp" "$url" <<'PY'
import html, re, sys
path, url = sys.argv[1], sys.argv[2]
raw = open(path, encoding="utf-8", errors="replace").read()

def clean(s):
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).replace("\u00a0", " ").strip()

# Headlines: the classes Apple actually uses on product pages.
heads = []
for m in re.finditer(r'class="[^"]*(?:header-headline|section-header-headline|typography-marquee-headline[^"]*)[^"]*"[^>]*>(.*?)</', raw, re.S):
    t = clean(m.group(1))
    if 4 < len(t) < 200:
        heads.append(t)

# Body copy blocks, then dedupe: Apple ships start-frame AND end-frame copies of
# scroll-animated text, which otherwise invents "typos".
paras = []
for m in re.finditer(r"<(?:p|div)[^>]*>(.*?)</(?:p|div)>", raw, re.S):
    t = clean(m.group(1))
    if 25 < len(t) < 260:
        paras.append(t)

# Footnotes are the half of the system that makes the claim defensible.
notes = [clean(m.group(1)) for m in re.finditer(r'<li[^>]*id="footnote-[^"]*"[^>]*>(.*?)</li>', raw, re.S)]
notes = [n for n in notes if n]

def dedupe(xs):
    out, seen = [], set()
    for x in xs:
        k = x.lower()
        if k in seen:
            continue
        # Drop the doubled-frame artifact: a block whose words repeat adjacently.
        if re.search(r"\b(\w+)\s+\1\b", x, re.I):
            continue
        seen.add(k); out.append(x)
    return out

print(f"# {url}\n# {len(heads)} headlines · {len(dedupe(paras))} body blocks · {len(notes)} footnotes\n")
print("## Headlines")
for h in dedupe(heads): print(" -", h)
print("\n## Body copy")
for p in dedupe(paras)[:60]: print(" -", p)
print("\n## Footnotes (the evidence half — never teach a claim without these)")
for n in notes[:40]: print(" -", n[:400] + ("…" if len(n) > 400 else ""))
PY
  rm -f "$tmp"
}

# ------------------------------------------------------------------------ HIG
cmd_hig() {
  local slug="${1:?usage: fetch-apple-copy.sh hig <slug>   (writing, inclusion, branding, onboarding, feedback, privacy, accessibility, ...)}"
  need_python
  local url="https://developer.apple.com/tutorials/data/design/human-interface-guidelines/${slug}.json"
  local tmp; tmp="$(mktemp -t hig.XXXXXX).json"
  local code; code=$(curl -s -m 25 -A "$UA_SAFARI" -o "$tmp" -w "%{http_code}" "$url")
  if [ "$code" != "200" ] || [ "$(wc -c < "$tmp" | tr -d ' ')" -lt 1000 ]; then
    echo "JSON route failed ($code). Falling back to the reader proxy…" >&2
    curl -sS -m 40 "https://r.jina.ai/https://developer.apple.com/design/human-interface-guidelines/${slug}" || die "both routes failed for '$slug'"
    rm -f "$tmp"; return
  fi
  python3 - "$tmp" "$slug" <<'PY'
import json, re, sys
path, slug = sys.argv[1], sys.argv[2]
d = json.load(open(path, encoding="utf-8"))
out = []
def walk(o):
    if isinstance(o, dict):
        if o.get("type") == "text" and isinstance(o.get("text"), str):
            out.append(o["text"])
        for v in o.values():
            walk(v)
    elif isinstance(o, list):
        for v in o:
            walk(v)
walk(d)
text = "\n".join(out)
print(f"# HIG · {slug}\n# source: https://developer.apple.com/design/human-interface-guidelines/{slug}\n")
print(re.sub(r"\n{3,}", "\n\n", text))
PY
  rm -f "$tmp"
}

# ------------------------------------------------------------- style guide (web)
cmd_asg() {
  local slug="${1:?usage: fetch-apple-copy.sh asg <section-slug>   (see: list)}"
  [ "$slug" = "welcome" ] && die "'welcome' is a JS shell — pick a section slug (see: list)"
  curl -s -m 30 -A "$UA_SAFARI" -L "https://support.apple.com/guide/applestyleguide/${slug}/web" \
    | python3 -c '
import html, re, sys
raw = sys.stdin.read()
raw = re.sub(r"<(script|style)\b.*?</\1>", " ", raw, flags=re.S)
raw = re.sub(r"</(p|li|h[1-6]|div|tr)>", "\n", raw)
t = html.unescape(re.sub(r"<[^>]+>", " ", raw))
lines, seen = [], set()
for line in t.split("\n"):
    line = re.sub(r"[ \t\u00a0]+", " ", line).strip()
    if not line or line in seen:
        continue
    seen.add(line); lines.append(line)
print("\n".join(lines))'
}

# ---------------------------------------------------------------- local corpus
cmd_grep() {
  local pat="${1:?usage: fetch-apple-copy.sh grep <pattern>}"
  [ -n "$CORPUS" ] || die "local corpus not found — set it up or use 'page'/'hig'/'asg' instead"
  echo "# matches for: $pat   (source: $CORPUS/apple-style-guide.txt)"
  python3 - "$CORPUS/apple-style-guide.txt" "$pat" <<'PY'
import re, sys
text = re.sub(r"\s+", " ", open(sys.argv[1], encoding="utf-8", errors="replace").read())
hits = list(re.finditer(re.escape(sys.argv[2]), text, re.I))
if not hits:
    print("  (no match)")
for m in hits[:12]:
    print(" -", text[max(0, m.start() - 120): m.end() + 220].strip())
PY
}

cmd_list() {
  echo "# HIG pages with writing guidance"
  echo "  writing inclusion branding onboarding feedback accessibility privacy layout typography"
  echo "  (enumerate all: curl -s https://developer.apple.com/tutorials/data/design/human-interface-guidelines.json)"
  echo
  echo "# Apple Style Guide sections"
  if [ -n "$CORPUS" ] && [ -f "$CORPUS/asg-sections.txt" ]; then
    sed 's/^/  /' "$CORPUS/asg-sections.txt"
  else
    echo "  (local corpus not found — fetch https://support.apple.com/guide/applestyleguide/ and read its links)"
  fi
}

case "${1:-}" in
  page) shift; cmd_page "$@" ;;
  hig)  shift; cmd_hig  "$@" ;;
  asg)  shift; cmd_asg  "$@" ;;
  grep) shift; cmd_grep "$@" ;;
  list) cmd_list ;;
  *) sed -n '2,20p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; exit 1 ;;
esac
