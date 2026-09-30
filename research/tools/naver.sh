#!/bin/bash
# naver.sh "QUERY" [where]  where=news|cafearticle|blog|kin|webkr
Q=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$1")
W="${2:-news}"
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
curl -sL --compressed --max-time 25 -A "$UA" -H "Accept-Language: ko-KR,ko;q=0.9" "https://search.naver.com/search.naver?where=$W&query=$Q" | python3 -c "
import sys,re,html
s=sys.stdin.read()
seen=set()
for m in re.finditer(r'href=\"(https?://[^\"]+)\"[^>]*>(.{0,200}?)</a>', s, re.S):
    u=html.unescape(m.group(1)); t=html.unescape(re.sub('<[^>]+>','',m.group(2))).strip()
    if any(x in u for x in ['naver.com/search','naver.com/main','policy','help','ads.','.css','.js','.png','.jpg','.gif','naver.com/']): continue
    if len(t)<10 or u in seen: continue
    seen.add(u); print('-',t[:110]); print('  ',u)
    if len(seen)>=20: break
"
