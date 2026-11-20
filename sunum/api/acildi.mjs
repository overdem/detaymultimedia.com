// Sends a push notification (ntfy) when a client opens a presentation page.
// The ntfy topic lives in the NTFY_TOPIC environment variable, never in this public repo.
// The e-mail copy is sent from the visitor's browser through FormSubmit (see the page script).

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

  const ok = r && r.ok;
  return new Response(null, { status: ok ? 202 : 502, headers: { 'x-push': String(r ? r.status : 0) } });
}
