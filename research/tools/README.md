# Research tooling (all web_search providers are DOWN — use these instead)

`web_search` fails in this session (SearXNG/Tavily/Brave/DDG all error). `web_fetch` works for single
article URLs but sometimes returns an empty body — always fall back to `curl` + the scripts below.

## Tools (all executable, in this directory)

| Tool | Use |
|---|---|
| `bash fetch.sh <URL> [outfile]` | Fetch a URL, auto-fallback to Wayback, print readable text. **Primary fetch tool.** |
| `bash rss.sh "<query>"` | **Bing News RSS search — the main working general search engine.** |
| `python3 bnews.py "q1" "q2" ...` | Same, multiple queries at once. |
| `bash hsearch.sh "<query>"` | Hacker News (Algolia) story search. Good for OPINION/critique pieces. |
| `bash cl.sh "<query>"` | CourtListener opinion search (JSON). For court rulings. |
| `bash naver.sh "<query>" news` | Naver search (news / blog / cafearticle / kin / webkr). Korean sources. |

## Manual one-liners that work

**Wayback (always use `--compressed`, else you get gzip binary):**
```bash
curl -sL --compressed --max-time 45 -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36" \
  "https://web.archive.org/web/2025id_/https://example.com/article"
```

**Readable text from any HTML file (works for EUC-KR too):**
```bash
python3 -c "
import re,html,sys
s=open('/tmp/x.html',encoding='utf-8',errors='replace').read()
s=re.sub(r'<(script|style|noscript|svg)[^>]*>.*?</\1>',' ',s,flags=re.S|re.I)
t=html.unescape(re.sub(r'[ \t]+',' ',re.sub('<[^>]+>','\n',s)))
print(re.sub(r'\n\s*\n+','\n',t)[:12000])"
```

**Korean/EUC-KR pages:** add `| iconv -f euc-kr -t utf-8` after curl, or `-H "Accept-Language: ko-KR,ko;q=0.9"`.

## Site-specific searches that WORK (200 OK)

- Ars Technica: `https://arstechnica.com/search/?q=QUERY`
- 9to5Mac: `https://9to5mac.com/?s=QUERY`
- MacRumors: `https://www.macrumors.com/search/?s=QUERY`
- ASA (UK ad regulator) rulings: `https://www.asa.org.uk/codes-and-rulings/rulings.html?query=QUERY`
  (results are JS-rendered — may need the individual ruling URL)
- 나무위키: `https://namu.wiki/search/QUERY` (URL-encode the query)
- 다음 뉴스: `https://search.daum.net/search?w=news&q=QUERY`
- 클리앙: `https://www.clien.net/service/search?q=QUERY`
- 뽐뿌: `https://www.ppomppu.co.kr/search_bbs.php?keyword=QUERY` (EUC-KR)
- Wikipedia API: `https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=QUERY&format=json`
- CourtListener API: `https://www.courtlistener.com/api/rest/v4/search/?q=QUERY&type=o`
- CourtListener RECAP dockets: `https://www.courtlistener.com/api/rest/v4/search/?q=QUERY&type=r`

## Blocked / do not waste time on

Google (JS interstitial), Bing web search HTML **and** `&format=rss` (returns garbage),
DuckDuckGo (202), Brave (429), Ecosia (403), Yandex (captcha), Startpage (Anubis JS challenge),
all public SearXNG instances tried (429 / bot check), Mojeek (403), Qwant (JS),
justice.gov direct (Akamai — **use Wayback instead**), ftc.gov may work directly,
content.guardianapis.com with `api-key=test` (401).

## Rules

- **NEVER invent a URL or a quote.** If you cannot retrieve it, list it under dead ends.
- Record the exact date and byline. Use Wayback to confirm the URL resolves.
- Mark each source DOCUMENTED (primary source / reporting with evidence) /
  OPINION (a writer's critique) / UNVERIFIED (could not retrieve).
