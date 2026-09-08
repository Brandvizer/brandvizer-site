import os, re
R = os.path.expanduser('~/mnt/brandvizer-site')

# ---------- de twee diepe cases terughalen uit /werk ----------
w = open(R + '/werk/index.html').read()
arts = re.findall(r'<article class="cs[^"]*">.*?</article>', w, re.S)
assert len(arts) == 2, len(arts)
extra = [a.replace('src="/assets/', 'src="assets/').replace('<article class="cs flip">', '<article class="cs">') for a in arts]

# ---------- homepage: rail bouwen ----------
p = R + '/index.html'; h = open(p).read()
s = h.index('  <!-- WALDO / SVB -->')
e = h.index('  <!-- KORTE CASES -->')
waldo = h[s:e].replace('  <!-- WALDO / SVB -->\n', '').strip()

names = ['SVB', 'ABN AMRO', 'Belastingdienst']
tabs = ''.join('<button class="cs-tab" type="button" role="tab" aria-current="%s" data-go="%d">%s</button>' % ('true' if i == 0 else 'false', i, n) for i, n in enumerate(names))

rail = '''  <div class="cs-ctrl wrap">
    <div class="cs-tabs" role="tablist" aria-label="Kies een project">%s</div>
    <div class="cs-arrows">
      <button class="cs-arrow" type="button" data-dir="-1" aria-label="Vorig project"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 5l-7 7 7 7"/></svg></button>
      <button class="cs-arrow" type="button" data-dir="1" aria-label="Volgend project"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 5l7 7-7 7"/></svg></button>
    </div>
  </div>
  <div class="cs-rail" id="csRail" tabindex="0" role="region" aria-label="Projecten, veeg of gebruik de pijltjes">
%s

%s

%s
  </div>
  <div class="cs-prog" aria-hidden="true"><i id="csProg"></i></div>
  <p class="cs-hint wrap">Veeg of gebruik de pijltjes om de projecten door te lopen.</p>

''' % (tabs, waldo, extra[0], extra[1])

h = h[:s] + rail + h[e:]
h = h.replace('<p class="lead rv" style="margin-top:22px">Dit zijn grote organisaties, maar het recept is voor jouw bedrijf hetzelfde: eerst begrijpen wat klanten nodig hebben, dan bouwen. Hieronder één project helemaal uitgelegd, daaronder vier kort. Klik op de kleine beelden om meer te zien.</p>',
              '<p class="lead rv" style="margin-top:22px">Dit zijn grote organisaties, maar het recept is voor jouw bedrijf hetzelfde: eerst begrijpen wat klanten nodig hebben, dan bouwen. Drie projecten helemaal uitgelegd, daaronder vier kort.</p>')
h = h.replace('  <div class="wrap"><p class="rv" style="margin-top:34px"><a class="btn ghost" href="/werk">Bekijk alle projecten</a></p></div>\n', '')

# JS voor de slider, net voor het slot van het bestaande script
anchor = "  /* Cases: thumbs wisselen het hoofdbeeld */"
js = '''  /* Cases: horizontale slider */
  (function(){
    var rail=document.getElementById('csRail'); if(!rail) return;
    var slides=Array.prototype.slice.call(rail.querySelectorAll('.cs'));
    var tabs=Array.prototype.slice.call(document.querySelectorAll('.cs-tab'));
    var arrows=Array.prototype.slice.call(document.querySelectorAll('.cs-arrow'));
    var prog=document.getElementById('csProg');
    function index(){
      var best=0, min=1e9;
      slides.forEach(function(s,i){ var d=Math.abs(s.offsetLeft-rail.scrollLeft); if(d<min){min=d;best=i;} });
      return best;
    }
    function go(i){
      i=Math.max(0,Math.min(slides.length-1,i));
      rail.scrollTo({left:slides[i].offsetLeft-parseFloat(getComputedStyle(rail).paddingLeft),behavior:reduce?'auto':'smooth'});
    }
    function sync(){
      var i=index();
      tabs.forEach(function(t,j){ t.setAttribute('aria-current', j===i?'true':'false'); });
      arrows[0].disabled=i===0; arrows[1].disabled=i===slides.length-1;
      if(prog){ prog.style.width=(100/slides.length)+'%'; prog.style.transform='translateX('+(i*100)+'%)'; }
    }
    tabs.forEach(function(t){ t.addEventListener('click',function(){ go(parseInt(t.dataset.go,10)); }); });
    arrows.forEach(function(a){ a.addEventListener('click',function(){ go(index()+parseInt(a.dataset.dir,10)); }); });
    rail.addEventListener('keydown',function(e){
      if(e.key==='ArrowRight'){ e.preventDefault(); go(index()+1); }
      if(e.key==='ArrowLeft'){ e.preventDefault(); go(index()-1); }
    });
    var t=null;
    rail.addEventListener('scroll',function(){ clearTimeout(t); t=setTimeout(sync,80); },{passive:true});
    addEventListener('resize',sync); sync();
  })();

'''
assert h.count(anchor) == 1
h = h.replace(anchor, js + anchor)
open(p, 'w').write(h)
print('index klaar')

# ---------- CSS ----------
css = open(R + '/assets/cases.css').read()
add = '''

/* ---- Slider op de homepage ---- */
.cs-ctrl{display:flex;align-items:center;justify-content:space-between;gap:20px;flex-wrap:wrap;margin-top:38px}
.cs-tabs{display:flex;gap:8px;flex-wrap:wrap}
.cs-tab{border:1.5px solid var(--line);background:var(--white);color:var(--ink2);border-radius:999px;padding:10px 18px;font-family:var(--display);font-weight:600;font-size:var(--small);cursor:pointer;transition:background .2s,color .2s,border-color .2s}
.cs-tab:hover{border-color:var(--ink);color:var(--ink)}
.cs-tab[aria-current="true"]{background:var(--ink);border-color:var(--ink);color:var(--white)}
.cs-arrows{display:flex;gap:8px}
.cs-arrow{width:44px;height:44px;border-radius:50%;border:1.5px solid var(--line);background:var(--white);color:var(--ink);cursor:pointer;display:grid;place-items:center;transition:border-color .2s,opacity .2s}
.cs-arrow:hover:not(:disabled){border-color:var(--ink)}
.cs-arrow:disabled{opacity:.3;cursor:default}
.cs-rail{display:flex;gap:20px;overflow-x:auto;overscroll-behavior-x:contain;scroll-snap-type:x mandatory;padding:22px var(--pad) 8px;scroll-padding-left:var(--pad);margin:0;scrollbar-width:none;-ms-overflow-style:none}
.cs-rail::-webkit-scrollbar{display:none}
.cs-rail:focus-visible{outline:3px solid var(--pink);outline-offset:-3px;border-radius:26px}
.cs-rail .cs{flex:0 0 calc(100% - 52px);scroll-snap-align:start;scroll-snap-stop:always;display:grid;grid-template-columns:minmax(0,1.02fr) minmax(0,.98fr);column-gap:clamp(26px,3.4vw,54px);align-items:start;background:var(--white);border:1px solid var(--line);border-radius:26px;padding:clamp(22px,2.6vw,38px);margin:0}
.cs-rail .cs.flip{grid-template-columns:minmax(0,1.02fr) minmax(0,.98fr)}
.cs-rail .cs-media,.cs-rail .cs.flip .cs-media{grid-column:1;position:static;order:0}
.cs-rail .cs-text,.cs-rail .cs.flip .cs-text{grid-column:2;padding:0}
.cs-rail .cs-main,.cs-rail .cs.flip .cs-main{border-radius:18px;box-shadow:0 18px 44px rgba(15,27,45,.12)}
.cs-rail .cs-thumbs,.cs-rail .cs.flip .cs-thumbs{padding:0;justify-content:flex-start}
.cs-rail .cs h3{font-size:clamp(24px,2.6vw,34px)}
.cs-prog{height:3px;background:var(--line);border-radius:99px;margin:18px var(--pad) 0;overflow:hidden}
.cs-prog i{display:block;height:100%;width:33.33%;background:var(--pink);border-radius:99px;transition:transform .35s var(--ease)}
.cs-hint{margin-top:14px;font-family:var(--hand);font-size:var(--hand-m);color:var(--mute)}
@media(max-width:960px){
  .cs-arrows{display:none}
  .cs-rail{padding-top:16px}
  .cs-rail .cs{flex:0 0 calc(100% - 34px);grid-template-columns:1fr;row-gap:22px;padding:18px}
  .cs-rail .cs-media,.cs-rail .cs-text,.cs-rail .cs.flip .cs-media,.cs-rail .cs.flip .cs-text{grid-column:1}
  .cs-rail .cs-main,.cs-rail .cs.flip .cs-main{margin:0;border-radius:14px}
  .cs-tabs{width:100%}
  .cs-tab{flex:1;text-align:center;padding:10px 12px}
}
'''
if '/* ---- Slider' not in css:
    open(R + '/assets/cases.css', 'w').write(css + add)
print('css klaar')
