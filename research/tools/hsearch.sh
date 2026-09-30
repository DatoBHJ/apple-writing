#!/bin/bash
# hsearch.sh "QUERY"  -- Hacker News Algolia search (good for criticism/opinion)
Q=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote_plus(sys.argv[1]))" "$1")
curl -sL --compressed --max-time 25 "https://hn.algolia.com/api/v1/search?query=$Q&tags=story&hitsPerPage=15" | python3 -c "
import json,sys
d=json.load(sys.stdin)
for h in d.get('hits',[]):
    print('-',h.get('title'),'|',h.get('points'),'pts |',h.get('created_at','')[:10])
    print('  ',h.get('url') or ('https://news.ycombinator.com/item?id='+h['objectID']))
    print('   HN: https://news.ycombinator.com/item?id='+h['objectID'])
"
