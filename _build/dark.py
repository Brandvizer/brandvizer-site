import os, re
R = os.path.expanduser('~/mnt/brandvizer-site')

DARK_TOKENS = '''
  @media (prefers-color-scheme: dark){
    :root{
      --paper:#0C1626; --paper2:#152238; --grid:rgba(255,255,255,.05);
      --ink:#EDF1F5; --ink2:#B4BECC; --mute:#8A94A6; --line:rgba(255,255,255,.14);
      --pink:#FF5B92; --pink-soft:#3A1526; --green:#3FBF9A; --green-soft:#14332B;
      --note:#FFD84D; --note-ink:#2A2000; --white:#132038;
      --inv-bg:#1B2A45; --inv-ink:#EDF1F5;
    }
    .mock,.pack,.pain,.why,.kcard,.aside-me,.aside-list,.csm,.contact,.cs{background:var(--white)}
    .aside-card,.check,.pack.feat,.chip small{background:var(--inv-bg)}
    img{filter:brightness(.94)}
  }
'''

def patch_css(css):
    # inverted blokken: van harde inkt naar een token dat in beide standen donker is
    css = css.replace('.pack.feat{background:var(--ink);color:#fff;border-color:var(--ink)}',
                      '.pack.feat{background:var(--inv-bg);color:var(--inv-ink);border-color:var(--inv-bg)}')
    css = css.replace('.check{background:var(--ink);color:#fff;',
                      '.check{background:var(--inv-bg);color:var(--inv-ink);')
    css = css.replace('.chip small{display:none;position:absolute;left:0;top:calc(100% + 8px);z-index:5;width:260px;background:var(--ink);color:#fff;',
                      '.chip small{display:none;position:absolute;left:0;top:calc(100% + 8px);z-index:5;width:260px;background:var(--inv-bg);color:var(--inv-ink);')
    css = css.replace('.m-btn{background:var(--ink);color:#fff;', '.m-btn{background:var(--inv-bg);color:var(--inv-ink);')
    css = css.replace('.m-field{border:1.5px solid var(--line);border-radius:10px;padding:12px 14px;font-size:14px;color:var(--mute);margin-bottom:10px;position:relative;background:#fff}',
                      '.m-field{border:1.5px solid var(--line);border-radius:10px;padding:12px 14px;font-size:14px;color:var(--mute);margin-bottom:10px;position:relative;background:var(--white)}')
    css = css.replace('.aside-card{background:var(--ink);color:#fff;', '.aside-card{background:var(--inv-bg);color:var(--inv-ink);')
    css = css.replace('.aside-card h4{color:#fff;', '.aside-card h4{color:var(--inv-ink);')
    css = css.replace('.check .h2{color:#fff}', '.check .h2{color:var(--inv-ink)}')
    # resterende harde #fff binnen de donkere blokken
    for sel in ['.q h3', '.res .diag', '.book h3', '.opt', '.res .btn.ghost,.book .btn.ghost', '.pack.feat .meta span', '.pack.feat .btn.ghost']:
        pat = re.compile(re.escape(sel) + r'\{([^}]*)\}')
        m = pat.search(css)
        if m and '#fff' in m.group(1):
            css = css[:m.start(1)] + m.group(1).replace('color:#fff', 'color:var(--inv-ink)') + css[m.end(1):]
    return css

# ---------- index.html ----------
p = R + '/index.html'; h = open(p).read()
s = h.index('<style>') + len('<style>'); e = h.index('</style>')
css = patch_css(h[s:e])
if 'prefers-color-scheme: dark' not in css:
    css = css.rstrip() + '\n' + DARK_TOKENS
h = h[:s] + css + h[e:]
h = h.replace('<meta name="theme-color" content="#F3F6F8">',
              '<meta name="theme-color" content="#F3F6F8" media="(prefers-color-scheme: light)">\n<meta name="theme-color" content="#0C1626" media="(prefers-color-scheme: dark)">')
if 'color-scheme' not in h:
    h = h.replace('<meta name="viewport"', '<meta name="color-scheme" content="light dark">\n<meta name="viewport"', 1)
open(p, 'w').write(h)
print('index klaar')

# ---------- site.css ----------
p = R + '/assets/site.css'; c = open(p).read()
c = patch_css(c)
if 'prefers-color-scheme: dark' not in c:
    c = c.rstrip() + '\n' + '\n'.join(l[2:] if l.startswith('  ') else l for l in DARK_TOKENS.strip().split('\n')) + '\n'
open(p, 'w').write(c)
print('site.css klaar')

# ---------- overige pagina's: meta's gelijk trekken ----------
import glob
for f in glob.glob(R + '/kennis/*.html') + [R + '/privacy.html', R + '/404.html', R + '/werk/index.html']:
    x = open(f).read()
    if 'color-scheme' not in x:
        x = x.replace('<meta name="viewport"', '<meta name="color-scheme" content="light dark">\n<meta name="viewport"', 1)
    x = x.replace('<meta name="theme-color" content="#F3F6F8">',
                  '<meta name="theme-color" content="#F3F6F8" media="(prefers-color-scheme: light)">\n<meta name="theme-color" content="#0C1626" media="(prefers-color-scheme: dark)">')
    open(f, 'w').write(x)

# generator gelijk houden
g = R + '/_build/gen_kennis.py'; s2 = open(g).read()
if 'color-scheme' not in s2:
    s2 = s2.replace('<meta name="viewport"', '<meta name="color-scheme" content="light dark">\n<meta name="viewport"', 1)
    s2 = s2.replace('<meta name="theme-color" content="#F3F6F8">',
                    '<meta name="theme-color" content="#F3F6F8" media="(prefers-color-scheme: light)">\n<meta name="theme-color" content="#0C1626" media="(prefers-color-scheme: dark)">')
    open(g, 'w').write(s2)
print('overige klaar')
