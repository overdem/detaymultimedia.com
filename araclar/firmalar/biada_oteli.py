# tasarim/biada-oteli.md — grafit/sıva/panjur yeşili/kiremit/fener, Forum + Kumbh Sans + Meow Script, panjur çıtası çizgileri + dikey pencere
TEL = '0533 459 30 00'; ADR = 'Mehtepaltı Sk. No:3, Rum Mahallesi · Bozcaada'
PH = dict(konak='konak.png', aksam='aksam.png', oda='oda.png')
CSS = """
.s{background:var(--siva);color:var(--grafit);font-family:var(--font-govde);text-align:center}
.t{font:400 128px/1.02 var(--font-baslik)}
.lab{font:600 21px var(--font-govde);letter-spacing:.34em;text-transform:uppercase}
.sig{font:400 170px/1 var(--font-vurgu)}
.sc{font:400 92px/1 var(--font-vurgu);color:var(--kiremit)}
.bd{font:400 30px/1.5 var(--font-govde)}
.win{position:absolute;background-size:cover;background-position:center}
.sl{position:absolute;top:0;bottom:0;width:2px;background:currentColor;opacity:.35}
.r .t{font-size:90px}.r .sc{font-size:72px}.r .bd{font-size:24px}.r .sig{font-size:120px}
"""
def slats(c='var(--grafit)'): return f'<div style="color:{c}"><div class="sl" style="left:44px"></div><div class="sl" style="left:56px"></div><div class="sl" style="right:44px"></div><div class="sl" style="right:56px"></div></div>'
def s1(P): return f"""<div class="s">{slats()}<div class="win" style="left:150px;right:150px;top:90px;height:880px;background-image:url('{P(PH['konak'])}')"></div>
<div style="position:absolute;left:0;right:0;top:985px"><div class="sig">biAda</div><div class="lab" style="margin-top:10px">Rum Mahallesi · Bozcaada</div></div></div>"""
def s2(P): return f"""<div class="s" style="background:var(--panjur);color:var(--siva)">{slats('var(--siva)')}<div style="position:absolute;left:120px;right:120px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center">
<div class="lab" style="color:var(--fener)">Hikâye</div><div class="t" style="margin-top:44px;font-size:150px">Meydandaki<br>taş konak</div>
<div class="bd" style="margin-top:56px;font-size:34px">Rum Mahallesi’nin en huzurlu meydanında, yeniden hayat bulan bir ada evi. Koyu yeşil panjurlar, taş merdiven, akşam fenerleri.</div></div></div>"""
def s3(P): return f"""<div class="s"><div class="ph" style="background-image:url('{P(PH['aksam'])}')"></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:520px;background:linear-gradient(180deg,rgba(37,51,44,0),rgba(37,51,44,.94) 60%)"></div>
<div style="position:absolute;left:80px;right:80px;bottom:90px;color:var(--siva)"><div class="sc" style="color:var(--fener)">akşam meydanda</div><div class="t" style="font-size:96px;margin-top:10px">biAda Kitchen</div></div></div>"""
def s4(P): return f"""<div class="s" style="background:var(--beyaz)">{slats()}<div class="win" style="left:190px;right:190px;top:90px;height:820px;background-image:url('{P(PH['oda'])}')"></div>
<div style="position:absolute;left:0;right:0;top:950px"><div class="t" style="font-size:96px">Grande · Medio</div><div class="bd" style="margin-top:14px">İki konak, her odada ada sessizliği.</div></div></div>"""
def s5(P): return f"""<div class="s">{slats()}<div style="position:absolute;left:100px;right:100px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center">
<div class="lab">sizi bekliyoruz</div><div class="sig" style="font-size:230px;margin-top:30px">biAda</div><div class="lab" style="margin-top:6px">Bozcaada</div>
<div style="width:120px;height:2px;background:var(--kiremit);margin:60px auto"></div><div class="bd">{ADR}</div><div style="font:400 70px var(--font-baslik);margin-top:26px">{TEL}</div><div class="bd" style="margin-top:8px;font-size:26px">biadaoteli.com · WhatsApp’tan da yazabilirsiniz</div></div></div>"""
def post(P): return f"""<div class="s"><div class="ph" style="background-image:url('{P(PH['konak'])}')"></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:480px;background:linear-gradient(180deg,rgba(232,225,214,0),rgba(232,225,214,.96) 60%)"></div>
<div style="position:absolute;left:0;right:0;bottom:80px"><div class="sig" style="font-size:150px">biAda</div><div class="lab" style="margin-top:6px">Bozcaada’nın kalbinde</div></div></div>"""
def ov(t=None, sc=None, bd=None):
    a = f'<div class="t">{t}</div>' if t else ''
    c = f'<div class="sc">{sc}</div>' if sc else ''
    b = f'<div class="bd" style="margin-top:10px">{bd}</div>' if bd else ''
    return f'<div class="s r" style="background:transparent"><div style="position:absolute;left:60px;right:60px;bottom:140px;background:rgba(232,225,214,.95);padding:40px 30px">{c}{a}{b}</div></div>'
CFG = dict(
    slug='biada-oteli', name='Biada Oteli',
    fonts_url='https://fonts.googleapis.com/css2?family=Forum&family=Kumbh+Sans:wght@400;600&family=Meow+Script&display=swap',
    tokens='--grafit:#45494B;--siva:#E8E1D6;--panjur:#25332C;--kiremit:#A9573A;--fener:#E6A65B;--beyaz:#FFFFFF;--font-baslik:"Forum",serif;--font-govde:"Kumbh Sans",sans-serif;--font-vurgu:"Meow Script",cursive;--zemin:#E8E1D6',
    css=CSS, slides=[s1, s2, s3, s4, s5], post=post,
    reel=[(PH['konak'], ov(None, None, '<span class="sig">biAda</span><br>Rum Mahallesi · Bozcaada')), (PH['aksam'], ov('Akşam meydanda', None, 'biAda Kitchen')), (PH['oda'], ov('Grande · Medio', None, 'Her odada ada sessizliği')), (PH['konak'], ov(None, 'sizi bekliyoruz', f'{ADR}<br>{TEL}'))],
    page=dict(
        vars='  color-scheme: light;\n  --bg: #E8E1D6;\n  --panel: #F6F2EB;\n  --line: #cfc5b6;\n  --text: #45494B;\n  --muted: #5d5f5c;\n  --accent: #25332C;\n  --accent-ink: #E8E1D6;\n  --display: "Forum", serif;\n  --display-w: 400;\n  --body: "Kumbh Sans", sans-serif;\n  --vurgu: "Meow Script", cursive;',
        extra_css='h1 em { font-family: var(--vurgu); font-style: normal; font-weight: 400; color: #A9573A; font-size: 1.25em; display: block; }\n.shot { border-radius: 2px; }\n.kimlik { font-size: 12px; color: #5d5f5c; margin: 0; }\n.motif { display: flex; gap: 6px; justify-content: center; }\n.motif i { width: 2px; height: 30px; background: #45494B; opacity: .45; }\n',
        motif='<div class="motif" aria-hidden="true"><i></i><i></i><i></i><i></i></div>',
        lede='Haftalık paylaşımların nasıl görüneceğini göstermek için hazırladığımız kısa bir reels, beş karelik bir karusel ve tek gönderi; logonuzun el yazısı, konağın panjur yeşili ve meydandaki akşam ışıklarıyla.',
        reel_meta='12 sn · dikey',
        reel_note='Konak cephesi, akşam masası, oda ve iletişim. Video sessizdir; müzik Instagram’da paylaşırken eklenir.',
        alts=['biAda, Rum Mahallesi, Bozcaada: meydandaki taş konak.', 'Hikâye: Rum Mahallesi’nin en huzurlu meydanında yeniden hayat bulan ada evi.', 'Akşam meydanda: biAda Kitchen masaları.', 'Grande ve Medio: iki konak, her odada ada sessizliği.', f'Sizi bekliyoruz: {ADR} · {TEL}'],
        post_alt='biAda: Bozcaada’nın kalbinde.',
        post_note='Konum ve “Rum Mahallesi’nin en huzurlu meydanı” Instagram profilinizden; Grande, Medio, Lounge ve Kitchen öne çıkan hikâyelerinizden; adres ve telefon Google Haritalar kaydınızdan alındı.',
        music=[('Akşam akustik', 'Aramaya “evening acoustic guitar” yazın. Meydan akşamı için.'), ('Bossa nova', 'Aramaya “bossa nova cafe” yazın. Kitchen kareleri için.'), ('Sakin piyano', 'Aramaya “soft piano” yazın. Oda kareleri için.')],
        caps=[('reel', 'Reels', f'Rum Mahallesi’nin meydanında, taş bir konakta akşam. 🌙\nBozcaada’nın kalbindeyiz.\n\n📍 {ADR}\n📞 {TEL}\n\n#biAda #Bozcaada #RumMahallesi #butikotel'),
              ('kar', 'Karusel', f'Meydandaki taş konak. 🤍\nKoyu yeşil panjurlar, taş merdiven, akşam fenerleri ve ada sessizliği.\nAda planın için kaydet. 👇\n\n📍 {ADR}\n📞 {TEL}\n\n#biAda #Bozcaada #Çanakkale #adatatili'),
              ('post', 'Tek gönderi', 'Bozcaada’nın kalbinde bir akşam. ✨\nAdada en sevdiğin sokak hangisi? 👇\n\n#biAda #Bozcaada')],
        sign='<p class="kimlik">“biAda” imzası logonuzdaki el yazısına yakın bir yazı tipiyle hazırlandı; logo dosyanız gelince o kullanılır.</p>',
    ),
)
