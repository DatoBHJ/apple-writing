#!/usr/bin/env bash
# Fallback web search for DSH agents when the web_search tool's providers fail.
# Usage: ./search.sh "query" [num_results]
# Output: title | url | snippet   (one result per line)
set -uo pipefail
Q="${1:?usage: search.sh \"query\" [n]}"
N="${2:-8}"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"

BING_PY='
import sys, re, html, base64, urllib.parse
n = int(sys.argv[1]); data = sys.stdin.read()

def unwrap(u):
    u = html.unescape(u)
    m = re.search(r"[?&]u=a1([A-Za-z0-9_\-]+)", u)
    if "bing.com/ck/a" in u and m:
        s = m.group(1).replace("-", "+").replace("_", "/")
        s += "=" * (-len(s) % 4)
        try: return base64.b64decode(s).decode("utf-8", "replace")
        except Exception: return u
    return u

blocks = re.findall(r"<li class=\"b_algo\".*?(?=<li class=\"b_algo\"|</ol>)", data, re.S)
out = []
for b in blocks:
    m = re.search(r"<h2[^>]*>\s*<a[^>]*href=\"([^\"]+)\"[^>]*>(.*?)</a>", b, re.S)
    if not m: continue
    url, title = unwrap(m.group(1)), re.sub(r"<[^>]+>", "", m.group(2))
    sn = re.search(r"<p[^>]*>(.*?)</p>", b, re.S)
    snip = re.sub(r"<[^>]+>", "", sn.group(1)) if sn else ""
    out.append("%s | %s | %s" % (html.unescape(title).strip(), url, html.unescape(snip).strip()[:280]))
    if len(out) >= n: break
print("\n".join(out))
'

MOJEEK_PY='
import sys, re, html
n = int(sys.argv[1]); data = sys.stdin.read()
out = []
for m in re.finditer(r"<a class=\"ob\"[^>]*href=\"([^\"]+)\"[^>]*>(.*?)</a>(.*?)(?=<li|</ul>)", data, re.S):
    url, title, rest = m.group(1), re.sub(r"<[^>]+>", "", m.group(2)), m.group(3)
    sn = re.search(r"<p class=\"s\">(.*?)</p>", rest, re.S)
    snip = re.sub(r"<[^>]+>", "", sn.group(1)) if sn else ""
    out.append("%s | %s | %s" % (html.unescape(title).strip(), html.unescape(url), html.unescape(snip).strip()[:280]))
    if len(out) >= n: break
print("\n".join(out))
'

r="$(curl -s -m 20 -A "$UA" -H "Accept-Language: en-US,en;q=0.9" -G --data-urlencode "q=$Q" "https://www.bing.com/search" | python3 -c "$BING_PY" "$N")"
if [ -z "$r" ]; then
  r="$(curl -s -m 20 -A "$UA" -G --data-urlencode "q=$Q" "https://www.mojeek.com/search" | python3 -c "$MOJEEK_PY" "$N")"
fi
if [ -z "$r" ]; then
  echo "NO RESULTS from Bing/Mojeek for: $Q" >&2
  exit 1
fi
printf '%s\n' "$r"
