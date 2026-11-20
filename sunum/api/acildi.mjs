// Sends a push notification (ntfy) when a client opens a presentation page.
// The ntfy topic (NTFY_TOPIC) and the e-mail address (NOTIFY_EMAIL) live in environment variables, never in this public repo.

const PAGES = {
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

  // E-mail copy via FormSubmit (free; the first message asks the address owner to confirm once).
  let m = null;
  if (process.env.NOTIFY_EMAIL) {
    m = await fetch(`https://formsubmit.co/ajax/${process.env.NOTIFY_EMAIL}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Accept: 'application/json', Referer: 'https://sunum.detaymultimedia.com/' },
      body: JSON.stringify({
        _subject: `${PAGES[page]} sunumu açıldı`,
        _template: 'box',
        _captcha: 'false',
        Sayfa: `https://sunum.detaymultimedia.com/${page}/`,
        Bilgi: `${time} · ${city} · ${device(h.get('user-agent') || '')}`,
      }),
    }).catch(() => null);
  }

  const ok = (r && r.ok) || (m && m.ok);
  return new Response(null, { status: ok ? 202 : 502, headers: { 'x-push': String(r ? r.status : 0), 'x-mail': String(m ? m.status : 0) } });
}
