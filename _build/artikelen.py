"""Bouwt de kennisartikelen uit één sjabloon, met Article, FAQPage en BreadcrumbList schema.
Draaien vanuit de root: python3 _build/artikelen.py"""
import json, re, html

BASE = "https://www.brandvizer.nl"
TPL = open("kennis/wat-kost-een-website-laten-maken.html", encoding="utf-8").read()
HEAD_END = TPL.index("<script type=\"application/ld+json\">")
NAV = TPL[TPL.index("<body>"):TPL.index("<main>")]
FOOT = TPL[TPL.index("<section class=\"wrap\"><div class=\"art-cta\">"):]

ALL = {
 "wat-kost-een-website-laten-maken": ("Prijzen", "Wat kost een website laten maken in 2026?"),
 "bureau-freelancer-of-zelf-met-ai": ("Kiezen", "Bureau, webbouwer of zelf met AI: wat past bij jouw bedrijf?"),
 "waarom-je-website-geen-klanten-oplevert": ("Verbeteren", "Waarom je nieuwe website geen klanten oplevert (en drie dingen die je morgen kunt fixen)"),
 "wat-kost-een-webshop-laten-maken": ("Prijzen", "Wat kost een webshop laten maken in 2026?"),
 "wat-kost-een-app-laten-maken": ("Prijzen", "Wat kost een app laten maken in 2026?"),
 "website-vakantiewoning-directe-boekingen": ("Branche", "Een eigen website voor je vakantiewoning: meer directe boekingen, minder commissie"),
 "website-laten-maken-apeldoorn-zwolle-deventer": ("Kiezen", "Website laten maken in Apeldoorn, Zwolle of Deventer: lokaal of online?"),
}

def words(h): return len(re.sub(r"<[^>]+>", " ", h).split())

def build(a):
    slug = a["slug"]; url = f"{BASE}/kennis/{slug}"
    faq_html = "".join(f"<h3>{q}</h3><p>{ans}</p>" for q, ans in a["faq"])
    body = a["body"] + f"\n<h2>Veelgestelde vragen</h2>\n<div class=\"faq\">{faq_html}</div>\n"
    mins = max(3, round(words(body) / 200))
    ld = [
      {"@context": "https://schema.org", "@type": "Article", "headline": a["title"], "description": a["desc"],
       "datePublished": a["date"], "dateModified": a["date"], "inLanguage": "nl",
       "image": f"{BASE}/og.png",
       "author": {"@type": "Person", "name": "Rudolf van der Velde", "url": f"{BASE}/#over"},
       "publisher": {"@type": "Organization", "name": "Brandvizer", "url": BASE, "logo": {"@type": "ImageObject", "url": f"{BASE}/apple-touch-icon.png"}},
       "mainEntityOfPage": url},
      {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", ans)}} for q, ans in a["faq"]]},
      {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Kennis", "item": BASE + "/kennis"},
        {"@type": "ListItem", "position": 3, "name": a["title"], "item": url}]},
    ]
    head = TPL[:HEAD_END]
    head = re.sub(r"<title>.*?</title>", f"<title>{a['seo_title']}</title>", head)
    for prop, val in (("description", a["desc"]),):
        head = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{val}">', head)
    head = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{url}">', head)
    head = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{a["title"]}">', head)
    head = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{a["desc"]}">', head)
    head = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{url}">', head)
    scripts = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in ld)
    rest = TPL[HEAD_END:TPL.index("</head>")]
    rest = re.sub(r'<script type="application/ld\+json">.*?</script>\n?', "", rest, flags=re.S)
    also = "".join(f'<a href="/kennis/{s}">{ALL[s][1]}</a>' for s in a["also"])
    main = f'''<main>
<nav class="wrap crumbs" aria-label="Kruimelpad"><a href="/">Home</a><span>/</span><a href="/kennis">Kennis</a></nav>
<section class="wrap art-head">
  <div class="eyebrow">{a["cat"]}</div>
  <h1>{a["title"]}</h1>
  <p class="lead">{a["lead"]}</p>
  <div class="art-meta"><span>Rudolf van der Velde</span><span>{mins} minuten leestijd</span><span>{a["month"]}</span></div>
</section>
<section class="wrap art">
  <article class="art-body">
{body}</article>
  <aside class="aside">
  <div class="aside-card"><div class="k">Twee minuten</div><h4>Welk pakket past bij jouw bedrijf?</h4><p>Vijf vragen, dan weet je wat je nodig hebt en wat het ongeveer kost. Geen account, geen nieuwsbrief.</p><a class="btn" href="/prijzen#check">Doe de check</a></div>
  <div class="aside-me"><img src="/assets/img/rudolf-foto.jpg" alt="Rudolf van der Velde"><b>Rudolf van der Velde</b><span>Ontwerpt en bouwt websites en apps voor ondernemers. Vijftien jaar ervaring bij banken en overheid. Vaassen.</span></div>
  <div class="aside-list"><div class="k">Ook lezen</div>{also}</div>
</aside>
</section>
'''
    out = head + scripts + rest + "</head>\n" + NAV + main + FOOT
    open(f"kennis/{slug}.html", "w", encoding="utf-8").write(out)
    return slug, mins

if __name__ == "__main__":
    import importlib.util, sys
    spec = importlib.util.spec_from_file_location("teksten", "_build/teksten.py")
    t = importlib.util.module_from_spec(spec); spec.loader.exec_module(t)
    for a in t.ARTIKELEN:
        print(build(a))
