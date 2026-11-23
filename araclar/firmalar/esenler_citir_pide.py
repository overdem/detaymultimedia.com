# tasarim/esenler-citir-pide.md — krem/çıtır turuncu/kahve, Rokkitt 900 + Chivo + Abril Fatface, kurdele şerit + retro rozet, ofset gölge
TEL = '0286 214 11 27'; ADR = 'Demokrasi Cd. 8-10/A · Esenler'
CSS = """
.s{background:var(--krem);color:var(--kahve);font-family:var(--font-govde);text-align:center}
.t{font:900 140px/.92 var(--font-baslik);text-transform:uppercase;color:var(--citir);text-shadow:6px 6px 0 var(--kahve)}
.t2{font:900 84px/1 var(--font-baslik);text-transform:uppercase;color:var(--kahve)}
.bd{font:400 30px/1.45 var(--font-govde);color:var(--kahve)}
.rib{display:inline-block;position:relative;background:var(--kor);color:var(--krem);font:700 24px var(--font-govde);letter-spacing:.12em;text-transform:uppercase;padding:14px 46px}
.rib:before,.rib:after{content:"";position:absolute;top:0;border:26px solid var(--kor);border-width:26px 18px}
.rib:before{left:-26px;border-left-color:transparent}.rib:after{right:-26px;border-right-color:transparent}
.card{position:absolute;background-size:cover;background-position:center;border:14px solid var(--citir);border-radius:28px;box-shadow:10px 10px 0 var(--kahve)}
.badge{position:absolute;width:250px;height:250px;border-radius:50%;background:var(--kahve);color:var(--krem);display:flex;flex-direction:column;align-items:center;justify-content:center;border:6px dashed var(--citir);outline:8px solid var(--kahve)}
.badge b{font:400 72px/1 var(--font-vurgu);color:var(--krem)}.badge span{font:700 20px var(--font-govde);letter-spacing:.1em;margin-top:6px}
.r .t{font-size:104px}.r .t2{font-size:62px}.r .bd{font-size:24px}.r .rib{font-size:18px;padding:10px 32px}
"""
def s1(P): return f"""<div class="s"><div style="position:absolute;left:0;right:0;top:64px"><div class="t2" style="font-size:44px;letter-spacing:.2em">Esenler</div><div class="t" style="font-size:190px;margin-top:4px">ÇITIR</div>
<div class="rib" style="margin-top:18px">2012’den beri</div></div>
<div class="card" style="left:90px;right:90px;top:480px;bottom:150px;background-image:url('{P('904157a2.png')}')"></div>
<div class="bd" style="position:absolute;left:0;right:0;bottom:62px;font:700 30px var(--font-govde);letter-spacing:.14em">PİDE · LAHMACUN · KEBAP</div></div>"""
def item(P, ph, no, t, bd):
    return f"""<div class="s"><div class="card" style="left:70px;right:70px;top:70px;height:880px;background-image:url('{P(ph)}')"></div>
<div class="badge" style="right:50px;top:800px"><b>{no}</b><span>ÇITIR</span></div>
<div style="position:absolute;left:80px;right:300px;top:1000px;text-align:left"><div class="t" style="font-size:96px">{t}</div><div class="bd" style="margin-top:18px">{bd}</div></div></div>"""
def s2(P): return item(P, '904157a2.png', '01', 'Pide', 'Kuşbaşılı kaşarlı, bol malzemeli; taş fırından çıtır kenar.')
def s3(P): return item(P, 'c5b615b2.png', '02', 'Lahmacun', 'İnce ve çıtır; maydanoz, soğan, limon yanında.')
def s4(P): return item(P, 'fcfcfa0b.png', '03', 'Kebap', 'Usta işi, ocaktan sıcak sıcak.')
def s5(P): return f"""<div class="s" style="background:var(--citir)"><div style="position:absolute;left:60px;right:60px;top:150px"><div class="t" style="color:var(--krem);font-size:150px">SİPARİŞ<br>VER!</div>
<div class="rib" style="margin-top:40px;background:var(--kahve)">Paket servis</div></div>
<div style="position:absolute;left:110px;right:110px;bottom:150px;background:var(--krem);border-radius:28px;padding:44px;box-shadow:10px 10px 0 var(--kahve)">
<div style="font:400 88px/1 var(--font-vurgu);color:var(--kahve)">{TEL}</div><div class="bd" style="margin-top:20px;font-weight:700">Demokrasi Cd. 8-10/A · Esenler</div></div></div>"""
def post(P): return f"""<div class="s"><div class="card" style="left:70px;right:70px;top:360px;bottom:70px;background-image:url('{P('c5b615b2.png')}')"></div>
<div style="position:absolute;left:0;right:0;top:70px"><div class="t2" style="font-size:60px">Bugün ne yesek?</div><div class="t" style="font-size:150px;margin-top:8px">LAHMACUN</div></div>
<div class="badge" style="right:40px;bottom:40px;width:220px;height:220px"><b style="font-size:40px">Sipariş</b><span>{TEL}</span></div></div>"""
def ov(t, sub=None, rib=None):
    s = f'<div class="bd" style="margin-top:14px;font-weight:700">{sub}</div>' if sub else ''
    r = f'<div class="rib" style="margin-top:10px">{rib}</div>' if rib else ''
    return f'<div class="s r" style="background:transparent"><div style="position:absolute;left:40px;right:40px;bottom:120px;background:var(--krem);border:10px solid var(--citir);border-radius:26px;padding:30px 20px;box-shadow:8px 8px 0 var(--kahve)"><div class="t">{t}</div>{s}{r}</div></div>'
CFG = dict(
    slug='esenler-citir-pide', name='Esenler Çıtır Pide',
    fonts_url='https://fonts.googleapis.com/css2?family=Rokkitt:wght@800;900&family=Chivo:wght@400;700&family=Abril+Fatface&display=swap',
    tokens='--krem:#FFF0DF;--citir:#D06E12;--kahve:#5E2E1E;--kor:#A9301C;--yesil:#5B7F3A;--font-baslik:"Rokkitt",serif;--font-govde:"Chivo",sans-serif;--font-vurgu:"Abril Fatface",serif;--zemin:#FFF0DF',
    css=CSS, slides=[s1, s2, s3, s4, s5], post=post,
    reel=[('904157a2.png', ov('ÇITIR', 'Esenler’de pide, lahmacun, kebap', '2012’den beri')),
          ('c5b615b2.png', ov('LAHMACUN', 'İnce, çıtır, bol yeşillik')),
          ('fcfcfa0b.png', ov('KEBAP', 'Usta işi, ocaktan')),
          ('904157a2.png', ov('SİPARİŞ VER', f'{TEL} · Paket servis'))],
    page=dict(
        vars='  color-scheme: light;\n  --bg: #FFF0DF;\n  --panel: #fff8ef;\n  --line: #e4c9ab;\n  --text: #5E2E1E;\n  --muted: #7a4b38;\n  --accent: #A9301C;\n  --accent-ink: #FFF0DF;\n  --display: "Rokkitt", serif;\n  --display-w: 900;\n  --body: "Chivo", sans-serif;\n  --vurgu: "Abril Fatface", serif;',
        extra_css='h1 { text-transform: uppercase; }\nh1 em { font-style: normal; color: #D06E12; text-shadow: 3px 3px 0 #5E2E1E; display: block; }\n.shot { border: 6px solid #D06E12; border-radius: 18px; box-shadow: 5px 5px 0 #5E2E1E; }\n.motif { display: inline-block; margin: 0 auto; background: #A9301C; color: #FFF0DF; font: 700 12px var(--body); letter-spacing: .14em; text-transform: uppercase; padding: 8px 22px; }\n',
        motif='<span class="motif">Pide · Lahmacun · Kebap · 2012’den beri</span>',
        lede='Haftalık paylaşımların nasıl görüneceğini göstermek için hazırladığımız kısa bir reels, beş karelik bir karusel ve tek gönderi; logonuzdaki krem, çıtır turuncu ve kurdeleyle.',
        reel_meta='12 sn · dikey',
        reel_note='Çıtır pide, ince lahmacun, usta işi kebap ve sipariş hattı; 4 sahnede Esenler Çıtır. Video sessizdir; müzik Instagram’da paylaşırken eklenir.',
        alts=['Esenler Çıtır, 2012’den beri. Pide, lahmacun, kebap.', 'Pide: kuşbaşılı kaşarlı, bol malzemeli.', 'Lahmacun: ince ve çıtır; maydanoz, soğan, limon yanında.', 'Kebap: usta işi, ocaktan.', f'Sipariş ver! {TEL} · {ADR} · Paket servis'],
        post_alt=f'Bugün ne yesek? Lahmacun. Sipariş {TEL}.',
        post_note='Telefon, adres ve servis bilgisi Google Haritalar kaydınızdan; “2012” logonuzdan alındı.',
        music=[('Hareketli darbuka', 'Aramaya “darbuka beat” yazın. Ritmi yüksek, iştah açıcı.'), ('Türkçe pop enstrümantal', 'Aramaya “turkish pop instrumental” yazın. Enerjik.'), ('Funk', 'Aramaya “funky food” yazın. Hızlı kesimlere yakışır.')],
        caps=[('reel', 'Reels', f'Çıtır pide, ince lahmacun, usta işi kebap. 🔥\nEsenler’de sıcak sıcak.\n\n📍 Demokrasi Cd. 8-10/A, Esenler\n📞 Sipariş: {TEL}\n\n#EsenlerÇıtır #Çanakkale #pide #lahmacun #kebap'),
              ('kar', 'Karusel', f'Bugün ne yesek? 🤔\nKuşbaşılı kaşarlı pide, çıtır lahmacun ya da ocaktan kebap; karar senin.\nArkadaşını etiketle, beraber gelin. 👇\n\n📍 {ADR}\n📞 {TEL} · Paket servis\n\n#EsenlerÇıtır #Çanakkale #çanakkalepide #lahmacun'),
              ('post', 'Tek gönderi', f'Bugün ne yesek? Lahmacun. 🍋🌿\nİnce, çıtır, bol yeşillikli.\n\n📞 Sipariş: {TEL}\n📍 Esenler\n\n#EsenlerÇıtır #lahmacun #Çanakkale')],
    ),
)
