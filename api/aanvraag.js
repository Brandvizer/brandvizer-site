// Vercel serverless function: ontvangt een aanvraag uit de pakketkiezer en
// stuurt twee mails via Resend: één naar Rudolf, één bevestiging naar de klant.
//
// Vereist in Vercel (Settings > Environment Variables):
//   RESEND_API_KEY   je Resend API key
//   MAIL_TO          (optioneel) waar aanvragen heen gaan, standaard rudolf@brandvizer.nl
//   MAIL_FROM        (optioneel) afzender, standaard "Rudolf van der Velde <rudolf@brandvizer.nl>"
//                    Werkt pas als brandvizer.nl in Resend geverifieerd is.

const MAIL_TO = process.env.MAIL_TO || 'rudolf@brandvizer.nl';
const MAIL_FROM = process.env.MAIL_FROM || 'Rudolf van der Velde <rudolf@brandvizer.nl>';

function esc(s) {
  return String(s || '').replace(/[&<>"']/g, function (c) {
    return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
  });
}
function nl2br(s) { return esc(s).replace(/\n/g, '<br>'); }

function rows(pairs) {
  return pairs.filter(function (p) { return p[1]; }).map(function (p) {
    return '<tr><td style="padding:6px 14px 6px 0;color:#6B7686;white-space:nowrap;vertical-align:top">' + esc(p[0]) + '</td><td style="padding:6px 0;color:#0F1B2D">' + nl2br(p[1]) + '</td></tr>';
  }).join('');
}

function shell(title, inner) {
  return '<!doctype html><html lang="nl"><body style="margin:0;background:#F3F6F8;font-family:-apple-system,Segoe UI,Helvetica,Arial,sans-serif;color:#0F1B2D">' +
    '<div style="max-width:600px;margin:0 auto;padding:32px 20px">' +
    '<div style="font-weight:800;font-size:20px;letter-spacing:-.02em;margin-bottom:18px"><span style="display:inline-block;width:12px;height:12px;background:#FF3D7F;border-radius:3px;transform:rotate(12deg);margin-right:8px"></span>Brandvizer</div>' +
    '<div style="background:#fff;border:1px solid rgba(15,27,45,.12);border-radius:18px;padding:26px 28px;font-size:16px;line-height:1.55">' +
    '<h1 style="font-size:22px;margin:0 0 14px;letter-spacing:-.02em">' + esc(title) + '</h1>' + inner + '</div>' +
    '<p style="font-size:13px;color:#6B7686;margin-top:16px">Brandvizer · Rudolf van der Velde · Vaassen · rudolf@brandvizer.nl · +31 6 43 42 60 82</p>' +
    '</div></body></html>';
}

async function send(payload, key) {
  const r = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: { 'Authorization': 'Bearer ' + key, 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });
  if (!r.ok) { const t = await r.text(); throw new Error('Resend ' + r.status + ': ' + t); }
  return r.json();
}

module.exports = async function (req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') return res.status(204).end();
  if (req.method !== 'POST') return res.status(405).json({ ok: false, error: 'Alleen POST' });

  const key = process.env.RESEND_API_KEY;
  if (!key) return res.status(500).json({ ok: false, error: 'RESEND_API_KEY ontbreekt' });

  let b = req.body;
  if (typeof b === 'string') { try { b = JSON.parse(b); } catch (e) { b = {}; } }
  b = b || {};

  // Honeypot: echte mensen vullen dit veld niet in
  if (b.website) return res.status(200).json({ ok: true });

  const name = String(b.name || '').trim().slice(0, 120);
  const email = String(b.email || '').trim().slice(0, 200);
  const company = String(b.company || '').trim().slice(0, 160);
  const phone = String(b.phone || '').trim().slice(0, 40);
  const note = String(b.note || '').trim().slice(0, 2000);
  const days = String(b.days || '').slice(0, 80);
  const part = String(b.part || '').slice(0, 120);
  const where = String(b.where || '').slice(0, 60);
  const pk = String(b.pk || '').slice(0, 60);
  const diag = String(b.diag || '').slice(0, 400);
  const summary = String(b.summary || '').slice(0, 1200);

  if (!name || !email || email.indexOf('@') < 0) {
    return res.status(400).json({ ok: false, error: 'Naam en een geldig e-mailadres zijn nodig' });
  }

  const subject = 'Nieuwe aanvraag: ' + (company || name) + (pk ? ' (' + pk + ')' : '');
  const toRudolf = shell(subject,
    '<table style="border-collapse:collapse;font-size:15px">' +
    rows([['Naam', name], ['Bedrijf', company], ['E-mail', email], ['Telefoon', phone]]) +
    '</table>' +
    '<h2 style="font-size:15px;margin:22px 0 8px;color:#FF3D7F">Wanneer past het</h2>' +
    '<table style="border-collapse:collapse;font-size:15px">' + rows([['Dagen', days || 'geen voorkeur'], ['Dagdeel', part || 'geen voorkeur'], ['Waar', where || 'online']]) + '</table>' +
    '<h2 style="font-size:15px;margin:22px 0 8px;color:#FF3D7F">Uitkomst van de check</h2>' +
    '<div style="font-size:15px;white-space:pre-line">' + esc(summary) + '</div>' +
    (pk ? '<p style="font-size:15px;margin:10px 0 0"><b>Pakket:</b> ' + esc(pk) + '</p>' : '') +
    (diag ? '<p style="font-size:15px;margin:6px 0 0"><b>Inschatting:</b> ' + esc(diag) + '</p>' : '') +
    (note ? '<h2 style="font-size:15px;margin:22px 0 8px;color:#FF3D7F">Vooraf goed om te weten</h2><div style="font-size:15px">' + nl2br(note) + '</div>' : '') +
    '<p style="margin-top:24px"><a href="mailto:' + esc(email) + '?subject=' + encodeURIComponent('Re: kennismaking Brandvizer') + '" style="display:inline-block;background:#0F1B2D;color:#fff;text-decoration:none;padding:12px 18px;border-radius:999px;font-weight:600">Antwoord ' + esc(name.split(' ')[0]) + '</a></p>'
  );

  const first = name.split(' ')[0];
  const toClient = shell('Gelukt, ' + first + '. Ik kom bij je terug.',
    '<p>Bedankt voor je aanvraag. Ik lees hem vandaag nog en stuur je binnen één werkdag twee of drie momenten voor een gesprek van 30 minuten' + (where ? ' (' + esc(where.toLowerCase()) + ')' : '') + '.</p>' +
    '<p>Dit heb je ingevuld, zodat je het nog even terug kunt lezen:</p>' +
    '<div style="background:#F3F6F8;border-radius:12px;padding:14px 16px;font-size:15px;white-space:pre-line">' + esc(summary) + (pk ? '\nPakket: ' + esc(pk) : '') + '</div>' +
    (diag ? '<p style="margin-top:14px"><b>Mijn eerste inschatting:</b> ' + esc(diag) + '</p>' : '') +
    '<p style="margin-top:18px">Wil je in de tussentijd al iets kwijt? Antwoord gewoon op deze mail, of bel me op 06 43 42 60 82.</p>' +
    '<p style="margin-top:18px">Groetjes,<br>Rudolf</p>'
  );

  try {
    await send({ from: MAIL_FROM, to: [MAIL_TO], reply_to: email, subject: subject, html: toRudolf }, key);
    await send({ from: MAIL_FROM, to: [email], reply_to: MAIL_TO, subject: 'Je aanvraag bij Brandvizer is binnen', html: toClient }, key);
    return res.status(200).json({ ok: true });
  } catch (e) {
    console.error(e);
    return res.status(502).json({ ok: false, error: 'Versturen mislukt' });
  }
};
