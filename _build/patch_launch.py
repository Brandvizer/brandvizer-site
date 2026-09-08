import os, re, glob
R=os.path.expanduser('~/mnt/brandvizer-site')
BASE='https://www.brandvizer.nl'

HEADBITS = '''<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#F3F6F8">
'''
OG = '''<meta property="og:image" content="{base}/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:site_name" content="Brandvizer">
<meta property="og:locale" content="nl_NL">
<meta name="twitter:card" content="summary_large_image">
'''.format(base=BASE)
ANALYTICS = '<script defer src="/_vercel/insights/script.js"></script>\n'

def head_inject(h, canonical=None):
    if 'favicon.svg' not in h:
        h = h.replace('<link rel="preconnect" href="https://fonts.googleapis.com">', HEADBITS + '<link rel="preconnect" href="https://fonts.googleapis.com">', 1)
    if 'og:image' not in h:
        # na de laatste bestaande og-tag, anders voor </head>
        m = list(re.finditer(r'<meta property="og:[^>]*>\n', h))
        if m:
            i = m[-1].end(); h = h[:i] + OG + h[i:]
        else:
            h = h.replace('</head>', OG + '</head>', 1)
    if '_vercel/insights' not in h:
        h = h.replace('</head>', ANALYTICS + '</head>', 1)
    if canonical and 'rel="canonical"' not in h:
        h = h.replace('</head>', '<link rel="canonical" href="%s">\n</head>' % canonical, 1)
    return h

# 1. Homepage
p = R + '/index.html'; h = open(p).read()
h = head_inject(h, BASE + '/')
h = h.replace('<a href="/kennis">Kennis</a><a href="#over">Over</a><a href="mailto:rudolf@brandvizer.nl">Mail</a>',
              '<a href="/kennis">Kennis</a><a href="#over">Over</a><a href="/privacy">Privacy</a><a href="mailto:rudolf@brandvizer.nl">Mail</a>', 1)
open(p, 'w').write(h)

# 2. Kennispagina's
for f in glob.glob(R + '/kennis/*.html'):
    h = open(f).read()
    h = head_inject(h)
    h = h.replace('<a href="/kennis">Kennis</a><a href="mailto:rudolf@brandvizer.nl">Mail</a>',
                  '<a href="/kennis">Kennis</a><a href="/privacy">Privacy</a><a href="mailto:rudolf@brandvizer.nl">Mail</a>', 1)
    open(f, 'w').write(h)

# 3. Generator gelijk houden
g = R + '/_build/gen_kennis.py'; s = open(g).read()
if 'favicon.svg' not in s:
    s = s.replace('<link rel="preconnect" href="https://fonts.googleapis.com">', HEADBITS + '<link rel="preconnect" href="https://fonts.googleapis.com">', 1)
    s = s.replace('<meta property="og:url" content="{url}">', '<meta property="og:url" content="{url}">\n' + OG.rstrip('\n'), 1)
    s = s.replace('<script type="application/ld+json">{ld}</script>', ANALYTICS.rstrip('\n') + '\n<script type="application/ld+json">{ld}</script>', 1)
    s = s.replace('<a href="/kennis">Kennis</a><a href="mailto:rudolf@brandvizer.nl">Mail</a>',
                  '<a href="/kennis">Kennis</a><a href="/privacy">Privacy</a><a href="mailto:rudolf@brandvizer.nl">Mail</a>', 1)
    open(g, 'w').write(s)

# 4. sitemap: privacy erbij (404 en assets niet)
sm = R + '/sitemap.xml'; x = open(sm).read()
if '/privacy' not in x:
    x = x.replace('</urlset>', '  <url><loc>%s/privacy</loc><lastmod>2026-09-08</lastmod><changefreq>yearly</changefreq><priority>0.2</priority></url>\n</urlset>' % BASE)
    open(sm, 'w').write(x)

print('klaar')
