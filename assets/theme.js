/* Brandvizer: licht of donker. Standaard volgt de browser, een eigen keuze wordt onthouden. */
(function(){
  function current(){
    return document.documentElement.dataset.theme ||
      (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  }
  function labels(t){
    document.querySelectorAll('[data-theme-toggle]').forEach(function(b){
      b.setAttribute('aria-label', t === 'dark' ? 'Zet de site in de lichte stand' : 'Zet de site in de donkere stand');
    });
  }
  document.addEventListener('click', function(e){
    var b = e.target.closest && e.target.closest('[data-theme-toggle]');
    if(!b) return;
    var next = current() === 'dark' ? 'light' : 'dark';
    document.documentElement.dataset.theme = next;
    try{ localStorage.setItem('thema', next); }catch(e){}
    labels(next);
  });
  labels(current());
})();

/* Navigatie: mobiel menu en actieve sectie op de homepage. Werkt op elke pagina. */
(function(){
  function ready(fn){ if(document.readyState!=='loading') fn(); else document.addEventListener('DOMContentLoaded',fn); }
  ready(function(){
    var btn=document.getElementById('menuBtn'), m=document.getElementById('mmenu');
    if(btn && m){
      var setMenu=function(o){ m.classList.toggle('open',o); btn.setAttribute('aria-expanded',o); btn.textContent=o?'Sluit':'Menu'; document.body.style.overflow=o?'hidden':''; };
      btn.addEventListener('click',function(){ setMenu(!m.classList.contains('open')); });
      m.querySelectorAll('a').forEach(function(a){ a.addEventListener('click',function(){ setMenu(false); }); });
      document.addEventListener('keydown',function(e){ if(e.key==='Escape' && m.classList.contains('open')){ setMenu(false); btn.focus(); } });
      matchMedia('(min-width:961px)').addEventListener('change',function(e){ if(e.matches) setMenu(false); });
    }
    /* Alleen op de homepage: markeer het menu-item van de sectie waar je bent, en niets als die sectie niet in het menu staat */
    var home=location.pathname==='/'||/\/index\.html$/.test(location.pathname);
    if(!home) return;
    var map={werk:'/werk',aanpak:'#aanpak',pakketten:'/prijzen',over:'#over',kennis:'/kennis',contact:'#contact'};
    var links=[].slice.call(document.querySelectorAll('.nav-links a'));
    var secs=[].slice.call(document.querySelectorAll('main > section[id]'));
    function mark(){
      var y=scrollY+innerHeight*0.35, cur=null;
      secs.forEach(function(s){ if(s.offsetTop<=y) cur=s.id; });
      if(innerHeight+scrollY>=document.documentElement.scrollHeight-4) cur='contact';
      var href=map[cur];
      links.forEach(function(a){ var on=!!href && a.getAttribute('href')===href; a.classList.toggle('here',on); });
    }
    addEventListener('scroll',mark,{passive:true}); addEventListener('resize',mark); mark();
  });
})();
