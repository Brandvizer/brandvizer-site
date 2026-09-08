import os
R = os.path.expanduser('~/mnt/brandvizer-site')
p = R + '/index.html'
h = open(p).read()

def rep(a, b, n=1):
    global h
    c = h.count(a)
    assert c == n, (a[:70], c)
    h = h.replace(a, b)

# ---------------- HERO ----------------
rep('<p class="lead" data-hero>Voor ondernemers die het goed willen doen, zonder bureau eromheen. Ik ontwerp én bouw het zelf, met de ervaring van banken en overheid. Vaste prijs, in weken live, hosting geregeld.</p>',
    '<p class="lead" data-hero>Ik maakte apps voor de Belastingdienst en ABN AMRO, waar miljoenen mensen mee werken. Diezelfde blik zet ik op jouw website, voor een prijs die past bij een bedrijf van vijf tot vijftig mensen. Eén vast bedrag, in weken live, hosting geregeld.</p>')
rep('<a class="btn ghost" href="#pakketten">Bekijk de pakketten</a>', '<a class="btn ghost" href="#pakketten">Bekijk de prijzen</a>')

# ---------------- OVER ----------------
rep('<h2 class="rv">Vijftien jaar bij banken en overheid. Nu voor ondernemers die het goed willen doen.</h2>',
    '<h2 class="rv">Vijftien jaar schermen voor miljoenen Nederlanders. Nu voor bedrijven van vijf tot vijftig mensen.</h2>')
rep('<p class="rv">Ik heb apps en websites gemaakt voor de Belastingdienst, ABN AMRO, de Sociale Verzekeringsbank en Easyjobs. Plekken waar miljoenen mensen iets in één keer moeten snappen, en waar een foutje in een scherm meteen duizenden telefoontjes betekent. Daar leer je eerst begrijpen, dan bouwen.</p>',
    '<p class="rv">Ik maakte apps en websites voor de Belastingdienst, ABN AMRO, de Sociale Verzekeringsbank en Easyjobs. Eén onduidelijk scherm daar betekent de volgende ochtend duizenden telefoontjes. Dan leer je vanzelf om eerst te kijken waar mensen vastlopen, en pas daarna te bouwen.</p>')
rep('<p class="rv">Die manier van werken was altijd alleen betaalbaar voor grote organisaties. Met AI als gereedschap bouw ik nu zo snel dat het ook kan voor een bedrijf met vijf of vijftig mensen. Zonder bureau eromheen, met mij aan tafel.</p>',
    '<p class="rv">Dat werk was altijd alleen betaalbaar voor grote organisaties. Met AI als gereedschap bouw ik in weken wat vroeger maanden kostte. Daarom kan het nu ook voor jouw bedrijf, zonder bureau ertussen.</p>')
rep('<p class="rv">Je werkt met mij, niet met een accountmanager. En als ik denk dat je iets niet moet bouwen, zeg ik dat. Ook als het me een opdracht kost.</p>',
    '<p class="rv">Je appt de man die het bouwt, niet een accountmanager. En denk ik dat je iets beter niet kunt maken, dan zeg ik dat. Ook als het me de opdracht kost.</p>')

# ---------------- PIJN ----------------
rep('<p class="lead rv" style="margin-top:22px">Dit zijn de zinnen die ik het vaakst hoor van ondernemers die een nieuwe website of app willen. Onder elke zin: wat er meestal echt speelt.</p>',
    '<p class="lead rv" style="margin-top:22px">Vier zinnen die ik bijna elke week hoor. Onder elke zin staat wat er werkelijk aan de hand is, en wat ik eraan doe.</p>')
rep('<p>Je kunt kwaliteit niet beoordelen, en dat is niet gek. De ene bouwt een template, de ander verkoopt zijn eigen proces. Niemand legt uit wat jouw klanten straks beter kunnen.</p>',
    '<p>Je koopt iets wat je niet kunt beoordelen. De een zet een template onder je logo, de ander rekent zijn eigen proces door. Vraag wat je klant straks beter kan en hoe je dat gaat zien. Bij mij staat het bedrag in de offerte, niet "vanaf".</p>')
rep('<p>Je bent geen websitebouwer, en dat hoeft ook niet. Je hebt iemand nodig die de goede vragen stelt en het daarna gewoon regelt. Van eerste gesprek tot live.</p>',
    '<p>Je hebt geen tijd om je hierin te verdiepen, en dat hoeft ook niet. Ik stel de vragen, ik schrijf de teksten, ik bouw en ik zet hem live. Jij keurt goed en levert je logo.</p>')
rep("<p>Je bent afhankelijk gemaakt. Een goede site is van jou: je kunt er zelf in werken, en de bouwer is bereikbaar als het nodig is. Geen ticketsysteem, gewoon een appje.</p>",
    "<p>Je bent afhankelijk gemaakt. Een goede site is van jou: teksten en foto's pas je zelf aan, voor de rest app je mij. Geen ticketsysteem, geen wachtrij, geen factuur voor elk klein dingetje.</p>")
rep("<p>Dat kan, en het wordt ook meteen zo'n site. AI is gereedschap. Het verschil zit in wie de vragen stelt vóór er gebouwd wordt: wie zijn je klanten en wat moeten ze kunnen? Dat gereedschap gebruik ik ook, alleen met vijftien jaar ervaring erachter.</p>",
    "<p>Je hebt binnen een uur een site staan. Alleen weet die tool niet wie jouw klanten zijn en waar ze afhaken. Ik gebruik dezelfde tools, met vijftien jaar ervaring in wat je ze moet laten doen. Dat scheelt jou maanden en een site die niets oplevert.</p>")

# ---------------- CASES ----------------
rep('<p class="lead rv" style="margin-top:22px">Dit zijn grote organisaties, maar het recept is voor jouw bedrijf hetzelfde: eerst begrijpen wat klanten nodig hebben, dan bouwen. Drie projecten helemaal uitgelegd, daaronder vier kort. Klik op de kleine beelden om meer te zien.</p>',
    '<p class="lead rv" style="margin-top:22px">Grote namen, hetzelfde recept als voor jouw bedrijf: eerst uitzoeken waar mensen vastlopen, dan pas bouwen. Drie projecten helemaal uitgelegd, daaronder vier kort.</p>')

# ---------------- AANPAK ----------------
rep('<p class="lead rv" style="margin-top:22px">Drie stappen, altijd in deze volgorde. Je begint klein en met een vaste prijs. Doorgaan beslis je pas als je hebt gezien wat je krijgt.</p>',
    '<p class="lead rv" style="margin-top:22px">Drie stappen, altijd in deze volgorde. Je weet vooraf wat het kost en wanneer het klaar is, en je levert zelf bijna niets aan.</p>')
rep('<div class="why rv"><h4>Eén persoon, van eerste gesprek tot live</h4><p>Geen overdracht tussen designer en bouwer, geen accountmanager. Je praat met degene die het maakt.</p></div>',
    '<div class="why rv"><h4>Eén persoon, van eerste gesprek tot live</h4><p>Geen overdracht tussen designer en bouwer, geen accountmanager die het doorgeeft. Je appt de man die het maakt.</p></div>')
rep('<div class="why rv"><h4>Eerst begrijpen, dan bouwen</h4><p>Voor ik iets ontwerp kijk ik wie je klanten zijn en wat ze moeten kunnen. Dat is het verschil tussen mooi en werkend.</p></div>',
    '<div class="why rv"><h4>Eerst begrijpen, dan bouwen</h4><p>Ik kijk eerst wie je klanten zijn en waar ze afhaken. Sla je dat over, dan bouw je iets moois waar niemand op klikt.</p></div>')
rep('<div class="why rv"><h4>Je klanten snappen het in één keer</h4><p>Vijftien jaar maakte ik apps waar miljoenen Nederlanders mee moesten werken, van belastingaangifte tot bankieren. Wie iets meteen snapt, komt terug.</p></div>',
    '<div class="why rv"><h4>Je klanten snappen het in één keer</h4><p>Vijftien jaar schermen gemaakt voor miljoenen Nederlanders. Wat daar werkt, werkt ook voor een installatiebedrijf of een bakkerij.</p></div>')
rep('<div class="why rv"><h4>Vaste prijs, vaste doorlooptijd</h4><p>Je weet vooraf wat het kost en wanneer het klaar is. Geen uurtje factuurtje, geen verrassingen.</p></div>',
    '<div class="why rv"><h4>Vaste prijs, vaste doorlooptijd</h4><p>Het bedrag staat in de offerte, niet "vanaf". Wil je meer, dan kies je dat zelf uit een lijst met vaste prijzen.</p></div>')
rep('<div class="why rv"><h4>Meetbaar</h4><p>Na livegang laat ik zien wat het doet: bezoekers, aanvragen, bestellingen. Geen gevoel, maar cijfers.</p></div>',
    '<div class="why rv"><h4>Je ziet wat het doet</h4><p>Een maand na livegang zit je met de cijfers voor je: bezoekers, aanvragen, bestellingen. Geen gevoel, geen aannames.</p></div>')
rep('<div class="why rv"><h4>Alles geregeld</h4><p>Hosting, domein en onderhoud regel ik via mijn vaste partner. Jij hoeft nergens over na te denken.</p></div>',
    '<div class="why rv"><h4>Alles geregeld</h4><p>Hosting, domein, updates en beveiliging lopen via mij en mijn vaste partner. Jij krijgt één factuur en verder geen gedoe.</p></div>')
rep('<div class="step3 rv"><div class="ph">Stap 1</div><h3>Kickstart</h3><p>In één week weten we wat je nodig hebt, wat het kost en hoe het eruit gaat zien. Je krijgt een klikbaar prototype en een vaste prijs voor de bouw.</p></div>',
    '<div class="step3 rv"><div class="ph">Stap 1</div><h3>Kennismaken, 30 minuten</h3><p>Je vertelt wat je wilt en wie je klanten zijn. Ik zeg eerlijk wat het kost en of het slim is. Binnen twee werkdagen heb je een voorstel met één vast bedrag en een datum.</p></div>')
rep('<div class="step3 rv"><div class="ph">Stap 2</div><h3>Bouwen</h3><p>Ik ontwerp en bouw, in korte rondes. Je kijkt elke week mee en stuurt bij. Teksten, vindbaarheid en hosting zitten erin. Dan gaat het live.</p></div>',
    '<div class="step3 rv"><div class="ph">Stap 2</div><h3>Bouwen</h3><p>Ik ontwerp, schrijf en bouw. Elke week zie je waar we staan en stuur je bij. Teksten, vindbaarheid en hosting zitten erin, jij levert alleen je logo en je goedkeuring.</p></div>')
rep('<div class="step3 rv"><div class="ph">Stap 3</div><h3>Meten en verbeteren</h3><p>Na livegang kijken we wat het doet. Wil je blijven verbeteren, dan doen we dat met een vast aantal uren per maand op een gezamenlijke roadmap.</p></div>',
    '<div class="step3 rv"><div class="ph">Stap 3</div><h3>Live en meten</h3><p>Ik zet hem live en regel hosting en domein. Na een maand kijken we samen naar de cijfers: wat levert het op, en wat verbeteren we als eerste.</p></div>')

# ---------------- PAKKETTEN ----------------
s = h.index('<!-- PAKKETTEN -->'); e = h.index('<!-- CHECK -->')
h = h[:s] + '''<!-- PAKKETTEN -->
<section id="pakketten" class="sec wrap">
  <div class="eyebrow rv">Prijzen</div>
  <h2 class="h2 rv">Wat het kost. <span class="mark" data-mark>Zonder "vanaf".</span></h2>
  <p class="lead rv" style="margin-top:22px">Alle bedragen zijn exclusief btw en staan vast voordat we beginnen. Wil je meer dan het pakket, dan kies je dat zelf uit de lijst eronder. <a href="#check">Twijfel je welke past?</a></p>
  <div class="packs">
    <div class="pack rv">
      <div class="ph">Compact</div>
      <h3>Eén sterke pagina, of home plus drie</h3>
      <div class="meta"><span>2 weken</span><span class="price">€2.950</span></div>
      <ul><li>Drie templates</li><li>Jij levert de teksten, ik redigeer</li><li>Vindbaar in Google, meten ingericht</li></ul>
      <a class="btn ghost" href="#contact">Vraag een voorstel</a>
    </div>
    <div class="pack feat rv">
      <div class="ph">Compleet</div>
      <h3>Home plus zes pagina's, teksten inbegrepen</h3>
      <div class="meta"><span>3 weken</span><span class="price">€4.950</span></div>
      <ul><li>Vijf templates</li><li>Ik schrijf je teksten</li><li>Vindbaar, snel, meten ingericht</li></ul>
      <a class="btn" href="#contact">Vraag een voorstel</a>
    </div>
    <div class="pack rv">
      <div class="ph">Webshop of portaal</div>
      <h3>Klanten laten bestellen, boeken of inloggen</h3>
      <div class="meta"><span>5 weken</span><span class="price">€8.500</span></div>
      <ul><li>Onderzoek en prototype vooraf</li><li>Koppeling met wat je al gebruikt</li><li>Beheer en hosting geregeld</li></ul>
      <a class="btn ghost" href="#contact">Vraag een voorstel</a>
    </div>
    <div class="pack rv">
      <div class="ph">App</div>
      <h3>iOS en Android, van idee tot in de store</h3>
      <div class="meta"><span>6 tot 10 weken</span><span class="price">€12.500</span></div>
      <ul><li>Getest met echte gebruikers</li><li>Volgens de regels van Apple en Google</li><li>Bouw, test en publicatie</li></ul>
      <a class="btn ghost" href="#contact">Vraag een voorstel</a>
    </div>
  </div>

  <div class="pricelist rv">
    <div class="pl-head">Wil je meer? Dat heeft ook een vaste prijs.</div>
    <ul>
      <li><span>Extra pagina op een bestaand template</span><b>€175</b></li>
      <li><span>Extra template</span><b>€450</b></li>
      <li><span>Teksten laten schrijven</span><b>€150 per pagina</b></li>
      <li><span>Tweede taal</span><b>€900</b></li>
      <li><span>Koppeling met je boekhouding, kassa of CRM</span><b>vanaf €750</b></li>
      <li><span>Hosting, updates en kleine wijzigingen</span><b>€95 per maand</b></li>
      <li><span>Elke maand verbeteren op een gezamenlijke roadmap</span><b>€750 per maand</b></li>
    </ul>
  </div>
  <p class="after-line rv"><b>Webshop, portaal of app?</b> Daar beginnen we altijd met een Kickstart van €950: één week onderzoek en een klikbaar prototype dat je aan je klanten kunt laten zien. Ga je door, dan gaat dat bedrag van de prijs af. Bij een website is een gesprek van 30 minuten genoeg.</p>
</section>

''' + h[e:]

# CSS voor de prijslijst en vier kaarten
rep('  .packs{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:22px}',
    '''  .packs{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:34px}
  .pricelist{margin-top:26px;background:var(--white);border:1px solid var(--line);border-radius:22px;padding:26px 30px}
  .pl-head{font-family:var(--hand);font-size:var(--hand-l);color:var(--pink);line-height:1;margin-bottom:16px}
  .pricelist ul{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:1fr 1fr;gap:2px 40px}
  .pricelist li{display:flex;justify-content:space-between;align-items:baseline;gap:16px;padding:11px 0;border-bottom:1px solid var(--line);font-size:var(--body)}
  .pricelist li span{color:var(--ink2)}
  .pricelist li b{font-family:var(--display);font-weight:600;white-space:nowrap}''')
rep('  .kick-line{display:flex;gap:18px;align-items:center;margin-top:36px;background:var(--white);border:2px solid var(--ink);border-radius:18px;padding:18px 22px}\n  .kick-line .kick-badge{flex-shrink:0;font-family:var(--hand);font-weight:600;font-size:var(--hand-m);line-height:1;background:var(--note);color:var(--note-ink);padding:10px 14px;border-radius:12px;transform:rotate(-2deg)}\n  .kick-line div:last-child{color:var(--ink2)} .kick-line b{color:var(--ink);font-weight:600}\n', '')
rep('    .packs{grid-template-columns:1fr}', '    .packs{grid-template-columns:1fr 1fr}\n    .pricelist ul{grid-template-columns:1fr}')
rep('    .kick-line{flex-direction:column;align-items:flex-start}', '    .packs{grid-template-columns:1fr}\n    .pricelist{padding:20px 22px}')
rep('  .pack h3{font-size:var(--h4);margin:4px 0 12px}', '  .pack h3{font-size:20px;line-height:1.25;margin:4px 0 12px}')
rep('  .pack li{display:flex;gap:11px;font-size:var(--body);align-items:flex-start}', '  .pack li{display:flex;gap:10px;font-size:var(--small);align-items:flex-start}')
rep('  .pack{background:var(--white);border:1px solid var(--line);border-radius:24px;padding:32px 30px;', '  .pack{background:var(--white);border:1px solid var(--line);border-radius:22px;padding:26px 24px;')

# ---------------- CHECK: budget en uitkomst ----------------
rep('<button class="opt" data-v="b1">Tot €5.000</button>\n          <button class="opt" data-v="b2">€5.000 tot €10.000</button>\n          <button class="opt" data-v="b3">€10.000 tot €25.000</button>',
    '<button class="opt" data-v="b1">Tot €3.000</button>\n          <button class="opt" data-v="b2">€3.000 tot €6.000</button>\n          <button class="opt" data-v="b3">€6.000 tot €15.000</button>')

js_s = h.index("  var L={website:'een website'")
js_e = h.index("    window.__check={summary:")
h = h[:js_s] + '''  var L={website:'een website',webapp:'een webshop of webapp',app:'een app',weetniet:'iets nieuws'};
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
      ex=pk.n+' kost '+pk.p+' exclusief btw en staat in '+pk.t+' live. Dat bedrag is het bedrag: wil je later meer pagina\\'s of een tweede taal, dan kies je dat zelf uit de prijslijst.';
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
''' + h[js_e:]
rep("pk:(a[0]==='weetniet'?'Kickstart':(pk?pk.n:''))};", "pk:(a[0]==='weetniet'?'Nog onbekend':(pk?pk.n+' ('+pk.p+')':''))};")

# ---------------- CONTACT ----------------
rep('<p class="lead">Dertig minuten, online of bij jou aan tafel. Vertel wat je wilt maken en waar je tegenaan loopt. Je gaat sowieso weg met een eerlijk advies, ook als dat is: doe het (nog) niet.</p>',
    '<p class="lead">Dertig minuten, online of bij jou aan tafel. Je krijgt een eerlijk advies en binnen twee werkdagen een voorstel met één vast bedrag en een opleverdatum. Ook als mijn advies is: doe het nu even niet.</p>')

open(p, 'w').write(h)
print('index klaar')

# ---------------- artikel: prijzen gelijktrekken ----------------
f = R + '/kennis/wat-kost-een-website-laten-maken.html'
art = open(f).read()
old = '<p>Een website bij mij begint <span class="mark">vanaf 3.950 euro</span> en staat in twee tot drie weken live. Ontwerp, bouw, teksten, vindbaarheid, meten en hosting zitten erin. Twijfel je of dat past? Begin met een <a href="/#pakketten">Kickstart</a>: in één week weet je precies wat je nodig hebt en wat het kost, voor 950 euro die verrekend wordt als je doorgaat.</p>'
new = '<p>Bij mij kost een compacte site <span class="mark">2.950 euro</span> en een complete site van zeven pagina\'s inclusief teksten <span class="mark">4.950 euro</span>. Geen "vanaf": dat bedrag staat in de offerte. Wil je later meer pagina\'s of een tweede taal, dan staat daar ook een vaste prijs op. <a href="/#pakketten">Alle prijzen staan op de site</a>.</p>'
if old in art:
    art = art.replace(old, new); open(f, 'w').write(art); print('artikel bijgewerkt')
else:
    print('LET OP: artikelblok niet gevonden')

g = R + '/_build/gen_kennis.py'; s2 = open(g).read()
if old in s2:
    open(g, 'w').write(s2.replace(old, new)); print('generator bijgewerkt')
