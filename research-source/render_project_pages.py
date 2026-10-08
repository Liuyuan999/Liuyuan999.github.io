G=json.loads((ROOT/'content/project-guides.json').read_text())
def guide_source(g,anchor):
 return g['source']+('#page='+anchor if g['source'].endswith('.pdf') else '#'+anchor)
def figure_reading(g):
 return '<div class="figure-reading" aria-label="How to read the figure">'+''.join('<p><strong>'+e(title)+'.</strong> '+e(body)+'</p>' for title,body in g['figure_read'])+'</div>'
def evidence_panels(p,g,prose=e):
 buttons=''.join(f'<button type="button" id="evidence-tab-{i}" role="tab" aria-selected="{str(i==0).lower()}" aria-controls="evidence-panel-{i}" tabindex="{0 if i==0 else -1}" data-evidence-tab="{i}">{e(x["label"])}</button>' for i,x in enumerate(g['panels']))
 panels=''
 for i,x in enumerate(g['panels']):
  rows=''
  for row in x['rows']:
   featured=row[0] in ['SURF','BiRQ','PBGD-Free','BLOCC','ALT-PBGD','PBGD-BLOCC']
   rows+='<tr'+(' class="featured-result"' if featured else '')+'><th scope="row">'+e(row[0])+'</th>'+''.join('<td>'+e(cell)+'</td>' for cell in row[1:])+'</tr>'
  table='<div class="table-scroll" role="region" tabindex="0" aria-label="'+e(x['title'])+' results"><table class="research-table"><caption>'+e(x['caption'])+'</caption><thead><tr>'+''.join('<th scope="col">'+e(col)+'</th>' for col in x['columns'])+'</tr></thead><tbody>'+rows+'</tbody></table></div><p class="table-hint" hidden>Scroll horizontally to see all columns.</p>'
  panels+=f'<div id="evidence-panel-{i}" class="evidence-panel" data-evidence-panel="{i}"><h3>{e(x["title"])}</h3>{table}<div class="result-reading"><span>Result</span><p>{prose(x["reading"])}</p></div><details class="protocol"><summary>Experiment setup and comparison details</summary><p>{prose(x["protocol"])}</p></details><a class="source-anchor" href="{e(guide_source(g,x["source"]))}">Read the original {"analysis" if p["slug"]=="smoothness" or x["label"]=="Algorithm map" else "result"} <span aria-hidden="true">↗</span></a></div>'
 return '<div class="evidence-lab" data-evidence-lab><div class="evidence-tabs" role="tablist" aria-label="Select a reported comparison" hidden>'+buttons+'</div>'+panels+'</div>'
def notation_symbol(slug,symbol):
 tex=MATH_CONFIG.get('notation_inline',{}).get(slug,{}).get(symbol)
 return MATH_HTML['inline:'+tex] if tex else e(symbol)
def research_cards(g):
 return '<div class="research-statements">'+''.join('<div class="research-statement"><p class="statement-source">'+e(label)+'</p><h3>'+e(title)+'</h3><p>'+e(body)+'</p><a href="'+e(guide_source(g,source))+'">'+e(label)+' in the paper <span aria-hidden="true">↗</span></a></div>' for label,title,body,source in g['cards'])+'</div>'
def project_page(p,a,t):
 s=p['slug'];g=G[s];seen_concepts=set();prose=lambda text:concept_prose(text,seen_concepts)
 labels=[('takeaway','Summary'),('idea','Method'),('technical','Analysis'),('interactive','Illustration'),('evidence','Results'),('citation','Citation')]
 toc='<aside class="toc" aria-label="Page contents"><div class="eyebrow">On this page</div>'+''.join(f'<a href="#{i}">{label}</a>' for i,label in labels)+'</aside>'
 actions=f'<a class="button primary" href="{e(p["paper"])}">Read the paper <span aria-hidden="true">↗</span></a>'
 if p.get('code'):actions+=f'<a class="button" href="{e(p["code"])}">Code <span aria-hidden="true">↗</span></a>'
 if PUBLISH_VIDEOS:actions+=f'<a class="button" href="../../videos/{s}/">Video &amp; storyboard</a>'
 actions+='<a class="text-action" href="#citation">Cite</a>'
 venue=p['venue'] if p['venue']!='Preprint' else 'Preprint · '+str(p['year'])
 hero=f'<header class="project-hero refined-hero"><a class="route-back" href="../../index.html#papers"><span aria-hidden="true">←</span> Publications &amp; projects</a><div class="paper-identity"><p class="meta"><span class="venue">{e(venue)}</span><span>{e(p["topic"])}</span></p><h1>{e(p["title"])}</h1><p class="authors">{authorshtml(p)}</p><div class="actions">{actions}</div></div></header>'
 summary='<ul class="research-summary">'+''.join('<li>'+prose(point['text'])+' <a class="summary-reference" href="#'+e(point['anchor'])+'">'+e(point['label'])+'</a></li>' for point in g['summary_points'])+'</ul>'
 takeaway='<section id="takeaway" class="project-takeaway"><h2>Summary</h2><p class="lede">'+prose(a['takeaway'])+'</p>'+summary+'</section>'
 if s=='efficient-penalty':
  related=BY['pbgd-free']
  takeaway+='<aside class="companion-paper"><p class="eyebrow">Related paper · NeurIPS 2025</p><h3><a href="'+e(related['paper'])+'">'+e(related['title'])+'</a></h3><p>PBGD-Free develops value-function removal under flatness. This preprint expands the smoothness analysis and develops fixed-set and coupled-constraint updates.</p><div class="actions"><a class="button" href="'+e(related['paper'])+'">Read the PBGD-Free paper</a><a href="../pbgd-free/">PBGD-Free project page</a></div></aside>'
 story=''.join('<div class="story-block"><h3>'+e(title)+'</h3><p>'+prose(body)+'</p></div>' for title,body in g['story'])
 method='<div class="method-description">'+''.join('<p><strong>'+e(title)+'.</strong> '+prose(body)+'</p>' for title,body in t['steps'])+'</div>'
 fig='' if s=='smoothness' else original_paper_figure(p,g['figure'])+figure_reading(g)
 implication='' if s=='surf' else '<div class="method-implication"><h3>'+e(t['why_title'])+'</h3><p>'+prose(t['why'])+'</p></div>'
 idea=f'<section id="idea"><h2>{e(g["scene"])}</h2>{story}{fig}<h3 class="method-heading">{e(g["method_title"])}</h3>{method}{implication}</section>'
 companion=original_paper_figure(p,0) if s=='surf' else ''
 interactive=f'<section id="interactive"><p class="section-label">Illustration</p><h2>{e(g["example_title"])}</h2>{companion}{demo(p)}<div class="application-note"><h3>{e(g["application"][0])}</h3><p>{prose(g["application"][1])}</p></div></section>'
 evidence_figure=original_paper_figure(p,0)+figure_reading(g) if s=='smoothness' else ''
 evidence=f'<section id="evidence"><h2>{e(t["result_title"])}</h2>{evidence_figure}{evidence_panels(p,g,prose)}<div class="result-context"><h3>{e(g["result_note_title"])}</h3><p>{prose(a["boundary"])}</p></div></section>'
 extra={'surf':('surf-refine','Damped empirical CDF refinement'),'retailagent':('retail-decompose','Equation 2 · Return decomposition'),'birq':('birq-update','Algorithm 1 · Weighted-gradient update'),'smoothness':('smoothness-cancel','The cancellation analyzed by directional derivatives'),'blocc':('blocc-value-gradient','Lemma 2 · Value gradient with boundary movement'),'pbgd-free':('pbgd-floor','Theorem 3 · Penalty-stationarity bound')}.get(s)
 notation='<div class="notation-key"><h3>Notation</h3><dl class="notation">'+''.join('<dt'+(' class="notation-wide"' if len(symbol)>28 else '')+'>'+notation_symbol(s,symbol)+'</dt><dd'+(' class="notation-wide"' if len(symbol)>28 else '')+'>'+e(desc)+'</dd>' for symbol,desc in t['notation'])+'</dl></div>'
 core=notation
 for equation in MATH_CONFIG['papers'][s]:
  core+=display_math(equation['tex'],equation['label'])
  if s=='pbgd-free' and equation == MATH_CONFIG['papers'][s][0]:core+=extra_math('pbgd-gradient','Equation 5 · Reduced penalty gradient')
 core+='<p class="formula-reading">'+prose(a['formula_note'])+'</p>'
 if s=='birq':core+=extra_math('birq-penalty','Equation 9 · Penalized anchor-constrained objective')
 if s=='smoothness':core+=extra_math('smoothness-value-gradient','Equation 7 · Lower-level value gradient')
 if extra:core+=extra_math(extra[0],extra[1])
 if s=='smoothness':core+=extra_math('smoothness-gradient','Proposition 2 · Projected-gradient mapping')
 deeper='<div class="analysis-discussion">'+''.join('<div class="story-block"><h3>'+e(title)+'</h3><p>'+prose(body)+'</p></div>' for title,body in t['reasoning'])+'</div>'
 if t.get('update_equations') or s=='pbgd-free':deeper+='<details class="technical-detail"><summary>Single-loop update</summary><div class="equation-set update-set">'+extra_math('update-lower','Equation 8 · Lower tracking update')+extra_math('update-upper','Equation 8 · Outer update')+'</div><p>'+prose(t.get('update_caption','Algorithm 1 uses K tracking updates; Theorem 3 analyzes the single-loop case K = 1.'))+'</p></details>'
 deeper+='<details class="technical-detail"><summary>Assumptions behind the analysis</summary><p>'+prose(a['formal'])+'</p><a href="'+e(p['paper'])+'">'+e(t['anchor'])+' in the paper</a></details>'
 faq='<div class="reader-questions"><h3>Further details</h3>'+''.join('<details><summary>'+e(question)+'</summary><p>'+prose(answer)+'</p></details>' for question,answer in g['faq'])+'</div>'
 technical=f'<section id="technical"><h2>{e(g["technical_title"])}</h2>{core}{research_cards(g)}{deeper}{faq}<div class="connection"><h3>Related projects</h3><p>{prose(t["connection"])}</p>{relatedhtml(p,a)}</div></section>'
 venue_note='<p class="note">'+e(p['venue_note'])+'</p>' if p.get('venue_note') else ''
 citation=f'<section id="citation"><h2>Cite this work</h2><button class="button" type="button" data-copy="bibtex">Copy BibTeX</button><p class="status" role="status"></p><pre id="bibtex">{e(bib(p))}</pre>{venue_note}<h3>Research sources</h3>{sourcehtml(p)}</section>'
 return head(p['short']+' | Liuyuan Jiang',t['deck'],2,'papers/'+s+'/')+'<main id="main" class="wrap refined-project professional-project">'+hero+'<div class="project-layout">'+toc+'<article class="article">'+takeaway+idea+technical+interactive+evidence+citation+'</article></div></main>'+footer(2)
