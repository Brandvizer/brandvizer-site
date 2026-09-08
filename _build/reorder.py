import os, re
R = os.path.expanduser('~/mnt/brandvizer-site')
p = R + '/index.html'
h = open(p).read()

def cut(start, end):
    """knip het blok tussen twee markers uit h en geef het terug"""
    global h
    s = h.index(start); e = h.index(end)
    block = h[s:e]
    h = h[:s] + h[e:]
    return block

# ---------- 1. Case-CSS naar een eigen bestand ----------
cs_start = h.index('  /* Cases */\n  .cs{')
cs_end = h.index('  /* Kennis */')
case_css = h[cs_start:cs_end].replace('  /* Cases */\n', '')
case_css = '\n'.join(l[2:] if l.startswith('  ') else l for l in case_css.split('\n'))
h = h[:cs_start] + h[cs_end:]
open(R + '/assets/cases.css', 'w').write('/* Brandvizer: cases, gedeeld door de homepage en /werk */\n' + case_css.strip() + '\n')
h = h.replace('<link rel="stylesheet" href="/assets/site.css">', '', 1)  # bestaat niet op index, no-op
h = h.replace('<style>', '<link rel="stylesheet" href="/assets/cases.css">\n<style>', 1)

# mobiele case-regels staan in de media queries van index: verplaats mee
mob = []
for pat in [
    r'    \.cs,\.cs\.flip\{[^}]*\}\n', r'    \.cs-thumbs button\{[^}]*\}\n',
    r'    \.cs-media,\.cs\.flip \.cs-media\{[^}]*\}\n', r'    \.cs-text,\.cs\.flip \.cs-text\{[^}]*\}\n',
    r'    \.cs-main,\.cs\.flip \.cs-main\{[^}]*\}\n', r'    \.cs\.flip \.cs-thumbs\{[^}]*\}\n',
    r'    \.cs-grid\{[^}]*\}\n']:
    for m in re.findall(pat, h):
        mob.append(m.strip()); h = h.replace(m, '')
if mob:
    open(R + '/assets/cases.css', 'a').write('\n@media(max-width:960px){\n  ' + '\n  '.join(mob) + '\n}\n')

# ---------- 2. Blokken uitknippen ----------
statement = cut('<!-- STATEMENT -->', '<!-- AANPAK -->')
aanpak    = cut('<!-- AANPAK -->', '<!-- PAKKETTEN -->')
pakketten = cut('<!-- PAKKETTEN -->', '<!-- CHECK -->')
check     = cut('<!-- CHECK -->', '<!-- CASES -->')
cases     = cut('<!-- CASES -->', '<!-- KENNIS -->')
kennis    = cut('<!-- KENNIS -->', '<!-- OVER -->')
over      = cut('<!-- OVER -->', '<!-- CONTACT -->')
contact   = cut('<!-- CONTACT -->', '</main>')

# ---------- 3. Statement opsplitsen ----------
cols_start = statement.index('  <div class="cols">')
why_start  = statement.index('  <div class="why-me">')
why_end    = statement.rindex('</section>')
cols_html  = statement[cols_start:why_start].rstrip()
why_html   = statement[why_start:why_end].rstrip()
# zes redenen compacter maken
why_html = why_html.replace('<div class="why-head rv"><div class="eyebrow">Wat ik anders doe</div><h3>Zes redenen om het met mij te doen.</h3></div>',
                            '<div class="why-head rv"><div class="eyebrow">Wat je van mij krijgt</div><h3>Zes redenen om het met mij te doen.</h3></div>')

# ---------- 4. Sectie 2: probleem en opties samen ----------
pijn = cut('<!-- PIJN -->', '</main>')
pijn = pijn.rstrip()
pijn_end = pijn.rindex('</section>')
merged = pijn[:pijn_end] + '''
  <div class="opties">
    <h3 class="rv">En je hebt drie opties. <span class="dim">Geen van drie klopt helemaal.</span></h3>
''' + cols_html.replace('  <div class="cols">', '    <div class="cols">').replace('    <div class="col rv">', '      <div class="col rv">') + '''
    <p class="opties-out rv">Er is een vierde optie die de meeste ondernemers niet kennen: <b>één persoon die ontwerpt én bouwt.</b> Met de vragen van een bureau, het tempo van een webbouwer en het gereedschap van nu. Dat is wat ik doe.</p>
  </div>
''' + pijn[pijn_end:]

# ---------- 5. Cases inkorten: twee diepe naar /werk ----------
def take_article(src, marker):
    s = src.index(marker); e = src.index('</article>', s) + len('</article>') + 1
    return src[s:e], src[:s] + src[e:]

abn, cases = take_article(cases, '  <!-- ABN AMRO OPEN DOMEIN -->')
ict, cases = take_article(cases, '  <!-- ICT888 / BELASTINGDIENST -->')

cases = cases.replace('<div class="eyebrow rv">Drie cases, uitgelegd</div>', '<div class="eyebrow rv">Bewijs</div>')
cases = cases.replace('<p class="lead rv" style="margin-top:22px">Dit zijn grote organisaties, maar het recept is voor jouw bedrijf precies hetzelfde: eerst begrijpen wat klanten nodig hebben, dan bouwen. Bij elke case vertel ik wat er misging, wat ik deed en waarom dat werkte. Klik op de kleine beelden om meer te zien.</p>',
                      '<p class="lead rv" style="margin-top:22px">Dit zijn grote organisaties, maar het recept is voor jouw bedrijf hetzelfde: eerst begrijpen wat klanten nodig hebben, dan bouwen. Hieronder één project helemaal uitgelegd, daaronder vier kort. Klik op de kleine beelden om meer te zien.</p>')
cases = cases.replace('<h3 class="rv">Vier keer hetzelfde recept: eerst begrijpen, dan bouwen.</h3>',
                      '<h3 class="rv">Vier keer hetzelfde recept: eerst begrijpen, dan bouwen.</h3>')
cases = cases.replace('</section>', '''  <div class="wrap"><p class="rv" style="margin-top:34px"><a class="btn ghost" href="/werk">Bekijk alle projecten</a></p></div>
</section>''')

# ---------- 6. Zes redenen in Aanpak ----------
aanpak = aanpak.replace('  <div class="steps3">', why_html + '\n  <div class="steps3">', 1)
aanpak = aanpak.replace('<h2 class="h2 rv">Eerst begrijpen. Dan bouwen. <span class="mark" data-mark>Dan meten.</span></h2>',
                        '<h2 class="h2 rv">Eerst begrijpen. Dan bouwen. <span class="mark" data-mark>Dan meten.</span></h2>')
# stappen-kop erboven zodat de sectie leest
aanpak = aanpak.replace('  <div class="steps3">', '  <h3 class="rv steps-head">En zo gaat het in de praktijk.</h3>\n  <div class="steps3">', 1)

# ---------- 7. Nieuwe volgorde plaatsen ----------
anchor = '<!-- KENNIS-PLACEHOLDER -->'
h = h.replace('</main>', anchor + '\n</main>', 1)
h = h.replace(anchor, merged + '\n' + cases + '\n' + over + '\n' + aanpak + '\n' + pakketten + '\n' + check + '\n' + kennis + '\n' + contact + '\n')

# ---------- 8. Navigatie in dezelfde volgorde ----------
for old, new in [
 ('<a href="#pijn">Herken je dit?</a><a href="#aanpak">Aanpak</a><a href="#pakketten">Pakketten</a><a href="#cases">Cases</a><a href="/kennis">Kennis</a><a href="#over">Over Rudolf</a><a href="#contact">Contact</a>',
  '<a href="#pijn">Herken je dit?</a><a href="#cases">Werk</a><a href="#over">Over Rudolf</a><a href="#aanpak">Aanpak</a><a href="#pakketten">Pakketten</a><a href="/kennis">Kennis</a><a href="#contact">Contact</a>'),
 ('<a href="#pijn">Herken je dit?</a><a href="#aanpak">Aanpak</a><a href="#pakketten">Pakketten</a><a href="#check" class="accent">Welk pakket past?</a><a href="#cases">Cases</a><a href="/kennis">Kennis</a><a href="#over">Over Rudolf</a><a href="#contact">Contact</a>',
  '<a href="#pijn">Herken je dit?</a><a href="#cases">Werk</a><a href="#over">Over Rudolf</a><a href="#aanpak">Aanpak</a><a href="#pakketten">Pakketten</a><a href="#check" class="accent">Welk pakket past?</a><a href="/kennis">Kennis</a><a href="#contact">Contact</a>')]:
    assert h.count(old) == 1, old[:60]
    h = h.replace(old, new)

# ---------- 9. CSS voor de nieuwe onderdelen ----------
h = h.replace('  /* Why me */', '''  /* Opties in de pijnsectie */
  .opties{margin-top:clamp(50px,7vw,86px);padding-top:clamp(34px,4vw,52px);border-top:1px solid var(--line)}
  .opties h3{font-size:var(--h3);max-width:24ch}
  .opties h3 .dim{color:var(--mute)}
  .opties .cols{margin-top:34px}
  .opties-out{margin-top:30px;font-size:var(--lead);color:var(--ink2);max-width:64ch}
  .opties-out b{color:var(--ink);font-weight:600}
  .steps-head{font-size:var(--h4);margin-top:clamp(44px,6vw,72px);color:var(--mute);font-weight:500}
  /* Why me */''', 1)
h = h.replace('  .why-me{margin-top:clamp(60px,8vw,110px)}', '  .why-me{margin-top:clamp(40px,5vw,64px)}', 1)

open(p, 'w').write(h)
print('index klaar')

# ---------- 10. /werk pagina ----------
head = '''<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Werk | Brandvizer</title>
<meta name="description" content="Projecten van Rudolf van der Velde voor de Belastingdienst, ABN AMRO, de SVB, Easyjobs, Actify en Grip. Per project: wat er misging, wat ik deed en waarom het werkte.">
<link rel="canonical" href="https://www.brandvizer.nl/werk">
<meta property="og:title" content="Werk | Brandvizer">
<meta property="og:description" content="Zeven projecten, uitgelegd: wat er misging, wat ik deed en waarom het werkte.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.brandvizer.nl/werk">
<meta property="og:image" content="https://www.brandvizer.nl/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:site_name" content="Brandvizer">
<meta property="og:locale" content="nl_NL">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#F3F6F8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,500;12..96,600;12..96,800&family=Instrument+Sans:ital,wght@0,400;0,500;0,600;1,400&family=Caveat:wght@500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
<link rel="stylesheet" href="/assets/cases.css">
<script defer src="/_vercel/insights/script.js"></script>
</head>
<body>
<header class="nav">
  <a class="brand" href="/"><i></i>Brandvizer</a>
  <div class="nav-right">
    <nav class="nav-links" aria-label="Hoofdmenu">
      <a href="/#pijn">Herken je dit?</a><a href="/werk" class="on">Werk</a><a href="/#over">Over Rudolf</a><a href="/#aanpak">Aanpak</a><a href="/#pakketten">Pakketten</a><a href="/kennis">Kennis</a><a href="/#contact">Contact</a>
    </nav>
    <a class="btn sm pink" href="/#check">Welk pakket past?</a>
  </div>
</header>
<main>
<section class="wrap art-head">
  <div class="eyebrow">Werk</div>
  <h1>Wat er misging, wat ik deed, waarom het werkte.</h1>
  <p class="lead">Grote organisaties, maar het recept is voor jouw bedrijf hetzelfde: eerst begrijpen wat klanten nodig hebben, dan bouwen. Hieronder de projecten helemaal uitgelegd.</p>
</section>
'''
foot = '''<section class="wrap"><div class="art-cta">
  <div><h2>Hetzelfde recept, <em>voor jouw bedrijf.</em></h2><p class="lead">Doe de check van vijf vragen of plan direct een gesprek van 30 minuten. Je gaat sowieso weg met een eerlijk advies.</p></div>
  <div class="acts"><a class="btn pink" href="/#check">Welk pakket past bij mij?</a><a class="btn ghost" href="/#contact">Plan een gesprek</a></div>
</div></section>
</main>
<footer class="wrap">
  <div class="row">
    <span>&copy; 2026 Brandvizer &middot; Rudolf van der Velde &middot; Vaassen</span>
    <span><a href="/#aanpak">Aanpak</a><a href="/#pakketten">Pakketten</a><a href="/kennis">Kennis</a><a href="/privacy">Privacy</a><a href="mailto:rudolf@brandvizer.nl">Mail</a></span>
  </div>
</footer>
<script>
document.querySelectorAll('.cs-media, .csm-media').forEach(function(m){
  var main=m.querySelector('.cs-main img, .csm-main');
  m.querySelectorAll('button').forEach(function(b){
    b.addEventListener('click',function(){
      var src=b.querySelector('img').getAttribute('src'); if(main.getAttribute('src')===src) return;
      m.querySelectorAll('button').forEach(function(x){x.classList.remove('on');}); b.classList.add('on');
      main.style.opacity=0; setTimeout(function(){ main.setAttribute('src',src); main.onload=function(){ main.style.opacity=1; }; }, 160);
    });
  });
});
</script>
</body>
</html>
'''
# beeldpaden absoluut maken en reveal-klassen eruit
def fix(a):
    return a.replace('src="assets/', 'src="/assets/').replace(' rv"', '"')

os.makedirs(R + '/werk', exist_ok=True)
open(R + '/werk/index.html', 'w').write(head + fix(abn) + fix(ict) + foot)
print('werk klaar')

# sitemap
sm = R + '/sitemap.xml'; x = open(sm).read()
if '/werk' not in x:
    x = x.replace('  <url><loc>https://www.brandvizer.nl/kennis</loc>',
                  '  <url><loc>https://www.brandvizer.nl/werk</loc><lastmod>2026-09-08</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>\n  <url><loc>https://www.brandvizer.nl/kennis</loc>')
    open(sm, 'w').write(x)
print('sitemap klaar')
