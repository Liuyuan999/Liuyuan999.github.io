A=json.loads((ROOT/'content/articles.json').read_text())
BY={p['slug']:p for p in PAPERS}
def paragraphs(xs): return ''.join('<p>'+e(x)+'</p>' for x in xs)
def svgframe(label): return f'<svg viewBox="0 0 620 300" role="img" aria-label="{e(label)}"><g data-plot></g></svg>'
def demo(p):
 t=p['type'];s=p['slug']
 if t=='surf':
  return '<div class="demo" data-demo="surf"><div class="eyebrow">Appendix F.1 / exact gear toy</div><h3>Change traversal, keep the same front</h3><p>Here x is a scalar decision, w weights the first raw objective, and p is the gear parameter. The raw objectives h₁ᵖ(x) and h₂(x) select x_w^*. The fixed evaluation vector h̄(x) traces the same front as p changes.</p>'+extra_math('surf-gear')+'<div class="demo-controls"><label for="gear-parameter">Gear parameter p</label><input id="gear-parameter" data-gear type="range" min="1" max="10" value="9"><output for="gear-parameter" data-gear-count>9</output></div><div class="demo-controls"><label for="sample-count">Front segments N</label><input id="sample-count" data-segments type="range" min="4" max="40" value="9"><output for="sample-count" data-count>9</output></div>'+svgframe('The paper’s fixed quadratic evaluation front with equal-weight and equal-arc-length solutions')+'<div class="legend"><span>Uniform weights</span><span>Uniform arc length</span></div><p class="metric" data-metric aria-live="polite"></p><p class="note">N segments give N + 1 solutions. This Appendix F.1 example uses the exact scalarized solution and direct numerical arc-length inversion. SURF’s iterative reconstruction is described in the method section.</p></div>'
 if t=='constraint':
  return '<div class="demo" data-demo="constraint"><div class="eyebrow">Figure 1 / exact lower-level example</div><h3>Move the constraint, change the response</h3><p>x is the upper variable and y is the lower response. The lower objective g is minimized subject to the inequality g^c(x, y) ≤ 0.</p>'+extra_math('constraint-demo')+'<div class="demo-controls"><label for="outer-x">Upper-level variable x</label><input id="outer-x" type="range" min="0.1" max="3" step="0.05" value="1"><output for="outer-x" data-count>1.00</output></div>'+svgframe('The BLOCC Figure 1 quadratic objective with the moving lower bound y greater than or equal to 3x')+'<div class="legend"><span>Unconstrained minimum</span><span>Constrained response</span></div><p class="metric" data-metric aria-live="polite"></p><p class="note">The shaded region satisfies the paper’s constraint g^c(x, y) ≤ 0. The optimum is y_g^*(x) = 3x, with μ_g^*(x) = 2x. Moving the boundary adds a constraint contribution to the value gradient. This is an exact lower-level solve of the paper’s example.</p></div>'
 if t=='timing':
  return '<div class="demo" data-demo="timing"><h3>Same exposure, different timing</h3><p>Toggle whether a toy agent is long or flat before each interval. Returns are fixed at −20, +15, −10, +25, −15, and +5 basis points.</p><div class="toy-actions">'+''.join(f'<button type="button" data-action="{i}" aria-pressed="{str(i%2==0).lower()}">Interval {i+1}: {"Long" if i%2==0 else "Flat"}</button>' for i in range(6))+'</div><div class="demo-controls"><button class="button" type="button" data-invert>Invert schedule</button><button class="button" type="button" data-reset>Reset</button></div>'+svgframe('Synthetic interval returns and a selected binary exposure schedule')+'<p class="metric" data-metric aria-live="polite"></p><p class="note">The paper’s timing formula is evaluated on six synthetic returns. Inverting the schedule negates its centered timing score.</p></div>'
 if t=='speech':
  return '<div class="demo" data-demo="speech"><h3>Two target-generation branches</h3><div class="demo-controls"><button class="button primary" type="button" data-source="anchor" aria-pressed="true">Raw-input anchor</button><button class="button" type="button" data-source="enhanced" aria-pressed="false">Enhanced target</button></div><div class="diagram-flow"><div class="flow-node" data-node="input">Audio features<small>Observed input</small></div><span class="flow-separator" aria-hidden="true">›</span><div class="flow-node" data-node="repr">Intermediate features<small>Inside the speech model</small></div><span class="flow-separator" aria-hidden="true">›</span><div class="flow-node" data-node="quant">Random quantizer<small>Discrete pseudo-labels</small></div></div><p data-explanation aria-live="polite"></p><p class="note">Select a target source to follow its information path.</p><h3>Measured downstream WER</h3>'+svgframe('Reported LibriSpeech word error rates for BEST-RQ and BiRQ')+'<div class="legend"><span>BEST-RQ</span><span>BiRQ</span></div><p class="note">Source: Table 2. 155M Conformer, 960h LibriSpeech SSL pretraining, 100h labeled fine-tuning. Lower WER is better.</p></div>'
 if t=='curvature':
  return '<div class="demo" data-demo="curvature"><h3>Joint curvature and reduced curvature</h3><p>x is the upper variable, y is the lower variable, and γ weights the lower-level penalty. Minimizing over y gives y = x. Move γ to see the fixed slice steepen while the reduced curve stays in place.</p>'+extra_math('curvature-demo')+'<div class="demo-controls"><label for="penalty">Penalty γ</label><input id="penalty" type="range" min="1" max="10" value="1"><output for="penalty" data-count>1</output></div>'+svgframe('Joint fixed-slice and reduced objective values on fixed axes: x from minus 1 to 1, objective value from 0 to 12')+'<div class="legend"><span>Fixed slice Hγ(x, 0)</span><span>Reduced Fγ(x)</span></div><p class="metric" data-metric aria-live="polite"></p><p class="note">Both axes stay fixed for every penalty setting. In this quadratic example, the fixed slice has curvature 1 + 2γ and the reduced objective has curvature 1.</p></div>'
 return '<div class="demo" data-demo="schedule"><h3>One update per level or repeated inner steps</h3><div class="demo-controls"><button class="button primary" type="button" data-mode="single" aria-pressed="true">Single-loop illustration</button><button class="button" type="button" data-mode="nested" aria-pressed="false">Nested-loop illustration</button><button class="button" type="button" data-next>Next update</button></div><div class="diagram-flow"><div class="flow-node" data-stage="lower">Lower-level update<small data-lower>0 updates</small></div><span class="flow-separator" aria-hidden="true">›</span><div class="flow-node" data-stage="upper">Upper-level update<small data-upper>0 updates</small></div></div><p data-explanation aria-live="polite"></p><p class="note">This illustrative schedule uses four inner updates per outer step for the nested loop and one for the single loop.</p></div>'
base_demo=demo
def demo(p):
 if p['slug']=='efficient-penalty':
  return '<div class="demo" data-demo="regime"><div class="eyebrow">Method structure</div><h3>Does the lower-level feasible set move?</h3><p>Y is the base lower-level domain, Ỹ is a fixed feasible set, and Y(x) is the feasible set at upper variable x. The inequalities c(x, y) ≤ 0 define coupled constraints. The update structure depends on whether these constraints move with x.</p><div class="demo-controls"><button class="button primary" type="button" data-regime="fixed" aria-pressed="true">Fixed feasible set</button><button class="button" type="button" data-regime="coupled" aria-pressed="false">Coupled constraints</button></div>'+extra_math('regime-fixed',attributes='data-regime-formula="fixed"')+extra_math('regime-coupled',attributes='data-regime-formula="coupled" hidden')+'<div class="regime-result"><strong data-regime-title>Uncoupled constraints</strong><p data-regime-description aria-live="polite"></p></div><p class="note">Sections 4–5 analyze the update structure for fixed and coupled feasible sets.</p></div>'
 if p['slug']=='pbgd-free':
  return '<div class="demo" data-demo="flatness"><div class="eyebrow">Definition 1 / illustrative envelope</div><h3>How does the flatness bound shrink?</h3><p>In Definition 1, y_g^*(x) is a lower-level optimum for the fixed upper variable x. The modulus c, exponent α, and residual δ define the bound. Use the distance ‖y_g^*(x) − y‖ directly. The green curve evaluates its right-hand side with the constants below; the blue curve shows the distance itself for comparison.</p>'+extra_math('flatness-demo')+'<div class="demo-controls"><label for="deviation">Distance to the lower-level optimum</label><input id="deviation" type="range" min="0" max="1" step="0.01" value="0.1"><output for="deviation" data-count>0.10</output></div>'+svgframe('Distance to the lower-level optimum and the illustrative flatness upper bound')+'<div class="legend"><span>Distance to optimum</span><span>Flatness upper bound</span></div><div class="flatness-values"><span>Distance to optimum<strong data-linear></strong></span><span>Flatness upper bound<strong data-flat></strong></span></div><p class="metric" data-metric aria-live="polite"></p><p class="note">The residual sets the envelope’s floor as the distance approaches zero.</p></div>'
 if p['type']=='speech':
  return '<div class="demo" data-demo="speech"><div class="eyebrow">Information flow / schematic</div><h3>Two target-generation branches</h3><div class="demo-controls"><button class="button primary" type="button" data-source="anchor" aria-pressed="true">Raw-input anchor</button><button class="button" type="button" data-source="enhanced" aria-pressed="false">Enhanced target</button></div><div class="target-diagram"><div class="flow-node" data-node="input">Audio features<small>Observed input</small></div><div class="target-branches"><div class="flow-node" data-node="anchor">Raw-input quantization<small>Anchor labels</small></div><div class="flow-node" data-node="repr">Intermediate representation<small>Enhanced-label source</small></div></div><div class="flow-node" data-node="quant">Target prediction<small>Learning with both label sources</small></div></div><p data-explanation aria-live="polite"></p><p class="note">Both target sources feed the shared masked-frame prediction task.</p></div>'
 return base_demo(p)
def bib(p):
 authors=' and '.join(p['authors']);key='jiang'+str(p['year'])+p['slug'].replace('-','')
 if p['slug']=='retailagent':key='zhang2026retailagent'
 fields=[('title',p['title']),('author',authors)]
 if p['venue']=='Preprint':
  kind='misc';fields.extend([('year',str(p['year'])),('eprint',p['arxiv']),('archivePrefix','arXiv')])
 else:
  kind='inproceedings';fields.append(('booktitle',p['bib_venue']))
  if p.get('bib_volume'):fields.append(('volume',p['bib_volume']))
  fields.append(('year',str(p['year'])))
 return '@'+kind+'{'+key+',\n'+',\n'.join('  '+name+' = {'+value+'}' for name,value in fields)+'\n}'

def sourcehtml(p):
 return '<ul class="source-list">'+''.join('<li><a href="'+e(s['url'])+'">'+e(s['label'])+'</a></li>' for s in p['sources'])+'</ul>'
def videohtml(p,a):
 return ''.join(f'<div class="story-scene"><time>{e(time)}</time><div><p>{e(narration)}</p><p class="visual"><strong>On screen:</strong> {e(visual)}</p></div></div>' for time,visual,narration in a['scenes'])+f'<p><a class="button" href="../../resources/{p["slug"]}-video-script.md" download>Download narration and storyboard</a></p>'
def relatedhtml(p,a):
 return '<div class="pill-links">'+''.join(f'<a href="../{s}/">{e(BY[s]["short"])}</a>' for s in a['related'])+'</div>'
S=json.loads((ROOT/'content/project-stories.json').read_text())
def authorshtml(p):
 return ', '.join('<span class="self">'+e(n)+'</span>' if n=='Liuyuan Jiang' else e(n) for n in p['authors'])
def kicker(n,label):return f'<div class="section-kicker"><span>{n:02}</span><span>{e(label)}</span></div>'
exec((ROOT/'render_project_pages.py').read_text())
for p in PAPERS:
 s=p['slug'];a=A[s];t=S[s]
 body=project_page(p,a,t)
 save('papers/'+s+'/index.html',body)
 if PUBLISH_VIDEOS:
  video=head(p['short']+' | Video storyboard', 'Narration and storyboard for '+p['title'],2,'videos/'+s+'/')+f'<main id="main" class="wrap"><article class="video-page"><a class="route-back" href="../../papers/{s}/">{e(p["short"])} project page</a><div class="video-intro"><div><p class="eyebrow" style="margin-top:30px">{e(p["short"])} / Video</p><h1>{e(t["headline"])}</h1><p class="subtitle">{e(p["title"])}</p><p class="authors">{authorshtml(p)}</p><div class="actions"><a class="button primary" href="../../papers/{s}/">Project page</a><a class="button" href="{p["paper"]}">Read the paper</a></div></div><aside class="video-meta"><p><strong>Narration and storyboard</strong>Approximately 2 minutes</p><p>Video not yet available.</p></aside></div><section aria-label="Narration and storyboard">{videohtml(p,a)}</section><section class="video-sources"><h2>Research sources</h2>{sourcehtml(p)}</section></article></main>'+footer(2)
  save('videos/'+s+'/index.html',video)
 # Preserve old incoming URLs while keeping one substantive page per paper.
 target=f'../../papers/{s}/#idea'
 canonical=ORIGIN+'/papers/'+s+'/'
 redirect='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Project page for this paper."><meta name="robots" content="noindex,follow"><title>'+e(p['short'])+' explanation</title><link rel="canonical" href="'+e(canonical)+'"><meta http-equiv="refresh" content="0; url='+e(target)+'"></head><body><main><h1>Continue to the project page</h1><p><a href="'+e(target)+'">Read the project page</a></p></main><script>location.replace('+json.dumps(target)+');</script></body></html>'
 save('blog/'+s+'/index.html',redirect)
 md='# '+a['explanation_title']+'\n\n'+a['lead']+'\n\n'+''.join('## '+title+'\n\n'+text+'\n\n' for title,text in a['explanation'])+'## Source\n\n['+p['title']+']('+p['paper']+')\n'
 (ROOT/'content/explanations').mkdir(exist_ok=True)
 (ROOT/'content/explanations'/f'{s}.md').write_text(md)
 script='# '+p['short']+' — video narration and storyboard\n\nNarration and storyboard. Approximately 2 minutes.\n\nPaper: '+p['paper']+'\n\n'+''.join('## '+time+'\n\n**On screen:** '+visual+'\n\n**Narration:** '+narration+'\n\n' for time,visual,narration in a['scenes'])+'## Recording notes\n\n- Keep toy diagrams visibly labeled as illustrative.\n- Show paper figure/table identifiers when discussing measured results.\n- End with the project URL and a link to the primary paper.\n- Record narration, then add figures and captions.\n'
 (ROOT/'video-scripts'/f'{s}.md').write_text(script)
 if PUBLISH_VIDEOS:
  save('resources/'+s+'-video-script.md',script)
 else:
  # Remove only the known generated video drafts from the hosted output.
  for draft in (D/'videos'/s/'index.html', D/'resources'/f'{s}-video-script.md'):
   if draft.exists():draft.unlink()
 # Structured metadata contains only publicly sourced bibliographic facts.
 schema={'@context':'https://schema.org','@type':'ScholarlyArticle','name':p['title'],'author':[{'@type':'Person','name':n} for n in p['authors']],'url':p['paper'],'datePublished':str(p['year'])}
 f=D/'papers'/s/'index.html';v=f.read_text();f.write_text(v.replace('</head>','<script type="application/ld+json">'+json.dumps(schema).replace('<','\\u003c')+'</script></head>'))
paths=['']+['papers/'+p['slug']+'/' for p in PAPERS]
if PUBLISH_VIDEOS:paths+=['videos/'+p['slug']+'/' for p in PAPERS]
if ORIGIN:
 save('sitemap.xml','<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+e(ORIGIN+'/'+path)+'</loc><lastmod>2026-10-08</lastmod></url>' for path in paths)+'</urlset>')
 save('robots.txt','User-agent: *\nAllow: /\nSitemap: '+ORIGIN+'/sitemap.xml\n')
save('404.html',head('Page not found | Liuyuan Jiang','Return to the research collection.')+'<main id="main" class="wrap" style="padding:70px 0"><h1>Page not found</h1><p><a href="'+e((ORIGIN or '.')+'/')+'">Return to the research collection</a></p></main>'+footer())
