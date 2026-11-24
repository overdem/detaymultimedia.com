# tasarim/cream-coffee-kitchen.md — kahve/krem/latte/kum/gün batımı, Petrona + Source Sans 3 + Great Vibes, ince dalga çizgisi + yuvarlak kart
TEL = '0539 925 72 96'; ADR = 'Zakkum Sk. No:7 · Boğazkent, Kepez Sahil'
PH = dict(sahil='sahil.png', filtre='filtre.png', gunbatimi='gunbatimi.png')
WAVE = '<svg width="360" height="24" viewBox="0 0 360 24" xmlns="http://www.w3.org/2000/svg"><path d="M0 12 Q 22.5 0 45 12 T 90 12 T 135 12 T 180 12 T 225 12 T 270 12 T 315 12 T 360 12" fill="none" stroke="currentColor" stroke-width="3"/></svg>'
CSS = """
.s{background:var(--krem);color:var(--kahve);font-family:var(--font-govde);text-align:center}
.t{font:800 150px/.95 var(--font-baslik);letter-spacing:-.01em}
.lab{font:600 22px var(--font-govde);letter-spacing:.34em;text-transform:uppercase}
.sc{font:400 104px/1 var(--font-vurgu);color:var(--latte)}
.bd{font:400 31px/1.45 var(--font-govde)}
.card{position:absolute;background:var(--krem);border-radius:24px}
.wave{color:var(--latte);display:flex;justify-content:center}
.r .t{font-size:100px}.r .sc{font-size:78px}.r .bd{font-size:24px}.r .lab{font-size:17px}
"""
def s1(P): return f"""<div class="s"><div class="ph" style="background-image:url('{P(PH['sahil'])}');bottom:450px;border-radius:0 0 36px 36px"></div>
<div style="position:absolute;left:0;right:0;bottom:70px"><div class="lab">Kepez Sahili · Çanakkale</div><div class="t" style="margin-top:22px">Cream</div><div class="lab" style="margin-top:8px;letter-spacing:.5em"><span lang="en">Coffee &amp; Kitchen</span></div><div class="wave" style="margin-top:28px">{WAVE}</div></div>
<div style="position:absolute;right:70px;top:700px;transform:rotate(-6deg)"><div class="sc" style="color:var(--krem);font-size:96px;text-shadow:0 2px 14px rgba(75,43,37,.45)">denize sıfır</div></div></div>"""
def s2(P): return f"""<div class="s" style="background:var(--kahve);color:var(--krem)"><div class="ph" style="background-image:url('{P(PH['sahil'])}');opacity:.92"></div>
<div class="card" style="left:80px;right:80px;bottom:80px;padding:48px 40px;color:var(--kahve)"><div class="lab" style="color:var(--kahve)">Hasır gölgelik altında</div><div class="t" style="font-size:112px;margin-top:16px">Serpme kahvaltı</div><div class="bd" style="margin-top:14px">Dalga sesi eşliğinde, denizin hemen kenarında.</div></div></div>"""
def s3(P): return f"""<div class="s" style="background:var(--kum)"><div class="ph" style="background-image:url('{P(PH['filtre'])}');left:80px;right:80px;top:80px;bottom:420px;border-radius:24px"></div>
<div style="position:absolute;left:0;right:0;bottom:90px"><div class="sc" style="color:var(--kahve);font-size:92px">yavaş demlenir</div><div class="t" style="font-size:118px;margin-top:4px">Filtre kahve</div><div class="bd" style="margin-top:12px">Misafir yorumlarında övülen fincan.</div></div></div>"""
def s4(P): return f"""<div class="s" style="background:var(--kahve);color:var(--krem)"><div class="ph" style="background-image:url('{P(PH['gunbatimi'])}');bottom:430px"></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:430px;padding:56px 80px"><div class="lab" style="color:var(--latte)">Sabahın ilk çayından</div><div class="t" style="font-size:118px;margin-top:18px;color:var(--krem)">gün batımına</div><div class="wave" style="margin-top:26px">{WAVE}</div></div></div>"""
def s5(P): return f"""<div class="s" style="background:var(--kum)"><div style="position:absolute;left:90px;right:90px;top:200px">
<div class="lab">Rezervasyon</div><div class="t" style="font-size:190px;margin-top:30px">Cream</div><div class="lab" style="margin-top:8px;letter-spacing:.5em"><span lang="en">Coffee &amp; Kitchen</span></div>
<div class="wave" style="margin:56px 0">{WAVE}</div><div class="sc" style="color:var(--kahve);font-size:90px">masanız hazır</div>
<div class="bd" style="margin-top:36px">Zakkum Sk. No:7, Boğazkent · Kepez Sahil<br>Sabahtan gün batımına</div><div style="font:800 64px var(--font-baslik);margin-top:34px">{TEL}</div></div></div>"""
def post(P): return f"""<div class="s"><div class="ph" style="background-image:url('{P(PH['gunbatimi'])}')"></div>
<div class="card" style="left:150px;right:150px;bottom:110px;padding:40px 30px"><div class="sc" style="color:var(--kahve);font-size:92px">iyi akşamlar</div><div class="lab" style="margin-top:16px">Gün batımı Cream’de · Kepez</div></div></div>"""
def ov(t=None, sc=None, bd=None):
    a = f'<div class="t">{t}</div>' if t else ''
    c = f'<div class="sc" style="color:var(--kahve)">{sc}</div>' if sc else ''
    b = f'<div class="bd" style="margin-top:10px">{bd}</div>' if bd else ''
    return f'<div class="s r" style="background:transparent"><div class="card" style="left:60px;right:60px;bottom:140px;padding:40px 30px;background:rgba(246,240,231,.95)">{c}{a}{b}</div></div>'
CFG = dict(
    slug='cream-coffee-kitchen', name='Cream Coffee & Kitchen',
    fonts_url='https://fonts.googleapis.com/css2?family=Petrona:wght@600;800&family=Source+Sans+3:wght@400;600&family=Great+Vibes&display=swap',
    tokens='--kahve:#4B2B25;--krem:#F6F0E7;--latte:#C8A27C;--kum:#EADBC8;--gunbatimi:#D98C5F;--font-baslik:"Petrona",serif;--font-govde:"Source Sans 3",sans-serif;--font-vurgu:"Great Vibes",cursive;--zemin:#F6F0E7',
    css=CSS, slides=[s1, s2, s3, s4, s5], post=post,
    reel=[(PH['sahil'], ov('Cream', 'denize sıfır')), (PH['filtre'], ov('Filtre kahve', 'yavaş demlenir')), (PH['gunbatimi'], ov('Gün batımı', None, 'Sabahın ilk çayından akşama')), (PH['sahil'], ov('Cream', 'masanız hazır', f'{ADR}<br>{TEL}'))],
    page=dict(
        vars='  color-scheme: light;\n  --bg: #F6F0E7;\n  --panel: #FBF8F3;\n  --line: #dccbb6;\n  --text: #4B2B25;\n  --muted: #6a4a42;\n  --accent: #4B2B25;\n  --accent-ink: #F6F0E7;\n  --display: "Petrona", serif;\n  --display-w: 800;\n  --body: "Source Sans 3", sans-serif;\n  --vurgu: "Great Vibes", cursive;',
        extra_css='h1 em { font-family: var(--vurgu); font-style: normal; font-weight: 400; color: #8a6440; font-size: 1.25em; display: block; }\n.shot { border-radius: 24px; }\n.kimlik { font-size: 12px; color: #6a4a42; margin: 0; }\n.motif { color: #C8A27C; display: flex; justify-content: center; }\n',
        motif='<div class="motif" aria-hidden="true"><svg width="120" height="12" viewBox="0 0 120 12"><path d="M0 6 Q 7.5 0 15 6 T 30 6 T 45 6 T 60 6 T 75 6 T 90 6 T 105 6 T 120 6" fill="none" stroke="currentColor" stroke-width="2"/></svg></div>',
        lede='Haftalık paylaşımların nasıl görüneceğini göstermek için hazırladığımız kısa bir reels, beş karelik bir karusel ve tek gönderi; logonuzdaki kahve ve krem tonları, denize sıfır sabahlar ve gün batımıyla.',
        reel_meta='12 sn · dikey',
        reel_note='Hasır gölgelik altında kahvaltı, filtre kahve, gün batımı ve rezervasyon. Video sessizdir; müzik Instagram’da paylaşırken eklenir.',
        alts=['Cream Coffee & Kitchen, Kepez Sahili: denize sıfır.', 'Hasır gölgelik altında serpme kahvaltı, dalga sesi eşliğinde.', 'Filtre kahve: misafir yorumlarında övülen fincan.', 'Sabahın ilk çayından gün batımına.', f'Rezervasyon: {ADR} · Sabahtan gün batımına · {TEL}'],
        post_alt='İyi akşamlar: gün batımı Cream’de, Kepez.',
        post_note='Adres ve telefon Google Haritalar kaydınızdan; hasır gölgelik, dalga sesi ve filtre kahve misafir yorumlarından, “sabahın ilk çayından gün batımına” web sitenizden alındı.',
        music=[('Akustik deniz', 'Aramaya “acoustic beach morning” yazın. Kahvaltı karelerine uyar.'), ('Bossa nova', 'Aramaya “bossa nova” yazın. Sahil havası.'), ('Gün batımı chill', 'Aramaya “sunset chill” yazın. Akşam paylaşımları için.')],
        caps=[('reel', 'Reels', f'Kepez sahilinde, denize sıfır bir sabah. 🌊☕️\nSerpme kahvaltı, filtre kahve ve gün batımı.\n\n📍 {ADR}\n📞 {TEL}\n\n#CreamCoffeeKitchen #Çanakkale #Kepez #kahvaltı #filtrekahve'),
              ('kar', 'Karusel', f'Sabahın ilk çayından gün batımına. 🤎\nHasır gölgelik altında serpme kahvaltı, yavaş demlenen filtre kahve ve deniz.\nHafta sonu kahvaltısı için kaydet. 👇\n\n📍 {ADR}\n🌅 Sabahın ilk çayından gün batımına\n📞 {TEL}\n\n#CreamCoffeeKitchen #Çanakkale #çanakkalekahvaltı #Kepez'),
              ('post', 'Tek gönderi', 'İyi akşamlar! 🌅\nBugün gün batımı Cream’de.\nMasanı ayırt: 0539 925 72 96\n\n#CreamCoffeeKitchen #günbatımı #Çanakkale')],
        sign='<p class="kimlik">Renkler web sitenizdeki logodan; yazı-imza yerine kendi logo dosyanızı kullanırız.</p>',
    ),
)
