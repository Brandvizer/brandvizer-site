import os, datetime
ROOT=os.path.expanduser('~/mnt/brandvizer-site')
BASE='https://www.brandvizer.nl'
TODAY='2026-09-07'

HEAD='''<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Brandvizer</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="article">
<meta property="og:url" content="{url}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,500;12..96,600;12..96,800&family=Instrument+Sans:ital,wght@0,400;0,500;0,600;1,400&family=Caveat:wght@500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
<script type="application/ld+json">{ld}</script>
</head>
<body>
<header class="nav">
  <a class="brand" href="/"><i></i>Brandvizer</a>
  <div class="nav-right">
    <nav class="nav-links" aria-label="Hoofdmenu">
      <a href="/#aanpak">Aanpak</a><a href="/#pakketten">Pakketten</a><a href="/#cases">Cases</a><a href="/kennis" class="on">Kennis</a><a href="/#over">Over Rudolf</a><a href="/#contact">Contact</a>
    </nav>
    <a class="btn sm pink" href="/#check">Welk pakket past?</a>
  </div>
</header>
'''
FOOT='''<footer class="wrap">
  <div class="row">
    <span>© 2026 Brandvizer · Rudolf van der Velde · Vaassen · Websites en apps voor Apeldoorn, Zwolle, Deventer en de Veluwe</span>
    <span><a href="/#aanpak">Aanpak</a><a href="/#pakketten">Pakketten</a><a href="/kennis">Kennis</a><a href="mailto:rudolf@brandvizer.nl">Mail</a></span>
  </div>
</footer>
</body>
</html>
'''
ASIDE='''<aside class="aside">
  <div class="aside-card"><div class="k">Twee minuten</div><h4>Welk pakket past bij jouw bedrijf?</h4><p>Vijf vragen, dan weet je wat je nodig hebt en wat het ongeveer kost. Geen account, geen nieuwsbrief.</p><a class="btn" href="/#check">Doe de check</a></div>
  <div class="aside-me"><img src="/assets/img/rudolf-foto.jpg" alt="Rudolf van der Velde"><b>Rudolf van der Velde</b><span>Ontwerpt en bouwt websites en apps voor ondernemers. Vijftien jaar ervaring bij banken en overheid. Vaassen.</span></div>
  <div class="aside-list"><div class="k">Ook lezen</div>{links}</div>
</aside>'''
CTA='''<section class="wrap"><div class="art-cta">
  <div><h2>Weet je genoeg? <em>Dan is dit de volgende stap.</em></h2><p class="lead">Doe de check van vijf vragen of plan direct een gesprek van 30 minuten. Je gaat sowieso weg met een eerlijk advies, ook als dat is: doe het (nog) niet.</p></div>
  <div class="acts"><a class="btn pink" href="/#check">Welk pakket past bij mij?</a><a class="btn ghost" href="/#contact">Plan een gesprek</a></div>
</div></section>
'''

ARTICLES=[
{
 'slug':'wat-kost-een-website-laten-maken',
 'cat':'Prijzen',
 'title':'Wat kost een website laten maken in 2026?',
 'desc':'Eerlijke prijzen voor een website laten maken: wat een webbouwer, een bureau en zelf bouwen met AI kosten, waar het verschil in zit en wanneer je te veel betaalt.',
 'lead':'Drie offertes, van 1.500 tot 25.000 euro, en geen idee waarom. Dit is wat je betaalt, waarvoor, en hoe je de goede keuze maakt zonder websitebouwer te hoeven zijn.',
 'read':'6 minuten',
 'body':'''
<p>De vraag die ik het vaakst krijg van ondernemers is niet "kun je een website maken", maar "wat kost dat eigenlijk". Terecht. Het antwoord dat de meeste bureaus geven ("dat hangt ervan af") helpt je niets. Dus hier het echte antwoord, met bedragen.</p>

<h2>De korte versie</h2>
<table>
<tr><th>Wie bouwt</th><th>Wat je betaalt</th><th>Wat je krijgt</th></tr>
<tr><td>Zelf, met Wix, Squarespace of een AI-tool</td><td>0 tot 50 euro per maand</td><td>Een site die er redelijk uitziet en waar niemand over nagedacht heeft</td></tr>
<tr><td>Een webbouwer of freelancer</td><td>1.500 tot 5.000 euro</td><td>Een template met jouw logo en teksten, gebouwd zoals jij het vraagt</td></tr>
<tr><td>Een zelfstandig ontwerper die ook bouwt (zoals ik)</td><td>4.000 tot 12.000 euro</td><td>Een site die ontworpen is op wat je klanten doen, gebouwd, gemeten en geregeld</td></tr>
<tr><td>Een bureau</td><td>8.000 tot 25.000 euro en meer</td><td>Hetzelfde als hierboven, plus een accountmanager, een projectleider en hun proces</td></tr>
</table>
<p>De bedragen zijn richtprijzen exclusief btw voor een bedrijfswebsite van vijf tot tien pagina's. Een webshop of iets met inloggen zit daar boven.</p>

<h2>Waar zit het verschil in?</h2>
<p>Niet in het aantal pagina's. Niet in de techniek. Bijna elke site draait tegenwoordig op dezelfde soort bouwstenen. Het verschil zit in <strong>wie er nadenkt over je klant voordat er gebouwd wordt</strong>.</p>
<p>Een webbouwer bouwt wat je vraagt. Vraag je om een homepage met een slider, drie diensten en een contactformulier, dan krijg je dat. Netjes, op tijd, betaalbaar. Maar niemand heeft gevraagd waarom iemand op je site komt, wat hij wil weten en wat hem tegenhoudt om te bellen. Dus je hebt een site, en geen klanten.</p>
<p>Een bureau denkt daar wel over na, en laat je dat merken op de factuur. Je betaalt voor een strateeg, een ontwerper, een bouwer en iemand die dat allemaal coördineert. Bij een groot project is dat het waard. Bij een bedrijf met vijf tot vijftig mensen betaal je vooral voor de overhead.</p>

<div class="callout"><div class="k">Wat er echt speelt</div><p>Je kunt kwaliteit niet beoordelen, en dat is niet gek. Vraag daarom niet "wat kost het", maar "wat gaat mijn klant straks beter kunnen, en hoe weten we of dat lukt". Wie daar geen antwoord op heeft, verkoopt je een plaatje.</p></div>

<h2>Wat zit er in een goede prijs?</h2>
<p>Als je een offerte krijgt, check dan of dit erin zit. Zo niet, dan komt het er later bij, en dan is het duurder.</p>
<ul>
<li><strong>Gesprek over je klanten en je doelen.</strong> Wie komt er op je site, wat wil die weten, wat moet hij doen? Zonder dit is alles daarna gokwerk.</li>
<li><strong>Teksten.</strong> De meeste offertes gaan ervan uit dat jij de teksten aanlevert. Dat is het moment waarop projecten drie maanden stilvallen. Teksten die verkopen horen erbij.</li>
<li><strong>Vindbaarheid.</strong> Een technisch schone site, snel, goede titels, en de basis zodat Google je vindt op je bedrijfsnaam en je regio.</li>
<li><strong>Meten.</strong> Statistieken die aan staan én iemand die ze na een maand met je bekijkt. Anders weet je nooit of het werkt.</li>
<li><strong>Hosting, domein en onderhoud.</strong> Iemand die het regelt, updates doet en bereikbaar is als er iets kapot is. Ook na oplevering.</li>
<li><strong>Zelf aanpassen.</strong> Teksten, foto's en nieuws moet je zelf kunnen wijzigen, zonder factuur.</li>
</ul>

<h2>Wanneer betaal je te veel?</h2>
<p>Drie signalen die ik vaak zie:</p>
<ol>
<li><strong>Uurtje factuurtje zonder plafond.</strong> Een website is een afgebakend product. Wie geen vaste prijs durft te geven, weet zelf niet wat hij gaat bouwen.</li>
<li><strong>Onderhoudscontract dat meer kost dan de site.</strong> 150 euro per maand voor "beheer" is 1.800 euro per jaar. Vraag wat je daar precies voor krijgt.</li>
<li><strong>Een strategiefase van vier weken voor een site van zes pagina's.</strong> Nadenken is goed, maar dit hoort dagen te duren, geen maanden.</li>
</ol>

<h2>En wanneer betaal je te weinig?</h2>
<p>Ook dat bestaat. Een site van 1.200 euro die geen klanten oplevert is duurder dan een site van 5.000 euro die dat wel doet. Als je een bedrijf hebt waar een nieuwe klant honderden of duizenden euro's waard is, dan is besparen op het ding dat die klanten binnenhaalt een rare plek om te besparen.</p>

<div class="callout green"><div class="k">Zo doe ik het</div><p>Een website bij mij begint <span class="mark">vanaf 3.950 euro</span> en staat in twee tot drie weken live. Ontwerp, bouw, teksten, vindbaarheid, meten en hosting zitten erin. Twijfel je of dat past? Begin met een <a href="/#pakketten">Kickstart</a>: in één week weet je precies wat je nodig hebt en wat het kost, voor 950 euro die verrekend wordt als je doorgaat.</p></div>

<h2>Wat ik zou doen als ik jou was</h2>
<p>Vraag niet drie offertes voor "een website". Vraag drie mensen om in een halfuur te vertellen wat jouw klant straks beter kan, en hoe ze dat gaan aantonen. Degene die daar het scherpste antwoord op heeft, is degene die je wilt. De prijs is daarna een detail.</p>
'''
},
{
 'slug':'bureau-freelancer-of-zelf-met-ai',
 'cat':'Kiezen',
 'title':'Bureau, webbouwer of zelf met AI: wat past bij jouw bedrijf?',
 'desc':'Een eerlijke vergelijking van de drie manieren om een website of app te laten maken: bureau, webbouwer en zelf bouwen met AI. Met de voordelen, de valkuilen en wanneer je welke kiest.',
 'lead':'Je hebt drie opties, en geen van drie is de goede voor iedereen. Dit is wanneer je welke kiest, en waarom ik er zelf tussenin ben gaan zitten.',
 'read':'5 minuten',
 'body':'''
<p>Als je een nieuwe website of app wilt, kom je in een markt terecht waar iedereen zegt dat hij de beste keuze is. Laat ik het anders doen: hier zijn de drie opties, met wat ze goed doen én waar ze je laten vallen.</p>

<h2>Optie 1: Het bureau</h2>
<p><strong>Goed in:</strong> grote projecten met veel disciplines. Merk, strategie, campagnes, techniek, alles onder één dak. Als je vijftig mensen hebt en een marketingafdeling, is een bureau vaak logisch.</p>
<p><strong>Waar het misgaat bij kleinere bedrijven:</strong> je betaalt voor het proces. Een accountmanager die tussen jou en de maker zit. Een projectleider die vergaderingen plant. Een strategiefase van weken voor een site van acht pagina's. En na oplevering ben je van ze afhankelijk: elke wijziging is een ticket.</p>
<p><strong>Kies een bureau als:</strong> je budget boven de 25.000 euro zit, je meerdere kanalen tegelijk aanpakt en je iemand hebt die het traject intern kan trekken.</p>

<h2>Optie 2: De webbouwer of freelancer</h2>
<p><strong>Goed in:</strong> snel en betaalbaar iets neerzetten. Je zegt wat je wilt, hij bouwt het. Voor een simpele site die vooral moet bestaan (adres, openingstijden, wat foto's) is dit prima.</p>
<p><strong>Waar het misgaat:</strong> hij bouwt wat je vraagt. En jij bent geen expert in wat je klanten nodig hebben. Dus je krijgt een site die er goed uitziet en waarvan niemand weet of hij werkt. Niemand heeft gemeten, niemand heeft klanten gesproken, niemand heeft "waarom" gevraagd.</p>
<p><strong>Kies een webbouwer als:</strong> je precies weet wat je wilt, je site vooral een visitekaartje is en je geen klanten via je site hoeft binnen te halen.</p>

<h2>Optie 3: Zelf, met een template of een AI-tool</h2>
<p><strong>Goed in:</strong> vandaag beginnen, bijna gratis. Wix, Squarespace, en tegenwoordig AI-tools die in een minuut een hele site genereren. Voor een eerste versie, een test of een hobbyproject is dat fantastisch.</p>
<p><strong>Waar het misgaat:</strong> het wordt meteen zo'n site. Generiek, want de tool weet niets van jouw klanten. En zodra je iets wilt dat niet in de template zit (een boekingssysteem, een koppeling met je kassa, iets dat écht van jou is) loop je vast. Dan begin je alsnog opnieuw, met een bouwer.</p>
<p><strong>Kies zelf bouwen als:</strong> je net begint, je nog geen budget hebt, of je eerst wilt testen of je idee überhaupt leeft.</p>

<div class="callout"><div class="k">En AI dan?</div><p>Iedereen roept dat je tegenwoordig zelf een site of app maakt met AI. Klopt, en het wordt ook meteen zo'n site. AI is gereedschap. Het verschil zit in wie de vragen stelt vóór er gebouwd wordt. Dat gereedschap gebruik ik ook, met vijftien jaar ervaring erachter. Daarom kan ik het in weken, voor een prijs die een bureau niet kan maken.</p></div>

<h2>Optie 4, en daarom besta ik</h2>
<p>Er is een vierde optie die de meeste ondernemers niet kennen: <strong>een zelfstandig ontwerper die ook bouwt.</strong> Iemand die de vragen stelt van een bureau, het tempo heeft van een webbouwer, en de tools gebruikt van een AI-bouwer. Zonder overhead, zonder overdracht, met één persoon van eerste gesprek tot live.</p>
<p>Dat is wat ik doe. Vijftien jaar heb ik apps en websites gemaakt bij de Belastingdienst, ABN AMRO en de SVB, plekken waar miljoenen mensen iets in één keer moeten snappen. Die manier van werken was altijd alleen betaalbaar voor grote organisaties. Met AI in het bouwproces kan het nu ook voor een bedrijf met vijf of vijftig mensen.</p>

<h2>De eerlijke vergelijking</h2>
<table>
<tr><th></th><th>Bureau</th><th>Webbouwer</th><th>Zelf met AI</th><th>Ontwerper die bouwt</th></tr>
<tr><td>Denkt na over je klant</td><td>Ja</td><td>Nee</td><td>Nee</td><td>Ja</td></tr>
<tr><td>Doorlooptijd</td><td>Maanden</td><td>Weken</td><td>Uren</td><td>Weken</td></tr>
<tr><td>Prijs website</td><td>8.000 tot 25.000+</td><td>1.500 tot 5.000</td><td>Bijna niets</td><td>4.000 tot 12.000</td></tr>
<tr><td>Meet of het werkt</td><td>Soms</td><td>Nee</td><td>Nee</td><td>Ja</td></tr>
<tr><td>Wie je spreekt</td><td>Accountmanager</td><td>De bouwer</td><td>Niemand</td><td>De maker</td></tr>
<tr><td>Na oplevering</td><td>Ticketsysteem</td><td>Als hij tijd heeft</td><td>Jijzelf</td><td>Een appje</td></tr>
</table>

<div class="callout green"><div class="k">Nog niet zeker?</div><p>Doe de <a href="/#check">check van vijf vragen</a>. Die zegt eerlijk welk pakket past, en ook wanneer je beter nog even niets kunt laten bouwen.</p></div>
'''
},
{
 'slug':'waarom-je-website-geen-klanten-oplevert',
 'cat':'Verbeteren',
 'title':'Waarom je nieuwe website geen klanten oplevert (en drie dingen die je morgen kunt fixen)',
 'desc':'Je website ziet er goed uit, maar levert niets op. Dit zijn de zeven lekken die ik het vaakst zie bij MKB-websites, en drie fixes die je zelf vandaag kunt doen.',
 'lead':'Er komen mensen op je site. Ze bellen alleen niet. Dit zijn de plekken waar het bijna altijd misgaat, en wat je er zelf aan kunt doen voordat je iemand belt.',
 'read':'7 minuten',
 'body':'''
<p>Ik krijg regelmatig ondernemers aan de lijn met een site die vorig jaar is opgeleverd. Mooi ding. Foto's, animaties, alles erop en eraan. En de conclusie na een jaar: "Ik weet niet of hij iets doet." Meestal doet hij weinig. Niet omdat de bouwer slecht werk leverde, maar omdat niemand naar de klant heeft gekeken. Dit zijn de zeven lekken die ik het vaakst zie.</p>

<h2>Lek 1: Je zegt niet wat je doet</h2>
<p>"Wij maken het verschil." "Samen naar een duurzame toekomst." "Passie voor kwaliteit." Iemand landt op je site en weet na vijf seconden nog niet wat je verkoopt, voor wie, en waarom bij jou. Dan is hij weg.</p>
<p><strong>De test:</strong> laat iemand die je bedrijf niet kent vijf seconden naar je homepage kijken. Vraag dan: wat doen ze, en voor wie? Als het antwoord hapert, is dit je grootste lek.</p>

<h2>Lek 2: De volgende stap is onduidelijk</h2>
<p>Wat moet iemand doen na het lezen? Bellen, mailen, een offerte aanvragen, een afspraak maken? Op veel sites staan vier knoppen naast elkaar en dus doet niemand iets. Eén duidelijke volgende stap, overal dezelfde, werkt beter dan vijf opties.</p>

<h2>Lek 3: Het formulier vraagt te veel</h2>
<p>Naam, bedrijf, adres, telefoon, hoe heeft u ons gevonden, onderwerp, bericht. Elke extra vraag kost je aanvragen. Vraag alleen wat je nodig hebt om terug te bellen: naam, e-mail of telefoon, en waar het over gaat.</p>

<h2>Lek 4: Op mobiel is het een ramp</h2>
<p>Meer dan de helft van je bezoekers zit op een telefoon. Open je site eens op je eigen telefoon, met de ogen van iemand die haast heeft. Kun je het nummer aantikken om te bellen? Staat de belangrijkste knop boven de vouw? Laadt het binnen drie seconden op 4G?</p>

<h2>Lek 5: Geen bewijs</h2>
<p>Mensen geloven niet wat jij over jezelf zegt. Ze geloven wat anderen over je zeggen en wat je hebt gedaan. Een echte klant met naam en foto die vertelt wat het opleverde, doet meer dan tien alinea's over je passie.</p>

<h2>Lek 6: Prijzen zijn geheim</h2>
<p>"Vraag een offerte aan" is een drempel. Als je geen enkel bedrag noemt, denkt een deel van je bezoekers dat het te duur is, en een ander deel dat het gedoe wordt. Beide bellen niet. Een vanaf-prijs of een voorbeeld ("een keuken zoals deze vanaf 12.000 euro") haalt die twijfel weg en filtert meteen de mensen eruit die het toch niet kunnen betalen.</p>

<h2>Lek 7: Je meet niets</h2>
<p>Dit is het lek onder alle andere lekken. Als je niet weet hoeveel mensen op je site komen, waar ze binnenkomen en waar ze afhaken, kun je niets verbeteren. Dan wordt elke discussie over je site een discussie over smaak.</p>

<div class="callout"><div class="k">Wat er echt speelt</div><p>Bijna nooit is het één groot probleem. Het zijn drie of vier kleine dingen die samen een groot lek vormen. Daarom zie je het zelf niet: elk ding op zich lijkt onbelangrijk.</p></div>

<h2>Drie dingen die je morgen kunt fixen</h2>
<ol>
<li><strong>Herschrijf je eerste zin.</strong> Wat je doet, voor wie, en wat het oplevert. In gewone taal. "Wij ontwerpen en plaatsen keukens voor gezinnen in Apeldoorn en omgeving, binnen vier weken" verslaat elke slogan.</li>
<li><strong>Zet één knop bovenaan, en laat die overal terugkomen.</strong> "Plan een gratis adviesgesprek" of "Bel me terug". Eén actie, één kleur, op elke pagina op dezelfde plek.</li>
<li><strong>Zet statistieken aan.</strong> Google Analytics of een privacyvriendelijk alternatief zoals Plausible. Vandaag aanzetten, over een maand kijken. Pas dan weet je waar je moet verbeteren.</li>
</ol>

<h2>En als dat niet genoeg is</h2>
<p>Dan is het tijd voor de andere lekken, en die zitten vaak dieper: in de opbouw, in hoe mensen door je site lopen, in wat ze verwachten en niet vinden. Dat is precies wat ik in een <a href="/#pakketten">Kickstart</a> in één week uitzoek: waar het lekt, wat het kost, en een klikbaar voorstel hoe het beter kan. Vaak hoef je daarna niet eens een nieuwe site. Soms wel. Maar dan weet je waarom.</p>

<div class="callout green"><div class="k">Zelf kijken</div><p>Doe de <a href="/#check">check van vijf vragen</a>. Je krijgt meteen een eerste inschatting waar het bij jou waarschijnlijk zit.</p></div>
'''
},
]

def ld(a,url):
    import json
    return json.dumps({"@context":"https://schema.org","@type":"Article","headline":a['title'],"description":a['desc'],"datePublished":TODAY,"dateModified":TODAY,"inLanguage":"nl","author":{"@type":"Person","name":"Rudolf van der Velde"},"publisher":{"@type":"Organization","name":"Brandvizer"},"mainEntityOfPage":url},ensure_ascii=False)

os.makedirs(ROOT+'/kennis',exist_ok=True)
urls=[]
for a in ARTICLES:
    url=BASE+'/kennis/'+a['slug']; urls.append(url)
    links=''.join('<a href="/kennis/%s">%s</a>'%(b['slug'],b['title']) for b in ARTICLES if b is not a)
    html=HEAD.format(title=a['title'],desc=a['desc'],url=url,ld=ld(a,url))
    html+='''<main>
<section class="wrap art-head">
  <div class="eyebrow">%s</div>
  <h1>%s</h1>
  <p class="lead">%s</p>
  <div class="art-meta"><span>Rudolf van der Velde</span><span>%s leestijd</span><span>September 2026</span></div>
</section>
<section class="wrap art">
  <article class="art-body">%s</article>
  %s
</section>
%s</main>
'''%(a['cat'],a['title'],a['lead'],a['read'],a['body'],ASIDE.format(links=links),CTA)
    html+=FOOT
    open(ROOT+'/kennis/'+a['slug']+'.html','w').write(html)

# Overzicht
url=BASE+'/kennis'
html=HEAD.format(title='Kennis: lezen voordat je kiest',desc='Eerlijke artikelen voor ondernemers die een website, webshop of app willen: wat het kost, hoe je kiest en waarom sites geen klanten opleveren.',url=url,ld='{"@context":"https://schema.org","@type":"CollectionPage","name":"Kennis","inLanguage":"nl"}')
html=html.replace('<title>Kennis: lezen voordat je kiest | Brandvizer</title>','<title>Kennis: lezen voordat je een website of app laat maken | Brandvizer</title>')
cards=''.join('<a class="kcard" href="/kennis/%s"><div class="cat">%s · %s</div><h3>%s</h3><p>%s</p><div class="more">Lees verder</div></a>'%(a['slug'],a['cat'],a['read'],a['title'],a['desc']) for a in ARTICLES)
html+='''<main>
<section class="wrap art-head">
  <div class="eyebrow">Lezen voordat je kiest</div>
  <h1>Wat je wilt weten vóór je iemand belt.</h1>
  <p class="lead">Geen vakjargon, geen verkooppraatjes. Wat een website of app echt kost, hoe je kiest wie het maakt, en waarom de meeste sites geen klanten opleveren. Geschreven voor ondernemers, niet voor designers.</p>
</section>
<section class="wrap"><div class="klist">%s</div></section>
%s</main>
'''%(cards,CTA)
html+=FOOT
open(ROOT+'/kennis/index.html','w').write(html)

# sitemap + robots
sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
sm+='  <url><loc>%s/</loc><lastmod>%s</lastmod><changefreq>monthly</changefreq><priority>1.0</priority></url>\n'%(BASE,TODAY)
sm+='  <url><loc>%s/kennis</loc><lastmod>%s</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>\n'%(BASE,TODAY)
for u in urls: sm+='  <url><loc>%s</loc><lastmod>%s</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>\n'%(u,TODAY)
sm+='</urlset>\n'
open(ROOT+'/sitemap.xml','w').write(sm)
open(ROOT+'/robots.txt','w').write('User-agent: *\nAllow: /\nDisallow: /_build/\nSitemap: %s/sitemap.xml\n'%BASE)

# Blok op homepage
p=ROOT+'/index.html'; h=open(p).read()
if 'id="kennis"' not in h:
    block='''<!-- KENNIS -->
<section id="kennis" class="sec wrap">
  <div class="eyebrow rv">Lezen voordat je kiest</div>
  <h2 class="h2 rv">Eerst weten hoe het zit? <span class="mark" data-mark>Lees dit.</span></h2>
  <p class="lead rv" style="margin-top:22px">Eerlijke stukken over wat het kost, hoe je kiest en waarom de meeste sites geen klanten opleveren. Voor ondernemers, niet voor designers.</p>
  <div class="klist">%s</div>
  <p class="rv"><a class="btn ghost" href="/kennis">Alle artikelen</a></p>
</section>

<!-- OVER -->'''%(''.join('<a class="kcard rv" href="/kennis/%s"><div class="cat">%s · %s</div><h3>%s</h3><p>%s</p><div class="more">Lees verder</div></a>'%(a['slug'],a['cat'],a['read'],a['title'],a['desc']) for a in ARTICLES))
    h=h.replace('<!-- OVER -->',block,1)
    css='''  /* Kennis */
  .klist{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin:44px 0 30px}
  .kcard{background:var(--white);border:1px solid var(--line);border-radius:22px;padding:26px 26px 24px;text-decoration:none;display:flex;flex-direction:column;transition:transform .4s var(--ease),box-shadow .4s;position:relative}
  .kcard::before{content:"";position:absolute;left:26px;top:0;width:44px;height:4px;background:var(--pink);border-radius:0 0 4px 4px}
  .kcard:hover{transform:translateY(-4px);box-shadow:0 24px 60px rgba(15,27,45,.12)}
  .kcard .cat{font-size:var(--small);color:var(--mute);font-weight:600;margin:6px 0 10px}
  .kcard h3{font-size:var(--h4);margin-bottom:10px} .kcard p{color:var(--ink2);font-size:var(--small);flex:1}
  .kcard .more{margin-top:16px;font-family:var(--display);font-weight:600;color:var(--pink)}
  /* About */'''
    h=h.replace('  /* About */',css,1)
    h=h.replace('    .about{grid-template-columns:1fr}','    .about{grid-template-columns:1fr}\n    .klist{grid-template-columns:1fr}',1)
    # nav
    h=h.replace('<a href="#cases">Cases</a><a href="#over">Over Rudolf</a><a href="#contact">Contact</a>\n    </nav>','<a href="#cases">Cases</a><a href="/kennis">Kennis</a><a href="#over">Over Rudolf</a><a href="#contact">Contact</a>\n    </nav>',1)
    h=h.replace('<a href="#cases">Cases</a><a href="#over">Over Rudolf</a><a href="#contact">Contact</a>\n</nav>','<a href="#cases">Cases</a><a href="/kennis">Kennis</a><a href="#over">Over Rudolf</a><a href="#contact">Contact</a>\n</nav>',1)
    h=h.replace('<a href="#cases">Cases</a><a href="#over">Over</a><a href="mailto:rudolf@brandvizer.nl">Mail</a>','<a href="#cases">Cases</a><a href="/kennis">Kennis</a><a href="#over">Over</a><a href="mailto:rudolf@brandvizer.nl">Mail</a>',1)
    open(p,'w').write(h)
print('kennis ok', len(ARTICLES))
