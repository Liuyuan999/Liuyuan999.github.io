import subprocess,shutil,re,json
from html.parser import HTMLParser
MATH_CONFIG=json.loads((ROOT/'content/equations.json').read_text())
node_path=shutil.which('node') or '/Users/liuyuan/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node'
MATH_HTML=json.loads(subprocess.check_output([node_path,str(ROOT/'compile_math.mjs')],cwd=ROOT,text=True))
MATH_PATTERN=re.compile('|'.join(re.escape(k) for k in sorted(MATH_CONFIG['inline'],key=len,reverse=True)))
def display_math(tex,label='',attributes=''):
 label_html='<div class="math-label">'+e(label)+'</div>' if label else ''
 return '<div class="math-block" data-equation-label="'+e(label or 'Equation')+'" '+attributes+'>'+label_html+MATH_HTML['display:'+tex]+'<p class="math-scroll-hint" hidden>Scroll horizontally to read the full equation.</p></div>'
def extra_math(key,label='',attributes=''):
 return display_math(MATH_CONFIG['extra'][key],label,attributes)
def paper_math(slug):
 return '<div class="equation-set">'+''.join(display_math(v['tex'],v['label']) for v in MATH_CONFIG['papers'][slug])+'</div>'
class TypesetProse(HTMLParser):
 def __init__(self,mapping):
  super().__init__(convert_charrefs=False);self.out=[];self.stack=[];self.mapping=mapping;self.pattern=re.compile("|".join(re.escape(k) for k in sorted(mapping,key=len,reverse=True)))
 def handle_starttag(self,tag,attrs):
  self.out.append(self.get_starttag_text());a=dict(attrs)
  if tag not in ['meta','link','img','input','br','hr','source','area','base','embed','param','wbr']:
   self.stack.append((tag,tag in ['script','style','pre','code','svg','math','title'] or 'katex' in a.get('class','').split()))
 def handle_startendtag(self,tag,attrs):self.out.append(self.get_starttag_text())
 def handle_endtag(self,tag):
  self.out.append('</'+tag+'>')
  for i in range(len(self.stack)-1,-1,-1):
   if self.stack[i][0]==tag:self.stack=self.stack[:i];break
 def handle_data(self,data):
  if any(skip for _,skip in self.stack):self.out.append(data);return
  self.out.append(self.pattern.sub(lambda m:MATH_HTML['inline:'+self.mapping[m.group()]],data))
 def handle_entityref(self,name):self.out.append('&'+name+';')
 def handle_charref(self,name):self.out.append('&#'+name+';')
 def handle_comment(self,data):self.out.append('<!--'+data+'-->')
 def handle_decl(self,data):self.out.append('<!'+data+'>')
def typeset_prose(document,slug=None):
 mapping={**MATH_CONFIG['inline'],**MATH_CONFIG.get('paper_inline',{}).get(slug,{})}
 parser=TypesetProse(mapping);parser.feed(document);return ''.join(parser.out)
# Bundle stylesheet and fonts with the site. Typesetting does not require browser JavaScript.
(D/'assets/katex').mkdir(parents=True,exist_ok=True)
shutil.copy2(ROOT/'vendor/katex/dist/katex.min.css',D/'assets/katex/katex.min.css')
shutil.copytree(ROOT/'vendor/katex/dist/fonts',D/'assets/katex/fonts',dirs_exist_ok=True)
shutil.copy2(ROOT/'vendor/katex/LICENSE',D/'assets/katex/LICENSE')
