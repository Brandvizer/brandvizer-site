import os
p=os.path.expanduser('~/mnt/brandvizer-site/index.html')
h=open(p).read()
def rep(a,b,n=1):
    global h; c=h.count(a); assert c==n,(a[:70],c); h=h.replace(a,b)

# honeypot + succes-state in HTML
rep('''          <div class="book-field full"><label for="bNote">Iets wat ik vooraf moet weten?''',
'''          <div class="book-field hp" aria-hidden="true"><label for="bWeb">Website</label><input id="bWeb" type="text" tabindex="-1" autocomplete="off"></div>
          <div class="book-field full"><label for="bNote">Iets wat ik vooraf moet weten?''')
rep('''        <p class="note-p" id="bHint">Dit opent een mail aan mij met alles al ingevuld: je antwoorden, je voorkeur en je gegevens. Je hoeft alleen op verzenden te drukken. Ik reageer binnen één werkdag met concrete momenten.</p>''',
'''        <p class="note-p" id="bHint">Je krijgt direct een bevestiging per mail. Ik reageer binnen één werkdag met twee of drie concrete momenten. Je gegevens gebruik ik alleen om contact op te nemen.</p>
        <p class="note-p err-p" id="bErr" hidden></p>
      </div>

      <div class="done" id="done">
        <div class="done-mark">✓</div>
        <h3>Gelukt. Je aanvraag is binnen.</h3>
        <p class="ex" id="doneTxt">Ik heb je een bevestiging gemaild. Binnen één werkdag krijg je van mij twee of drie momenten voor een gesprek van 30 minuten.</p>
        <p class="ex" style="margin-top:10px">Kun je niet wachten? Bel me gewoon: <a href="tel:+31643426082" style="color:var(--note)">06 43 42 60 82</a>.</p>''')

# CSS
rep('  /* Cases */\n  .cs{','''  .book-field.hp{position:absolute;left:-9999px;top:auto;width:1px;height:1px;overflow:hidden}
  .err-p{color:var(--pink)!important}
  .btn.busy{opacity:.6;pointer-events:none}
  .done{display:none;text-align:center;padding:20px 0}
  .done.on{display:block;animation:fade .5s var(--ease)}
  .done-mark{width:64px;height:64px;border-radius:50%;background:var(--green);color:#fff;font-size:30px;font-weight:800;display:flex;align-items:center;justify-content:center;margin:0 auto 18px}
  .done h3{color:#fff}
  .done .ex{max-width:48ch;margin-left:auto;margin-right:auto}
  /* Cases */
  .cs{''')

# JS: verzenden via /api/aanvraag, terugval op mailto
old_s=h.index("    var c=window.__check||{summary:'',diag:'',pk:''};")
old_e=h.index("    location.href='mailto:rudolf@brandvizer.nl?subject='+encodeURIComponent('Gesprek plannen: '+(comp||name))+'&body='+encodeURIComponent(body);\n  });")
old_e_full=old_e+len("    location.href='mailto:rudolf@brandvizer.nl?subject='+encodeURIComponent('Gesprek plannen: '+(comp||name))+'&body='+encodeURIComponent(body);\n  });")
new='''    var c=window.__check||{summary:'',diag:'',pk:''};
    var pref='Dagen: '+(gDays()||'geen voorkeur')+'\\nDagdeel: '+(gPart()||'geen voorkeur')+'\\nWaar: '+(gWhere()||'online');
    if(BOOKING_URL){
      var u=BOOKING_URL+(BOOKING_URL.indexOf('?')>0?'&':'?')+'name='+encodeURIComponent(name)+'&email='+encodeURIComponent(mail)+'&notes='+encodeURIComponent('Bedrijf: '+comp+'\\nTelefoon: '+tel+'\\n\\n'+c.summary+'\\nPakket: '+c.pk+'\\n\\n'+pref+'\\n\\n'+note);
      window.open(u,'_blank'); return;
    }
    var btn=document.getElementById('bSend'), errEl=document.getElementById('bErr');
    btn.classList.add('busy'); btn.textContent='Versturen...'; errEl.hidden=true;
    var payload={name:name,email:mail,company:comp,phone:tel,note:note,days:gDays(),part:gPart(),where:gWhere(),pk:c.pk,diag:c.diag,summary:c.summary,website:document.getElementById('bWeb').value};
    function fallbackMail(){
      var body='Hoi Rudolf,\\n\\nIk wil graag een gesprek van 30 minuten plannen.\\n\\nWANNEER PAST HET MIJ\\n'+pref+'\\n\\nMIJN GEGEVENS\\nNaam: '+name+'\\nBedrijf: '+comp+'\\nE-mail: '+mail+'\\nTelefoon: '+(tel||'-')+'\\n\\nUITKOMST VAN DE CHECK\\n'+c.summary+'\\nJouw inschatting: '+c.diag+'\\nPakket: '+c.pk+(note?'\\n\\nVOORAF GOED OM TE WETEN\\n'+note:'')+'\\n\\nGroeten,\\n'+name;
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
  });'''
h=h[:old_s]+new+h[old_e_full:]
# reset ook done-state
rep("document.getElementById('res').classList.remove('on'); document.getElementById('book').classList.remove('on'); qnav.style.display='flex'; show(0); });",
    "document.getElementById('res').classList.remove('on'); document.getElementById('book').classList.remove('on'); document.getElementById('done').classList.remove('on'); qnav.style.display='flex'; show(0); });")
open(p,'w').write(h); print('ok')
