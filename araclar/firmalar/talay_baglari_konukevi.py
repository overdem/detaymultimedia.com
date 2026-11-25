# tasarim/talay-baglari-konukevi.md — logo mavisi/bağ yeşili/üzüm/kireç, Cardo + Hind + Ms Madi, asma çizgisi + üç üzüm tanesi
TEL = '0533 232 83 95'; ADR = 'Sulubahçe Bağ Yolu No:24 · Bozcaada'
PH = dict(teras='teras.png', uzum='uzum.png', oda='oda.png')
CSS = """
.s{background:var(--kirec);color:var(--murekkep);font-family:var(--font-govde);text-align:center}
.t{font:700 150px/1 var(--font-baslik);letter-spacing:.01em}
.lab{font:600 22px var(--font-govde);letter-spacing:.3em;text-transform:uppercase;color:var(--toprak)}
.sc{font:400 96px/1 var(--font-vurgu);color:var(--uzum)}
.bd{font:400 31px/1.45 var(--font-govde)}
.win{position:absolute;background-size:cover;background-position:center;border-radius:28px}
.vine{display:flex;align-items:center;justify-content:center;gap:14px}
.vine i{display:block;width:120px;height:2px;background:currentColor;opacity:.6}
.vine b{display:block;width:14px;height:14px;border-radius:50%;background:var(--uzum)}
.r .t{font-size:96px}.r .sc{font-size:70px}.r .bd{font-size:24px}.r .lab{font-size:16px}
"""
def vine(c='var(--murekkep)'): return f'<div class="vine" style="color:{c}"><i></i><b></b><b></b><b></b><i></i></div>'
def s1(P): return f"""<div class="s"><div class="win" style="left:70px;right:70px;top:70px;height:860px;background-image:url('{P(PH['teras'])}')"></div>
<div style="position:absolute;left:0;right:0;top:970px"><div class="lab">Bozcaada</div><div class="t" style="font-size:112px;margin-top:10px">TALAY BAĞLARI</div><div class="sc" style="font-size:78px;margin-top:4px">bağların arasında</div></div></div>"""
def s2(P): return f"""<div class="s" style="background:var(--murekkep);color:var(--kirec)"><div style="position:absolute;left:110px;right:110px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center">
<div class="lab" style="color:var(--kirec);opacity:.8">Hikâyemiz</div>
<div class="t" style="font-size:140px;margin-top:40px;color:var(--kirec)">Dört kardeş,<br>bir bağevi</div>
<div style="margin:60px 0">{vine('var(--kirec)')}</div>
<div class="bd" style="font-size:34px">Talay ailesinden dört kardeş olarak, yıllardır ailemize ait bağevini restore ettik. Bağları korumak için açtığımız, yalnızca dört odalı bir konukevi.</div></div></div>"""
def s3(P): return f"""<div class="s"><div class="ph" style="background-image:url('{P(PH['uzum'])}')"></div>
<div style="position:absolute;left:80px;right:80px;bottom:80px;background:var(--kirec);padding:46px 40px;border-radius:20px"><div class="sc">bağ manzaralı teras</div><div class="bd" style="margin-top:14px">Bağların ortasında, denize bakan bir teras. Sabah kahvaltısı orada.</div></div></div>"""
def s4(P): return f"""<div class="s" style="background:var(--bag);color:var(--kirec)"><div class="win" style="left:150px;right:150px;top:100px;height:780px;background-image:url('{P(PH['oda'])}')"></div>
<div style="position:absolute;left:0;right:0;top:930px"><div class="t" style="font-size:104px;color:var(--kirec)">Yalnızca 4 oda</div><div class="bd" style="margin-top:16px">Sakin, özenli, ev gibi. Sezon kısa; yerinizi erken ayırtın.</div></div></div>"""
def s5(P): return f"""<div class="s"><div style="position:absolute;left:100px;right:100px;top:220px">
<div class="sc">sizi bekliyoruz</div><div class="lab" style="margin-top:40px">Bozcaada</div><div class="t" style="font-size:150px;margin-top:6px">TALAY<br>BAĞLARI</div><div class="lab" style="margin-top:10px">Konuk Evi</div>
<div style="margin:56px 0">{vine()}</div><div class="bd">{ADR}</div><div style="font:700 64px var(--font-baslik);margin-top:26px">{TEL}</div><div class="bd" style="margin-top:8px;font-size:26px">talaybaglari.com · WhatsApp’tan da yazabilirsiniz</div></div></div>"""
def post(P): return f"""<div class="s"><div class="ph" style="background-image:url('{P(PH['teras'])}')"></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:520px;background:linear-gradient(180deg,rgba(29,90,134,0),rgba(29,90,134,.93) 58%)"></div>
<div style="position:absolute;left:0;right:0;bottom:90px;color:var(--kirec)"><div class="sc" style="color:var(--kirec)">günaydın bağlar</div><div class="lab" style="margin-top:18px;color:var(--kirec)">Teras kahvaltısı · Talay Bağları Konuk Evi</div></div></div>"""
def ov(t=None, sc=None, bd=None):
    a = f'<div class="t">{t}</div>' if t else ''
    c = f'<div class="sc">{sc}</div>' if sc else ''
    b = f'<div class="bd" style="margin-top:10px">{bd}</div>' if bd else ''
    return f'<div class="s r" style="background:transparent"><div style="position:absolute;left:60px;right:60px;bottom:140px;background:rgba(247,244,236,.95);border-radius:22px;padding:44px 30px 40px">{c}{a}{b}</div></div>'
CFG = dict(
    slug='talay-baglari-konukevi', name='Talay Bağları Konukevi',
    fonts_url='https://fonts.googleapis.com/css2?family=Cardo:wght@400;700&family=Hind:wght@400;600&family=Ms+Madi&display=swap',
    tokens='--murekkep:#1D5A86;--bag:#4B6633;--uzum:#5A2A46;--kirec:#F7F4EC;--toprak:#6B5646;--font-baslik:"Cardo",serif;--font-govde:"Hind",sans-serif;--font-vurgu:"Ms Madi",cursive;--zemin:#F7F4EC',
    css=CSS, slides=[s1, s2, s3, s4, s5], post=post,
    reel=[(PH['uzum'], ov('TALAY BAĞLARI', 'bağların arasında')), (PH['teras'], ov('Teras kahvaltısı', None, 'Bağ ve deniz manzarası')), (PH['oda'], ov('Yalnızca 4 oda', None, 'Sakin, özenli, ev gibi')), (PH['teras'], ov('TALAY BAĞLARI', 'sizi bekliyoruz', f'{ADR}<br>{TEL}'))],
    page=dict(
        vars='  color-scheme: light;\n  --bg: #F7F4EC;\n  --panel: #FFFDF8;\n  --line: #d9d3c4;\n  --text: #1D5A86;\n  --muted: #6B5646;\n  --accent: #1D5A86;\n  --accent-ink: #F7F4EC;\n  --display: "Cardo", serif;\n  --display-w: 700;\n  --body: "Hind", sans-serif;\n  --vurgu: "Ms Madi", cursive;',
        extra_css='h1 em { font-family: var(--vurgu); font-style: normal; font-weight: 400; color: #5A2A46; font-size: 1.15em; display: block; }\n.shot { border-radius: 22px; }\n.kimlik { font-size: 12px; color: #6B5646; margin: 0; }\n.motif { display: flex; gap: 8px; justify-content: center; align-items: center; color: #1D5A86; }\n.motif i { width: 60px; height: 2px; background: currentColor; opacity: .5; }\n.motif b { width: 9px; height: 9px; border-radius: 50%; background: #5A2A46; }\n',
        motif='<div class="motif" aria-hidden="true"><i></i><b></b><b></b><b></b><i></i></div>',
        lede='Haftalık paylaşımların nasıl görüneceğini göstermek için hazırladığımız kısa bir reels, beş karelik bir karusel ve tek gönderi; logonuzun mavisi, bağların yeşili ve dört kardeşin bağevi hikâyesiyle.',
        reel_meta='12 sn · dikey',
        reel_note='Bağ, teras kahvaltısı, oda ve iletişim. Video sessizdir; müzik Instagram’da paylaşırken eklenir.',
        alts=['Talay Bağları, Bozcaada: bağların arasında.', 'Hikâyemiz: dört kardeş, ailenin bağevini restore ederek yalnızca dört odalı bir konukevi açtı.', 'Bağ manzaralı teras: bağların ortasında, denize bakan teras ve kahvaltı.', 'Yalnızca 4 oda: sakin, özenli, ev gibi.', f'Sizi bekliyoruz: {ADR} · {TEL}'],
        post_alt='Günaydın bağlar: teras kahvaltısı. Talay Bağları Konuk Evi.',
        post_note='Hikâye, oda sayısı ve teras web sitenizdeki “Hakkımızda” yazısından; adres ve telefon Google Haritalar kaydınızdan alındı. Renkler web sitenizdeki logonun mavisinden.',
        music=[('Akustik gitar', 'Aramaya “acoustic guitar morning” yazın. Bağ sabahına uyar.'), ('Ege ezgisi', 'Aramaya “aegean instrumental” yazın. Ada havası.'), ('Sakin piyano', 'Aramaya “calm piano nature” yazın. Oda kareleri için.')],
        caps=[('reel', 'Reels', f'Bağların arasında dört oda, bir teras ve deniz. 🍇\nBozcaada’da Talay ailesinin bağevi.\n\n📍 {ADR}\n📞 {TEL}\n\n#TalayBağları #Bozcaada #bağevi #konukevi'),
              ('kar', 'Karusel', f'Dört kardeş, bir bağevi. 🌿\nAilemizin yıllardır bizimle olan bağevini restore ettik; bağları korumak için açtığımız yalnızca dört odalı bir konukevi.\nAda planın için kaydet. 👇\n\n📍 {ADR}\n📞 {TEL}\n\n#TalayBağları #Bozcaada #Çanakkale #bağevi'),
              ('post', 'Tek gönderi', 'Günaydın bağlar! ☀️\nTerasta kahvaltı hazır; sen hangi manzarayla uyanmak istersin? 👇\n\n#TalayBağları #Bozcaada #kahvaltı')],
        sign='<p class="kimlik">Logo dosyanız elimizde olmadığı için “Talay Bağları” yazı-imzası web sitenizdeki logonun renginden hazırlandı.</p>',
    ),
)
