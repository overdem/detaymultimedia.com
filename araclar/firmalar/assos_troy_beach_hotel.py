# tasarim/assos-troy-beach-hotel.md — bakır/pembe bakır/toprak/Kadırga denizi/kum, Castoro + Mukta + Alex Brush, taş sırası çizgisi + yumuşak köşe
TEL = '0543 721 71 50'; TEL2 = '0544 721 71 50'; ADR = 'Kadırga Koyu No:15 · Behram, Ayvacık'
PH = dict(kabana='kabana.png', havuz='havuz.png', liman='liman.png')
CSS = """
.s{background:var(--kum);color:var(--toprak);font-family:var(--font-govde);text-align:center}
.t{font:400 132px/1 var(--font-baslik);letter-spacing:.1em;text-transform:uppercase}
.cu{background:linear-gradient(180deg,var(--pembe_bakir),var(--bakir));-webkit-background-clip:text;background-clip:text;color:transparent}
.lab{font:600 22px var(--font-govde);letter-spacing:.36em;text-transform:uppercase}
.sc{font:400 104px/1 var(--font-vurgu);color:var(--pembe_bakir)}
.bd{font:400 31px/1.45 var(--font-govde)}
.stone{display:flex;gap:8px;justify-content:center}.stone i{display:block;height:10px;border-radius:3px;background:var(--bakir);opacity:.75}
.pic{position:absolute;background-size:cover;background-position:center;border-radius:18px}
.r .t{font-size:84px}.r .sc{font-size:78px}.r .bd{font-size:24px}.r .lab{font-size:17px}
"""
STONE = '<div class="stone"><i style="width:60px"></i><i style="width:34px"></i><i style="width:80px"></i><i style="width:46px"></i><i style="width:64px"></i></div>'
def s1(P): return f"""<div class="s"><div class="pic" style="left:60px;right:60px;top:60px;height:820px;background-image:url('{P(PH['kabana'])}')"></div>
<div style="position:absolute;left:0;right:0;top:920px"><div class="lab">Assos</div><div class="t cu" style="font-size:170px;margin-top:6px">Troy</div><div class="lab" style="margin-top:2px">Beach Hotel</div><div style="margin-top:28px">{STONE}</div></div>
<div style="position:absolute;left:0;right:0;top:770px"><div class="sc" style="color:var(--kum);text-shadow:0 2px 16px rgba(31,95,115,.6)">Kadırga Koyu</div></div></div>"""
def s2(P): return f"""<div class="s" style="background:var(--deniz);color:var(--kum)"><div class="pic" style="left:60px;right:60px;top:60px;height:860px;background-image:url('{P(PH['havuz'])}')"></div>
<div style="position:absolute;left:0;right:0;top:965px"><div class="t" style="font-size:96px;color:var(--kum)">Denize sıfır</div><div class="bd" style="margin-top:16px;color:var(--kum)">Havuz, plaj ve kabanalar aynı bahçede.</div><div style="margin-top:30px">{STONE}</div></div></div>"""
def s3(P): return f"""<div class="s" style="background:var(--deniz);color:var(--kum)"><div style="position:absolute;left:90px;right:90px;top:250px">
<div class="lab" style="color:var(--pembe_bakir)">Misafirlerimiz ne diyor?</div><div class="t" style="font-size:330px;letter-spacing:0;margin-top:40px;color:var(--kum)">4,9</div>
<div class="bd" style="margin-top:10px;font-size:36px">Google’da 1.300’ü aşkın yorum</div><div style="margin:60px 0">{STONE}</div><div class="sc">Mavi ve yeşilin buluştuğu nokta</div></div></div>"""
def s4(P): return f"""<div class="s"><div class="pic" style="left:0;right:0;top:0;height:800px;border-radius:0;background-image:url('{P(PH['liman'])}')"></div>
<div style="position:absolute;left:0;right:0;top:850px;padding:0 80px"><div class="lab" style="color:var(--bakir)">Sonbahar ve kış</div><div class="t" style="font-size:96px;margin-top:16px">Antik Liman’da</div><div class="bd" style="margin-top:16px">Kardeş otelimiz Troy Port, Assos Antik Liman’da yıl boyu açık.</div></div></div>"""
def s5(P): return f"""<div class="s"><div style="position:absolute;left:90px;right:90px;top:180px">
<div class="sc" style="color:var(--bakir)">rezervasyon</div><div class="lab" style="margin-top:40px">Assos</div><div class="t cu" style="font-size:180px">Troy</div><div class="lab">Beach Hotel</div>
<div style="margin:56px 0">{STONE}</div><div class="bd">Kadırga Koyu No:15, Behram · Ayvacık</div>
<div style="font:400 62px var(--font-baslik);margin-top:30px;letter-spacing:.06em">{TEL}</div><div class="bd" style="margin-top:22px;font-size:27px">Troy Port Hotel · Antik Liman: {TEL2}</div></div></div>"""
def post(P): return f"""<div class="s"><div class="ph" style="background-image:url('{P(PH['kabana'])}')"></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:520px;background:linear-gradient(180deg,rgba(31,95,115,0),rgba(31,95,115,.93) 55%)"></div>
<div style="position:absolute;left:0;right:0;bottom:90px;color:var(--kum)"><div class="sc" style="color:var(--kum)">yaz burada başlar</div><div class="lab" style="margin-top:18px;color:var(--kum)">Assos Troy Beach Hotel · Kadırga Koyu</div></div></div>"""
def ov(t=None, sc=None, bd=None):
    a = f'<div class="t">{t}</div>' if t else ''
    c = f'<div class="sc" style="color:var(--bakir)">{sc}</div>' if sc else ''
    b = f'<div class="bd" style="margin-top:10px">{bd}</div>' if bd else ''
    return f'<div class="s r" style="background:transparent"><div style="position:absolute;left:60px;right:60px;bottom:140px;background:rgba(248,241,234,.95);border-radius:18px;padding:40px 30px">{c}{a}{b}</div></div>'
CFG = dict(
    slug='assos-troy-beach-hotel', name='Assos Troy Beach Hotel',
    fonts_url='https://fonts.googleapis.com/css2?family=Castoro&family=Mukta:wght@400;600&family=Alex+Brush&display=swap',
    tokens='--bakir:#966638;--pembe_bakir:#D99983;--toprak:#5A422B;--deniz:#1F5F73;--kum:#F8F1EA;--font-baslik:"Castoro",serif;--font-govde:"Mukta",sans-serif;--font-vurgu:"Alex Brush",cursive;--zemin:#F8F1EA',
    css=CSS, slides=[s1, s2, s3, s4, s5], post=post,
    reel=[(PH['kabana'], ov('Troy', 'Kadırga Koyu')), (PH['havuz'], ov('Denize sıfır', None, 'Havuz, plaj ve kabanalar')), (PH['liman'], ov('Antik Liman', 'Troy Port', 'Yıl boyu açık')), (PH['kabana'], ov('Troy', 'rezervasyon', f'{ADR}<br>{TEL}'))],
    page=dict(
        vars='  color-scheme: light;\n  --bg: #F8F1EA;\n  --panel: #FCF8F4;\n  --line: #e0cdbb;\n  --text: #5A422B;\n  --muted: #6e5640;\n  --accent: #1F5F73;\n  --accent-ink: #F8F1EA;\n  --display: "Castoro", serif;\n  --display-w: 400;\n  --body: "Mukta", sans-serif;\n  --vurgu: "Alex Brush", cursive;',
        extra_css='h1 { letter-spacing: .02em; }\nh1 em { font-family: var(--vurgu); font-style: normal; font-weight: 400; color: #966638; font-size: 1.3em; display: block; }\n.eyebrow { color: #966638; }\n.shot { border-radius: 18px; }\n.kimlik { font-size: 12px; color: #6e5640; margin: 0; }\n.motif { display: flex; gap: 6px; justify-content: center; }\n.motif i { display: block; height: 7px; border-radius: 2px; background: #966638; opacity: .75; }\n',
        motif='<div class="motif" aria-hidden="true"><i style="width:30px"></i><i style="width:16px"></i><i style="width:40px"></i><i style="width:22px"></i><i style="width:32px"></i></div>',
        lede='Haftalık paylaşımların nasıl görüneceğini göstermek için hazırladığımız kısa bir reels, beş karelik bir karusel ve tek gönderi; logonuzdaki bakır tonları, Kadırga Koyu’nun mavisi ve Troy Port’un antik limanıyla.',
        reel_meta='12 sn · dikey',
        reel_note='Kabanalar, havuz, Troy Port ve rezervasyon. Video sessizdir; müzik Instagram’da paylaşırken eklenir.',
        alts=['Assos Troy Beach Hotel, Kadırga Koyu.', 'Denize sıfır: havuz, plaj ve kabanalar aynı bahçede.', 'Google’da 1.300’ü aşkın yorumla 4,9. Mavi ve yeşilin buluştuğu nokta.', 'Sonbahar ve kış: kardeş otel Troy Port, Assos Antik Liman’da yıl boyu açık.', f'Rezervasyon: {ADR} · {TEL} · Troy Port: {TEL2}'],
        post_alt='Yaz burada başlar: Assos Troy Beach Hotel, Kadırga Koyu.',
        post_note='Adres, telefon ve Google puanı Haritalar kaydınızdan; “Mavi ve yeşilin buluştuğu nokta” ve Troy Port bilgisi web sitenizden alındı. Kış aylarında karusel Troy Port’u, yaz öncesi Kadırga’yı öne çıkarır.',
        music=[('Akdeniz akustik', 'Aramaya “mediterranean acoustic” yazın. Koy ve deniz için.'), ('Chill house', 'Aramaya “summer chill house” yazın. Havuz kareleri için.'), ('Gitar instrumental', 'Aramaya “spanish guitar relax” yazın. Antik Liman akşamı için.')],
        caps=[('reel', 'Reels', f'Mavi ve yeşilin buluştuğu nokta. 🌊🌿\nKadırga Koyu’nda denize sıfır; havuz, plaj ve kabanalar.\nKışın Troy Port, Assos Antik Liman’da açık.\n\n📍 {ADR}\n📞 {TEL}\n\n#AssosTroyBeach #Assos #Kadırga #Çanakkale #denizesıfır'),
              ('kar', 'Karusel', f'Yaz Kadırga’da, kış Antik Liman’da. 🧡\nGoogle’da 1.300’ü aşkın yorumla 4,9; teşekkürler!\nYaz planın için kaydet. 👇\n\n📍 {ADR}\n📞 {TEL}\n🏛 Troy Port Hotel: {TEL2}\n\n#AssosTroyBeach #TroyPort #Assos #Ayvacık'),
              ('post', 'Tek gönderi', f'Yaz burada başlar. ☀️\nKadırga Koyu’nda yerini şimdiden ayırt.\n\n📞 {TEL}\n\n#AssosTroyBeach #Assos #Kadırga')],
        sign='<p class="kimlik">Bakır tonları web sitenizdeki logodan; vektör logo dosyanızla birebir uygularız.</p>',
    ),
)
