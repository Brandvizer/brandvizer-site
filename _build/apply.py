import os
home=os.path.expanduser('~')
p=home+'/mnt/brandvizer-site/index.html'
h=open(p).read()
sec=open(home+'/mnt/brandvizer-site/_build/cases-section.html').read()
css=open(home+'/mnt/brandvizer-site/_build/cases.css').read()

s=h.index('<!-- CASES -->'); e=h.index('<!-- OVER -->')
h=h[:s]+sec+h[e:]
cs=h.index('  /* Cases */'); ce=h.index('  /* About */')
h=h[:cs]+css+'\n'+h[ce:]

# mobile css for cases
old_mob='''    .case.on{grid-template-columns:1fr;row-gap:26px;padding:28px 0 40px}
    .case-shot{grid-column:1;position:relative;top:auto;border-radius:0 24px 24px 0;margin-right:var(--pad)}
    .case>div:last-child{grid-column:1;padding:0 var(--pad)}'''
new_mob='''    .cs,.cs.flip{grid-template-columns:1fr;row-gap:26px;padding:28px 0 40px}
    .cs-media,.cs.flip .cs-media{grid-column:1;order:0;position:relative;top:auto}
    .cs-text,.cs.flip .cs-text{grid-column:1;padding:0 var(--pad)}
    .cs-main,.cs.flip .cs-main{border-radius:0 24px 24px 0;margin-right:var(--pad)}
    .cs.flip .cs-thumbs{padding-left:var(--pad);padding-right:0;justify-content:flex-start}
    .cs-grid{grid-template-columns:1fr}'''
assert h.count(old_mob)==1; h=h.replace(old_mob,new_mob)

# JS: replace old case tab/pin code with thumb switching
js_s=h.index('  /* Cases */\n  document.querySelectorAll(\'.case-tab\')')
js_e=h.index('  /* Zelfcheck */')
new_js='''  /* Cases: thumbs wisselen het hoofdbeeld */
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

'''
h=h[:js_s]+new_js+h[js_e:]
open(p,'w').write(h)
print('ok', len(h))
