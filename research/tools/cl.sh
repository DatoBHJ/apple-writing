#!/bin/bash
# cl.sh QUERY  -- CourtListener opinion + RECAP docket search
Q=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$1")
curl -sL --compressed --max-time 30 "https://www.courtlistener.com/api/rest/v4/search/?q=$Q&type=o&order_by=score%20desc" | python3 -c "
import json,sys
try: d=json.load(sys.stdin)
except Exception as e: print('ERR',e); sys.exit()
print('count',d.get('count'))
for r in d.get('results',[])[:12]:
    print('-',r.get('caseName'),'|',r.get('court'),'|',r.get('dateFiled'))
    print('  https://www.courtlistener.com'+ (r.get('absolute_url') or ''))
    print('  ',(r.get('snippet') or '')[:250].replace('\n',' '))
"
