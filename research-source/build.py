from pathlib import Path
import json,html,math,re,os
ROOT=Path(__file__).resolve().parent
D=ROOT/'dist'
PAPERS=json.loads((ROOT/'content/papers.json').read_text())
PROFILE=json.loads((ROOT/'content/profile.json').read_text())
e=html.escape
CONCEPTS=json.loads((ROOT/'content/concepts.json').read_text())
def concept_prose(text,seen=None):
    seen=seen if seen is not None else set()
    matches=[]
    for c in CONCEPTS:
        if c['term'] in seen:continue
        terms=[c['term']]+c.get('alternatives',[])
        pattern=r'\b(?:'+ '|'.join(re.escape(term) for term in terms)+r')\b'
        m=re.search(pattern,text,re.IGNORECASE)
        if m:matches.append((m.start(),m.end(),c))
    parts=[];end=0
    for start,stop,c in sorted(matches,key=lambda x:x[0]):
        if start<end:continue
        parts.extend([e(text[end:start]),'<a class="concept-link" href="'+e(c['url'])+'" title="'+e(c['title'])+'">'+e(text[start:stop])+'</a>'])
        seen.add(c['term']);end=stop
    return ''.join(parts)+e(text[end:])
SITE=json.loads((ROOT/'content/site.json').read_text()) if (ROOT/'content/site.json').exists() else {}
ORIGIN=os.environ.get('SITE_ORIGIN',SITE.get('origin','')).rstrip('/')
PUBLISH_VIDEOS=SITE.get('publish_videos',False)
exec((ROOT/'math_typesetting.py').read_text())
def head(title,desc,depth=0,path=''):
    b='../'*depth
    photo=PROFILE.get('photo')
    avatar=f'<span class="avatar"><img src="{b}assets/{e(photo["file"])}" width="39" height="39" alt="" decoding="async"></span>' if photo else '<span class="monogram">LJ</span>'
    canonical=f'<link rel="canonical" href="{ORIGIN}/{path}"><meta property="og:url" content="{ORIGIN}/{path}">' if ORIGIN else ''
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)}</title><meta name="description" content="{e(desc)}"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:type" content="website">{canonical}<link rel="stylesheet" href="{b}assets/katex/katex.min.css"><link rel="stylesheet" href="{b}assets/style.css"><link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 32 32%27%3E%3Crect width=%2732%27 height=%2732%27 rx=%2716%27 fill=%27%23111d34%27/%3E%3Ctext x=%275%27 y=%2721%27 fill=%27white%27 font-size=%2714%27 font-family=%27Arial%27%3ELJ%3C/text%3E%3C/svg%3E"></head><body><a class="skip" href="#main">Skip to content</a><header class="site-header"><div class="wrap header-inner"><a class="brand" href="{b}index.html">{avatar}Liuyuan Jiang <span class="note">/ Research</span></a><nav aria-label="Main navigation"><a href="{b}index.html#papers">Papers</a><a href="{b}index.html#about">About</a><a href="https://liuyuan999.github.io/">Homepage</a><a href="mailto:{e(PROFILE["email"])}">Email</a></nav></div></header>'
def footer(depth=0):
    b='../'*depth
    return f'<footer class="footer"><div class="wrap"><span>Liuyuan Jiang · University of Rochester</span><span><a href="{b}index.html#papers">Research collection</a> · Updated October 8, 2026</span></div></footer><script src="{b}assets/site.js" defer></script></body></html>'
def save(path,s):
    target=D/path;target.parent.mkdir(parents=True,exist_ok=True);parts=path.split('/');slug=parts[1] if len(parts)>2 and parts[0] in ['papers','videos'] else None;target.write_text(typeset_prose(s,slug) if path.endswith('.html') else s)
exec((ROOT/'research_hub.py').read_text())
save('index.html',home())
if (ROOT/'content/articles.json').exists():
    exec((ROOT/'render_articles.py').read_text())
print('Generated research hub and available articles.')
