#!/bin/bash
# fetch.sh URL [outfile]  -- fetch a URL (auto-falls back to Wayback if blocked), print readable text
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
U="$1"
OUT="${2:-/tmp/fetch_out.html}"
code=$(curl -sL --compressed --max-time 35 -A "$UA" -H "Accept-Language: en-US,en;q=0.9" -o "$OUT" -w "%{http_code}" "$U")
size=$(wc -c < "$OUT" | tr -d ' ')
echo "== DIRECT http=$code size=$size url=$U"
if [ "$code" != "200" ] || [ "$size" -lt 3000 ]; then
  echo "== RETRY VIA WAYBACK"
  curl -sL --compressed --max-time 45 -A "$UA" -o "$OUT" -w "wayback http=%{http_code} size=%{size_download}\n" "https://web.archive.org/web/2025id_/$U"
fi
python3 - "$OUT" <<'PY'
import sys,re,html
p=sys.argv[1]
s=open(p,encoding='utf-8',errors='replace').read()
s=re.sub(r'<(script|style|noscript|svg)[^>]*>.*?</\1>',' ',s,flags=re.S|re.I)
s=re.sub(r'<!--.*?-->',' ',s,flags=re.S)
t=html.unescape(re.sub(r'[ \t]+',' ',re.sub('<[^>]+>','\n',s)))
t=re.sub(r'\n\s*\n+','\n',t)
print(t.strip()[:14000])
PY
