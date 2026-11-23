# tasarim/revgan-canakkale.md — tabya/derin/şeftali/krem/bronz, Cinzel + Libre Bodoni + Schibsted Grotesk, yarım güneş + dalga motifi
TEL = '0530 132 10 17'; ADR = 'Anadolu Hamidiye Tabyası · Barbaros'
PH = dict(bahce='6683dfe0.png', kahvalti='KAHVALTI.png', aksam='AKSAM.png', kutlama='KUTLAMA.png')
def sun(w=150, c='var(--seftali)'):
    h = w // 2
    waves = ''.join(f'<path d="M0 {h+10+i*14} q {w/8} -8 {w/4} 0 t {w/4} 0 t {w/4} 0 t {w/4} 0" stroke="{c}" stroke-width="{max(2,w//50)}" fill="none"/>' for i in range(3))
    return f'<svg width="{w}" height="{h+52}" viewBox="0 0 {w} {h+52}"><path d="M0 {h} A{h} {h} 0 0 1 {w} {h} Z" fill="{c}"/>{waves}</svg>'
CSS = """
.s{background:var(--tabya);color:var(--krem);font-family:var(--font-govde);text-align:center}
.fade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(11,47,46,.55) 0%,rgba(11,47,46,0) 22%,rgba(11,47,46,0) 46%,rgba(10,82,80,.92) 78%,#0A5250 100%)}
.t{font:400 76px/1.1 var(--font-baslik);letter-spacing:.16em;text-transform:uppercase}
.it{font:italic 400 60px/1.1 var(--font-govde);color:var(--seftali)}
.bd{font:400 30px/1.45 var(--font-govde)}
.lbl{font:500 20px var(--font-vurgu);letter-spacing:.28em;text-transform:uppercase}
.arch{position:absolute;background-size:cover;background-position:center;border-radius:420px 420px 0 0}
.r .t{font-size:52px}.r .it{font-size:46px}.r .bd{font-size:23px}.r .lbl{font-size:15px}
"""
def s1(P): return f"""<div class="s"><div class="ph" style="background-image:url('{P(PH['bahce'])}')"></div><div class="fade"></div>
<div class="lbl" style="position:absolute;left:0;right:0;top:76px">Revgan · Çanakkale</div>
<div style="position:absolute;left:70px;right:70px;bottom:100px">{sun(140)}<div class="t" style="margin-top:26px">Boğaz kıyısında</div><div class="it" style="margin-top:10px">tabyanın içinde</div><div class="bd" style="margin-top:22px">Anadolu Hamidiye Tabyası’nda, denize sıfır bahçe.</div></div></div>"""
def arch(P, ph, lbl, t, it, bd):
    return f"""<div class="s"><div class="arch" style="left:130px;right:130px;top:90px;height:820px;background-image:url('{P(ph)}')"></div>
<div style="position:absolute;left:70px;right:70px;top:950px"><div class="lbl" style="color:var(--seftali)">{lbl}</div><div class="t" style="margin-top:18px;font-size:66px">{t}</div><div class="it" style="font-size:50px">{it}</div><div class="bd" style="margin-top:14px;font-size:27px">{bd}</div></div></div>"""
def s2(P): return arch(P, PH['kahvalti'], 'Her gün 08:00’den', 'Kahvaltı', 'deniz kenarında', 'Pazar günleri açık büfe kahvaltı.')
def s3(P): return arch(P, PH['aksam'], 'Akşam', 'Türk mutfağı', 'mum ışığında', 'Gece yarısına kadar, Boğaz’a karşı.')
def s4(P): return f"""<div class="s"><div class="ph" style="background-image:url('{P(PH['kutlama'])}')"></div><div class="fade"></div>
<div class="lbl" style="position:absolute;left:0;right:0;top:76px">Organizasyon</div>
<div style="position:absolute;left:70px;right:70px;bottom:100px"><div class="it">Söz, nişan,</div><div class="t" style="margin-top:8px">doğum günü</div><div class="bd" style="margin-top:20px">Grup yemekleri ve set menüler; sofrayı birlikte kuralım.</div></div></div>"""
def s5(P): return f"""<div class="s" style="background:var(--derin)"><div style="position:absolute;left:70px;right:70px;top:180px">{sun(220)}
<div class="t" style="margin-top:40px;font-size:96px;letter-spacing:.24em">Revgan</div><div class="lbl" style="margin-top:6px;color:var(--seftali)">Çanakkale</div>
<div style="width:160px;height:1px;background:var(--seftali);margin:56px auto"></div>
<div class="lbl" style="font-size:22px">Rezervasyon</div><div style="font:400 64px var(--font-govde);margin-top:16px;color:var(--seftali)">{TEL}</div>
<div class="bd" style="margin-top:28px">Her gün 08:00 – 00:00<br>Anadolu Hamidiye Tabyası, Barbaros</div></div></div>"""
def post(P): return f"""<div class="s" style="background:var(--krem);color:var(--derin)"><div class="arch" style="left:110px;right:110px;top:80px;height:880px;background-image:url('{P(PH['kahvalti'])}')"></div>
<div style="position:absolute;left:70px;right:70px;top:1000px"><div class="lbl" style="color:var(--bronz)">Pazar</div><div class="t" style="margin-top:12px;font-size:64px;color:var(--tabya)">Açık büfe</div><div class="it" style="color:var(--bronz);font-size:52px">kahvaltı, denize karşı</div></div></div>"""
def ov(t, it=None, bd=None):
    i = f'<div class="it" style="margin-top:6px">{it}</div>' if it else ''
    b = f'<div class="bd" style="margin-top:14px">{bd}</div>' if bd else ''
    return f'<div class="s r" style="background:transparent"><div class="fade"></div><div class="lbl" style="position:absolute;left:0;right:0;top:64px">Revgan · Çanakkale</div><div style="position:absolute;left:40px;right:40px;bottom:130px">{sun(100)}<div class="t" style="margin-top:18px">{t}</div>{i}{b}</div></div>'
CFG = dict(
    slug='revgan-canakkale', name='Revgan Çanakkale',
    fonts_url='https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600&family=Libre+Bodoni:ital,wght@0,400;1,400&family=Schibsted+Grotesk:wght@500&display=swap',
    tokens='--tabya:#0A5250;--derin:#0B2F2E;--seftali:#F0C1A6;--krem:#F6F0E7;--bronz:#8A6633;--font-baslik:"Cinzel",serif;--font-govde:"Libre Bodoni",Georgia,serif;--font-vurgu:"Schibsted Grotesk",sans-serif;--zemin:#0A5250',
    css=CSS, slides=[s1, s2, s3, s4, s5], post=post,
    reel=[(PH['bahce'], ov('Boğaz kıyısında', 'tabyanın içinde')),
          (PH['kahvalti'], ov('Kahvaltı', 'her gün 08:00’den')),
          (PH['aksam'], ov('Akşam', 'mum ışığında')),
          (PH['kutlama'], ov('Söz · nişan', 'doğum günü')),
          (PH['bahce'], ov('Rezervasyon', None, f'{TEL}<br>Anadolu Hamidiye Tabyası'))],
    page=dict(
        vars='  color-scheme: dark;\n  --bg: #0A5250;\n  --panel: #0B2F2E;\n  --line: #2c6b68;\n  --text: #F6F0E7;\n  --muted: #c9d8d4;\n  --accent: #F0C1A6;\n  --accent-ink: #0B2F2E;\n  --display: "Cinzel", serif;\n  --body: "Libre Bodoni", Georgia, serif;\n  --vurgu: "Schibsted Grotesk", sans-serif;',
        extra_css='h1 { letter-spacing: .08em; }\nh1 em { font-family: var(--body); color: #F0C1A6; display: block; letter-spacing: 0; }\n.eyebrow, .meta, h3 { font-family: var(--vurgu); }\n.motif svg { display: block; margin: 0 auto; }\n',
        motif=f'<div class="motif" aria-hidden="true">{sun(70, "#F0C1A6")}</div>',
        lede='Haftalık paylaşımların nasıl görüneceğini göstermek için hazırladığımız kısa bir reels, beş karelik bir karusel ve tek gönderi; logonuzdaki petrol yeşili, şeftali güneş ve dalgalarla.',
        reel_meta='15 sn · dikey',
        reel_note='Tabyadaki bahçe, deniz kenarında kahvaltı, akşam sofrası ve organizasyon; 5 sahnede Revgan. Video sessizdir; müzik Instagram’da paylaşırken eklenir.',
        alts=['Boğaz kıyısında, tabyanın içinde. Anadolu Hamidiye Tabyası’nda denize sıfır bahçe.', 'Her gün 08:00’den: kahvaltı, deniz kenarında. Pazar açık büfe.', 'Akşam: Türk mutfağı, mum ışığında, gece yarısına kadar.', 'Organizasyon: söz, nişan, doğum günü; grup yemekleri ve set menüler.', f'Revgan · Rezervasyon {TEL} · Her gün 08:00–00:00 · {ADR}'],
        post_alt='Pazar: açık büfe kahvaltı, denize karşı.',
        post_note='Saatler, Pazar açık büfe kahvaltı ve organizasyon bilgisi web sitenizden; telefon Google Haritalar kaydınızdan alındı.',
        music=[('Ud ve deniz', 'Aramaya “oud instrumental calm” yazın. Tabya ve Boğaz’a yakışır.'), ('Sabah akustik', 'Aramaya “acoustic morning” yazın. Kahvaltı sahnesi için.'), ('Zarif piyano', 'Aramaya “elegant piano” yazın. Organizasyon kareleri için.')],
        caps=[('reel', 'Reels', f'Boğaz kıyısında, tabyanın içinde. 🌅\nKahvaltıdan akşam yemeğine, her gün 08:00 – 00:00.\n\n📍 Anadolu Hamidiye Tabyası, Barbaros\n📞 Rezervasyon: {TEL}\n\n#Revgan #Çanakkale #kahvaltı #boğaz #tabya'),
              ('kar', 'Karusel', f'Revgan’da bir gün. 🌊\nSabah kahvaltı, akşam mum ışığında yemek, özel günlerde sofrayı birlikte kuralım.\nPazar kahvaltısı için kaydet. 👇\n\n📍 {ADR}\n⏰ Her gün 08:00 – 00:00\n📞 {TEL}\n\n#Revgan #Çanakkale #çanakkalekahvaltı #nişanyemeği'),
              ('post', 'Tek gönderi', f'Pazar günleri açık büfe kahvaltı, denize karşı. ☕️\nMasanızı şimdiden ayırtın.\n\n📞 {TEL}\n📍 Anadolu Hamidiye Tabyası\n\n#Revgan #pazarkahvaltısı #Çanakkale')],
    ),
)
