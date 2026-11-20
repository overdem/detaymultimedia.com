// Sends a push notification (ntfy) when a client opens a presentation page.
// Secrets live in environment variables, never in this public repo:
// NTFY_TOPIC (push), RESEND_API_KEY + NOTIFY_EMAIL (e-mail copy), NOTIFY_FROM (optional sender).

const PAGES = {
  'sahinler-simit-evi-ornek': 'Şahinler Simit Evi',
  'beyzade-pide-lahmacun-ornek': 'Beyzade Pide & Lahmacun',
  'ayhan-cicekcilik-ornek': 'Ayhan Çiçekçilik',
  'kuzey-cicekcilik-ornek': 'Kuzey Çiçekçilik',
  'sayka-ornek': 'Şayka Balık & Meze',
  'sevket-24-kasim': 'Şevket Steakhouse',
};

function device(ua = '') {
  if (/iPhone/i.test(ua)) return 'iPhone';
  if (/iPad/i.test(ua)) return 'iPad';
  if (/Android/i.test(ua)) return 'Android';
  if (/Macintosh/i.test(ua)) return 'Mac';
  if (/Windows/i.test(ua)) return 'Windows';
  return 'Bilinmeyen cihaz';
}

export async function POST(request) {
  const topic = process.env.NTFY_TOPIC;
  if (!topic) return new Response('not configured', { status: 204 });

  let page = '';
  try { page = String((await request.json()).sayfa || ''); } catch {}
  if (!PAGES[page]) return new Response(null, { status: 204 });

  const h = request.headers;
  const city = decodeURIComponent(h.get('x-vercel-ip-city') || '') || 'şehir bilinmiyor';
  const time = new Date().toLocaleTimeString('tr-TR', { timeZone: 'Europe/Istanbul', hour: '2-digit', minute: '2-digit' });

  const r = await fetch('https://ntfy.sh', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      topic,
      title: `${PAGES[page]} sunumu açıldı`,
      message: `${time} · ${city} · ${device(h.get('user-agent') || '')}`,
      tags: ['eyes'],
      click: `https://sunum.detaymultimedia.com/${page}/`,
    }),
  }).catch(() => null);

  // E-mail copy through Resend (domain motoron.com.tr is verified there).
  let m = null;
  if (process.env.RESEND_API_KEY && process.env.NOTIFY_EMAIL) {
    const title = `${PAGES[page]} sunumu açıldı`;
    const info = `${time} · ${city} · ${device(h.get('user-agent') || '')}`;
    const link = `https://sunum.detaymultimedia.com/${page}/`;
    m = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: { Authorization: `Bearer ${process.env.RESEND_API_KEY}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        from: process.env.NOTIFY_FROM || 'Detay Sunum <bildirim@motoron.com.tr>',
        to: [process.env.NOTIFY_EMAIL],
        subject: title,
        text: `${title}\n${info}\n${link}`,
        html: `<p><b>${title}</b></p><p>${info}</p><p><a href="${link}">${link}</a></p>`,
      }),
    }).catch(() => null);
  }

  const ok = (r && r.ok) || (m && m.ok);
  return new Response(null, { status: ok ? 202 : 502, headers: { 'x-push': String(r ? r.status : 0), 'x-mail': String(m ? m.status : 0) } });
}
