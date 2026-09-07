import os, re
p=os.path.expanduser('~/mnt/brandvizer-site/index.html')
h=open(p).read()
def rep(a,b,n=1):
    global h; c=h.count(a); assert c==n,(a[:70],c); h=h.replace(a,b)
def between(start,end,new):
    global h; s=h.index(start); e=h.index(end); h=h[:s]+new+h[e:]

# ---------- HEAD ----------
rep('<title>Brandvizer | Je digitale product lekt klanten. Ik vind waar.</title>','<title>Brandvizer | Een nieuwe website of app die klanten oplevert</title>')
rep('<meta name="description" content="Brandvizer helpt ondernemers met een webshop, app of portaal dat niet doet wat het moet doen. Eerst meten waar klanten weglekken, dan gericht verbeteren. Persoonlijk, zonder bureau eromheen.">',
    '<meta name="description" content="Een nieuwe website, webshop of app voor je bedrijf, ontworpen én gebouwd door één persoon met de ervaring van banken en overheid. Vaste prijs, in weken live, hosting geregeld.">')
rep('<meta property="og:title" content="Brandvizer | Je digitale product lekt klanten. Ik vind waar.">','<meta property="og:title" content="Brandvizer | Een nieuwe website of app die klanten oplevert">')
rep('<meta property="og:description" content="Eerst meten, dan bouwen. Product Scan in 2 tot 3 weken, daarna samen verbeteren. Door Rudolf van der Velde.">','<meta property="og:description" content="Ontworpen én gebouwd door Rudolf van der Velde. Vaste prijs, in weken live, hosting geregeld.">')
rep('"description":"UX en digitale productontwikkeling voor het MKB. Eerst meten waar klanten weglekken, dan verbeteren."','"description":"Websites, webshops en apps voor het MKB. Ontwerp en bouw door één persoon, vaste prijs, hosting geregeld."')

# ---------- NAV ----------
rep('<a href="#pijn">Herken je dit?</a><a href="#aanpak">Aanpak</a><a href="#cases">Cases</a><a href="#over">Over Rudolf</a><a href="#contact">Contact</a>\n    </nav>\n    <a class="btn sm pink" href="#check">Doe de check</a>',
    '<a href="#pijn">Herken je dit?</a><a href="#aanpak">Aanpak</a><a href="#pakketten">Pakketten</a><a href="#cases">Cases</a><a href="#over">Over Rudolf</a><a href="#contact">Contact</a>\n    </nav>\n    <a class="btn sm pink" href="#check">Welk pakket past?</a>')
rep('<a href="#pijn">Herken je dit?</a><a href="#aanpak">Aanpak</a><a href="#check" class="accent">Doe de check</a><a href="#cases">Cases</a><a href="#over">Over Rudolf</a><a href="#contact">Contact</a>',
    '<a href="#pijn">Herken je dit?</a><a href="#aanpak">Aanpak</a><a href="#pakketten">Pakketten</a><a href="#check" class="accent">Welk pakket past?</a><a href="#cases">Cases</a><a href="#over">Over Rudolf</a><a href="#contact">Contact</a>')

# ---------- HERO ----------
rep('<span>Hoi, ik ben Rudolf. Product designer voor ondernemers.</span>','<span>Hoi, ik ben Rudolf. Ik ontwerp en bouw websites en apps voor ondernemers.</span>')
rep('''        <span class="line" data-hero>Je product <em>lekt</em> klanten.</span><br>
        <span class="line" data-hero>Vaak op plekken die je <span class="ul-pink" id="ul1">niet ziet.<svg viewBox="0 0 200 12" preserveAspectRatio="none"><path d="M2 8 C 40 2, 80 10, 120 5 S 180 4, 198 7"/></svg></span></span>''',
'''        <span class="line" data-hero>Een nieuwe website of app</span><br>
        <span class="line" data-hero>die <em>klanten oplevert.</em></span><br>
        <span class="line" data-hero>Niet alleen een <span class="ul-pink" id="ul1">mooie.<svg viewBox="0 0 200 12" preserveAspectRatio="none"><path d="M2 8 C 40 2, 80 10, 120 5 S 180 4, 198 7"/></svg></span></span>''')
rep('<p class="lead" data-hero>Een webshop, app of klantportaal dat er prima uitziet, maar niet oplevert wat je hoopte. Ik zoek uit waar het misgaat, laat je zien wat het je kost, en repareer het samen met jou. Zonder bureau eromheen.</p>',
    '<p class="lead" data-hero>Voor ondernemers die het goed willen doen, zonder bureau eromheen. Ik ontwerp én bouw het zelf, met de ervaring van banken en overheid. Vaste prijs, in weken live, hosting geregeld.</p>')
rep('<a class="btn pink" href="#check">Doe de check in 2 minuten</a>\n        <a class="btn ghost" href="#aanpak">Zo werk ik</a>',
    '<a class="btn pink" href="#check">Welk pakket past bij mij?</a>\n        <a class="btn ghost" href="#pakketten">Bekijk de pakketten</a>')
rep('<span class="hint"><svg viewBox="0 0 40 22"><path d="M2 4 C 12 20, 26 20, 36 6 M30 6 l6 0 l0 6"/></svg> Gratis, geen account, geen mailtjes achteraf</span>',
    '<span class="hint"><svg viewBox="0 0 40 22"><path d="M2 4 C 12 20, 26 20, 36 6 M30 6 l6 0 l0 6"/></svg> Vijf vragen, twee minuten, geen account</span>')
rep('<p class="mock-cap">Fictief voorbeeld, maar dit zie ik elke week.</p>','<p class="mock-cap">Fictief voorbeeld. Zo ziet een site eruit die "af" is, maar geen klanten oplevert.</p>')

# ---------- PIJN ----------
between('<!-- PIJN -->','<!-- STATEMENT -->','''<!-- PIJN -->
<section id="pijn" class="sec wrap">
  <div class="eyebrow rv">Herken je dit?</div>
  <h2 class="h2 rv">Je wilt iets nieuws. Maar <span class="mark" data-mark>wie moet je geloven?</span></h2>
  <p class="lead rv" style="margin-top:22px">Dit zijn de zinnen die ik het vaakst hoor van ondernemers die een nieuwe website of app willen. Onder elke zin: wat er meestal echt speelt.</p>
  <div class="pains">
    <article class="pain rv">
      <q>Ik heb drie offertes. Eén van 4.000 euro en één van 25.000. Ik snap niet waar het verschil in zit.</q>
      <div class="real"><span class="tag">Wat er echt speelt:</span><p>Je kunt kwaliteit niet beoordelen, en dat is niet gek. De ene bouwt een template, de ander verkoopt zijn eigen proces. Niemand legt uit wat jouw klanten straks beter kunnen.</p></div>
    </article>
    <article class="pain rv">
      <q>Mijn site is uit 2018. Ik schaam me er een beetje voor, maar ik weet niet waar ik moet beginnen.</q>
      <div class="real"><span class="tag">Wat er echt speelt:</span><p>Je bent geen websitebouwer, en dat hoeft ook niet. Je hebt iemand nodig die de goede vragen stelt en het daarna gewoon regelt. Van eerste gesprek tot live.</p></div>
    </article>
    <article class="pain rv">
      <q>Het vorige bureau leverde iets moois. Maar ik kan er zelf niks in aanpassen en ze reageren niet meer.</q>
      <div class="real"><span class="tag">Wat er echt speelt:</span><p>Je bent afhankelijk gemaakt. Een goede site is van jou: je kunt er zelf in werken, en de bouwer is bereikbaar als het nodig is. Geen ticketsysteem, gewoon een appje.</p></div>
    </article>
    <article class="pain rv">
      <q>Iedereen zegt dat je tegenwoordig zelf een site of app maakt met AI. Waarom zou ik dan nog iemand betalen?</q>
      <div class="real"><span class="tag">Wat er echt speelt:</span><p>Dat kan, en het wordt ook meteen zo'n site. AI is gereedschap. Het verschil zit in wie de vragen stelt vóór er gebouwd wordt: wie zijn je klanten en wat moeten ze kunnen? Dat gereedschap gebruik ik ook, alleen met tien jaar ervaring erachter.</p></div>
    </article>
  </div>
</section>

''')

# ---------- STATEMENT ----------
between('<!-- STATEMENT -->','<!-- AANPAK -->','''<!-- STATEMENT -->
<section class="sec wrap statement">
  <div class="eyebrow rv">Waarom dit zo lastig kiezen is</div>
  <h2 class="h2 rv">Drie opties. En <span class="mark" data-mark>geen van drie klopt.</span></h2>
  <div class="cols">
    <div class="col rv"><h3>Het bureau</h3><p>Duur, traag, een accountmanager ertussen. Ze verkopen hun proces, niet jouw resultaat. En na oplevering ben je van ze afhankelijk.</p></div>
    <div class="col rv"><h3>De webbouwer</h3><p>Betaalbaar, maar hij bouwt wat je vraagt. Niemand vraagt of je klanten dat ook willen. Je krijgt een mooie site, geen klanten.</p></div>
    <div class="col rv"><h3>Zelf, met een template of AI-tool</h3><p>Snel en goedkoop. Maar generiek, en zodra het ingewikkeld wordt zit je vast. En je klant merkt het.</p></div>
  </div>
  <div class="why-me">
    <div class="why-head rv"><div class="eyebrow">Wat ik anders doe</div><h3>Zes redenen om het met mij te doen.</h3></div>
    <div class="why-grid">
      <div class="why rv"><h4>Eén persoon, van eerste gesprek tot live</h4><p>Geen overdracht tussen designer en bouwer, geen accountmanager. Je praat met degene die het maakt.</p></div>
      <div class="why rv"><h4>Eerst begrijpen, dan bouwen</h4><p>Voor ik iets ontwerp kijk ik wie je klanten zijn en wat ze moeten kunnen. Dat is het verschil tussen mooi en werkend.</p></div>
      <div class="why rv"><h4>Je klanten snappen het in één keer</h4><p>Tien jaar maakte ik apps waar miljoenen Nederlanders mee moesten werken, van belastingaangifte tot bankieren. Wie iets meteen snapt, komt terug.</p></div>
      <div class="why rv"><h4>Vaste prijs, vaste doorlooptijd</h4><p>Je weet vooraf wat het kost en wanneer het klaar is. Geen uurtje factuurtje, geen verrassingen.</p></div>
      <div class="why rv"><h4>Meetbaar</h4><p>Na livegang laat ik zien wat het doet: bezoekers, aanvragen, bestellingen. Geen gevoel, maar cijfers.</p></div>
      <div class="why rv"><h4>Alles geregeld</h4><p>Hosting, domein en onderhoud regel ik via mijn vaste partner. Jij hoeft nergens over na te denken.</p></div>
    </div>
  </div>
</section>

''')

# ---------- AANPAK + PAKKETTEN ----------
between('<!-- AANPAK -->','<!-- CHECK -->','''<!-- AANPAK -->
<section id="aanpak" class="sec wrap">
  <div class="eyebrow rv">Zo werk ik</div>
  <h2 class="h2 rv">Eerst begrijpen. Dan bouwen. <span class="mark" data-mark>Dan meten.</span></h2>
  <p class="lead rv" style="margin-top:22px">Drie stappen, altijd in deze volgorde. Je begint klein en met een vaste prijs. Doorgaan beslis je pas als je hebt gezien wat je krijgt.</p>
  <div class="steps3">
    <div class="step3 rv"><div class="ph">Stap 1</div><h3>Kickstart</h3><p>In één week weten we wat je nodig hebt, wat het kost en hoe het eruit gaat zien. Je krijgt een klikbaar prototype en een vaste prijs voor de bouw.</p></div>
    <div class="step3 rv"><div class="ph">Stap 2</div><h3>Bouwen</h3><p>Ik ontwerp en bouw, in korte rondes. Je kijkt elke week mee en stuurt bij. Teksten, vindbaarheid en hosting zitten erin. Dan gaat het live.</p></div>
    <div class="step3 rv"><div class="ph">Stap 3</div><h3>Meten en verbeteren</h3><p>Na livegang kijken we wat het doet. Wil je blijven verbeteren, dan doen we dat met een vast aantal uren per maand op een gezamenlijke roadmap.</p></div>
  </div>
</section>

<!-- PAKKETTEN -->
<section id="pakketten" class="sec wrap">
  <div class="eyebrow rv">Pakketten</div>
  <h2 class="h2 rv">Vaste prijzen. <span class="mark" data-mark>Geen verrassingen.</span></h2>
  <p class="lead rv" style="margin-top:22px">Vanaf-prijzen, exclusief btw. Na de Kickstart weet je het precieze bedrag. Twijfel je welk pakket past? <a href="#check">Doe de check</a>.</p>
  <div class="packs">
    <div class="pack kick rv">
      <div class="sticky-note">Hier begint het altijd</div>
      <div class="ph">Stap 1</div>
      <h3>Kickstart</h3>
      <div class="meta"><span>1 week</span><span class="price">€950</span></div>
      <p>Je weet dat je iets wilt, maar niet precies wat. In één week: wat je nodig hebt, wat het kost, en een klikbaar prototype dat je aan je klanten kunt laten zien.</p>
      <ul><li>Gesprek over je klanten en je doelen</li><li>Klikbaar prototype van de belangrijkste schermen</li><li>Vaste prijs en planning voor de bouw</li><li>Ga je door? Dan wordt de €950 verrekend</li></ul>
      <a class="btn" href="#contact">Plan een Kickstart</a>
    </div>
    <div class="pack rv">
      <div class="ph">Website</div>
      <h3>Een site die klanten oplevert</h3>
      <div class="meta"><span>2 tot 3 weken</span><span class="price">Vanaf €3.950</span></div>
      <p>Voor bedrijven die gevonden willen worden en aanvragen willen krijgen.</p>
      <ul><li>Ontwerp én bouw</li><li>Teksten die verkopen</li><li>Vindbaar in Google, snel, op elk scherm</li><li>Meten wat het doet</li><li>Hosting en domein geregeld</li><li>Zelf teksten en foto's aanpassen</li></ul>
      <a class="btn ghost" href="#contact">Vraag een voorstel aan</a>
    </div>
    <div class="pack feat rv">
      <div class="ph">Webshop of webapp</div>
      <h3>Bestellen, boeken of een portaal</h3>
      <div class="meta"><span>4 tot 6 weken</span><span class="price">Vanaf €7.500</span></div>
      <p>Voor bedrijven waar klanten iets moeten kunnen doen: bestellen, boeken, inloggen, aanvragen.</p>
      <ul><li>Onderzoek bij je klanten</li><li>Prototype getest vóór de bouw</li><li>Ontwerp én bouw, koppelingen met wat je al gebruikt</li><li>Meten wat het doet</li><li>Hosting en beheer geregeld</li></ul>
      <a class="btn" href="#contact">Vraag een voorstel aan</a>
    </div>
    <div class="pack rv">
      <div class="ph">App</div>
      <h3>iOS en Android, van idee tot in de store</h3>
      <div class="meta"><span>6 tot 10 weken</span><span class="price">Vanaf €12.500</span></div>
      <p>Voor bedrijven die klanten of medewerkers iets in handen willen geven dat ze elke dag gebruiken.</p>
      <ul><li>Concept en validatie met echte gebruikers</li><li>Ontwerp volgens de regels van Apple en Google</li><li>Bouw, testen en publicatie in de stores</li><li>Meten wat het doet</li></ul>
      <a class="btn ghost" href="#contact">Vraag een voorstel aan</a>
    </div>
    <div class="pack ongoing rv">
      <div class="ph">Doorlopend</div>
      <h3>Elke maand een stap verder</h3>
      <div class="meta"><span>Per maand, opzegbaar</span><span class="price">Vanaf €750</span></div>
      <p>Een vast aantal uren per maand. We maken samen een roadmap, jij bepaalt wat voorgaat, ik pak het op. Geen offertes per klusje.</p>
      <ul><li>Vaste uren, vaste prijs</li><li>Gezamenlijke roadmap en prioriteiten</li><li>Onderhoud, verbeteringen en nieuwe functies</li><li>Voorrang in mijn planning</li></ul>
      <a class="btn ghost" href="#contact">Vraag naar de opties</a>
    </div>
  </div>
</section>

''')

# ---------- CHECK ----------
between('<!-- CHECK -->','<!-- CASES -->','''<!-- CHECK -->
<section id="check" class="sec wrap">
  <div class="check">
    <div class="eyebrow rv">Even digitaal kennismaken</div>
    <h2 class="h2 rv">Vijf vragen. Dan weet je <span class="mark" data-mark>welk pakket past</span> en wat het ongeveer kost.</h2>
    <p class="lead rv" style="margin-top:18px">Geen account, geen nieuwsbrief. Aan het eind kun je de uitkomst naar me mailen als je wilt, meer niet.</p>
    <div class="check-body rv" id="checkBody">
      <div class="prog" aria-hidden="true"><i id="progFill"></i></div>

      <div class="q on" data-q="0">
        <div class="step">Vraag 1 van 5</div>
        <h3>Wat wil je laten maken?</h3>
        <div class="opts">
          <button class="opt" data-v="website">Een website</button>
          <button class="opt" data-v="webapp">Een webshop, boekingssysteem of klantportaal</button>
          <button class="opt" data-v="app">Een app voor iOS en Android</button>
          <button class="opt" data-v="weetniet">Weet ik nog niet precies</button>
        </div>
      </div>
      <div class="q" data-q="1">
        <div class="step">Vraag 2 van 5</div>
        <h3>Wat heb je nu?</h3>
        <div class="opts">
          <button class="opt" data-v="niets">Nog niets</button>
          <button class="opt" data-v="oud">Een verouderde site of app</button>
          <button class="opt" data-v="zelf">Iets zelfgebouwds (Wix, Squarespace, een template)</button>
          <button class="opt" data-v="bureau">Iets van een bureau waar ik niet blij mee ben</button>
        </div>
      </div>
      <div class="q" data-q="2">
        <div class="step">Vraag 3 van 5</div>
        <h3>Wat moet het vooral opleveren?</h3>
        <div class="opts">
          <button class="opt" data-v="aanvragen">Meer aanvragen of nieuwe klanten</button>
          <button class="opt" data-v="verkopen">Online verkopen of boeken</button>
          <button class="opt" data-v="handwerk">Minder handwerk, telefoontjes en mailtjes</button>
          <button class="opt" data-v="uitstraling">Een uitstraling die klopt bij wat we zijn</button>
        </div>
      </div>
      <div class="q" data-q="3">
        <div class="step">Vraag 4 van 5</div>
        <h3>Wanneer wil je live?</h3>
        <div class="opts">
          <button class="opt" data-v="nu">Zo snel mogelijk</button>
          <button class="opt" data-v="3mnd">Binnen drie maanden</button>
          <button class="opt" data-v="jaar">Ergens dit jaar</button>
          <button class="opt" data-v="geen">Geen haast, ik oriënteer me</button>
        </div>
      </div>
      <div class="q" data-q="4">
        <div class="step">Vraag 5 van 5</div>
        <h3>Waar denk je aan qua budget?</h3>
        <div class="opts">
          <button class="opt" data-v="b1">Tot €5.000</button>
          <button class="opt" data-v="b2">€5.000 tot €10.000</button>
          <button class="opt" data-v="b3">€10.000 tot €25.000</button>
          <button class="opt" data-v="b0">Geen idee, daar wil ik juist over praten</button>
        </div>
      </div>

      <div class="q-nav" id="qnav"><button type="button" id="qBack">Vorige vraag</button><span id="qCount"></span></div>

      <div class="res" id="res">
        <div class="step" style="font-family:var(--hand);font-size:var(--hand-m);color:var(--note);margin-bottom:10px">Mijn eerste inschatting</div>
        <div class="diag" id="rDiag"></div>
        <p class="ex" id="rEx"></p>
        <div class="rb">
          <div><h4>Wat ik zou voorstellen</h4><ul id="rStart"></ul></div>
          <div><h4>Wat we gaan meten</h4><ul id="rBlocks"></ul></div>
        </div>
        <div class="actions">
          <a class="btn pink" id="rMail" href="#">Mail me deze uitkomst en plan een gesprek</a>
          <button class="btn ghost" type="button" id="rReset">Opnieuw</button>
        </div>
        <p class="note-p">De mail opent in je eigen mailprogramma, met de uitkomst al ingevuld. Er wordt niets opgeslagen op deze site.</p>
      </div>
    </div>
  </div>
</section>

''')

# ---------- CASES intro ----------
rep('<p class="lead rv" style="margin-top:22px">Bij elke case vertel ik wat er misging, wat ik deed en waarom dat effect had. Klik op de kleine beelden om meer te zien.</p>',
    '<p class="lead rv" style="margin-top:22px">Dit zijn grote organisaties, maar het recept is voor jouw bedrijf precies hetzelfde: eerst begrijpen wat klanten nodig hebben, dan bouwen. Bij elke case vertel ik wat er misging, wat ik deed en waarom dat werkte. Klik op de kleine beelden om meer te zien.</p>')

# ---------- OVER ----------
rep('<h2 class="rv">Tien jaar bij banken en overheid. Nu voor ondernemers.</h2>','<h2 class="rv">Tien jaar bij banken en overheid. Nu voor ondernemers die het goed willen doen.</h2>')
rep('<p class="rv">Ik heb als product designer gewerkt voor de Belastingdienst, ABN AMRO, de Sociale Verzekeringsbank en Easyjobs. Plekken waar een foutje in een scherm meteen duizenden telefoontjes betekent. Daar leer je meten voordat je bouwt.</p>',
    '<p class="rv">Ik heb apps en websites gemaakt voor de Belastingdienst, ABN AMRO, de Sociale Verzekeringsbank en Easyjobs. Plekken waar miljoenen mensen iets in één keer moeten snappen, en waar een foutje in een scherm meteen duizenden telefoontjes betekent. Daar leer je eerst begrijpen, dan bouwen.</p>')
rep('<p class="rv">Wat me opvalt bij ondernemers: dezelfde problemen, maar niemand die er met die blik naar kijkt. Bureaus zijn te duur, freelancers te vrijblijvend, AI-bouwers te snel klaar. Ik zit daar tussenin. Persoonlijk, met bewijs, en met AI als gereedschap zodat het betaalbaar blijft.</p>',
    '<p class="rv">Die manier van werken was altijd alleen betaalbaar voor grote organisaties. Met AI als gereedschap bouw ik nu zo snel dat het ook kan voor een bedrijf met vijf of vijftig mensen. Zonder bureau eromheen, met mij aan tafel.</p>')
rep('<p class="rv">Je werkt met mij, niet met een accountmanager. Als ik denk dat je iets niet moet bouwen, zeg ik dat.</p>','<p class="rv">Je werkt met mij, niet met een accountmanager. En als ik denk dat je iets niet moet bouwen, zeg ik dat. Ook als het me een opdracht kost.</p>')
rep('<div><strong>1</strong><span>aanspreekpunt, van scan tot live</span></div>','<div><strong>1</strong><span>aanspreekpunt, van eerste gesprek tot live</span></div>')

# ---------- CONTACT ----------
rep('<p class="lead">Dertig minuten, online of bij jou aan tafel. Je gaat sowieso weg met twee of drie dingen die je morgen kunt doen. Of we daarna een Product Scan doen, beslis je zelf.</p>',
    '<p class="lead">Dertig minuten, online of bij jou aan tafel. Vertel wat je wilt maken en waar je tegenaan loopt. Je gaat sowieso weg met een eerlijk advies, ook als dat is: doe het (nog) niet.</p>')
rep('<a class="way" href="#check"><div><b>Eerst zelf kijken?</b><br><span>Doe de check in 2 minuten</span></div><span>→</span></a>','<a class="way" href="#check"><div><b>Eerst zelf kijken?</b><br><span>Welk pakket past bij mij?</span></div><span>→</span></a>')
rep('<a class="mcta" href="#check">Doe de check in 2 minuten</a>','<a class="mcta" href="#check">Welk pakket past bij mij?</a>')
rep('<span><a href="#aanpak">Aanpak</a><a href="#cases">Cases</a><a href="#over">Over</a><a href="mailto:rudolf@brandvizer.nl">Mail</a></span>','<span><a href="#aanpak">Aanpak</a><a href="#pakketten">Pakketten</a><a href="#cases">Cases</a><a href="#over">Over</a><a href="mailto:rudolf@brandvizer.nl">Mail</a></span>')

# ---------- CSS ----------
rep('  /* Approach */','''  /* Why me */
  .why-me{margin-top:clamp(60px,8vw,110px)}
  .why-head h3{font-size:var(--h3);margin-top:4px;max-width:20ch}
  .why-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:34px}
  .why{background:var(--white);border:1px solid var(--line);border-radius:18px;padding:24px 24px 22px;position:relative}
  .why::before{content:"";position:absolute;left:24px;top:0;width:44px;height:4px;background:var(--pink);border-radius:0 0 4px 4px}
  .why h4{margin:10px 0 8px}
  .why p{color:var(--ink2)}
  /* Steps */
  .steps3{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:44px}
  .step3{padding:26px 0 0;border-top:2px solid var(--ink)}
  .step3 .ph{font-family:var(--hand);font-size:var(--hand-l);color:var(--pink)}
  .step3 h3{font-size:var(--h4);margin:4px 0 10px}
  .step3 p{color:var(--ink2)}
  /* Packs */
  .packs{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:44px}
  .pack{background:var(--white);border:1px solid var(--line);border-radius:24px;padding:32px 30px;display:flex;flex-direction:column;position:relative;transition:transform .4s var(--ease),box-shadow .4s}
  .pack:hover{transform:translateY(-4px);box-shadow:0 24px 60px rgba(15,27,45,.12)}
  .pack.kick{border:2px solid var(--ink);grid-column:span 3;display:grid;grid-template-columns:1fr 1.2fr;column-gap:40px;align-items:start}
  .pack.kick>*{grid-column:1}
  .pack.kick ul{grid-column:2;grid-row:2/span 4;margin-top:0;align-self:center}
  .pack.kick .btn{justify-self:start;width:auto}
  .pack.feat{background:var(--ink);color:#fff;border-color:var(--ink)}
  .pack.feat .ph{color:var(--note)}
  .pack.feat p,.pack.feat li{color:rgba(255,255,255,.85)}
  .pack.feat .meta span{background:rgba(255,255,255,.12);color:#fff}
  .pack.feat .meta span.price{background:var(--note);color:var(--note-ink)}
  .pack.feat .btn{background:var(--pink);border-color:var(--pink)}
  .pack.ongoing{grid-column:span 3;display:grid;grid-template-columns:1fr 1.2fr;column-gap:40px;background:var(--green-soft);border-color:transparent}
  .pack.ongoing>*{grid-column:1}
  .pack.ongoing ul{grid-column:2;grid-row:2/span 4;margin-top:0;align-self:center}
  .pack.ongoing .btn{justify-self:start;width:auto}
  .pack .ph{font-family:var(--hand);font-size:var(--hand-l);color:var(--pink)}
  .pack h3{font-size:var(--h4);margin:4px 0 12px}
  .pack .meta{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 16px}
  .pack .meta span{font-size:var(--small);font-weight:600;padding:6px 12px;border-radius:999px;background:var(--paper2);color:var(--ink2)}
  .pack .meta span.price{background:var(--note);color:var(--note-ink)}
  .pack p{color:var(--ink2)}
  .pack ul{list-style:none;padding:0;margin:18px 0 0;display:grid;gap:9px}
  .pack li{display:flex;gap:11px;font-size:var(--body);align-items:flex-start}
  .pack li::before{content:"";width:18px;height:18px;border-radius:50%;background:var(--green-soft);flex-shrink:0;margin-top:4px;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23128C6E' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6L9 17l-5-5'/%3E%3C/svg%3E");background-size:11px;background-position:center;background-repeat:no-repeat}
  .pack.feat li::before{background-color:rgba(255,255,255,.15);background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23FFE27A' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6L9 17l-5-5'/%3E%3C/svg%3E")}
  .pack .btn{margin-top:26px;width:100%}
  .pack.feat .btn.ghost{color:#fff;border-color:rgba(255,255,255,.4)}
  .lead a{color:var(--pink);font-weight:600}
  /* Approach */''')
rep('''    .statement .cols{grid-template-columns:1fr}
    .phases{grid-template-columns:1fr}''','''    .statement .cols{grid-template-columns:1fr}
    .why-grid{grid-template-columns:1fr 1fr}
    .steps3{grid-template-columns:1fr}
    .packs{grid-template-columns:1fr}
    .pack.kick,.pack.ongoing{grid-column:auto;display:flex}
    .pack.kick ul,.pack.ongoing ul{margin-top:18px}
    .pack.kick .btn,.pack.ongoing .btn{width:100%}''')
rep('''    .pains{grid-template-columns:1fr}
    .pain .real''','''    .pains{grid-template-columns:1fr}
    .why-grid{grid-template-columns:1fr}
    .pain .real''') if '    .pains{grid-template-columns:1fr}\n    .pain .real' in h else rep('''    .pains{grid-template-columns:1fr}''','''    .pains{grid-template-columns:1fr}
    .why-grid{grid-template-columns:1fr}''')

# ---------- JS result ----------
s=h.index("  var L={webshop:'je webshop'"); e=h.index("    document.getElementById('rDiag').innerHTML=diag;")
newjs='''  var L={website:'een website',webapp:'een webshop of webapp',app:'een app',weetniet:'iets nieuws'};
  var PK={website:{n:'Website',p:'vanaf €3.950',t:'2 tot 3 weken'},webapp:{n:'Webshop of webapp',p:'vanaf €7.500',t:'4 tot 6 weken'},app:{n:'App',p:'vanaf €12.500',t:'6 tot 10 weken'}};
  var FLOOR={website:3950,webapp:7500,app:12500}, BUD={b1:5000,b2:10000,b3:25000,b0:0};
  function result(){
    var a=answers, what=L[a[0]]||'iets nieuws', pk=PK[a[0]], bud=BUD[a[4]];
    var diag='', ex='', start=[], blocks=[];
    if(a[0]==='weetniet'){
      diag='Je weet nog niet precies wat je wilt. <em>Dan is de Kickstart precies je eerste stap.</em>';
      ex='In één week zoeken we uit wat je klanten nodig hebben, wat dat kost en hoe het eruit gaat zien. Je krijgt een klikbaar prototype en een vaste prijs. Pas daarna beslis je of je bouwt, en de €950 wordt dan verrekend.';
      start=['Kickstart (1 week, €950)','Daarna een vaste prijs voor het pakket dat blijkt te passen'];
    } else if(bud>0 && bud<FLOOR[a[0]]){
      diag='Je wilt '+what+'. <em>Eerlijk: dat past nog niet in je budget.</em>';
      ex='Het pakket '+pk.n+' begint '+pk.p+'. Ik zou niet aanraden om voor minder een uitgeklede versie te laten maken, dan koop je twee keer. Wat wél kan: een Kickstart. Dan weet je precies wat je nodig hebt, wat het kost en of er een slimme kleinere eerste stap is.';
      start=['Kickstart (1 week, €950), verrekend als je doorgaat','Samen bepalen wat de kleinste versie is die al klanten oplevert'];
    } else {
      diag='Je wilt '+what+'. <em>Dat is het pakket '+pk.n+'.</em>';
      ex=pk.n+' begint '+pk.p+' en duurt '+pk.t+'. We starten met een Kickstart, dan weet je binnen een week precies wat het wordt en wat het kost. Daarna bouw ik, jij kijkt elke week mee.';
      start=['Kickstart (1 week, €950), verrekend in het pakket','Pakket '+pk.n+', '+pk.p+', '+pk.t+' tot live','Hosting en domein regel ik'];
      if(a[3]==='nu' && a[0]==='app') ex+=' Eén ding vooraf: een app in de stores krijgen kost minimaal zes weken, sneller kan niet zonder in te leveren op kwaliteit.';
      if(a[3]==='nu' && a[0]==='website') ex+=' Snel live wil je? Een website kan binnen drie weken staan als jij snel schakelt met teksten en beelden.';
    }
    if(a[1]==='bureau') ex+=' Je huidige site of app neem ik gewoon over, inclusief domein en hosting. Je hoeft je oude bureau niets uit te leggen.';
    if(a[1]==='zelf') ex+=' Wat je zelf gebouwd hebt is niet weggegooid: het vertelt me precies wat je belangrijk vindt.';
    if(a[2]==='aanvragen') blocks=['Aantal aanvragen per week','Hoeveel bezoekers een aanvraag doen','Waar mensen afhaken'];
    else if(a[2]==='verkopen') blocks=['Bestellingen of boekingen per week','Hoeveel bezoekers afrekenen','Gemiddelde orderwaarde'];
    else if(a[2]==='handwerk') blocks=['Telefoontjes en mailtjes per week, voor en na','Hoeveel klanten het zelf regelen','Tijd die jij bespaart'];
    else blocks=['Hoe lang mensen blijven','Hoeveel terugkomen','Wat klanten zeggen als je het ze vraagt'];
    var lab={0:{website:'Website',webapp:'Webshop, boekingssysteem of portaal',app:'App',weetniet:'Weet ik nog niet'},1:{niets:'Nog niets',oud:'Verouderde site of app',zelf:'Zelfgebouwd',bureau:'Van een bureau, niet blij mee'},2:{aanvragen:'Meer aanvragen',verkopen:'Online verkopen of boeken',handwerk:'Minder handwerk',uitstraling:'Uitstraling die klopt'},3:{nu:'Zo snel mogelijk','3mnd':'Binnen drie maanden',jaar:'Dit jaar',geen:'Geen haast'},4:{b1:'Tot €5.000',b2:'€5.000 tot €10.000',b3:'€10.000 tot €25.000',b0:'Geen idee'}};
'''
h=h[:s]+newjs+h[e:]
rep('''    var body='Hoi Rudolf,\\n\\nIk heb de check op brandvizer.nl gedaan. Dit kwam eruit:\\n\\n'+
      '- Product: '+lab[0][a[0]]+'\\n- Grootste ergernis: '+lab[1][a[1]]+'\\n- Hoe we meten: '+lab[2][a[2]]+'\\n- Wie bouwt: '+lab[3][a[3]]+'\\n- Over 3 maanden: '+lab[4][a[4]]+'\\n\\n'+''',
'''    var body='Hoi Rudolf,\\n\\nIk heb de check op brandvizer.nl gedaan. Dit kwam eruit:\\n\\n'+
      '- Wat ik wil: '+lab[0][a[0]]+'\\n- Wat ik nu heb: '+lab[1][a[1]]+'\\n- Wat het moet opleveren: '+lab[2][a[2]]+'\\n- Wanneer: '+lab[3][a[3]]+'\\n- Budget: '+lab[4][a[4]]+'\\n\\n'+''')
open(p,'w').write(h); print('ok',len(h))
