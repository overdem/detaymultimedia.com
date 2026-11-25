# tasarim/kalidna-otel-bozcaada.md — lacivert/ekru/çam/kum/deniz, Bellefair + Sarabun + Corinthia, ekru daire imza + çam iğnesi çizgileri
TEL = '0546 213 93 38'; ADR = 'Alaybey, Kumkuyu Mevkii · Bozcaada'
PH = dict(bahce='bahce.png', oda='oda.png', kahvalti='kahvalti.png')
CSS = """
.s{background:var(--ekru);color:var(--lacivert);font-family:var(--font-govde);text-align:center}
.t{font:400 120px/1.05 var(--font-baslik);letter-spacing:.08em;text-transform:uppercase}
.lab{font:600 21px var(--font-govde);letter-spacing:.32em;text-transform:uppercase}
.sc{font:700 104px/1 var(--font-vurgu);color:var(--deniz)}
.bd{font:400 30px/1.5 var(--font-govde)}
.disc{position:absolute;border-radius:50%;background:var(--ekru);display:flex;flex-direction:column;align-items:center;justify-content:center}
.rule{width:140px;height:1.5px;background:currentColor;margin:22px auto}
.pine{position:absolute;width:160px;height:90px}
.r .t{font-size:78px}.r .sc{font-size:80px}.r .bd{font-size:24px}
"""
PINE = '<svg class="pine" viewBox="0 0 160 90" style="{}"><g stroke="#3D5A45" stroke-width="2.5" fill="none" stroke-linecap="round"><path d="M10 80 L150 10"/>' + ''.join(f'<path d="M{20+i*16} {75-i*8} l-6 -16 M{20+i*16} {75-i*8} l14 4"/>' for i in range(8)) + '</g></svg>'
def s1(P): return f"""<div class="s"><div class="ph" style="background-image:url('{P(PH['bahce'])}')"></div>
<div class="disc" style="width:520px;height:520px;left:280px;bottom:70px"><div class="t" style="font-size:96px">Kalidna</div><div class="rule"></div><div class="lab">Otel · Bozcaada</div></div></div>"""
def s2(P): return f"""<div class="s">{PINE.format('left:70px;top:70px')}{PINE.format('right:70px;bottom:70px;transform:rotate(180deg)')}<div style="position:absolute;left:110px;right:110px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center">
<div class="sc">çamların gölgesinde</div><div class="t" style="margin-top:40px;font-size:104px">bir kahve molası</div><div class="rule" style="margin:60px auto"></div>
<div class="bd" style="font-size:34px">Kumkuyu’da bahçeli, aile işletmesi bir otel. Kafa dinlemek için gelen misafirlerimiz kendini evinde hissediyor.</div></div></div>"""
def s3(P): return f"""<div class="s" style="background:var(--lacivert);color:var(--ekru)"><div class="ph" style="background-image:url('{P(PH['oda'])}');bottom:430px"></div>
<div style="position:absolute;left:80px;right:80px;bottom:90px"><div class="t" style="font-size:92px;color:var(--ekru)">Ferah ve temiz</div><div class="bd" style="margin-top:14px">Aydınlık odalar, aile odaları, sessiz geceler.</div></div></div>"""
def s4(P): return f"""<div class="s" style="background:var(--kum)"><div class="ph" style="background-image:url('{P(PH['kahvalti'])}');inset:70px 70px 360px 70px"></div>
<div style="position:absolute;left:80px;right:80px;bottom:90px"><div class="sc" style="color:var(--lacivert)">ada sabahı</div><div class="bd" style="margin-top:14px">Bahçede kahvaltı, ardından Ayazma ya da Sulubahçe yolu.</div></div></div>"""
def s5(P): return f"""<div class="s" style="background:var(--cam);color:var(--ekru)"><div class="disc" style="width:820px;height:820px;left:130px;top:265px;color:var(--lacivert)">
<div class="lab">sizi bekliyoruz</div><div class="t" style="font-size:118px;margin-top:26px">Kalidna</div><div class="lab" style="margin-top:6px">Otel · Bozcaada</div><div class="rule"></div><div class="bd" style="font-size:27px">{ADR}</div><div style="font:400 64px var(--font-baslik);margin-top:18px">{TEL}</div><div class="bd" style="font-size:23px;margin-top:6px">WhatsApp’tan da yazabilirsiniz</div></div></div>"""
def post(P): return f"""<div class="s"><div class="ph" style="background-image:url('{P(PH['bahce'])}')"></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:500px;background:linear-gradient(180deg,rgba(38,50,78,0),rgba(38,50,78,.93) 58%)"></div>
<div style="position:absolute;left:0;right:0;bottom:90px;color:var(--ekru)"><div class="sc" style="color:var(--ekru)">günaydın Bozcaada</div><div class="lab" style="margin-top:18px">Bahçede kahve · Kalidna Otel</div></div></div>"""
def ov(t=None, sc=None, bd=None):
    a = f'<div class="t">{t}</div>' if t else ''
    c = f'<div class="sc">{sc}</div>' if sc else ''
    b = f'<div class="bd" style="margin-top:10px">{bd}</div>' if bd else ''
    return f'<div class="s r" style="background:transparent"><div style="position:absolute;left:60px;right:60px;bottom:140px;background:rgba(239,232,226,.95);border-radius:300px;padding:50px 40px">{c}{a}{b}</div></div>'
CFG = dict(
    slug='kalidna-otel-bozcaada', name='Kalidna Otel Bozcaada',
    fonts_url='https://fonts.googleapis.com/css2?family=Bellefair&family=Sarabun:wght@400;600&family=Corinthia:wght@400;700&display=swap',
    tokens='--lacivert:#26324E;--ekru:#EFE8E2;--cam:#3D5A45;--kum:#D9C8AE;--deniz:#4A7891;--font-baslik:"Bellefair",serif;--font-govde:"Sarabun",sans-serif;--font-vurgu:"Corinthia",cursive;--zemin:#EFE8E2',
    css=CSS, slides=[s1, s2, s3, s4, s5], post=post,
    reel=[(PH['bahce'], ov('Kalidna', 'çamların gölgesinde')), (PH['oda'], ov('Ferah ve temiz', None, 'Aydınlık odalar, sessiz geceler')), (PH['kahvalti'], ov(None, 'ada sabahı', 'Bahçede kahvaltı')), (PH['bahce'], ov('Kalidna', None, f'{ADR}<br>{TEL}'))],
    page=dict(
        vars='  color-scheme: light;\n  --bg: #EFE8E2;\n  --panel: #F8F4F0;\n  --line: #d6cbbf;\n  --text: #26324E;\n  --muted: #4d5568;\n  --accent: #26324E;\n  --accent-ink: #EFE8E2;\n  --display: "Bellefair", serif;\n  --display-w: 400;\n  --body: "Sarabun", sans-serif;\n  --vurgu: "Corinthia", cursive;',
        extra_css='h1 em { font-family: var(--vurgu); font-style: normal; font-weight: 700; color: #4A7891; font-size: 1.3em; display: block; }\n.shot { border-radius: 16px; }\n.kimlik { font-size: 12px; color: #4d5568; margin: 0; }\n.motif { width: 46px; height: 46px; border-radius: 50%; border: 1.5px solid #26324E; margin: 0 auto; }\n',
        motif='<div class="motif" aria-hidden="true"></div>',
        lede='Haftalık paylaşımların nasıl görüneceğini göstermek için hazırladığımız kısa bir reels, beş karelik bir karusel ve tek gönderi; logonuzun laciverti ve ekru dairesi, bahçenizdeki çam gölgesiyle.',
        reel_meta='12 sn · dikey',
        reel_note='Bahçe, oda, kahvaltı ve iletişim. Video sessizdir; müzik Instagram’da paylaşırken eklenir.',
        alts=['Kalidna Otel, Bozcaada.', 'Çamların gölgesinde bir kahve molası: Kumkuyu’da bahçeli aile işletmesi.', 'Ferah ve temiz: aydınlık odalar, aile odaları, sessiz geceler.', 'Ada sabahı: bahçede kahvaltı.', f'Sizi bekliyoruz: {ADR} · {TEL}'],
        post_alt='Günaydın Bozcaada: bahçede kahve. Kalidna Otel.',
        post_note='“Kalidna’nın gölgesinde bir kahve molası” Instagram paylaşımınızdan; bahçe, aile işletmesi ve temiz odalar misafir yorumlarından; adres ve telefon Google Haritalar kaydınızdan alındı. Renkler logonuzdan.',
        music=[('Sakin akustik', 'Aramaya “calm acoustic morning” yazın. Bahçe kareleri için.'), ('Ege ezgisi', 'Aramaya “aegean instrumental” yazın. Ada havası.'), ('Kuş sesi + piyano', 'Aramaya “piano birds” yazın. Kahvaltı karesi için.')],
        caps=[('reel', 'Reels', f'Çamların gölgesinde kahve, ferah odalar, sakin bir ada sabahı. 🌲☕️\nBozcaada’da kafa dinlemek için.\n\n📍 {ADR}\n📞 {TEL}\n\n#KalidnaBozcaada #Bozcaada #butikotel #adatatili'),
              ('kar', 'Karusel', f'Bozcaada’da kendini evinde hisset. 🤍\nKumkuyu’da bahçeli, aile işletmesi bir otel: çam gölgesi, aydınlık odalar, bahçede kahvaltı.\nAda planın için kaydet. 👇\n\n📍 {ADR}\n📞 {TEL}\n\n#KalidnaBozcaada #Bozcaada #Çanakkale'),
              ('post', 'Tek gönderi', 'Günaydın Bozcaada! ☀️\nBahçede ilk kahve hazır; sen kahveni nasıl içersin? 👇\n\n#KalidnaBozcaada #Bozcaada')],
        sign='<p class="kimlik">Renkler Instagram’daki logonuzdan alındı; yazı-imza logo dosyanız gelene kadar öneridir.</p>',
    ),
)
