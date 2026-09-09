(function(){
  document.documentElement.classList.add('js');
  var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hasGSAP=typeof gsap!=='undefined';

  /* Nav */
  var nav=document.getElementById('nav');
  addEventListener('scroll',function(){ nav.classList.toggle('solid',scrollY>20); },{passive:true});
  (function(){
    var links=Array.prototype.slice.call(document.querySelectorAll('.nav-links a[href^="#"]'));
    var secs=links.map(function(a){ return document.querySelector(a.getAttribute('href')); });
    function mark(){
      var y=scrollY+140, best=-1;
      secs.forEach(function(s,i){ if(s && s.offsetTop<=y) best=i; });
      links.forEach(function(a,i){ a.classList.toggle('here',i===best); });
    }
    addEventListener('scroll',mark,{passive:true}); addEventListener('resize',mark); mark();
  })();
  var btn=document.getElementById('menuBtn'), m=document.getElementById('mmenu');
  function setMenu(o){ m.classList.toggle('open',o); btn.setAttribute('aria-expanded',o); btn.textContent=o?'Sluit':'Menu'; document.body.style.overflow=o?'hidden':''; }
  btn.addEventListener('click',function(){ setMenu(!m.classList.contains('open')); });
  m.querySelectorAll('a').forEach(function(a){ a.addEventListener('click',function(){ setMenu(false); }); });

  /* Hero mock: place highlights around fields */
  function placeHL(){
    var mock=document.querySelector('.mock'); if(!mock) return;
    [['mf1','hl1'],['mf2','hl2']].forEach(function(p){
      var f=document.getElementById(p[0]), h=document.getElementById(p[1]);
      var r=f.getBoundingClientRect(), mr=mock.getBoundingClientRect();
      // compensate rotation by using offset positions instead
      h.style.left=(f.offsetLeft-6)+'px'; h.style.top=(f.offsetTop-6)+'px'; h.style.width=(f.offsetWidth+12)+'px'; h.style.height=(f.offsetHeight+12)+'px';
    });
  }
  placeHL(); addEventListener('resize',placeHL);

  /* Hero sequence */
  function heroSeq(){
    if(!document.getElementById('hl1')) return;
    var notes=['hl1','n1','hl2','n2','n4'];
    if(reduce){ notes.forEach(function(id){document.getElementById(id).classList.add('show');}); document.getElementById('ul1').classList.add('on'); return; }
    var t=900;
    notes.forEach(function(id,i){ setTimeout(function(){ document.getElementById(id).classList.add('show'); }, t+i*520); });
    setTimeout(function(){ document.getElementById('ul1').classList.add('on'); }, 700);
  }
  if(hasGSAP && !reduce){
    gsap.registerPlugin(ScrollTrigger);
    gsap.from('[data-hero]',{opacity:0,y:24,duration:.9,ease:'power3.out',stagger:.1,onComplete:heroSeq});
  } else { heroSeq(); }

  /* Mobile CTA: pas tonen na de hero */
  var mcta=document.querySelector('.mcta'), heroAct=document.querySelector('.hero .actions');
  if(mcta&&heroAct){ mcta.style.transform='translateY(120%)'; mcta.style.transition='transform .4s var(--ease)';
    new IntersectionObserver(function(es){ mcta.style.transform=es[0].isIntersecting||es[0].boundingClientRect.top>0?'translateY(120%)':'none'; },{threshold:0}).observe(heroAct); }
  var checkSec=document.getElementById('check');
  if(mcta&&checkSec){ new IntersectionObserver(function(es){ mcta.style.opacity=es[0].isIntersecting?'0':'1'; mcta.style.pointerEvents=es[0].isIntersecting?'none':'auto'; },{threshold:.15}).observe(checkSec); }

  /* Reveals + marker */
  if(hasGSAP && !reduce){
    gsap.utils.toArray('.rv').forEach(function(el){
      ScrollTrigger.create({trigger:el,start:'top 88%',once:true,onEnter:function(){ gsap.to(el,{opacity:1,y:0,duration:.85,ease:'power3.out'}); }});
    });
  } else { document.querySelectorAll('.rv').forEach(function(e){e.style.opacity=1;e.style.transform='none';}); }
  var io=new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('on'); io.unobserve(e.target);} }); },{threshold:.6});
  document.querySelectorAll('[data-mark]').forEach(function(el){ io.observe(el); });

  /* Chips: toggle on tap for touch */
  document.querySelectorAll('.chip').forEach(function(c){ c.addEventListener('click',function(){ c.focus(); }); });

  /* Cases: thumbs wisselen het hoofdbeeld */
  document.querySelectorAll('.cs-media, .csm-media').forEach(function(m){
    var main=m.querySelector('.cs-main img, .csm-main');
    m.querySelectorAll('button').forEach(function(b){
      b.addEventListener('click',function(){
        var src=b.querySelector('img').getAttribute('src'); if(main.getAttribute('src')===src) return;
        m.querySelectorAll('button').forEach(function(x){x.classList.remove('on');}); b.classList.add('on');
        main.classList.add('swap'); setTimeout(function(){ main.setAttribute('src',src); main.onload=function(){ main.classList.remove('swap'); }; }, 180);
      });
    });
  });

  /* Zelfcheck */
  (function(){
  if(!document.getElementById('check')) return;
  var answers=[], cur=0, qs=document.querySelectorAll('.q'), total=qs.length;
  var prog=document.getElementById('progFill'), qnav=document.getElementById('qnav'), qBack=document.getElementById('qBack');
  function show(i){ cur=i; qs.forEach(function(q,j){ q.classList.toggle('on',j===i); }); prog.style.width=((i)/total*100)+'%'; qBack.style.visibility=i>0?'visible':'hidden'; }
  qs.forEach(function(q,i){ q.querySelectorAll('.opt').forEach(function(o){ o.addEventListener('click',function(){
    q.querySelectorAll('.opt').forEach(function(x){x.classList.remove('sel');}); o.classList.add('sel'); answers[i]=o.dataset.v;
    setTimeout(function(){ if(i<total-1) show(i+1); else result(); }, 260);
  }); }); });
  qBack.addEventListener('click',function(){ if(cur>0) show(cur-1); });
  document.getElementById('rReset').addEventListener('click',function(){ answers=[]; document.querySelectorAll('.opt').forEach(function(x){x.classList.remove('sel');}); document.getElementById('res').classList.remove('on'); document.getElementById('book').classList.remove('on'); document.getElementById('done').classList.remove('on'); qnav.style.display='flex'; show(0); });

  /* ---- Afspraak plannen ---- */
  var BOOKING_URL=''; // Zet hier je Cal.com of Calendly link neer (bv. 'https://cal.com/rudolf/kennismaking'). Leeg = via mail.
  var book=document.getElementById('book'), res=document.getElementById('res');
  document.getElementById('rPlan').addEventListener('click',function(){ res.classList.remove('on'); book.classList.add('on'); book.scrollIntoView({behavior:reduce?'auto':'smooth',block:'start'}); setTimeout(function(){ document.getElementById('bName').focus(); },400); });
  document.getElementById('bBack').addEventListener('click',function(){ book.classList.remove('on'); res.classList.add('on'); });
  function chips(id,multi){ var box=document.getElementById(id); box.querySelectorAll('button').forEach(function(b){ b.addEventListener('click',function(){ if(multi){ b.classList.toggle('on'); } else { box.querySelectorAll('button').forEach(function(x){x.classList.remove('on');}); b.classList.add('on'); } }); }); return function(){ return Array.prototype.map.call(box.querySelectorAll('button.on'),function(b){return b.textContent;}).join(', '); }; }
  var gDays=chips('bDays',true), gPart=chips('bPart',true), gWhere=chips('bWhere',false);
  if(BOOKING_URL){ document.getElementById('bHint').textContent='Dit opent mijn agenda. Kies een moment dat jou past; je antwoorden gaan automatisch mee.'; }
  document.getElementById('bSend').addEventListener('click',function(ev){
    ev.preventDefault();
    var name=document.getElementById('bName').value.trim(), comp=document.getElementById('bComp').value.trim(), mail=document.getElementById('bMail').value.trim(), tel=document.getElementById('bTel').value.trim(), note=document.getElementById('bNote').value.trim();
    var ok=true; [['bName',name],['bMail',mail]].forEach(function(f){ var el=document.getElementById(f[0]).closest('.book-field'); var bad=!f[1] || (f[0]==='bMail' && mail.indexOf('@')<0); el.classList.toggle('err',bad); if(bad) ok=false; });
    if(!ok){ document.getElementById('bName').closest('.book-grid').scrollIntoView({behavior:'smooth',block:'center'}); return; }
    var c=window.__check||{summary:'',diag:'',pk:''};
    var pref='Dagen: '+(gDays()||'geen voorkeur')+'\nDagdeel: '+(gPart()||'geen voorkeur')+'\nWaar: '+(gWhere()||'online');
    if(BOOKING_URL){
      var u=BOOKING_URL+(BOOKING_URL.indexOf('?')>0?'&':'?')+'name='+encodeURIComponent(name)+'&email='+encodeURIComponent(mail)+'&notes='+encodeURIComponent('Bedrijf: '+comp+'\nTelefoon: '+tel+'\n\n'+c.summary+'\nPakket: '+c.pk+'\n\n'+pref+'\n\n'+note);
      window.open(u,'_blank'); return;
    }
    var btn=document.getElementById('bSend'), errEl=document.getElementById('bErr');
    btn.classList.add('busy'); btn.textContent='Versturen...'; errEl.hidden=true;
    var payload={name:name,email:mail,company:comp,phone:tel,note:note,days:gDays(),part:gPart(),where:gWhere(),pk:c.pk,diag:c.diag,summary:c.summary,website:document.getElementById('bWeb').value};
    function fallbackMail(){
      var body='Hoi Rudolf,\n\nIk wil graag een gesprek van 30 minuten plannen.\n\nWANNEER PAST HET MIJ\n'+pref+'\n\nMIJN GEGEVENS\nNaam: '+name+'\nBedrijf: '+comp+'\nE-mail: '+mail+'\nTelefoon: '+(tel||'-')+'\n\nUITKOMST VAN DE CHECK\n'+c.summary+'\nJouw inschatting: '+c.diag+'\nPakket: '+c.pk+(note?'\n\nVOORAF GOED OM TE WETEN\n'+note:'')+'\n\nGroeten,\n'+name;
      location.href='mailto:rudolf@brandvizer.nl?subject='+encodeURIComponent('Gesprek plannen: '+(comp||name))+'&body='+encodeURIComponent(body);
    }
    fetch('/api/aanvraag',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload)})
      .then(function(r){ return r.json().then(function(j){ return {ok:r.ok && j.ok, j:j}; }); })
      .then(function(o){
        if(o.ok){ book.classList.remove('on'); document.getElementById('done').classList.add('on'); document.getElementById('checkBody').scrollIntoView({behavior:reduce?'auto':'smooth',block:'nearest'}); }
        else { errEl.textContent='Versturen lukte niet ('+(o.j&&o.j.error?o.j.error:'onbekende fout')+'). Ik open je mailprogramma als alternatief.'; errEl.hidden=false; setTimeout(fallbackMail,1200); }
      })
      .catch(function(){ errEl.textContent='Geen verbinding met de server. Ik open je mailprogramma als alternatief.'; errEl.hidden=false; setTimeout(fallbackMail,1200); })
      .then(function(){ btn.classList.remove('busy'); btn.textContent='Verstuur en plan het gesprek'; });
  });
  show(0);

  var L={website:'een website',webapp:'een webshop of webapp',app:'een app',weetniet:'iets nieuws'};
  var PK={website:{n:'Compleet',p:'€4.950',t:'3 weken'},webapp:{n:'Webshop of portaal',p:'€8.500',t:'5 weken'},app:{n:'App',p:'€12.500',t:'6 tot 10 weken'}};
  var COMPACT={n:'Compact',p:'€2.950',t:'2 weken'};
  var FLOOR={website:2950,webapp:8500,app:12500}, BUD={b1:3000,b2:6000,b3:15000,b0:0};
  function result(){
    var a=answers, what=L[a[0]]||'iets nieuws', pk=PK[a[0]], bud=BUD[a[4]];
    var diag='', ex='', start=[], blocks=[];
    if(a[0]==='website' && bud>0 && bud<=3000) pk=COMPACT;
    if(a[0]==='weetniet'){
      diag='Je weet nog niet precies wat je wilt. <em>Begin dan met een gesprek, niet met een offerte.</em>';
      ex='In 30 minuten weet ik genoeg om je te zeggen wat je nodig hebt en wat het kost. Vaak is het minder dan mensen denken. Binnen twee werkdagen krijg je een voorstel met één vast bedrag en een opleverdatum.';
      start=['Gesprek van 30 minuten, gratis','Daarna een voorstel met een vast bedrag'];
    } else if(bud>0 && bud<FLOOR[a[0]]){
      diag='Je wilt '+what+'. <em>Eerlijk: dat past nog niet in dit budget.</em>';
      ex=pk.n+' kost '+pk.p+'. Voor minder een uitgeklede versie laten maken raad ik af, dan betaal je twee keer. Wat wel kan: we knippen het op en beginnen met het stuk dat het meeste oplevert.';
      start=['Gesprek van 30 minuten over wat er wel kan','Een eerste versie die al klanten oplevert'];
    } else {
      diag='Je wilt '+what+'. <em>Dat is het pakket '+pk.n+', '+pk.p+'.</em>';
      ex=pk.n+' kost '+pk.p+' exclusief btw en staat in '+pk.t+' live. Dat bedrag is het bedrag: wil je later meer pagina\'s of een tweede taal, dan kies je dat zelf uit de prijslijst.';
      start=['Gesprek van 30 minuten','Voorstel met vaste prijs binnen twee werkdagen','Pakket '+pk.n+', '+pk.p+', '+pk.t+' tot live'];
      if(a[0]!=='website') start.splice(2,0,'Kickstart van €950 vooraf, verrekend als je doorgaat');
      if(a[3]==='nu' && a[0]==='app') ex+=' Eén ding vooraf: een app in de stores krijgen kost minimaal zes weken. Sneller kan niet zonder in te leveren.';
      if(a[3]==='nu' && a[0]==='website') ex+=' Snel live? Als jij vlot reageert op wat ik voorleg, staat een website binnen twee tot drie weken.';
    }
    if(a[1]==='bureau') ex+=' Je huidige site neem ik over, inclusief domein en hosting. Je hoeft je oude bureau niets uit te leggen.';
    if(a[1]==='zelf') ex+=' Wat je zelf bouwde is niet weggegooid: het laat me precies zien wat jij belangrijk vindt.';
    if(a[2]==='aanvragen') blocks=['Aanvragen per week','Hoeveel bezoekers een aanvraag doen','Waar mensen afhaken'];
    else if(a[2]==='verkopen') blocks=['Bestellingen of boekingen per week','Hoeveel bezoekers afrekenen','Gemiddelde orderwaarde'];
    else if(a[2]==='handwerk') blocks=['Telefoontjes en mailtjes per week, voor en na','Hoeveel klanten het zelf regelen','Uren die jij bespaart'];
    else blocks=['Hoe lang mensen blijven','Hoeveel er terugkomen','Wat klanten zeggen als je het vraagt'];
    var lab={0:{website:'Website',webapp:'Webshop, boekingssysteem of portaal',app:'App',weetniet:'Weet ik nog niet'},1:{niets:'Nog niets',oud:'Verouderde site of app',zelf:'Zelfgebouwd',bureau:'Van een bureau, niet blij mee'},2:{aanvragen:'Meer aanvragen',verkopen:'Online verkopen of boeken',handwerk:'Minder handwerk',uitstraling:'Uitstraling die klopt'},3:{nu:'Zo snel mogelijk','3mnd':'Binnen drie maanden',jaar:'Dit jaar',geen:'Geen haast'},4:{b1:'Tot €3.000',b2:'€3.000 tot €6.000',b3:'€6.000 tot €15.000',b0:'Geen idee'}};
    window.__check={summary:'- Wat ik wil: '+lab[0][a[0]]+'\n- Wat ik nu heb: '+lab[1][a[1]]+'\n- Wat het moet opleveren: '+lab[2][a[2]]+'\n- Wanneer: '+lab[3][a[3]]+'\n- Budget: '+lab[4][a[4]], diag:diag.replace(/<[^>]+>/g,''), pk:(a[0]==='weetniet'?'Nog onbekend':(pk?pk.n+' ('+pk.p+')':''))};
    document.getElementById('rDiag').innerHTML=diag;
    document.getElementById('rEx').textContent=ex;
    function vul(id,items){ var ul=document.getElementById(id); ul.innerHTML=''; items.forEach(function(t){ var li=document.createElement('li'); li.textContent=t; ul.appendChild(li); }); }
    vul('rStart',start); vul('rBlocks',blocks);
    qs.forEach(function(q){q.classList.remove('on');}); qnav.style.display='none'; prog.style.width='100%';
    document.getElementById('res').classList.add('on');
    document.getElementById('checkBody').scrollIntoView({behavior:reduce?'auto':'smooth',block:'nearest'});
  }
  })();
})();
