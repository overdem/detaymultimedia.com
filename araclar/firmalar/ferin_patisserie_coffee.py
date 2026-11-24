# tasarim/ferin-patisserie-coffee.md — bordo/fildişi/gül kurusu/kaymak/altın, EB Garamond + Be Vietnam Pro + Parisienne, ince çift çerçeve + oval pencere
TEL = '0501 621 91 17'; ADR = 'Dibek Sk. No:22 · Kemalpaşa'
PH = dict(tart='tart.png', vitrin='vitrin.png', focaccia='focaccia.png')
CSS = """
.s{background:var(--fildisi);color:var(--bordo);font-family:var(--font-govde);text-align:center}
.fr{position:absolute;inset:44px;border:1px solid var(--bordo)}.fr2{position:absolute;inset:56px;border:3px solid var(--bordo)}
.t{font:500 120px/1 var(--font-baslik);letter-spacing:.12em;text-transform:uppercase}
.lab{font:600 21px var(--font-govde);letter-spacing:.34em;text-transform:uppercase}
.sc{font:400 92px/1 var(--font-vurgu);color:var(--bordo)}
.bd{font:400 29px/1.5 var(--font-govde)}
.oval{position:absolute;border-radius:50%;background-size:cover;background-position:center}
.rule{width:110px;height:2px;background:var(--gul);margin:0 auto}
.r .t{font-size:84px}.r .sc{font-size:70px}.r .bd{font-size:23px}.r .lab{font-size:16px}
"""
def s1(P): return f"""<div class="s"><div class="fr"></div><div class="fr2"></div>
<div class="oval" style="left:230px;top:140px;width:620px;height:780px;background-image:url('{P(PH['tart'])}')"></div>
<div style="position:absolute;left:0;right:0;top:965px"><div class="t" style="font-size:132px">Ferin</div><div class="lab" style="margin-top:12px"><span lang="en">Patisserie &amp; Coffee</span></div><div class="sc" style="margin-top:22px;font-size:72px">el yapımı, taze</div></div></div>"""
def s2(P): return f"""<div class="s" style="background:var(--bordo);color:var(--fildisi)"><div class="ph" style="background-image:url('{P(PH['tart'])}');bottom:420px"></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:420px;padding:60px 80px"><div class="lab" style="color:var(--gul)">Vitrinden</div><div class="t" style="margin-top:20px;color:var(--fildisi);font-size:104px">Kirazlı tart</div><div class="bd" style="margin-top:14px;color:var(--kaymak)">Tereyağlı hamur, parlak kirazlar.</div></div></div>"""
def s3(P): return f"""<div class="s" style="background:var(--kaymak)"><div class="ph" style="background-image:url('{P(PH['vitrin'])}');left:80px;right:80px;top:80px;bottom:430px"></div><div style="position:absolute;left:68px;right:68px;top:68px;bottom:418px;border:1px solid var(--bordo)"></div>
<div style="position:absolute;left:0;right:0;bottom:90px"><div class="sc" style="font-size:84px">Büşra Hanım’ın elinden</div><div class="rule" style="margin:26px auto"></div><div class="bd">Vitrindeki her tatlı burada, el yapımı hazırlanır.</div></div></div>"""
def s4(P): return f"""<div class="s"><div class="ph" style="background-image:url('{P(PH['focaccia'])}')"></div>
<div style="position:absolute;left:90px;right:90px;bottom:90px;background:var(--fildisi);padding:46px 40px"><div style="position:absolute;inset:12px;border:1px solid var(--bordo)"></div><div class="lab" style="color:var(--bordo)">Tatlı kadar tuzlu</div><div class="t" style="margin-top:16px;font-size:96px"><span lang="en">Focaccia</span></div><div class="bd" style="margin-top:12px">Yanına bir flat white.</div></div></div>"""
def s5(P): return f"""<div class="s" style="background:var(--bordo);color:var(--fildisi)"><div class="fr" style="border-color:var(--gul)"></div><div class="fr2" style="border-color:var(--fildisi)"></div>
<div style="position:absolute;left:100px;right:100px;top:250px"><div class="sc" style="color:var(--gul)">bekleriz</div><div class="t" style="font-size:150px;margin-top:30px;color:var(--fildisi)">Ferin</div><div class="lab" style="margin-top:12px;color:var(--kaymak)"><span lang="en">Patisserie &amp; Coffee</span></div>
<div class="rule" style="margin:60px auto"></div><div class="bd" style="color:var(--kaymak)">Dibek Sk. No:22, Kemalpaşa<br>08:30’dan itibaren</div><div style="font:500 60px var(--font-baslik);letter-spacing:.08em;margin-top:30px">{TEL}</div></div></div>"""
def post(P): return f"""<div class="s"><div class="fr"></div><div class="fr2"></div><div class="oval" style="left:170px;top:130px;width:740px;height:880px;background-image:url('{P(PH['vitrin'])}')"></div>
<div style="position:absolute;left:0;right:0;top:1060px"><div class="sc" style="font-size:96px">bugün vitrinde ne var?</div><div class="lab" style="margin-top:20px">Ferin · Kemalpaşa</div></div></div>"""
def ov(t=None, sc=None, bd=None):
    a = f'<div class="t">{t}</div>' if t else ''
    c = f'<div class="sc">{sc}</div>' if sc else ''
    b = f'<div class="bd" style="margin-top:10px">{bd}</div>' if bd else ''
    return f'<div class="s r" style="background:transparent"><div style="position:absolute;left:60px;right:60px;bottom:140px;background:rgba(247,241,232,.95);padding:44px 30px"><div style="position:absolute;inset:10px;border:1px solid var(--bordo)"></div>{c}{a}{b}</div></div>'
CFG = dict(
    slug='ferin-patisserie-coffee', name='ferin | patisserie & coffee',
    fonts_url='https://fonts.googleapis.com/css2?family=EB+Garamond:wght@500;600&family=Be+Vietnam+Pro:wght@400;600&family=Parisienne&display=swap',
    tokens='--bordo:#4A1B1B;--fildisi:#F7F1E8;--gul:#C9928A;--kaymak:#EDE2D3;--altin:#A8834F;--font-baslik:"EB Garamond",serif;--font-govde:"Be Vietnam Pro",sans-serif;--font-vurgu:"Parisienne",cursive;--zemin:#F7F1E8',
    css=CSS, slides=[s1, s2, s3, s4, s5], post=post,
    reel=[(PH['tart'], ov('Ferin', 'el yapımı')), (PH['vitrin'], ov(None, 'Büşra Hanım’ın elinden', 'Her tatlı burada hazırlanır')), (PH['focaccia'], ov('<span lang="en">Focaccia</span>', None, 'Yanına bir flat white')), (PH['tart'], ov('Ferin', 'bekleriz', f'{ADR}<br>{TEL}'))],
    page=dict(
        vars='  color-scheme: light;\n  --bg: #F7F1E8;\n  --panel: #FCF8F2;\n  --line: #dcc9bd;\n  --text: #4A1B1B;\n  --muted: #6b3f3a;\n  --accent: #4A1B1B;\n  --accent-ink: #F7F1E8;\n  --display: "EB Garamond", serif;\n  --display-w: 500;\n  --body: "Be Vietnam Pro", sans-serif;\n  --vurgu: "Parisienne", cursive;',
        extra_css='h1 { letter-spacing: .02em; }\nh1 em { font-family: var(--vurgu); font-style: normal; font-weight: 400; color: #8f4b45; font-size: 1.2em; display: block; }\nh2 { letter-spacing: .1em; text-transform: uppercase; font-size: 22px; }\n.shot { border-radius: 2px; outline: 1px solid var(--text); outline-offset: 5px; }\n.kimlik { font-size: 12px; color: #6b3f3a; margin: 0; }\n.motif { font-family: var(--display); font-size: 40px; line-height: 1; color: var(--text); }\n',
        motif='<div class="motif" aria-hidden="true">ƒ</div>',
        lede='Haftalık paylaşımların nasıl görüneceğini göstermek için hazırladığımız kısa bir reels, beş karelik bir karusel ve tek gönderi; logonuzdaki bordo, klasik serif yazı ve el yapımı tatlılarınızın zarafetiyle.',
        reel_meta='12 sn · dikey',
        reel_note='Kirazlı tart, el yapımı vitrin, focaccia ve adres. Video sessizdir; müzik Instagram’da paylaşırken eklenir.',
        alts=['Ferin Patisserie & Coffee: el yapımı, taze.', 'Vitrinden: kirazlı tart.', 'Büşra Hanım’ın elinden: vitrindeki her tatlı burada hazırlanır.', 'Tatlı kadar tuzlu: focaccia ve flat white.', f'Bekleriz: {ADR} · 08:30’dan itibaren · {TEL}'],
        post_alt='Bugün vitrinde ne var? Ferin, Kemalpaşa.',
        post_note='Adres, telefon ve açılış saati Google Haritalar kaydınızdan; kirazlı tart menünüzün öne çıkanlarından, el yapımı tatlılar ve focaccia misafir yorumlarından alındı.',
        music=[('Fransız kafe', 'Aramaya “french cafe accordion” yazın. Pastane havası.'), ('Klasik piyano', 'Aramaya “soft piano” yazın. Yakın plan tatlılar için.'), ('Caz', 'Aramaya “cafe jazz” yazın. Sakin ve şık.')],
        caps=[('reel', 'Reels', f'El yapımı, taze. 🍒\nKirazlı tart, focaccia ve vitrindeki her şey Büşra Hanım’ın elinden.\n\n📍 {ADR}\n📞 {TEL}\n\n#Ferin #FerinPatisserie #Çanakkale #pastane #tart'),
              ('kar', 'Karusel', f'Ferin’de bir sabah. 🤍\nKirazlı tart, el yapımı vitrin ve tatlı kadar tuzlu bir focaccia.\nBir sonraki tatlı molan için kaydet. 👇\n\n📍 {ADR}\n⏰ 08:30’dan itibaren\n📞 {TEL}\n\n#Ferin #Çanakkale #çanakkalepastane #Kemalpaşa'),
              ('post', 'Tek gönderi', 'Bugün vitrinde ne var? 🍰\nTahminini yorumlara yaz, gelip bak. 👇\n\n📍 Dibek Sk. No:22, Kemalpaşa\n\n#Ferin #Çanakkale #tatlı')],
        sign='<p class="kimlik">Renk ve yazı karakteri web sitenizdeki “fJ” logodan; vektör logo dosyanızla birebir uygularız.</p>',
    ),
)
