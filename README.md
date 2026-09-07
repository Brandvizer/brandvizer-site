# Brandvizer website

Statische site: `index.html` plus `assets/`. Geen build-stap.

## Live zetten
- Hosting: Vercel (project koppelen aan deze GitHub-repo, framework "Other", geen build command, output directory `.`)
- Push naar `main` = productie
- Domein: brandvizer.nl toevoegen in Vercel onder Settings > Domains, DNS bij de registrar aanpassen (A record 76.76.21.21 of CNAME cname.vercel-dns.com)

## Werken aan de site
- Alle CSS en JS staan in `index.html`
- Typografische schaal en kleuren staan bovenaan in `:root`
- Casebeelden in `assets/img/cases/`
- Agenda-link voor de pakketkiezer: zoek in `index.html` op `BOOKING_URL`
- Bouwscripts en context in `_build/`
