# tasarim/kinzi-house.md — ceviz/kireç/taş/yaprak/Boğaz (öneri), Sora + Asap + Yellowtail, ceviz doğrama çerçevesi + anahtar dairesi
TEL = '0532 783 60 60'; ADR = 'Kemalpaşa, Dibek Sk. No:18 · Çanakkale'
PH = dict(sokak='sokak.png', daire='daire.png', kordon='kordon.png')
CSS = """
.s{background:var(--kirec);color:var(--ceviz);font-family:var(--font-govde);text-align:left}
.t{font:700 132px/1 var(--font-baslik);letter-spacing:-.01em}
.lab{font:600 22px var(--font-govde);letter-spacing:.24em;text-transform:uppercase}
.sc{font:400 84px/1 var(--font-vurgu);color:var(--bogaz)}
.bd{font:400 31px/1.45 var(--font-govde)}
.fr{position:absolute;inset:44px;border:10px solid var(--ceviz);border-radius:6px}
.key{display:inline-block;width:22px;height:22px;border-radius:50%;border:4px solid var(--bogaz)}
.big{font:700 210px/0.9 var(--font-baslik);color:var(--bogaz)}
.r .t{font-size:84px}.r .sc{font-size:62px}.r .bd{font-size:24px}
"""
def s1(P): return f"""<div class="s"><div class="ph" style="background-image:url('{P(PH['sokak'])}')"></div><div class="fr"></div>
<div style="position:absolute;left:44px;right:44px;bottom:44px;background:var(--kirec);padding:44px 60px 50px"><div class="lab" style="color:var(--bogaz)"><span class="key" style="vertical-align:-4px;margin-right:16px"></span>Kemalpaşa · Çanakkale</div>
<div class="t" style="margin-top:18px">KINZI HOUSE</div><div class="sc" style="margin-top:8px;font-size:72px">şehrin ortasında eviniz</div></div></div>"""
def s2(P): return f"""<div class="s" style="background:var(--ceviz);color:var(--kirec)"><div class="fr" style="border-color:var(--tas);opacity:.35"></div><div style="position:absolute;left:120px;right:120px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center">
<div class="lab" style="color:var(--tas)"><span class="key" style="vertical-align:-4px;margin-right:16px;border-color:var(--tas)"></span>Konum</div><div class="big" style="margin-top:40px;color:var(--kirec);font-size:280px">1 dk</div>
<div class="t" style="font-size:92px;margin-top:20px;color:var(--kirec)">Saat Kulesi’ne</div>
<div class="bd" style="margin-top:50px;font-size:36px;color:var(--tas)">Kordon, çarşı, feribot iskelesi ve kafeler yürüme mesafesinde. Arabaya ihtiyacınız yok.</div></div></div>"""
def s3(P): return f"""<div class="s"><div class="ph" style="background-image:url('{P(PH['daire'])}');bottom:420px"></div>
<div style="position:absolute;left:90px;right:90px;bottom:80px"><div class="sc">aileyle rahat</div><div class="t" style="font-size:96px;margin-top:10px">Mutfaklı daireler</div><div class="bd" style="margin-top:12px">Geniş yatak, çekyat, kendi mutfağınız. Kalabalık aileler için ekonomik.</div></div></div>"""
def s4(P): return f"""<div class="s" style="background:var(--tas)"><div class="fr"></div><div style="position:absolute;left:120px;right:120px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center">
<div class="lab" style="color:var(--bogaz)">Misafirlerimiz ne diyor?</div>
<div class="big" style="margin-top:40px;color:var(--ceviz);font-size:280px">4,8</div><div class="bd" style="margin-top:10px;font-size:34px">Google’da 266 yorum</div>
<div style="height:3px;background:var(--ceviz);opacity:.3;margin:56px 0"></div>
<div class="t" style="font-size:72px">“Her yere yürüyerek ulaşabildik. Sahibi ilgili ve yardımcı, ev gayet hijyenik.”</div></div></div>"""
def s5(P): return f"""<div class="s"><div class="fr"></div><div style="position:absolute;left:120px;right:120px;top:220px">
<div class="sc">evinizdesiniz</div><div class="t" style="font-size:150px;margin-top:30px">KINZI<br>HOUSE</div>
<div style="width:120px;height:6px;background:var(--bogaz);margin:56px 0 44px"></div><div class="bd">{ADR}</div><div style="font:700 66px var(--font-baslik);margin-top:26px">{TEL}</div><div class="bd" style="margin-top:8px;font-size:26px">WhatsApp’tan da yazabilirsiniz</div></div></div>"""
def post(P): return f"""<div class="s"><div class="ph" style="background-image:url('{P(PH['kordon'])}')"></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:540px;background:linear-gradient(180deg,rgba(74,47,32,0),rgba(74,47,32,.93) 58%)"></div>
<div style="position:absolute;left:90px;right:90px;bottom:90px;color:var(--kirec)"><div class="sc" style="color:var(--kirec)">akşam kordonda</div><div class="lab" style="margin-top:20px;color:var(--tas)">Saat Kulesi’ne 1 dk · Kinzi House</div></div></div>"""
def ov(t=None, sc=None, bd=None):
    a = f'<div class="t">{t}</div>' if t else ''
    c = f'<div class="sc">{sc}</div>' if sc else ''
    b = f'<div class="bd" style="margin-top:10px">{bd}</div>' if bd else ''
    return f'<div class="s r" style="background:transparent"><div style="position:absolute;left:50px;right:50px;bottom:130px;background:rgba(245,240,230,.96);border-left:12px solid #4A2F20;padding:40px 36px">{c}{a}{b}</div></div>'
CFG = dict(
    slug='kinzi-house', name='Kinzi House',
    fonts_url='https://fonts.googleapis.com/css2?family=Sora:wght@600;700&family=Asap:wght@400;600&family=Yellowtail&display=swap',
    tokens='--ceviz:#4A2F20;--kirec:#F5F0E6;--tas:#D6CCBD;--yaprak:#4F6B3A;--bogaz:#2B5A70;--font-baslik:"Sora",sans-serif;--font-govde:"Asap",sans-serif;--font-vurgu:"Yellowtail",cursive;--zemin:#F5F0E6',
    css=CSS, slides=[s1, s2, s3, s4, s5], post=post,
    reel=[(PH['sokak'], ov('KINZI HOUSE', 'şehrin ortasında eviniz')), (PH['daire'], ov('Mutfaklı daireler', None, 'Aileler için geniş ve rahat')), (PH['kordon'], ov('Saat Kulesi’ne 1 dk', None, 'Kordon yürüme mesafesinde')), (PH['sokak'], ov('KINZI HOUSE', 'evinizdesiniz', f'{ADR}<br>{TEL}'))],
    page=dict(
        vars='  color-scheme: light;\n  --bg: #F5F0E6;\n  --panel: #FFFCF6;\n  --line: #ddd3c3;\n  --text: #4A2F20;\n  --muted: #6a5243;\n  --accent: #2B5A70;\n  --accent-ink: #F5F0E6;\n  --display: "Sora", sans-serif;\n  --display-w: 700;\n  --body: "Asap", sans-serif;\n  --vurgu: "Yellowtail", cursive;',
        extra_css='h1 em { font-family: var(--vurgu); font-style: normal; font-weight: 400; color: #2B5A70; font-size: 1.05em; display: block; }\n.shot { border-radius: 6px; outline: 6px solid #4A2F20; outline-offset: -6px; }\nvideo.shot { outline: none; border-radius: 12px; }\n.kimlik { font-size: 12px; color: #6a5243; margin: 0; }\n.motif { width: 16px; height: 16px; border-radius: 50%; border: 3px solid #2B5A70; margin: 0 auto; }\n',
        motif='<div class="motif" aria-hidden="true"></div>',
        lede='Haftalık paylaşımların nasıl görüneceğini göstermek için hazırladığımız kısa bir reels, beş karelik bir karusel ve tek gönderi; Dibek Sokak’taki girişinizin ceviz doğramaları ve Saat Kulesi’ne bir dakikalık konumunuzla.',
        reel_meta='12 sn · dikey',
        reel_note='Sokak girişi, mutfaklı daire, akşam kordon ve iletişim. Video sessizdir; müzik Instagram’da paylaşırken eklenir.',
        alts=['Kinzi House, Kemalpaşa, Çanakkale: şehrin ortasında eviniz.', 'Konum: Saat Kulesi’ne 1 dakika; kordon, çarşı ve iskele yürüme mesafesinde.', 'Mutfaklı daireler: geniş yatak, çekyat, kendi mutfağınız; aileler için rahat.', 'Google’da 266 yorumla 4,8: “Her yere yürüyerek ulaşabildik. Sahibi ilgili ve yardımcı, ev gayet hijyenik.”', f'Evinizdesiniz: {ADR} · {TEL}'],
        post_alt='Akşam kordonda: Saat Kulesi’ne 1 dakika. Kinzi House.',
        post_note='Konum, oda donanımı, puan ve misafir sözü Google Haritalar ve Tripadvisor yorumlarından özetlendi. Logo ve Instagram hesabınızı bulamadığımız için renkler giriş fotoğrafınızdan öneri olarak hazırlandı.',
        music=[('Lo-fi şehir', 'Aramaya “lofi city morning” yazın. Sokak ve daire kareleri için.'), ('Akustik pop', 'Aramaya “acoustic happy” yazın. Aile tatili havası.'), ('Akşam caz', 'Aramaya “evening jazz piano” yazın. Kordon karesi için.')],
        caps=[('reel', 'Reels', f'Saat Kulesi’ne 1 dakika, kendi mutfağınız ve sakin bir sokak. 🗝️\nÇanakkale’de şehrin ortasında eviniz.\n\n📍 {ADR}\n📞 {TEL}\n\n#KinziHouse #Çanakkale #apartotel #ailetatili'),
              ('kar', 'Karusel', f'Çanakkale’ye ailece mi geliyorsunuz? 👨‍👩‍👧‍👦\nMutfaklı daireler, Saat Kulesi’ne 1 dakika ve Google’da 4,8.\nGezi planın için kaydet. 👇\n\n📍 {ADR}\n📞 {TEL}\n\n#KinziHouse #Çanakkale #Kemalpaşa #konaklama'),
              ('post', 'Tek gönderi', 'Akşam kordonda yürüyüş, sabah evinizde kahvaltı. 🌅\nÇanakkale’de en sevdiğin yürüyüş rotası hangisi? 👇\n\n#KinziHouse #Çanakkale #kordon')],
        sign='<p class="kimlik">Logo ve renk dosyanız olmadığı için “Kinzi House” yazı-imzası ve renkler giriş fotoğrafınızdan öneri olarak hazırlandı.</p>',
    ),
)
