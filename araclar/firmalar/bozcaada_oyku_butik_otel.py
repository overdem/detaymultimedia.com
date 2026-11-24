# tasarim/bozcaada-oyku-butik-otel.md — gece/fener/taş/badana/asma (öneri), Vollkorn + Libre Franklin + Dancing Script, kitap sayfası çerçevesi + kemerli pencere
TEL = '0541 449 06 51'; ADR = 'Camii Sk., Alaybey · Bozcaada'
PH = dict(kahvalti='kahvalti.png', gece='gece.png', oda='oda.png')
CSS = """
.s{background:var(--badana);color:var(--gece);font-family:var(--font-govde);text-align:center}
.pg{position:absolute;inset:40px;border:1.5px solid rgba(46,26,20,.55)}
.t{font:800 160px/.95 var(--font-baslik)}
.lab{font:600 22px var(--font-govde);letter-spacing:.32em;text-transform:uppercase}
.sc{font:600 82px/1 var(--font-vurgu);color:var(--fener)}
.bd{font:400 31px/1.45 var(--font-govde)}
.arch{position:absolute;background-size:cover;background-position:center;border-radius:420px 420px 10px 10px}
.lamp{display:inline-block;width:18px;height:18px;border-radius:50%;background:var(--fener);box-shadow:0 0 22px 6px rgba(227,164,71,.55)}
.r .t{font-size:104px}.r .sc{font-size:62px}.r .bd{font-size:24px}.r .lab{font-size:17px}
"""
def s1(P): return f"""<div class="s" style="background:var(--gece);color:var(--badana)"><div class="pg" style="border-color:rgba(251,247,240,.35)"></div>
<div class="arch" style="left:190px;right:190px;top:110px;height:800px;background-image:url('{P(PH['gece'])}')"></div>
<div style="position:absolute;left:0;right:0;top:950px"><span class="lamp"></span><div class="t" style="margin-top:14px;color:var(--badana)">Öykü</div><div class="lab" style="margin-top:8px;color:var(--tas)">Butik Otel · Bozcaada</div><div class="sc" style="margin-top:22px;font-size:66px">limana bir dakika</div></div></div>"""
def s2(P): return f"""<div class="s"><div class="ph" style="background-image:url('{P(PH['kahvalti'])}')"></div>
<div style="position:absolute;left:80px;right:80px;bottom:80px;background:var(--badana);padding:48px 40px;border-radius:6px"><div class="sc" style="color:var(--asma)">Emel Hanım’ın sofrası</div><div class="t" style="font-size:108px;margin-top:12px">Ada kahvaltısı</div><div class="bd" style="margin-top:12px">Misafirlerimizin “efsane” dediği sabahlar.</div></div></div>"""
def s3(P): return f"""<div class="s" style="background:var(--tas)"><div class="arch" style="left:150px;right:150px;top:90px;height:820px;background-image:url('{P(PH['oda'])}')"></div>
<div style="position:absolute;left:0;right:0;top:960px"><div class="t" style="font-size:104px">Ev gibi</div><div class="bd" style="margin-top:14px">Tertemiz odalar, sessiz bir sokak, güler yüz.</div></div></div>"""
def s4(P): return f"""<div class="s" style="background:var(--gece);color:var(--badana)"><div class="pg" style="border-color:rgba(251,247,240,.35)"></div><div style="position:absolute;left:110px;right:110px;top:200px">
<div class="lab" style="color:var(--fener)">Konum</div><div class="t" style="font-size:130px;margin-top:30px;color:var(--badana)">Adanın tam ortasında</div>
<div style="margin-top:70px;display:flex;flex-direction:column;gap:34px">
<div class="bd" style="font-size:36px"><span class="lamp" style="width:14px;height:14px;margin-right:18px;vertical-align:middle"></span>Limana 1 dakika</div>
<div class="bd" style="font-size:36px"><span class="lamp" style="width:14px;height:14px;margin-right:18px;vertical-align:middle"></span>Feribot iskelesine 3 dakika</div>
<div class="bd" style="font-size:36px"><span class="lamp" style="width:14px;height:14px;margin-right:18px;vertical-align:middle"></span>Arnavut kaldırımlı Camii Sokak</div></div></div></div>"""
def s5(P): return f"""<div class="s"><div class="pg"></div><div style="position:absolute;left:100px;right:100px;top:230px">
<span class="lamp"></span><div class="sc" style="margin-top:30px;color:var(--asma)">sizi bekliyoruz</div><div class="t" style="font-size:200px;margin-top:20px">Öykü</div><div class="lab" style="margin-top:10px">Butik Otel · Bozcaada</div>
<div style="width:120px;height:2px;background:var(--fener);margin:60px auto"></div><div class="bd">Camii Sokak, Alaybey · Bozcaada</div><div style="font:800 66px var(--font-baslik);margin-top:30px">{TEL}</div><div class="bd" style="margin-top:10px;font-size:26px">WhatsApp’tan da yazabilirsiniz</div></div></div>"""
def post(P): return f"""<div class="s"><div class="ph" style="background-image:url('{P(PH['kahvalti'])}')"></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:520px;background:linear-gradient(180deg,rgba(46,26,20,0),rgba(46,26,20,.92) 55%)"></div>
<div style="position:absolute;left:0;right:0;bottom:90px;color:var(--badana)"><div class="sc">günaydın Bozcaada</div><div class="lab" style="margin-top:18px;color:var(--tas)">Kahvaltı hazır · Öykü Butik Otel</div></div></div>"""
def ov(t=None, sc=None, bd=None):
    a = f'<div class="t">{t}</div>' if t else ''
    c = f'<div class="sc" style="color:var(--asma)">{sc}</div>' if sc else ''
    b = f'<div class="bd" style="margin-top:10px">{bd}</div>' if bd else ''
    return f'<div class="s r" style="background:transparent"><div style="position:absolute;left:60px;right:60px;bottom:140px;background:rgba(251,247,240,.95);border-radius:300px 300px 8px 8px;padding:70px 30px 40px">{c}{a}{b}</div></div>'
CFG = dict(
    slug='bozcaada-oyku-butik-otel', name='Bozcaada Öykü Butik Otel',
    fonts_url='https://fonts.googleapis.com/css2?family=Vollkorn:wght@600;800&family=Libre+Franklin:wght@400;600&family=Dancing+Script:wght@600&display=swap',
    tokens='--gece:#2E1A14;--fener:#E3A447;--tas:#C9B49A;--badana:#FBF7F0;--asma:#55663F;--font-baslik:"Vollkorn",serif;--font-govde:"Libre Franklin",sans-serif;--font-vurgu:"Dancing Script",cursive;--zemin:#FBF7F0',
    css=CSS, slides=[s1, s2, s3, s4, s5], post=post,
    reel=[(PH['gece'], ov('Öykü', 'limana bir dakika')), (PH['kahvalti'], ov('Ada kahvaltısı', 'Emel Hanım’ın sofrası')), (PH['oda'], ov('Ev gibi', None, 'Tertemiz odalar, sessiz sokak')), (PH['gece'], ov('Öykü', 'sizi bekliyoruz', f'{ADR}<br>{TEL}'))],
    page=dict(
        vars='  color-scheme: light;\n  --bg: #FBF7F0;\n  --panel: #FFFDF9;\n  --line: #ddcdb8;\n  --text: #2E1A14;\n  --muted: #5b4237;\n  --accent: #2E1A14;\n  --accent-ink: #FBF7F0;\n  --display: "Vollkorn", serif;\n  --display-w: 800;\n  --body: "Libre Franklin", sans-serif;\n  --vurgu: "Dancing Script", cursive;',
        extra_css='h1 em { font-family: var(--vurgu); font-style: normal; font-weight: 600; color: #55663F; font-size: 1.05em; display: block; }\n.shot { border-radius: 260px 260px 10px 10px; }\nvideo.shot { border-radius: 14px; }\n.kimlik { font-size: 12px; color: #5b4237; margin: 0; }\n.motif { width: 14px; height: 14px; border-radius: 50%; margin: 0 auto; background: #E3A447; box-shadow: 0 0 18px 5px rgba(227,164,71,.5); }\n',
        motif='<div class="motif" aria-hidden="true"></div>',
        lede='Haftalık paylaşımların nasıl görüneceğini göstermek için hazırladığımız kısa bir reels, beş karelik bir karusel ve tek gönderi; Instagram’daki fenerli taş bina fotoğrafınızın ada akşamı tonları ve ünlü kahvaltınızla.',
        reel_meta='12 sn · dikey',
        reel_note='Fenerli taş bina, ada kahvaltısı, oda ve iletişim. Video sessizdir; müzik Instagram’da paylaşırken eklenir.',
        alts=['Öykü Butik Otel, Bozcaada: limana bir dakika.', 'Emel Hanım’ın sofrası: misafirlerin “efsane” dediği ada kahvaltısı.', 'Ev gibi: tertemiz odalar, sessiz bir sokak, güler yüz.', 'Konum: limana 1 dakika, feribot iskelesine 3 dakika, Arnavut kaldırımlı Camii Sokak.', f'Sizi bekliyoruz: {ADR} · {TEL}'],
        post_alt='Günaydın Bozcaada: kahvaltı hazır. Öykü Butik Otel.',
        post_note='Adres, telefon ve konum bilgisi Google Haritalar kaydınızdan; kahvaltı, Emel Hanım ve “ev gibi” misafir yorumlarından alındı. Logonuz olmadığı için yazı-imza öneri olarak hazırlandı.',
        music=[('Ege akustik', 'Aramaya “aegean acoustic” yazın. Ada sabahına uyar.'), ('Yunan bouzouki', 'Aramaya “bouzouki instrumental” yazın. Bozcaada havası.'), ('Sakin gitar', 'Aramaya “soft guitar morning” yazın. Kahvaltı kareleri için.')],
        caps=[('reel', 'Reels', f'Limana bir dakika, kahvaltısı efsane. 🏝️☕️\nBozcaada’da ev gibi bir otel.\n\n📍 {ADR}\n📞 {TEL}\n\n#ÖyküButikOtel #Bozcaada #bozcaadakahvaltı #butikotel'),
              ('kar', 'Karusel', f'Bozcaada’da bir sabah. 🤍\nEmel Hanım’ın sofrası, tertemiz odalar ve adanın tam ortasında sessiz bir sokak.\nAda planın için kaydet. 👇\n\n📍 {ADR}\n📞 {TEL}\n\n#ÖyküButikOtel #Bozcaada #Çanakkale #adatatili'),
              ('post', 'Tek gönderi', 'Günaydın Bozcaada! ☀️\nKahvaltı hazır; sen hangi reçelle başlarsın? 👇\n\n#ÖyküButikOtel #Bozcaada #kahvaltı')],
        sign='<p class="kimlik">Logo dosyanız olmadığı için “Öykü” yazı-imzası ve renkler fenerli bina fotoğrafınızdan öneri olarak hazırlandı.</p>',
    ),
)
