#!/usr/bin/env bash
# fetch-style-guide.sh — download Apple's official style guide and build the local
# text corpus that `fetch-apple-copy.sh grep` and the references cite.
#
#   ./fetch-style-guide.sh [target-dir]     (default: ../../research beside the skill)
#
# Produces:
#   apple-style-guide.pdf   244 pp, ~4.2 MB, the June 2026 edition
#   apple-style-guide.txt   page-marked plain text for grep
#   asg/                    the same guide as 52 web sections
#   asg-sections.txt        the section slugs
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Default target: the repository's research/ directory, found by walking up the
# tree so the script works from a clone, an installed copy, or anywhere else.
_default_target() {
  local d="$HERE"
  for _ in 1 2 3 4 5; do
    d="$(dirname "$d")"
    [ -f "$d/research/apple-style-guide.txt" ] && { echo "$d/research"; return; }
  done
  echo "$HERE/../../../research"
}
TARGET="${1:-$(_default_target)}"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
PDF_URL="https://help.apple.com/pdf/applestyleguide/en_US/apple-style-guide.pdf"

mkdir -p "$TARGET"
cd "$TARGET"

echo "→ PDF"
curl -sL -m 120 -A "$UA" -o apple-style-guide.pdf "$PDF_URL"
file apple-style-guide.pdf | grep -q PDF || { echo "error: did not get a PDF (Apple may have moved it — check references/sources.md)" >&2; exit 1; }
ls -l apple-style-guide.pdf | awk '{print "  ", $5, "bytes"}'

echo "→ text"
python3 - <<'PY'
from pypdf import PdfReader
r = PdfReader("apple-style-guide.pdf")
parts = [f"\n\n===== PAGE {i} =====\n{(p.extract_text() or '')}" for i, p in enumerate(r.pages, 1)]
open("apple-style-guide.txt", "w").write("".join(parts))
print(f"   {len(r.pages)} pages, {sum(len(x) for x in parts):,} chars")
PY

echo "→ web sections"
python3 - "$UA" <<'PY'
import html, os, re, subprocess, sys, time
ua = sys.argv[1]
root = subprocess.run(["curl", "-s", "-m", "30", "-A", ua, "-L",
                       "https://support.apple.com/guide/applestyleguide/"],
                      capture_output=True).stdout.decode("utf-8", "replace")
slugs, seen = [], set()
for s in re.findall(r"/guide/applestyleguide/([a-z0-9\-]+)/web", root):
    if s not in seen:
        seen.add(s); slugs.append(s)
if not slugs:
    print("   warning: could not enumerate sections (the root page is a JS shell); skipping")
    raise SystemExit(0)
open("asg-sections.txt", "w").write("\n".join(slugs) + "\n")
os.makedirs("asg", exist_ok=True)
BOILER = re.compile(r"^(Apple|Store|Mac|iPad|iPhone|Watch|Vision|AirPods|TV|Support|Shop|"
                    r"Sign in|Bag|Previous|Next|Helpful\?|Yes|No|Submit|United States|"
                    r"Apple Style Guide|Apple Footer|Search|Quick search|Clear Search|Table of Contents)$")
ok = 0
for slug in slugs:
    raw = subprocess.run(["curl", "-s", "-m", "30", "-A", ua, "-L",
                          f"https://support.apple.com/guide/applestyleguide/{slug}/web"],
                         capture_output=True).stdout.decode("utf-8", "replace")
    if len(raw) < 5000:
        continue
    body = re.sub(r"<(script|style|nav|header|footer)\b.*?</\1>", " ", raw, flags=re.S)
    body = re.sub(r"</(p|li|h[1-6]|div|tr)>", "\n", body)
    text = html.unescape(re.sub(r"<[^>]+>", " ", body))
    lines, seen_l = [], set()
    for line in text.split("\n"):
        line = re.sub(r"[ \t\u00a0]+", " ", line).strip()
        if line and line not in seen_l and not BOILER.match(line):
            seen_l.add(line); lines.append(line)
    open(f"asg/{slug}.txt", "w").write("\n".join(lines))
    ok += 1
    time.sleep(0.4)
print(f"   {ok}/{len(slugs)} sections written to asg/")
PY

echo
echo "done — corpus in $TARGET"
echo "next: ./fetch-apple-copy.sh grep \"serial comma\""
