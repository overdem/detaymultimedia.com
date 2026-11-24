# tasarim/veranda-coffee-company.md — kraft/mürekkep/fincan turuncusu/krem/siyah, Amatic SC + Mulish + Kaushan Script, ince çift daire motifi
TEL = '0533 470 17 00'; ADR = 'Yalı Cd. No:16 · Kemalpaşa (Kordon)'
PH = dict(teras='teras.png', ruby='ruby.png', kahvalti='kahvalti.png')
CSS = """
.s{background:var(--krem);color:var(--murekkep);font-family:var(--font-govde);text-align:center}
.grain{position:absolute;inset:0;background-image:radial-gradient(rgba(62,43,34,.07) 1px,transparent 1px);background-size:5px 5px}
.t{font:700 190px/.9 var(--font-baslik);letter-spacing:.04em;text-transform:uppercase}
.sub{font:700 22px var(--font-govde);letter-spacing:.38em;text-transform:uppercase}
.sc{font:400 76px/1.05 var(--font-vurgu)}
.bd{font:400 30px/1.45 var(--font-govde)}
.circ{position:absolute;border-radius:50%;background-size:cover;background-position:center}
.ring{position:absolute;border-radius:50%;border:3px solid var(--murekkep)}
.dot{position:absolute;width:34px;height:34px;border-radius:50%;background:var(--fincan)}
.badge{display:inline-block;background:var(--fincan);color:var(--siyah);font:700 24px var(--font-govde);letter-spacing:.2em;text-transform:uppercase;padding:14px 26px;border-radius:999px}
.r .t{font-size:120px}.r .sc{font-size:58px}.r .bd{font-size:24px}.r .sub{font-size:17px}
"""
def rings(x, y, d):
    return f'<div class="ring" style="left:{x-18}px;top:{y-18}px;width:{d+36}px;height:{d+36}px"></div><div class="ring" style="left:{x-34}px;top:{y-34}px;width:{d+68}px;height:{d+68}px;border-width:1.5px"></div>'
def s1(P): return f"""<div class="s" style="background:var(--kraft)"><div class="grain"></div>
<div class="circ" style="left:215px;top:110px;width:650px;height:650px;background-image:url('{P(PH['teras'])}')"></div>{rings(215,110,650)}
<div class="dot" style="left:523px;top:44px"></div>
<div style="position:absolute;left:0;right:0;top:850px"><div class="t">Veranda</div><div class="sub" style="margin-top:10px">Coffee &amp; Breakfast · Kordon</div><div class="sc" style="margin-top:34px;color:var(--siyah)">Boğaz’a karşı</div></div></div>"""
def s2(P): return f"""<div class="s" style="background:var(--siyah);color:var(--krem)"><div class="ph" style="background-image:url('{P(PH['ruby'])}');bottom:430px"></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:430px;padding:50px 80px"><span class="badge">Menünün yıldızı</span><div class="t" style="font-size:150px;margin-top:26px">Ruby</div><div class="bd" style="margin-top:6px;color:var(--krem)">Kırmızı meyveli cheesecake; yanına bir cappuccino.</div></div></div>"""
def s3(P): return f"""<div class="s"><div class="ph" style="background-image:url('{P(PH['kahvalti'])}')"></div>
<div style="position:absolute;left:80px;right:80px;bottom:80px;background:var(--krem);border-radius:28px;padding:44px 40px"><div class="sc" style="font-size:64px;color:var(--murekkep)">Boğaz’a karşı</div><div class="t" style="font-size:120px;margin-top:8px">Kahvaltı</div><div class="bd" style="margin-top:10px">Kordon’da denize bakan masada, sabah 08:30’dan itibaren.</div></div></div>"""
def s4(P): return f"""<div class="s" style="background:var(--siyah);color:var(--krem)"><div class="grain" style="opacity:.4"></div>
<div style="position:absolute;left:90px;right:90px;top:150px"><div class="sub" style="color:var(--kraft)">Üç adres, aynı fincan</div><div class="t" style="font-size:150px;margin-top:30px;color:var(--krem)">3 Veranda</div>
<div style="margin-top:70px;display:flex;flex-direction:column;gap:46px;text-align:left">
<div style="display:flex;gap:28px;align-items:center"><span class="dot" style="position:static;flex:none"></span><div><div class="t" style="font-size:80px;color:var(--krem)">Kordon</div><div class="bd" style="color:var(--kraft);font-size:26px">Yalı Cd. No:16, Kemalpaşa</div></div></div>
<div style="display:flex;gap:28px;align-items:center"><span class="dot" style="position:static;flex:none"></span><div><div class="t" style="font-size:80px;color:var(--krem)">Yeni Kordon</div><div class="bd" style="color:var(--kraft);font-size:26px">İğdelik Sk. No:21</div></div></div>
<div style="display:flex;gap:28px;align-items:center"><span class="dot" style="position:static;flex:none"></span><div><div class="t" style="font-size:80px;color:var(--krem)">Bahçe</div><div class="bd" style="color:var(--kraft);font-size:26px">Kepez</div></div></div>
</div></div></div>"""
def s5(P): return f"""<div class="s" style="background:var(--kraft)"><div class="grain"></div>{rings(190,170,700)}
<div style="position:absolute;left:190px;top:170px;width:700px;height:700px;border-radius:50%;background:var(--krem);display:flex;flex-direction:column;align-items:center;justify-content:center">
<div class="sc" style="font-size:66px">uğrayın</div><div class="t" style="font-size:170px;margin-top:6px">Veranda</div><div class="bd" style="margin-top:14px;font-size:28px">Yalı Cd. No:16, Kemalpaşa<br>08:30’dan itibaren</div></div>
<div style="position:absolute;left:0;right:0;top:1010px"><div style="font:700 84px var(--font-baslik);letter-spacing:.06em">{TEL}</div><div class="sub" style="margin-top:14px">Kordon · Yeni Kordon · Kepez Bahçe</div></div></div>"""
def post(P): return f"""<div class="s"><div class="ph" style="background-image:url('{P(PH['teras'])}')"></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:520px;background:linear-gradient(180deg,rgba(28,26,24,0),rgba(28,26,24,.92) 55%)"></div>
<div style="position:absolute;left:0;right:0;bottom:90px;color:var(--krem)"><div class="sc" style="color:var(--fincan);font-size:84px">günaydın Kordon</div><div class="t" style="font-size:120px;margin-top:6px">Kahven hazır</div><div class="sub" style="margin-top:12px;color:var(--kraft)">Veranda Coffee Company</div></div></div>"""
def ov(t=None, sc=None, bd=None):
    a = f'<div class="t">{t}</div>' if t else ''
    c = f'<div class="sc" style="margin-top:6px">{sc}</div>' if sc else ''
    b = f'<div class="bd" style="margin-top:10px">{bd}</div>' if bd else ''
    return f'<div class="s r" style="background:transparent"><div style="position:absolute;left:60px;right:60px;bottom:140px;background:rgba(244,235,221,.95);border-radius:30px;padding:40px 30px;border:3px solid var(--murekkep)">{c}{a}{b}</div></div>'
CFG = dict(
    slug='veranda-coffee-company', name='Veranda Coffee Company',
    fonts_url='https://fonts.googleapis.com/css2?family=Amatic+SC:wght@700&family=Mulish:wght@400;700&family=Kaushan+Script&display=swap',
    tokens='--kraft:#B9925A;--murekkep:#3E2B22;--fincan:#E7611D;--krem:#F4EBDD;--siyah:#1C1A18;--font-baslik:"Amatic SC",sans-serif;--font-govde:"Mulish",sans-serif;--font-vurgu:"Kaushan Script",cursive;--zemin:#F4EBDD',
    css=CSS, slides=[s1, s2, s3, s4, s5], post=post,
    reel=[(PH['teras'], ov('Veranda', 'Boğaz’a karşı')), (PH['ruby'], ov('Ruby', None, 'Kırmızı meyveli cheesecake')), (PH['kahvalti'], ov('Kahvaltı', 'denize bakan masada')), (PH['teras'], ov('Veranda', 'uğrayın', f'{ADR}<br>{TEL}'))],
    page=dict(
        vars='  color-scheme: light;\n  --bg: #F4EBDD;\n  --panel: #FBF6EE;\n  --line: #d6c3a3;\n  --text: #3E2B22;\n  --muted: #5e4638;\n  --accent: #1C1A18;\n  --accent-ink: #F4EBDD;\n  --display: "Amatic SC", sans-serif;\n  --display-w: 700;\n  --body: "Mulish", sans-serif;\n  --vurgu: "Kaushan Script", cursive;',
        extra_css='h1 { font-size: clamp(44px, 12vw, 60px); letter-spacing: .03em; }\nh2 { font-size: 34px; letter-spacing: .03em; }\nh1 em { font-family: var(--vurgu); font-style: normal; font-weight: 400; color: #B3480F; font-size: .62em; display: block; letter-spacing: 0; }\n.eyebrow { color: #B3480F; }\n.kimlik { font-size: 12px; color: #5e4638; margin: 0; }\n.motif { width: 46px; height: 46px; margin: 0 auto; border-radius: 50%; border: 2px solid var(--text); box-shadow: 0 0 0 5px var(--bg), 0 0 0 6px var(--text); position: relative; }\n.motif::after { content: ""; position: absolute; left: 15px; top: 15px; width: 12px; height: 12px; border-radius: 50%; background: #E7611D; }\n',
        motif='<div class="motif" aria-hidden="true"></div>',
        lede='Haftalık paylaşımların nasıl görüneceğini göstermek için hazırladığımız kısa bir reels, beş karelik bir karusel ve tek gönderi; menünüzdeki kraft kâğıt, ince el çizimi “VERANDA” yazısı ve turuncu fincanla.',
        reel_meta='12 sn · dikey',
        reel_note='Kordon terası, Ruby cheesecake, Boğaz’a karşı kahvaltı ve adres. Video sessizdir; müzik Instagram’da paylaşırken eklenir.',
        alts=['Veranda Coffee & Breakfast, Kordon: Boğaz’a karşı.', 'Menünün yıldızı: Ruby, kırmızı meyveli cheesecake.', 'Boğaz’a karşı kahvaltı, 08:30’dan itibaren.', 'Üç adres: Kordon, Yeni Kordon, Kepez Bahçe.', f'Uğrayın: {ADR} · {TEL}'],
        post_alt='Günaydın Kordon, kahven hazır. Veranda Coffee Company.',
        post_note='Adres, telefon ve açılış saati Google Haritalar kaydınızdan; Ruby cheesecake ve “Boğaz’a karşı kahvaltı” menünüzden, şube bilgisi Haritalar’daki üç kayıttan alındı.',
        music=[('Akustik sabah', 'Aramaya “acoustic morning” yazın. Kahvaltı karelerine uyar.'), ('Bossa nova', 'Aramaya “bossa nova cafe” yazın. Deniz kenarı havası.'), ('Lo-fi kahve', 'Aramaya “lofi coffee” yazın. Sakin ve modern.')],
        caps=[('reel', 'Reels', f'Kordon’da, Boğaz’a karşı bir fincan. ☕️🌊\nRuby cheesecake ve denize bakan kahvaltı.\n\n📍 {ADR}\n📞 {TEL}\n\n#VerandaCoffee #Çanakkale #Kordon #kahvaltı #cheesecake'),
              ('kar', 'Karusel', f'Veranda’da bir sabah. 🧡\nRuby cheesecake, Boğaz’a karşı kahvaltı ve üç adres: Kordon, Yeni Kordon, Kepez Bahçe.\nBir sonraki kahve molan için kaydet. 👇\n\n📍 {ADR}\n⏰ 08:30’dan itibaren\n📞 {TEL}\n\n#VerandaCoffee #Çanakkale #çanakkalekahve #Kordon'),
              ('post', 'Tek gönderi', 'Günaydın Kordon! ☕️\nKahven hazır, deniz de.\nBugün hangi şubedesin? Yorumlara yaz. 👇\n\n#VerandaCoffee #günaydın #Çanakkale')],
        sign='<p class="kimlik">Yazı-imza ve renkler menü kapağınızdaki logodan; vektör logo dosyanız varsa onunla değiştiririz.</p>',
    ),
)
