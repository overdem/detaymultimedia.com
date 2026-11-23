# tasarim/bizim-yaka-restaurant.md — gece/kıyı/köpük/zeytin/kum, Urbanist + Figtree + Allura, ufuk çizgisi + yarım güneş
TEL = '0505 810 00 66'; ADR = 'Kıyı AVM · Atatürk Cd. No:318 · Barbaros'
CSS = """
.s{background:var(--gece);color:var(--kopuk);font-family:var(--font-govde)}
.fade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(31,42,64,.5) 0%,rgba(31,42,64,0) 20%,rgba(31,42,64,0) 48%,rgba(31,42,64,.9) 76%,#1F2A40 100%)}
.lbl{font:700 20px var(--font-baslik);letter-spacing:.26em;text-transform:uppercase}
.sig{font:400 150px/.9 var(--font-vurgu);color:var(--kum)}
.t{font:700 76px/1.02 var(--font-baslik);letter-spacing:.06em;text-transform:uppercase}
.bd{font:400 30px/1.45 var(--font-govde)}
.hz{height:2px;background:var(--kum)}
.card{position:absolute;background:var(--kopuk);color:var(--gece);padding:40px 46px}
.card .t{color:var(--kiyi)}
.btn{display:inline-block;background:var(--zeytin);color:var(--kopuk);font:700 22px var(--font-baslik);letter-spacing:.2em;padding:14px 24px;text-transform:uppercase}
.sun{position:absolute;width:300px;height:150px;border-radius:300px 300px 0 0;background:var(--kum)}
.r .sig{font-size:110px}.r .t{font-size:54px}.r .bd{font-size:24px}.r .lbl{font-size:15px}
"""
def s1(P): return f"""<div class="s"><div class="ph" style="background-image:url('{P('edb5409e.png')}')"></div><div class="fade"></div>
<div class="lbl" style="position:absolute;left:80px;top:76px">Bizim Yaka · Kıyı AVM</div>
<div style="position:absolute;left:80px;right:80px;bottom:110px"><div class="sig">gün batımı</div><div class="hz" style="margin:26px 0 30px;width:300px"></div><div class="t">Kıyıda bir akşam</div><div class="bd" style="margin-top:16px">Deniz kenarında meze, ızgara ve uzun sohbet.</div></div></div>"""
def photo_card(P, ph, lbl, t, bd, pos='50% 50%'):
    return f"""<div class="s"><div class="ph" style="background-image:url('{P(ph)}');background-position:{pos}"></div>
<div class="card" style="left:70px;right:70px;bottom:80px"><div class="lbl" style="color:var(--zeytin)">{lbl}</div><div class="t" style="margin-top:14px">{t}</div><div class="hz" style="margin:22px 0;width:160px"></div><div class="bd">{bd}</div></div></div>"""
def s2(P): return photo_card(P, '8bd2302e.png', '01 · Meze', 'Bol çeşit', 'Haydari, fava, hamsi füme, deniz börülcesi, barbunya pilaki…')
def s3(P): return f"""<div class="s"><div class="ph" style="background-image:url('{P('3e56ab40.png')}')"></div><div class="fade"></div>
<div class="lbl" style="position:absolute;left:80px;top:76px">02 · Ara sıcak</div>
<div style="position:absolute;left:80px;right:80px;bottom:110px"><div class="sig">ahtapot</div><div class="hz" style="margin:26px 0 30px;width:300px"></div><div class="t">Izgarada</div><div class="bd" style="margin-top:16px">Zeytinyağı, limon ve maydanozla; ara sıcakların yıldızı.</div></div></div>"""
def s4(P): return photo_card(P, '5fd4e8a3.png', '03 · Izgara', 'Et de var', 'Beyti, kasap köfte, kuzu tandır, antrikot; balık kadar et sevenlere.')
def s5(P): return f"""<div class="s"><div class="sun" style="left:390px;top:300px"></div><div class="hz" style="position:absolute;left:80px;right:80px;top:450px"></div>
<div style="position:absolute;left:80px;right:80px;top:520px;text-align:center"><div class="sig" style="font-size:130px">bizim yaka</div><div class="t" style="margin-top:28px;font-size:60px">Masanız hazır</div>
<div class="bd" style="margin-top:24px">12:00’den itibaren · Kıyı AVM, Barbaros</div><div style="margin-top:46px"><span class="btn" style="font-size:34px;letter-spacing:.08em">{TEL}</span></div></div></div>"""
def post(P): return f"""<div class="s"><div class="ph" style="background-image:url('{P('edb5409e.png')}');background-size:130%;background-position:50% 30%"></div><div class="fade"></div>
<div style="position:absolute;left:80px;right:80px;bottom:110px"><div class="sig" style="font-size:130px">bu akşam</div><div class="hz" style="margin:24px 0 28px;width:300px"></div><div class="t" style="font-size:64px">Gün batımına<br>bir masa</div><div class="bd" style="margin-top:16px">Rezervasyon {TEL}</div></div></div>"""
def ov(sig, t, bd=None, lbl='Bizim Yaka · Kıyı AVM'):
    a = f'<div class="sig">{sig}</div><div class="hz" style="margin:18px 0 22px;width:220px"></div>' if sig else ''
    b = f'<div class="bd" style="margin-top:12px">{bd}</div>' if bd else ''
    return f'<div class="s r" style="background:transparent"><div class="fade"></div><div class="lbl" style="position:absolute;left:50px;top:64px">{lbl}</div><div style="position:absolute;left:50px;right:50px;bottom:130px">{a}<div class="t">{t}</div>{b}</div></div>'
CFG = dict(
    slug='bizim-yaka-restaurant', name='Bizim Yaka Restaurant',
    fonts_url='https://fonts.googleapis.com/css2?family=Urbanist:wght@500;700&family=Figtree:wght@400;600&family=Allura&display=swap',
    tokens='--gece:#1F2A40;--kiyi:#495A77;--kopuk:#F3F7F8;--zeytin:#4F772D;--kum:#CEB077;--font-baslik:"Urbanist",sans-serif;--font-govde:"Figtree",sans-serif;--font-vurgu:"Allura",cursive;--zemin:#1F2A40',
    css=CSS, slides=[s1, s2, s3, s4, s5], post=post,
    reel=[('edb5409e.png', ov('gün batımı', 'Kıyıda bir akşam')),
          ('8bd2302e.png', ov(None, 'Bol çeşit meze', 'Haydari, fava, hamsi füme…')),
          ('3e56ab40.png', ov('ahtapot', 'Izgarada')),
          ('5fd4e8a3.png', ov(None, 'Et de var', 'Beyti, kasap köfte, kuzu tandır')),
          ('edb5409e.png', ov('bizim yaka', 'Masanız hazır', f'{TEL}<br>Kıyı AVM · 12:00’den itibaren'))],
    page=dict(
        vars='  color-scheme: dark;\n  --bg: #1F2A40;\n  --panel: #27344f;\n  --line: #3d4b68;\n  --text: #F3F7F8;\n  --muted: #b9c2d0;\n  --accent: #CEB077;\n  --accent-ink: #1F2A40;\n  --display: "Urbanist", sans-serif;\n  --display-w: 700;\n  --body: "Figtree", sans-serif;\n  --vurgu: "Allura", cursive;',
        extra_css='h1 em { font-family: var(--vurgu); font-style: normal; font-weight: 400; color: #CEB077; font-size: 1.35em; display: block; }\n.motif { width: 90px; height: 45px; border-radius: 90px 90px 0 0; background: #CEB077; margin: 0 auto; box-shadow: 0 2px 0 #1F2A40, 0 4px 0 #CEB077; }\n',
        motif='<div class="motif" aria-hidden="true"></div>',
        lede='Haftalık paylaşımların nasıl görüneceğini göstermek için hazırladığımız kısa bir reels, beş karelik bir karusel ve tek gönderi; imza logonuzun el yazısı ve sitenizdeki deniz mavisi, zeytin yeşiliyle.',
        reel_meta='15 sn · dikey',
        reel_note='Gün batımı, meze çeşitleri, ızgara ahtapot ve et; 5 sahnede Bizim Yaka. Video sessizdir; müzik Instagram’da paylaşırken eklenir.',
        alts=['Gün batımı: kıyıda bir akşam. Deniz kenarında meze, ızgara ve uzun sohbet.', 'Meze: bol çeşit. Haydari, fava, hamsi füme, deniz börülcesi, barbunya pilaki.', 'Ara sıcak: ızgarada ahtapot, zeytinyağı ve limonla.', 'Izgara: et de var. Beyti, kasap köfte, kuzu tandır, antrikot.', f'Bizim Yaka: masanız hazır. 12:00’den itibaren · Kıyı AVM · {TEL}'],
        post_alt=f'Bu akşam: gün batımına bir masa. Rezervasyon {TEL}.',
        post_note='Telefon, adres ve açılış saati Google Haritalar kaydınızdan; yemek adları web sitenizden alındı.',
        music=[('Akustik gün batımı', 'Aramaya “acoustic sunset” yazın. Kıyı akşamına yakışır.'), ('Ege enstrümantal', 'Aramaya “aegean instrumental” yazın. Meze sofrası havası.'), ('Bossa nova', 'Aramaya “bossa nova evening” yazın. Rahat ve şık.')],
        caps=[('reel', 'Reels', f'Gün batarken kıyıda. 🌅\nBol çeşit meze, ızgara ahtapot ve et; Bizim Yaka’da bir akşam.\n\n📍 Kıyı AVM, Barbaros\n📞 Rezervasyon: {TEL}\n\n#BizimYaka #Çanakkale #meze #ahtapot #günbatımı'),
              ('kar', 'Karusel', f'Kıyıda bir akşam planı. 🌊\n01 Meze · 02 Ahtapot · 03 Izgara.\nArkadaşını etiketle, masayı ayırtın. 👇\n\n📍 {ADR}\n⏰ 12:00’den itibaren\n📞 {TEL}\n\n#BizimYaka #Çanakkale #çanakkalerestoran #kordon'),
              ('post', 'Tek gönderi', f'Bu akşam gün batımına bir masa. 🌅\nRezervasyon için arayın ya da yazın.\n\n📞 {TEL}\n📍 Kıyı AVM\n\n#BizimYaka #Çanakkale #günbatımı')],
    ),
)
