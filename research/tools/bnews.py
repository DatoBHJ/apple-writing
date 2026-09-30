import sys,re,html,urllib.parse,subprocess
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
def get(url,extra=None):
    cmd=["curl","-sL","--compressed","--max-time","30","-A",UA,"-H","Accept-Language: en-US,en;q=0.9"]
    if extra: cmd+=extra
    cmd.append(url)
    return subprocess.run(cmd,capture_output=True,text=True).stdout
def news(q,mkt="en-US"):
    url=f"https://www.bing.com/news/search?q={urllib.parse.quote_plus(q)}&format=rss&setmkt={mkt}&setlang={mkt.split('-')[0]}"
    s=get(url); out=[]
    for it in re.findall(r'<item>(.*?)</item>', s, re.S):
        t=re.search(r'<title>(.*?)</title>',it,re.S); l=re.search(r'<link>(.*?)</link>',it,re.S)
        d=re.search(r'<description>(.*?)</description>',it,re.S); p=re.search(r'<pubDate>(.*?)</pubDate>',it,re.S)
        src=re.search(r'<News:Source>(.*?)</News:Source>',it,re.S)
        if not l: continue
        u=html.unescape(l.group(1)); m=re.search(r'[?&]url=([^&]+)',u)
        if m: u=urllib.parse.unquote(m.group(1))
        out.append((html.unescape(t.group(1)) if t else '',u,html.unescape(re.sub('<[^>]+>','',d.group(1))) if d else '',p.group(1) if p else '',html.unescape(src.group(1)) if src else ''))
    return out
if __name__=="__main__":
    mkt="en-US"
    args=sys.argv[1:]
    if args and args[0].startswith("mkt="):
        mkt=args[0][4:]; args=args[1:]
    for q in args:
        r=news(q,mkt)
        print(f"\n### {q}  ({len(r)})")
        for i,(t,u,d,p,s) in enumerate(r[:10]):
            print(f"[{i+1}] {t}\n    {u}\n    {p} | {s}\n    {d[:230]}")
