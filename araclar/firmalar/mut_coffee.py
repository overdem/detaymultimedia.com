# tasarim/mut-coffee.md — mut/kum/kil/krem/hasır, Bodoni Moda + Commissioner + Sacramento, kemer çerçeve + sıva dokusu
TEL = '0541 440 94 88'; ADR = 'Eski Mahkeme Sk. No:14 · Kemalpaşa'
PH = dict(latte='f8ac7ea6.png', ic='d4c0d482.png', salep='SALEP.png')
CSS = """
.s{background:var(--kum);color:var(--mut);font-family:var(--font-govde);text-align:center}
.grain{position:absolute;inset:0;background-image:radial-gradient(rgba(58,38,27,.06) 1px,transparent 1px);background-size:6px 6px}
.t{font:800 150px/.95 var(--font-baslik);letter-spacing:.06em;text-transform:uppercase}
.sub{font:600 22px var(--font-govde);letter-spacing:.42em;text-transform:uppercase}
.sc{font:400 96px/1 var(--font-vurgu);color:var(--kil)}
.bd{font:400 30px/1.45 var(--font-govde)}
.arch{position:absolute;background-size:cover;background-position:center;border-radius:400px 400px 24px 24px}
.r .t{font-size:96px}.r .sc{font-size:70px}.r .bd{font-size:24px}.r .sub{font-size:17px}
"""
def s1(P): return f"""<div class="s"><div class="grain"></div><div class="arch" style="left:170px;right:170px;top:110px;height:820px;background-image:url('{P(PH['ic'])}')"></div>
<div style="position:absolute;left:0;right:0;top:960px"><div class="t">Mut</div><div class="sub" style="margin-top:8px">Coffee · Kemalpaşa</div><div class="sc" style="margin-top:18px;font-size:76px">sakin bir mola</div></div></div>"""
def s2(P): return f"""<div class="s" style="background:var(--krem)"><div class="arch" style="left:110px;right:110px;top:90px;height:900px;background-image:url('{P(PH['latte'])}')"></div>
<div style="position:absolute;left:0;right:0;top:1020px"><div class="sc">latte art</div><div class="bd" style="margin-top:14px">Her fincanda ayrı bir desen.</div></div></div>"""
def s3(P):
    if PH['salep'].startswith('SALEP'):
        return f"""<div class="s" style="background:var(--mut);color:var(--krem)"><div class="grain" style="opacity:.5"></div><div style="position:absolute;left:90px;right:90px;top:330px"><div class="sub" style="color:var(--kum)">Kış menüsü</div><div class="t" style="font-size:132px;margin-top:30px;color:var(--krem)">Sıcak<br>salep</div><div class="sc" style="margin-top:30px;color:var(--kum)">tarçınlı</div><div class="bd" style="margin-top:30px;color:var(--kum)">Soğuk günlerin en sevilen fincanı.</div></div></div>"""
    return f"""<div class="s"><div class="ph" style="background-image:url('{P(PH['salep'])}')"></div><div style="position:absolute;left:80px;right:80px;bottom:80px;background:var(--krem);border-radius:24px;padding:40px"><div class="sub" style="color:var(--kil)">Kış menüsü</div><div class="t" style="font-size:96px;margin-top:14px">Sıcak salep</div><div class="bd" style="margin-top:10px">Tarçınlı; soğuk günlerin en sevilen fincanı.</div></div></div>"""
def s4(P): return f"""<div class="s" style="background:var(--krem)"><div class="grain"></div>
<div style="position:absolute;left:80px;right:80px;top:110px"><div class="sub" style="color:var(--kil)">İki kat, iki ayrı mola</div></div>
<div class="arch" style="left:80px;width:440px;top:220px;height:640px;background-image:url('{P(PH['ic'])}');background-position:20% 50%"></div>
<div class="arch" style="right:80px;width:440px;top:220px;height:640px;background-image:url('{P(PH['latte'])}')"></div>
<div style="position:absolute;left:80px;width:440px;top:900px"><div class="t" style="font-size:64px">Alt kat</div><div class="bd" style="margin-top:12px">Sohbet için, rahat ve sessiz.</div></div>
<div style="position:absolute;right:80px;width:440px;top:900px"><div class="t" style="font-size:64px">Üst kat</div><div class="bd" style="margin-top:12px">Çalışmak için, sakin.</div></div></div>"""
def s5(P): return f"""<div class="s"><div class="grain"></div><div style="position:absolute;left:80px;right:80px;top:230px"><div class="t" style="font-size:190px">Mut</div><div class="sub" style="margin-top:8px">Coffee</div>
<div style="width:120px;height:3px;background:var(--kil);margin:60px auto"></div><div class="sc">uğrayın</div>
<div class="bd" style="margin-top:36px">Eski Mahkeme Sk. No:14, Kemalpaşa<br>Her gün 09:00’dan itibaren</div><div style="font:800 54px var(--font-baslik);margin-top:34px;letter-spacing:.04em">{TEL}</div></div></div>"""
def post(P): return f"""<div class="s"><div class="ph" style="background-image:url('{P(PH['latte'])}')"></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:420px;background:linear-gradient(180deg,rgba(234,219,196,0),var(--kum) 45%)"></div>
<div style="position:absolute;left:0;right:0;bottom:90px"><div class="sc" style="font-size:110px">günaydın</div><div class="sub" style="margin-top:14px">Bir latte? · Mut Coffee</div></div></div>"""
def ov(t=None, sc=None, bd=None):
    a = f'<div class="t">{t}</div>' if t else ''
    c = f'<div class="sc" style="margin-top:8px">{sc}</div>' if sc else ''
    b = f'<div class="bd" style="margin-top:10px">{bd}</div>' if bd else ''
    return f'<div class="s r" style="background:transparent"><div style="position:absolute;left:60px;right:60px;bottom:140px;background:rgba(247,240,229,.94);border-radius:300px 300px 24px 24px;padding:70px 30px 40px">{a}{c}{b}</div></div>'
CFG = dict(
    slug='mut-coffee', name='Mut Coffee',
    fonts_url='https://fonts.googleapis.com/css2?family=Bodoni+Moda:opsz,wght@6..96,700;6..96,800&family=Commissioner:wght@400;600&family=Sacramento&display=swap',
    tokens='--mut:#3A261B;--kum:#EADBC4;--kil:#B07E52;--krem:#F7F0E5;--hasir:#9C7B52;--font-baslik:"Bodoni Moda",serif;--font-govde:"Commissioner",sans-serif;--font-vurgu:"Sacramento",cursive;--zemin:#EADBC4',
    css=CSS, slides=[s1, s2, s3, s4, s5], post=post,
    reel=None,
    page=dict(
        vars='  color-scheme: light;\n  --bg: #EADBC4;\n  --panel: #F7F0E5;\n  --line: #cdb89a;\n  --text: #3A261B;\n  --muted: #5c4535;\n  --accent: #3A261B;\n  --accent-ink: #F7F0E5;\n  --display: "Bodoni Moda", serif;\n  --display-w: 800;\n  --body: "Commissioner", sans-serif;\n  --vurgu: "Sacramento", cursive;',
        extra_css='h1 em { font-family: var(--vurgu); font-style: normal; font-weight: 400; color: #8a5f39; font-size: 1.3em; display: block; }\n.shot { border-radius: 200px 200px 14px 14px; }\nvideo.shot { border-radius: 14px; }\n.kimlik { font-family: var(--body); font-size: 12px; color: #5c4535; margin: 0; }\n',
        motif='',
        lede='Haftalık paylaşımların nasıl görüneceğini göstermek için hazırladığımız kısa bir reels, beş karelik bir karusel ve tek gönderi; duvarınızdaki kalın “MUT” yazısı, kum rengi sıva ve rattan tonlarıyla.',
        reel_meta='15 sn · dikey',
        reel_note='Mekân, latte art, kış için salep ve iletişim; Mut Coffee’den kısa bir mola. Video sessizdir; müzik Instagram’da paylaşırken eklenir.',
        alts=['Mut Coffee, Kemalpaşa: sakin bir mola.', 'Latte art: her fincanda ayrı bir desen.', 'Kış menüsü: sıcak, tarçınlı salep.', 'İki kat, iki ayrı mola: alt kat sohbet, üst kat çalışmak için.', f'Mut Coffee: uğrayın. {ADR} · Her gün 09:00’dan itibaren · {TEL}'],
        post_alt='Günaydın, bir latte? Mut Coffee.',
        post_note='Adres, telefon ve açılış saati Google Haritalar kaydınızdan; latte ve salep menünün öne çıkanlarından, alt/üst kat bilgisi misafir yorumlarından alındı.',
        music=[('Lo-fi kahve', 'Aramaya “lofi coffee” yazın. Sakin ve modern.'), ('Akustik bohem', 'Aramaya “boho acoustic” yazın. Kum duvarlara yakışır.'), ('Caz piyano', 'Aramaya “cafe jazz piano” yazın. Çalışma katı için.')],
        caps=[('reel', 'Reels', f'Kemalpaşa’da sakin bir mola. ☕️\nLatte art, sıcak salep ve kum rengi duvarlar.\n\n📍 Eski Mahkeme Sk. No:14, Kemalpaşa\n📞 {TEL}\n\n#MutCoffee #Çanakkale #latteart #salep #kahve'),
              ('kar', 'Karusel', f'Mut’ta iki ayrı mola. 🤎\nAlt kat sohbet, üst kat çalışma; latte art ve kış için salep.\nBir sonraki kahve molan için kaydet. 👇\n\n📍 {ADR}\n⏰ Her gün 09:00’dan itibaren\n📞 {TEL}\n\n#MutCoffee #Çanakkale #çanakkalekahve #kemalpaşa'),
              ('post', 'Tek gönderi', 'Günaydın! Bir latte? ☕️\nBugünkü desen ne olsun, yorumlara yaz.\n\n📍 Eski Mahkeme Sk., Kemalpaşa\n\n#MutCoffee #günaydın #Çanakkale')],
        sign='<p class="kimlik">“MUT” yazısı duvarınızdaki tabeladan; elinizde logo dosyası varsa onunla değiştiririz.</p>',
    ),
)
def _reel():
    s = PH['salep'] if not PH['salep'].startswith('SALEP') else PH['latte']
    return [(PH['ic'], ov('Mut', 'sakin bir mola')), (PH['latte'], ov(None, 'latte art', 'Her fincanda ayrı bir desen')), (s, ov('Salep', 'tarçınlı')), (PH['ic'], ov('Mut', 'uğrayın', f'{ADR}<br>{TEL}'))]
CFG['reel'] = _reel()
