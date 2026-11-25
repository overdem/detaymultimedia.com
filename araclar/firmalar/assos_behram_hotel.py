# tasarim/assos-behram-hotel.md — bronz/Ege laciverti/taş/amber/gece, Philosopher + Alegreya Sans + Imperial Script, tapınak alınlığı + sütun çizgileri
TEL = '0545 721 70 16'; ADR = 'İskele Mevkii, Behramkale · Assos'
PH = dict(liman='liman.png', sofra='sofra.png', gun='gunbatimi.png')
CSS = """
.s{background:var(--tas);color:var(--ege);font-family:var(--font-govde);text-align:center}
.t{font:700 124px/1.02 var(--font-baslik)}
.lab{font:500 22px var(--font-govde);letter-spacing:.3em;text-transform:uppercase}
.sc{font:400 104px/1 var(--font-vurgu);color:var(--amber)}
.bd{font:400 31px/1.45 var(--font-govde)}
.ped{display:block;margin:0 auto}
.r .t{font-size:86px}.r .sc{font-size:76px}.r .bd{font-size:24px}
"""
def ped(c='#B48461', w=220):
    h = w * 0.62
    return (f'<svg class="ped" width="{w}" height="{h:.0f}" viewBox="0 0 220 136"><g fill="none" stroke="{c}" stroke-width="4">'
            '<path d="M14 44 L110 6 L206 44 Z"/><path d="M14 52 H206 M14 128 H206"/>'
            '<path d="M44 58 V122 M88 58 V122 M132 58 V122 M176 58 V122"/></g></svg>')
def s1(P): return f"""<div class="s"><div class="ph" style="background-image:url('{P(PH['liman'])}')"></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:560px;background:linear-gradient(180deg,rgba(24,33,44,0),rgba(24,33,44,.94) 55%)"></div>
<div style="position:absolute;left:0;right:0;bottom:90px;color:var(--tas)">{ped()}<div class="t" style="margin-top:24px;font-size:104px;color:var(--tas)">Assos Behram</div><div class="sc" style="margin-top:6px;font-size:84px">antik limanda</div></div></div>"""
def s2(P): return f"""<div class="s" style="background:var(--ege);color:var(--tas)"><div style="position:absolute;left:110px;right:110px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center">
{ped('#B48461', 260)}<div class="lab" style="margin-top:50px;color:var(--amber)">Assos · Behramkale</div>
<div class="t" style="margin-top:34px;font-size:104px;color:var(--tas)">Tanrıların<br>dünyasında</div>
<div class="bd" style="margin-top:50px;font-size:34px">Antik Yunan tanrıları temalı odalar, yaşamdan keyif almayı bilen çiftler için. Aristo’nun yürüdüğü kıyıda.</div></div></div>"""
def s3(P): return f"""<div class="s"><div class="ph" style="background-image:url('{P(PH['sofra'])}');bottom:400px"></div>
<div style="position:absolute;left:90px;right:90px;bottom:80px"><div class="sc" style="color:var(--ege)">limanda akşam</div><div class="t" style="font-size:90px;margin-top:6px">Taze deniz ürünleri</div><div class="bd" style="margin-top:12px">Antik Liman’da, denizin hemen kıyısında sofra.</div></div></div>"""
def s4(P): return f"""<div class="s" style="background:var(--gece);color:var(--tas)"><div class="ph" style="background-image:url('{P(PH['gun'])}');bottom:420px"></div>
<div style="position:absolute;left:90px;right:90px;bottom:90px"><div class="t" style="font-size:96px;color:var(--bronz)">Ege’nin en güzel<br>gün batımı</div><div class="bd" style="margin-top:14px">Midilli’nin silüeti, antik liman ve sakin bir akşam.</div></div></div>"""
def s5(P): return f"""<div class="s"><div style="position:absolute;left:100px;right:100px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center">
{ped('#B48461', 240)}<div class="sc" style="margin-top:36px;color:var(--ege)">sizi bekliyoruz</div><div class="t" style="font-size:132px;margin-top:20px">Assos Behram</div><div class="lab" style="margin-top:10px">Hotel · Antik Liman</div>
<div style="width:120px;height:3px;background:var(--bronz);margin:56px auto"></div><div class="bd">{ADR}</div><div style="font:700 66px var(--font-baslik);margin-top:24px">{TEL}</div><div class="bd" style="margin-top:8px;font-size:26px">assosbehramhotel.com · WhatsApp’tan da yazabilirsiniz</div></div></div>"""
def post(P): return f"""<div class="s"><div class="ph" style="background-image:url('{P(PH['gun'])}')"></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:500px;background:linear-gradient(180deg,rgba(24,33,44,0),rgba(24,33,44,.93) 58%)"></div>
<div style="position:absolute;left:0;right:0;bottom:90px;color:var(--tas)"><div class="sc">iyi akşamlar Assos</div><div class="lab" style="margin-top:18px">Antik Liman · Assos Behram Hotel</div></div></div>"""
def ov(t=None, sc=None, bd=None):
    a = f'<div class="t">{t}</div>' if t else ''
    c = f'<div class="sc">{sc}</div>' if sc else ''
    b = f'<div class="bd" style="margin-top:10px">{bd}</div>' if bd else ''
    return f'<div class="s r" style="background:transparent;color:#EDE4D7"><div style="position:absolute;left:60px;right:60px;bottom:140px;background:rgba(24,33,44,.86);border-top:4px solid #B48461;padding:40px 30px">{c}{a}{b}</div></div>'
CFG = dict(
    slug='assos-behram-hotel', name='Assos Behram Hotel',
    fonts_url='https://fonts.googleapis.com/css2?family=Philosopher:wght@400;700&family=Alegreya+Sans:wght@400;500&family=Imperial+Script&display=swap',
    tokens='--bronz:#B48461;--ege:#1D3A57;--tas:#EDE4D7;--amber:#F2A848;--gece:#18212C;--font-baslik:"Philosopher",sans-serif;--font-govde:"Alegreya Sans",sans-serif;--font-vurgu:"Imperial Script",cursive;--zemin:#EDE4D7',
    css=CSS, slides=[s1, s2, s3, s4, s5], post=post,
    reel=[(PH['liman'], ov('Assos Behram', 'antik limanda')), (PH['sofra'], ov('Limanda akşam', None, 'Taze deniz ürünleri')), (PH['gun'], ov('Ege’nin gün batımı', None, 'Tanrıların dünyasında bir gece')), (PH['liman'], ov('Assos Behram', 'sizi bekliyoruz', f'{ADR}<br>{TEL}'))],
    page=dict(
        vars='  color-scheme: light;\n  --bg: #EDE4D7;\n  --panel: #F7F2EA;\n  --line: #d5c7b4;\n  --text: #1D3A57;\n  --muted: #4b5866;\n  --accent: #1D3A57;\n  --accent-ink: #EDE4D7;\n  --display: "Philosopher", sans-serif;\n  --display-w: 700;\n  --body: "Alegreya Sans", sans-serif;\n  --vurgu: "Imperial Script", cursive;',
        extra_css='h1 em { font-family: var(--vurgu); font-style: normal; font-weight: 400; color: #1D3A57; font-size: 1.25em; display: block; }\n.shot { border-radius: 4px; border-top: 4px solid #B48461; }\nvideo.shot { border-top: none; border-radius: 12px; }\n.kimlik { font-size: 12px; color: #4b5866; margin: 0; }\n.motif { display: block; margin: 0 auto; }\n',
        motif='<svg class="motif" aria-hidden="true" width="66" height="41" viewBox="0 0 220 136"><g fill="none" stroke="#B48461" stroke-width="8"><path d="M14 44 L110 6 L206 44 Z"/><path d="M14 52 H206 M14 128 H206"/><path d="M44 58 V122 M88 58 V122 M132 58 V122 M176 58 V122"/></g></svg>',
        lede='Haftalık paylaşımların nasıl görüneceğini göstermek için hazırladığımız kısa bir reels, beş karelik bir karusel ve tek gönderi; logonuzdaki tapınak bronzu, Antik Liman’ın akşamı ve tanrılar temalı odalarınızın hikâyesiyle.',
        reel_meta='12 sn · dikey',
        reel_note='Liman akşamı, deniz ürünleri sofrası, gün batımı ve iletişim. Video sessizdir; müzik Instagram’da paylaşırken eklenir.',
        alts=['Assos Behram Hotel: antik limanda.', 'Tanrıların dünyasında: Antik Yunan tanrıları temalı odalar, Aristo’nun yürüdüğü kıyıda.', 'Limanda akşam: Antik Liman’da taze deniz ürünleri.', 'Ege’nin en güzel gün batımı: Midilli silüeti ve antik liman.', f'Sizi bekliyoruz: {ADR} · {TEL}'],
        post_alt='İyi akşamlar Assos: Antik Liman, Assos Behram Hotel.',
        post_note='Tanrılar teması, çiftlere özel konsept, Aristo ve liman restoranı web sitenizden; adres ve telefon Google Haritalar kaydınızdan alındı. Renkler logonuzun bronzu ve sitenizdeki amber düğmeden.',
        music=[('Antik lir', 'Aramaya “ancient greek lyre” yazın. Tanrılar teması için.'), ('Ege akşamı', 'Aramaya “aegean sunset instrumental” yazın. Gün batımı karesi için.'), ('Sakin gitar', 'Aramaya “romantic guitar” yazın. Çiftler için.')],
        caps=[('reel', 'Reels', f'Antik limanda bir akşam: taze deniz ürünleri, gün batımı ve tanrıların dünyası. 🏛️🌅\n\n📍 {ADR}\n📞 {TEL}\n\n#AssosBehram #Assos #Behramkale #AntikLiman'),
              ('kar', 'Karusel', f'Aristo’nun yürüdüğü kıyıda, tanrıların dünyasında bir kaçamak. 🏛️\nAntik Yunan tanrıları temalı odalar, liman sofrası ve Ege’nin gün batımı.\nKaçamak planın için kaydet. 👇\n\n📍 {ADR}\n📞 {TEL}\n\n#AssosBehram #Assos #Çanakkale #çiftlericin'),
              ('post', 'Tek gönderi', 'İyi akşamlar Assos! 🌅\nGün batımını en çok nereden izlemeyi seversin? 👇\n\n#AssosBehram #Assos #günbatımı')],
        sign='<p class="kimlik">Tapınak motifi logonuza gönderme olarak sade çizgilerle hazırlandı; logo dosyanız gelince o kullanılır.</p>',
    ),
)
