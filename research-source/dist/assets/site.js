document.querySelectorAll("[data-copy]").forEach(b=>b.addEventListener("click",async()=>{const t=document.getElementById(b.dataset.copy).textContent;const s=b.nextElementSibling;try{await navigator.clipboard.writeText(t);s.textContent="Citation copied."}catch{ s.textContent="Select the citation below to copy it."}}));
const NS='http://www.w3.org/2000/svg';
const node=(name,attrs={},text='')=>{const n=document.createElementNS(NS,name);for(const[k,v]of Object.entries(attrs))n.setAttribute(k,v);n.textContent=text;return n;};
function draw(d,lines=[],dots=[],bars=[],xLabel='',yLabel=''){
 const g=d.querySelector('[data-plot]');g.replaceChildren();
 g.append(node('path',{d:'M65 25 V250 H590',fill:'none',stroke:'#9aabc7'}));
 for(let i=0;i<5;i++)g.append(node('path',{d:`M65 ${45+i*48} H590`,stroke:'#e2e7f0',fill:'none'}));
 for(const l of lines)g.append(node('polyline',{points:l.points.map(p=>p.join(',')).join(' '),fill:'none',stroke:l.color||'#354ac6','stroke-width':l.width||3,'stroke-dasharray':l.dash||''}));
 for(const b of bars){g.append(node('rect',{x:b.x,y:b.y,width:b.width,height:b.height,fill:b.color,rx:3}));if(b.label)g.append(node('text',{x:b.x+b.width/2,y:b.y-8,fill:'#111d34','font-size':14,'text-anchor':'middle'},b.label));}
 for(const p of dots)g.append(node('circle',{cx:p.x,cy:p.y,r:p.r||5,fill:p.color||'#354ac6',stroke:'#fff','stroke-width':1.5}));
 g.append(node('text',{x:330,y:283,fill:'#546176','font-size':15,'text-anchor':'middle'},xLabel));
 g.append(node('text',{x:35,y:145,fill:'#546176','font-size':15,transform:'rotate(-90 35 145)','text-anchor':'middle'},yLabel));
}
const cv=a=>{const m=a.reduce((s,x)=>s+x,0)/a.length;return Math.sqrt(a.reduce((s,x)=>s+(x-m)**2,0)/a.length)/m;};
for(const d of document.querySelectorAll('[data-demo]')){
 const type=d.dataset.demo,range=d.querySelector('input[type=range]');
 if(type==='surf'){
  // Appendix F.1: exact raw scalarization solution and fixed evaluation front.
  const gear=d.querySelector('[data-gear]'),segments=d.querySelector('[data-segments]');
  const M=4000,xs=Array.from({length:M+1},(_,i)=>i/M),arcLengths=[0];
  for(let i=1;i<=M;i++){const x=xs[i],previous=xs[i-1];arcLengths.push(arcLengths[i-1]+Math.hypot((1-x)**2-(1-previous)**2,x*x-previous*previous));}
  const total=arcLengths[M],lengthAt=x=>{const index=Math.min(M-1,Math.floor(x*M)),fraction=x*M-index;return arcLengths[index]+fraction*(arcLengths[index+1]-arcLengths[index]);};
  const inverse=fraction=>{const target=fraction*total;let lo=0,hi=M;while(hi-lo>1){const mid=Math.floor((lo+hi)/2);if(arcLengths[mid]<target)lo=mid;else hi=mid;}return (lo+(target-arcLengths[lo])/(arcLengths[hi]-arcLengths[lo]))/M;};
  const xy=x=>[65+510*(1-x)**2,245-210*x*x];
  const update=()=>{const p=+gear.value,N=+segments.value,root=Math.sqrt(p);
   d.querySelector('[data-gear-count]').textContent=p;d.querySelector('[data-count]').textContent=N;
   const uniform=Array.from({length:N+1},(_,n)=>{const w=n/N;return root*w/(1+(root-1)*w);}),arc=Array.from({length:N+1},(_,n)=>inverse(n/N));
   const gaps=uniform.slice(1).map((x,n)=>lengthAt(x)-lengthAt(uniform[n]));
   draw(d,[{points:xs.filter((_,i)=>i%20===0).map(xy),color:'#adb7ca'}],uniform.map(x=>{const[px,py]=xy(x);return{x:px,y:py,color:'#354ac6',r:6}}).concat(arc.map(x=>{const[px,py]=xy(x);return{x:px,y:py,color:'#008274',r:4}})),[],'First evaluation objective','Second evaluation objective');
   d.querySelector('[data-metric]').textContent=`${N+1} solutions on the same front · arc-gap CV: ${cv(gaps).toFixed(2)} for equal weights; approximately 0 for equal arc length.`;};
  gear.addEventListener('input',update);segments.addEventListener('input',update);update();
 }
 if(type==='constraint'){
  const update=()=>{const x=+range.value;d.querySelector('[data-count]').textContent=x.toFixed(2);const yy=y=>245-210*(y-2*x)**2/100;
   draw(d,[{points:Array.from({length:121},(_,i)=>[65+510*i/120,yy(10*i/120)]),color:'#a2aeca'},{points:[[65+153*x,25],[65+153*x,250]],color:'#008274',dash:'6 5'}],[{x:65+102*x,y:yy(2*x),color:'#354ac6',r:6},{x:65+153*x,y:yy(3*x),color:'#008274',r:7}],[],'Lower-level variable y (0 to 10)','Lower-level objective (0 to 100)');
   d.querySelector('[data-plot]').prepend(node('rect',{x:65+153*x,y:25,width:510-153*x,height:225,fill:'#e1f2ee'}));
   d.querySelector('[data-metric]').textContent=`Constrained response: ${(3*x).toFixed(2)} · unconstrained minimum: ${(2*x).toFixed(2)} · constraint multiplier: ${(2*x).toFixed(2)}. Value gradient: ${(2*x).toFixed(2)} = partial objective derivative ${(-4*x).toFixed(2)} + constraint contribution ${(6*x).toFixed(2)}.`;
  };range.addEventListener('input',update);update();
 }
 if(type==='timing'){
  const rs=[-20,15,-10,25,-15,5];let ps=[1,0,1,0,1,0];
  const update=()=>{const mean=ps.reduce((s,x)=>s+x,0)/6,score=rs.reduce((s,r,i)=>s+(ps[i]-mean)*r,0);
   d.querySelectorAll('[data-action]').forEach((b,i)=>{b.setAttribute('aria-pressed',String(!!ps[i]));b.textContent=`Interval ${i+1}: ${ps[i]?'Long':'Flat'}`;});
   draw(d,[{points:[[65,145],[590,145]],color:'#9aabc7',width:1}],[],rs.map((r,i)=>({x:94+i*80,y:r>=0?145-r*3:145,width:40,height:Math.abs(r)*3,color:ps[i]?'#354ac6':'#aab5c8',label:`${r>0?'+':''}${r}`})),'Interval 1 to 6','Return (bps)');
   d.querySelector('[data-metric]').textContent=`Exposure ${(100*mean).toFixed(0)}% · centered timing ${score.toFixed(1)} bps`;};
  d.querySelectorAll('[data-action]').forEach((b,i)=>b.addEventListener('click',()=>{ps[i]=1-ps[i];update();}));d.querySelector('[data-invert]').addEventListener('click',()=>{ps=ps.map(x=>1-x);update();});d.querySelector('[data-reset]').addEventListener('click',()=>{ps=[1,0,1,0,1,0];update();});update();
 }
 if(type==='curvature'){
  // Keep the coordinate system fixed so only the joint slice changes with gamma.
  const ceiling=12,xPixel=x=>70+510*(x+1)/2,yPixel=value=>250-220*value/ceiling;
  const update=()=>{const gamma=+range.value;d.querySelector('[data-count]').textContent=gamma;
   const g=d.querySelector('[data-plot]');g.replaceChildren();
   for(const value of [0,2,4,6,8,10,12]){const y=yPixel(value);g.append(node('path',{d:`M70 ${y} H580`,stroke:'#e2e7f0',fill:'none'}));g.append(node('text',{x:58,y:y+5,'text-anchor':'end','font-size':14,fill:'#546176','data-curvature-tick':value},String(value)));}
   g.append(node('path',{d:'M70 30 V250 H580',stroke:'#9aabc7',fill:'none'}));
   for(const x of [-1,0,1])g.append(node('text',{x:xPixel(x),y:271,'text-anchor':'middle','font-size':14,fill:'#546176'},String(x)));
   for(const [key,coefficient,color] of [['joint',gamma+.5,'#354ac6'],['reduced',.5,'#008274']]){
    const points=Array.from({length:121},(_,i)=>{const x=-1+2*i/120;return[xPixel(x),yPixel(coefficient*x*x)];});
    g.append(node('polyline',{points:points.map(p=>p.join(',')).join(' '),fill:'none',stroke:color,'stroke-width':3.5,'data-curvature-curve':key}));
    g.append(node('circle',{cx:xPixel(1),cy:yPixel(coefficient),r:5,fill:color,stroke:'white','stroke-width':1.5}));
   }
   g.append(node('text',{x:325,y:296,'text-anchor':'middle','font-size':15,fill:'#546176'},'Upper variable x'));
   g.append(node('text',{x:22,y:140,'text-anchor':'middle',transform:'rotate(-90 22 140)','font-size':15,fill:'#546176'},'Objective value'));
   d.querySelector('[data-metric]').textContent=`Fixed-slice curvature: ${1+2*gamma} · reduced curvature: 1`;
  };range.addEventListener('input',update);update();
 }
 if(type==='speech'){
  const update=source=>{const enhanced=source==='enhanced';d.querySelectorAll('[data-source]').forEach(b=>{b.setAttribute('aria-pressed',String(b.dataset.source===source));b.classList.toggle('primary',b.dataset.source===source);});d.querySelectorAll('[data-node]').forEach(n=>n.classList.toggle('active',['input','quant',enhanced?'repr':'anchor'].includes(n.dataset.node)));d.querySelector('[data-explanation]').textContent=enhanced?'Enhanced targets use normalized intermediate features, a fixed random projection, and Gumbel-softmax selection. Gradients pass through this target-generation branch and the masked prediction branch.':'Anchor targets use nearest-neighbor quantization of raw audio features with a fixed projection and codebook. They define a reference task independent of the encoder parameters.';};
  d.querySelectorAll('[data-source]').forEach(b=>b.addEventListener('click',()=>update(b.dataset.source)));update('anchor');
 }
 if(type==='flatness'){
  const update=()=>{const v=+range.value;d.querySelector('[data-count]').textContent=v.toFixed(2);d.querySelector('[data-linear]').textContent=v.toFixed(4);d.querySelector('[data-flat]').textContent=(v**1.5+.003).toFixed(4);
   const pts=f=>Array.from({length:101},(_,i)=>[65+510*i/100,245-210*f(i/100)/1.05]);
   draw(d,[{points:pts(x=>x),color:'#354ac6'},{points:pts(x=>x**1.5+.003),color:'#008274'}],[{x:65+510*v,y:245-210*v/1.05,color:'#354ac6'},{x:65+510*v,y:245-210*(v**1.5+.003)/1.05,color:'#008274'}],[],'Distance to lower optimum (0 to 1)','Bound (0 to 1.05)');
   d.querySelector('[data-metric]').textContent=`Distance contribution: ${(v**1.5).toFixed(4)} · residual: 0.0030`;};range.addEventListener('input',update);update();
 }
 if(type==='regime'){
  const update=mode=>{const coupled=mode==='coupled';d.querySelectorAll('[data-regime]').forEach(b=>{b.setAttribute('aria-pressed',String(b.dataset.regime===mode));b.classList.toggle('primary',b.dataset.regime===mode);});d.querySelectorAll('[data-regime-formula]').forEach(form=>form.hidden=form.dataset.regimeFormula!==mode);d.querySelector('[data-regime-title]').textContent=coupled?'Coupled constraints / inner solve retained':'Uncoupled constraints / fully single-loop';d.querySelector('[data-regime-description]').textContent=coupled?'The feasible set moves with x. Constraint multipliers enter the value-function derivative, and the coupled PBGD-Free extension retains an inner loop. This remaining solve contributes to the total computation.':'The feasible set is fixed as x changes. Under flatness and the stated assumptions, PBGD-Free removes the value-function loop and is fully single-loop.';};
  d.querySelectorAll('[data-regime]').forEach(b=>b.addEventListener('click',()=>update(b.dataset.regime)));update('fixed');
 }
 if(type==='schedule'){
  let mode='single',step=0;
  const update=()=>{const k=mode==='single'?1:4,lower=Math.floor(step/(k+1))*k+Math.min(step%(k+1),k),upper=Math.floor(step/(k+1));d.querySelector('[data-lower]').textContent=lower+' updates';d.querySelector('[data-upper]').textContent=upper+' updates';d.querySelector('[data-stage=lower]').classList.toggle('active',step>0&&step%(k+1)!==0);d.querySelector('[data-stage=upper]').classList.toggle('active',step>0&&step%(k+1)===0);d.querySelector('[data-explanation]').textContent=`Illustrated schedule: ${k} lower-level update${k===1?'':'s'} per upper-level update. ${step===0?'Press Next update to advance the sequence.':'Completed '+step+' gradient updates in total.'}`;d.querySelectorAll('[data-mode]').forEach(b=>{b.setAttribute('aria-pressed',String(b.dataset.mode===mode));b.classList.toggle('primary',b.dataset.mode===mode);});};
  d.querySelectorAll('[data-mode]').forEach(b=>b.addEventListener('click',()=>{mode=b.dataset.mode;step=0;update();}));d.querySelector('[data-next]').addEventListener('click',()=>{step++;update();});update();
 }
}

const contents=document.querySelector('.toc');
if(contents&&'IntersectionObserver' in window){
 const links=[...contents.querySelectorAll('a[href^="#"]')];
 const observer=new IntersectionObserver(entries=>{for(const entry of entries){if(entry.isIntersecting){links.forEach(link=>{if(link.getAttribute('href')==='#'+entry.target.id)link.setAttribute('aria-current','location');else link.removeAttribute('aria-current');});}}},{rootMargin:'-5% 0px -70% 0px'});
 links.forEach(link=>{const section=document.querySelector(link.getAttribute('href'));if(section)observer.observe(section);});
}

// The home-page research explorer keeps paper links as native fragment links.
for (const explorer of document.querySelectorAll('[data-direction-explorer]')) {
 const tabs=[...explorer.querySelectorAll('[data-direction]')];
 const select=id=>{
  for (const tab of tabs) {
   const active=tab.dataset.direction===id;
   tab.setAttribute('aria-selected',String(active));tab.tabIndex=active?0:-1;
   document.getElementById(tab.getAttribute('aria-controls')).hidden=!active;
  }
 };
 for (const [i,tab] of tabs.entries()) {
  tab.addEventListener('click',()=>select(tab.dataset.direction));
  tab.addEventListener('keydown',event=>{
   let index;
   if(event.key==='ArrowRight')index=(i+1)%tabs.length;
   if(event.key==='ArrowLeft')index=(i+tabs.length-1)%tabs.length;
   if(event.key==='Home')index=0;
   if(event.key==='End')index=tabs.length-1;
   if(index!==undefined){event.preventDefault();select(tabs[index].dataset.direction);tabs[index].focus();}
  });
 }
 const followDirectionHash=()=>{const id=location.hash.slice(1);if(tabs.some(tab=>tab.dataset.direction===id))select(id);};
 followDirectionHash();window.addEventListener('hashchange',followDirectionHash);
}
for (const lab of document.querySelectorAll('[data-opening]')) {
 if(lab.dataset.opening==='pareto') {
  const a=.5,k=5,A=(1-a)*k/(1-Math.exp(-k));
  const loss=z=>a*(1-z)+(1-a)*(Math.exp(-k*z)-Math.exp(-k))/(1-Math.exp(-k));
  const slope=z=>a+A*Math.exp(-k*z);
  const wLo=slope(1)/(1+slope(1)),wHi=slope(0)/(1+slope(0));
  const solve=w=>w<=wLo?1:w>=wHi?0:Math.min(1,Math.max(0,-Math.log((w/(1-w)-a)/A)/k));
  const M=4000,arc=[0];
  for(let i=1;i<=M;i++){const z=i/M,p=(i-1)/M;arc.push(arc[i-1]+Math.hypot(z-p,loss(z)-loss(p)));}
  const at=z=>{const i=Math.min(M-1,Math.floor(z*M));return arc[i]+(z*M-i)*(arc[i+1]-arc[i]);};
  const inverse=q=>{const target=q*arc[M];let lo=0,hi=M;while(hi-lo>1){const mid=Math.floor((lo+hi)/2);if(arc[mid]<target)lo=mid;else hi=mid;}return(lo+(target-arc[lo])/(arc[hi]-arc[lo]))/M;};
  const points=[...lab.querySelectorAll('[data-front-point]')],range=lab.querySelector('#front-candidate');
  let mode='weights',zs=[],selected=4;
  const select=index=>{
   selected=Math.min(points.length-1,Math.max(0,index));range.value=String(selected+1);
   for(const [i,point] of points.entries()){point.setAttribute('aria-pressed',String(i===selected));point.setAttribute('r',i===selected?8:5.5);point.setAttribute('tabindex',i===selected?'0':'-1');}
   const z=zs[selected];
   lab.querySelector('[data-candidate-number]').textContent=`${selected+1} of ${points.length}`;
   lab.querySelector('[data-quality-score]').textContent=(1-z).toFixed(2);
   lab.querySelector('[data-faithfulness-score]').textContent=(1-loss(z)).toFixed(2);
  };
  const update=newMode=>{
   mode=newMode;lab.dataset.spacingMode=mode;
   for(const b of lab.querySelectorAll('[data-spacing]'))b.setAttribute('aria-pressed',String(b.dataset.spacing===mode));
   zs=points.map((point,i)=>{const z=mode==='arc'?inverse(i/(points.length-1)):solve(wHi-i*(wHi-wLo)/(points.length-1));point.setAttribute('cx',90+280*(1-z));point.setAttribute('cy',305-280*(1-loss(z)));point.setAttribute('aria-label',`Candidate ${i+1}: quality ${(1-z).toFixed(2)}, faithfulness ${(1-loss(z)).toFixed(2)}`);return z;});
   const gaps=zs.slice(1).map((z,i)=>at(z)-at(zs[i])),ratio=Math.max(...gaps)/Math.min(...gaps);
   lab.querySelector('[data-spacing-result]').textContent=mode==='arc'?'The candidates now cover the curve with even arc-length gaps.':`The largest gap is ${ratio.toFixed(1)}× the smallest. Equal weight steps produce uneven spacing.`;
   select(selected);
  };
  for(const b of lab.querySelectorAll('[data-spacing]'))b.addEventListener('click',()=>update(b.dataset.spacing));
  for(const [i,point] of points.entries()) {
   point.addEventListener('click',()=>select(i));
   point.addEventListener('keydown',event=>{
    let next=i;
    if(event.key==='ArrowRight'||event.key==='ArrowDown')next=Math.min(points.length-1,i+1);
    if(event.key==='ArrowLeft'||event.key==='ArrowUp')next=Math.max(0,i-1);
    if(event.key==='Home')next=0;
    if(event.key==='End')next=points.length-1;
    if(['Enter',' ','ArrowRight','ArrowLeft','ArrowUp','ArrowDown','Home','End'].includes(event.key)){event.preventDefault();select(next);points[next].focus();}
   });
  }
  range.addEventListener('input',()=>select(+range.value-1));
  update('weights');
 }
 if(lab.dataset.opening==='bakery') {
  const range=lab.querySelector('#bakery-price'),g=lab.querySelector('[data-bakery-plot]');
  const profitBase=lab.querySelector('[data-bakery-profit-base]'),profitOverlay=lab.querySelector('[data-bakery-profit-overlay]');
  const plotTabs=[...lab.querySelectorAll('[data-bakery-view]')],plotPanels=[...lab.querySelectorAll('[data-bakery-panel]')];
  const selectPlot=index=>{
   plotTabs.forEach((tab,i)=>{tab.setAttribute('aria-selected',String(i===index));tab.tabIndex=i===index?0:-1;plotPanels[i].hidden=i!==index;});
  };
  lab.querySelector('.bakery-plot-tabs').hidden=false;
  plotTabs.forEach((tab,i)=>{
   tab.addEventListener('click',()=>selectPlot(i));
   tab.addEventListener('keydown',event=>{
    let index;
    if(event.key==='ArrowRight'||event.key==='ArrowLeft')index=1-i;
    if(event.key==='Home')index=0;
    if(event.key==='End')index=1;
    if(index!==undefined){event.preventDefault();selectPlot(index);plotTabs[index].focus();}
   });
  });
  selectPlot(0);
  const xx=p=>55+340*(p-1)/7,yy=q=>205-175*q/7;
  const profitX=p=>65+330*(p-1)/7,profitY=value=>205-175*value/15;
  for(const value of [0,5,10,15]) {
   profitBase.append(node('path',{d:`M65 ${profitY(value)} H395`,fill:'none',stroke:'#e0e5ef','stroke-width':1}));
   profitBase.append(node('text',{x:54,y:profitY(value)+6,'text-anchor':'end','data-profit-tick':value},String(value)));
  }
  profitBase.append(node('path',{d:'M65 24 V205 H400',fill:'none',stroke:'#9aabc7'}));
  for(const price of [1,4,8])profitBase.append(node('text',{x:profitX(price),y:228,'text-anchor':'middle'},'$'+price));
  profitBase.append(node('text',{x:230,y:252,'text-anchor':'middle'},'Price per kg, x'));
  profitBase.append(node('text',{x:18,y:115,'text-anchor':'middle',transform:'rotate(-90 18 115)'},'Profit ($)'));
  const toggles=[...lab.querySelectorAll('[data-bakery-constraint]')];
  const money=x=>'$'+x.toFixed(2),quantity=x=>x.toFixed(2).replace(/\.?0+$/,'');
  const update=()=>{
   const price=+range.value,budget=toggles.some(b=>b.dataset.bakeryConstraint==='budget'&&b.getAttribute('aria-pressed')==='true'),stock=toggles.some(b=>b.dataset.bakeryConstraint==='stock'&&b.getAttribute('aria-pressed')==='true');
   const preferred=p=>Math.max(0,8-p);
   const purchase=p=>Math.min(preferred(p),budget?12/p:Infinity,stock?3:Infinity);
   const bought=purchase(price),profit=(price-1)*bought;
   lab.querySelector('[data-bakery-price]').textContent=money(price);
   lab.querySelector('[data-bakery-quantity]').textContent=quantity(bought)+' kg';
   lab.querySelector('[data-bakery-profit]').textContent=money(profit);
   lab.querySelector('[data-bakery-constraints]').textContent=budget&&stock?'Spending stays within $12; purchases stay within 3 kg.':budget?'The customer can spend at most $12.':stock?'The bakery can sell at most 3 kg.':'No extra constraints.';
   const reason=[];
   if(budget&&Math.abs(bought-12/price)<1e-8&&preferred(price)>bought+1e-8)reason.push('the $12 budget');
   if(stock&&Math.abs(bought-3)<1e-8&&preferred(price)>bought+1e-8)reason.push('the 3 kg stock limit');
   lab.querySelector('[data-bakery-result]').textContent=`At ${money(price)} per kg, the customer buys ${quantity(bought)} kg. The bakery earns ${money(profit)}.`+(reason.length?` The purchase is limited by ${reason.join(' and ')}.`:' The customer can buy their preferred amount.');

   g.replaceChildren();
   for(const q of [0,3,7]) {
    g.append(node('path',{d:`M55 ${yy(q)} H395`,stroke:'#e0e5ef','stroke-width':1}));
    g.append(node('text',{x:44,y:yy(q)+6,'text-anchor':'end'},String(q)));
   }
   g.append(node('path',{d:'M55 24 V205 H400',fill:'none',stroke:'#9aabc7'}));
   const curve=f=>Array.from({length:141},(_,i)=>{const p=1+7*i/140;return `${xx(p)},${yy(f(p))}`;}).join(' ');
   g.append(node('polyline',{points:curve(preferred),fill:'none',stroke:'#9caac2','stroke-width':3,'stroke-dasharray':'7 5'}));
   g.append(node('polyline',{points:curve(purchase),fill:'none',stroke:'#007c70','stroke-width':3}));
   g.append(node('path',{d:`M${xx(price)} 25 V205`,stroke:'#354ac6','stroke-width':1.5,'stroke-dasharray':'3 5'}));
   g.append(node('circle',{cx:xx(price),cy:yy(bought),r:6,fill:'#354ac6',stroke:'white','stroke-width':2}));
   for(const p of [1,4,8])g.append(node('text',{x:xx(p),y:228,'text-anchor':'middle'},'$'+p));
   g.append(node('text',{x:228,y:252,'text-anchor':'middle'},'Price per kg, x'));
   g.append(node('text',{x:18,y:115,'text-anchor':'middle',transform:'rotate(-90 18 115)'},'Bread bought, y (kg)'));
   profitOverlay.replaceChildren();
   const profitCurve=response=>Array.from({length:141},(_,i)=>{const p=1+7*i/140;return `${profitX(p)},${profitY((p-1)*response(p))}`;}).join(' ');
   const currentProfitPoints=profitCurve(purchase);
   profitOverlay.append(node('polygon',{points:`65,205 ${currentProfitPoints} 395,205`,fill:'#007c70','fill-opacity':.07}));
   profitOverlay.append(node('polyline',{points:profitCurve(preferred),fill:'none',stroke:'#9caac2','stroke-width':3,'stroke-dasharray':'7 5','data-profit-baseline':''}));
   profitOverlay.append(node('polyline',{points:currentProfitPoints,fill:'none',stroke:'#007c70','stroke-width':3.5,'stroke-linejoin':'round','data-profit-curve':''}));
   profitOverlay.append(node('path',{d:`M${profitX(price)} 30 V205 M65 ${profitY(profit)} H${profitX(price)}`,fill:'none',stroke:'#354ac6','stroke-width':1.5,'stroke-dasharray':'3 5'}));
   profitOverlay.append(node('circle',{cx:profitX(price),cy:profitY(profit),r:6,fill:'#354ac6',stroke:'#fff','stroke-width':2,'data-profit-selected':'','data-price':price,'data-profit':profit}));
   profitOverlay.append(node('text',{x:profitX(price)+(price>5.5?-10:10),y:profitY(profit)-12,'text-anchor':price>5.5?'end':'start',class:'profit-point-label'},money(profit)));
   lab.querySelector('.bakery-profit-plot').setAttribute('aria-label',`Bakery profit versus bread price, using the customer's purchase at every price. The horizontal axis is price from one to eight dollars per kg. The vertical axis is profit from zero to fifteen dollars. At ${money(price)} per kg, the customer buys ${quantity(bought)} kg and profit is ${money(profit)}.`);

  };
  range.addEventListener('input',update);
  for(const button of toggles)button.addEventListener('click',()=>{button.setAttribute('aria-pressed',String(button.getAttribute('aria-pressed')!=='true'));update();});
  update();
 }
 if(lab.dataset.opening==='applications') {
  const select=id=>{
   for(const b of lab.querySelectorAll('[data-application]'))b.setAttribute('aria-pressed',String(b.dataset.application===id));
   for(const view of lab.querySelectorAll('[data-application-view]'))view.hidden=view.dataset.applicationView!==id;
  };
  for(const b of lab.querySelectorAll('[data-application]'))b.addEventListener('click',()=>select(b.dataset.application));
  select('speech');
 }
}

// Evidence controls switch between source-reported comparisons, never simulated results.
for (const lab of document.querySelectorAll('[data-evidence-lab]')) {
 const list=lab.querySelector('[role=tablist]'),tabs=[...lab.querySelectorAll('[data-evidence-tab]')],panels=[...lab.querySelectorAll('[data-evidence-panel]')];
 const select=index=>{
  tabs.forEach((tab,i)=>{const active=i===index;tab.setAttribute('aria-selected',String(active));tab.tabIndex=active?0:-1;panels[i].hidden=!active;panels[i].setAttribute('role','tabpanel');panels[i].setAttribute('aria-labelledby',tab.id);});
  updateTableHints();
 };
 const updateTableHints=()=>panels.forEach(panel=>{const table=panel.querySelector('.table-scroll'),hint=panel.querySelector('.table-hint');hint.hidden=panel.hidden||table.scrollWidth<=table.clientWidth+1;});
 window.addEventListener('resize',updateTableHints);
 list.hidden=false;
 tabs.forEach((tab,i)=>{
  tab.addEventListener('click',()=>select(i));
  tab.addEventListener('keydown',event=>{
   let index;
   if(event.key==='ArrowRight')index=(i+1)%tabs.length;
   if(event.key==='ArrowLeft')index=(i+tabs.length-1)%tabs.length;
   if(event.key==='Home')index=0;
   if(event.key==='End')index=tabs.length-1;
   if(index!==undefined){event.preventDefault();select(index);tabs[index].focus();}
  });
 });
 select(0);
 const followEvidenceHash=()=>{
  const index=panels.findIndex(panel=>panel.id===location.hash.slice(1));
  if(index>=0){select(index);panels[index].scrollIntoView({block:'start'});}
 };
 panels.forEach((panel,index)=>document.querySelectorAll('a[href="#'+panel.id+'"]').forEach(link=>link.addEventListener('click',()=>select(index))));
 window.addEventListener('hashchange',followEvidenceHash);
 followEvidenceHash();
}

// Keep full equations readable and keyboard-scrollable when a panel is narrow.
for (const equation of document.querySelectorAll('.math-block .katex-display')) {
 const block=equation.closest('.math-block'),hint=block.querySelector('.math-scroll-hint');
 const update=()=>{
  const scrolls=equation.clientWidth>0&&equation.scrollWidth>equation.clientWidth+1;
  hint.hidden=!scrolls;
  if(scrolls){equation.tabIndex=0;equation.setAttribute('role','region');equation.setAttribute('aria-label',block.dataset.equationLabel||'Equation');}
  else{equation.removeAttribute('tabindex');equation.removeAttribute('role');equation.removeAttribute('aria-label');}
 };
 if('ResizeObserver' in window)new ResizeObserver(update).observe(equation);
 window.addEventListener('resize',update);
 document.fonts?.ready.then(update);
 update();
}
