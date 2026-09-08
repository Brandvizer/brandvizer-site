import os, re, glob
R = os.path.expanduser('~/mnt/brandvizer-site')

MARK = '@media (prefers-color-scheme: dark){'

def split_rules(inner):
    out = []
    for part in inner.split('}'):
        part = part.strip()
        if not part:
            continue
        sel, body = part.split('{', 1)
        out.append((sel.strip(), body.strip()))
    return out

def restructure(css, indent='  '):
    """maak van het dark-blok drie varianten: systeem, handmatig donker, handmatig licht wint"""
    if 'data-theme="dark"' in css:
        return css
    i = css.index(MARK)
    depth = 0
    for j in range(i + len(MARK) - 1, len(css)):
        if css[j] == '{': depth += 1
        elif css[j] == '}':
            depth -= 1
            if depth == 0:
                end = j
                break
    inner = css[i + len(MARK):end]
    rules = split_rules(inner)

    def block(prefix):
        lines = []
        for sel, body in rules:
            s = prefix if sel == ':root' else prefix + ' ' + sel
            lines.append('%s%s{%s}' % (indent, s, body))
        return '\n'.join(lines)

    auto = '%s@media (prefers-color-scheme: dark){\n%s\n%s}' % (indent, block(':root:not([data-theme="light"])'), indent)
    manual = block(':root[data-theme="dark"]')
    return css[:i - len(indent) if css[i-len(indent):i] == indent else i] + auto + '\n' + manual + '\n' + css[end+1:]

HEAD_SNIPPET = '<script>(function(){try{var t=localStorage.getItem("thema");if(t)document.documentElement.dataset.theme=t;}catch(e){}})();</script>\n'
THEME_JS = '<script defer src="/assets/theme.js"></script>\n'
BTN = ('<button class="theme-btn" data-theme-toggle type="button" aria-label="Wissel tussen licht en donker" title="Licht of donker">'
       '<svg class="ico sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4.2"/><path d="M12 2v2M12 20v2M4.2 4.2l1.4 1.4M18.4 18.4l1.4 1.4M2 12h2M20 12h2M4.2 19.8l1.4-1.4M18.4 5.6l1.4-1.4"/></svg>'
       '<svg class="ico moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 14.5A8.2 8.2 0 0 1 9.5 4a8.4 8.4 0 1 0 10.5 10.5z"/></svg>'
       '</button>')

BTN_CSS = '''  .theme-btn{display:inline-flex;align-items:center;justify-content:center;width:40px;height:40px;flex-shrink:0;border-radius:50%;border:1.5px solid var(--line);background:transparent;color:var(--ink2);cursor:pointer;transition:color .2s,border-color .2s,background .2s}
  .theme-btn:hover{color:var(--ink);border-color:var(--ink)}
  .theme-btn .ico{width:19px;height:19px}
  .theme-btn .sun{display:none}
  .theme-btn .moon{display:block}
  @media (prefers-color-scheme: dark){
    :root:not([data-theme="light"]) .theme-btn .sun{display:block}
    :root:not([data-theme="light"]) .theme-btn .moon{display:none}
  }
  :root[data-theme="dark"] .theme-btn .sun{display:block}
  :root[data-theme="dark"] .theme-btn .moon{display:none}
'''

# ---------------- index.html ----------------
p = R + '/index.html'; h = open(p).read()
s = h.index('<style>') + len('<style>'); e = h.index('</style>')
css = restructure(h[s:e])
if '.theme-btn{' not in css:
    css = css.replace('  /* Nav */', BTN_CSS + '  /* Nav */', 1) if '  /* Nav */' in css else css.rstrip() + '\n' + BTN_CSS
h = h[:s] + css + h[e:]
if 'localStorage.getItem("thema")' not in h:
    h = h.replace('<meta name="color-scheme"', HEAD_SNIPPET + '<meta name="color-scheme"', 1)
if 'assets/theme.js' not in h:
    h = h.replace('</head>', THEME_JS + '</head>', 1)
if 'data-theme-toggle' not in h:
    h = h.replace('<a class="btn sm pink" href="#check">Welk pakket past?</a>', BTN + '\n    <a class="btn sm pink" href="#check">Welk pakket past?</a>', 1)
open(p, 'w').write(h)
print('index klaar')

# ---------------- site.css ----------------
p = R + '/assets/site.css'; c = open(p).read()
c = restructure(c, indent='')
if '.theme-btn{' not in c:
    c += '\n' + '\n'.join(l[2:] if l.startswith('  ') and not l.strip().startswith(':root') else l for l in BTN_CSS.strip().split('\n')) + '\n'
open(p, 'w').write(c)
print('site.css klaar')

# ---------------- theme.js ----------------
open(R + '/assets/theme.js', 'w').write('''/* Brandvizer: licht of donker. Standaard volgt de browser, keuze wordt onthouden. */
(function(){
  function current(){
    return document.documentElement.dataset.theme ||
      (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  }
  function apply(t){
    document.documentElement.dataset.theme = t;
    try{ localStorage.setItem('thema', t); }catch(e){}
    document.querySelectorAll('[data-theme-toggle]').forEach(function(b){
      b.setAttribute('aria-label', t === 'dark' ? 'Zet de site in de lichte stand' : 'Zet de site in de donkere stand');
    });
  }
  document.addEventListener('click', function(e){
    var b = e.target.closest && e.target.closest('[data-theme-toggle]');
    if(!b) return;
    apply(current() === 'dark' ? 'light' : 'dark');
  });
  apply(current());
})();
''')
print('theme.js klaar')

# ---------------- overige pagina's ----------------
for f in glob.glob(R + '/kennis/*.html') + [R + '/privacy.html', R + '/404.html', R + '/werk/index.html']:
    x = open(f).read()
    if 'localStorage.getItem("thema")' not in x:
        x = x.replace('<meta name="color-scheme"', HEAD_SNIPPET + '<meta name="color-scheme"', 1)
    if 'assets/theme.js' not in x:
        x = x.replace('</head>', THEME_JS + '</head>', 1)
    if 'data-theme-toggle' not in x:
        x = re.sub(r'(<a class="btn sm pink" href="/#check">Welk pakket past\?</a>)', BTN + r'\n    \1', x, count=1)
    open(f, 'w').write(x)

g = R + '/_build/gen_kennis.py'; s2 = open(g).read()
if 'data-theme-toggle' not in s2:
    s2 = s2.replace('<meta name="color-scheme"', HEAD_SNIPPET + '<meta name="color-scheme"', 1)
    s2 = s2.replace('<script type="application/ld+json">{ld}</script>', THEME_JS.rstrip('\n') + '\n<script type="application/ld+json">{ld}</script>', 1)
    s2 = s2.replace('<a class="btn sm pink" href="/#check">Welk pakket past?</a>', BTN + '\n    <a class="btn sm pink" href="/#check">Welk pakket past?</a>', 1)
    open(g, 'w').write(s2)
print('overige klaar')
