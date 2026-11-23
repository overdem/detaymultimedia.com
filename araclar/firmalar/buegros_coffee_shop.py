# tasarim/buegros-coffee-shop.md — espresso/süt/kraft, Alfa Slab One + Rethink Sans + Tenor Sans, kraft etiket motifi, s/b ağırlıklı foto
TEL = '0530 495 56 75'; ADR = 'Çarşı Cd. No:84 · Fevzipaşa'
CSS = """
.s{background:var(--sut);color:var(--espresso);font-family:var(--font-govde)}
.bw{filter:grayscale(.82) contrast(1.12) brightness(.98)}
.t{font:400 120px/.95 var(--font-baslik);letter-spacing:-.01em}
.up{font:400 22px var(--font-vurgu);letter-spacing:.24em;text-transform:uppercase}
.bd{font:400 30px/1.45 var(--font-govde)}
.lab{position:absolute;background:var(--kraft);color:var(--espresso);border:4px solid var(--espresso);padding:28px 34px;box-shadow:10px 10px 0 var(--espresso)}
.lab .t{font-size:64px}
.lab .up{font-size:19px;margin-bottom:12px}
.fr{position:absolute;background-size:cover;background-position:center;border:4px solid var(--espresso)}
.r .t{font-size:84px}.r .lab .t{font-size:50px}.r .up{font-size:15px}.r .bd{font-size:22px}
"""
def s1(P): return f"""<div class="s"><div style="position:absolute;left:70px;top:70px;right:70px"><div class="up">Çarşı Caddesi · Fevzipaşa</div><div class="t" style="margin-top:22px">BİR FİNCAN<br>MOLA</div></div>
<div class="fr bw" style="left:70px;right:70px;top:420px;bottom:70px;background-image:url('{P('ca4c06ec.png')}')"></div>
<div class="lab" style="right:110px;bottom:120px;padding:18px 26px"><div class="up" style="margin:0">Flat white</div></div></div>"""
def s2(P): return f"""<div class="s" style="background:var(--espresso)"><div class="ph bw" style="background-image:url('{P('69300e5c.png')}');background-size:135%;background-position:30% 100%"></div>
<div class="lab" style="left:80px;right:80px;bottom:110px"><div class="up">Buenos granos de café</div><div class="t">TAZE<br>KAVRULMUŞ</div><div class="bd" style="margin-top:14px">Çekirdekten fincana, her gün taze.</div></div></div>"""
def s3(P): return f"""<div class="s"><div class="ph bw" style="background-image:url('{P('644e0b2c.png')}');filter:grayscale(.6) contrast(1.08)"></div>
<div class="lab" style="left:80px;right:80px;top:90px"><div class="up">Klasik</div><div class="t">TÜRK KAHVESİ<br>DE VAR</div><div class="bd" style="margin-top:14px">Köpüğü bol, yanında su ve lokum.</div></div></div>"""
def s4(P): return f"""<div class="s"><div class="ph bw" style="background-image:url('{P('d6f60af2.png')}');filter:grayscale(.55) contrast(1.08)"></div>
<div class="lab" style="right:80px;left:180px;bottom:110px"><div class="up">Soğuk bar</div><div class="t">BUZLU MU<br>OLSUN?</div><div class="bd" style="margin-top:14px">White chocolate mocha ve ev yapımı limonata.</div></div></div>"""
def s5(P): return f"""<div class="s" style="background:var(--espresso);color:var(--sut)"><div style="position:absolute;left:80px;right:80px;top:120px"><div class="up" style="color:var(--kraft)">Buegros · Coffee shop</div><div class="t" style="margin-top:28px;font-size:112px">UĞRAYIN,<br>KAHVENİZ<br>HAZIR</div></div>
<div class="lab" style="left:80px;right:80px;bottom:120px;box-shadow:10px 10px 0 var(--sut)"><div class="up" style="font-size:24px;line-height:2;margin:0">{ADR}<br>10:30’dan itibaren<br><span style="font:400 46px var(--font-baslik);letter-spacing:0">{TEL}</span></div></div></div>"""
def post(P): return f"""<div class="s" style="background:var(--espresso)"><div class="fr bw" style="left:0;top:0;width:540px;height:1350px;border:0;border-right:4px solid var(--espresso);background-image:url('{P('d6f60af2.png')}');background-position:35% 50%"></div>
<div class="fr bw" style="left:540px;top:0;width:540px;height:1350px;border:0;background-image:url('{P('ca4c06ec.png')}')"></div>
<div class="lab" style="left:120px;right:120px;top:500px;text-align:center"><div class="up">Bugün</div><div class="t" style="font-size:78px">BUZLU MU,<br>SICAK MI?</div><div class="bd" style="margin-top:12px">Yorumlarda söyle, gelince hazırlayalım.</div></div></div>"""
def ov(t, up=None, bd=None):
    u = f'<div class="up">{up}</div>' if up else ''
    b = f'<div class="bd" style="margin-top:10px">{bd}</div>' if bd else ''
    return f'<div class="s r" style="background:transparent"><div class="lab" style="left:50px;right:50px;bottom:130px">{u}<div class="t">{t}</div>{b}</div></div>'
CFG = dict(
    slug='buegros-coffee-shop', name='Buegros Coffee Shop',
    fonts_url='https://fonts.googleapis.com/css2?family=Alfa+Slab+One&family=Rethink+Sans:wght@400;600&family=Tenor+Sans&display=swap',
    tokens='--espresso:#1C1C1C;--sut:#FFFFFF;--kraft:#C8A27A;--cekirdek:#4A2C1D;--krema:#EFE6DA;--font-baslik:"Alfa Slab One",Rockwell,serif;--font-govde:"Rethink Sans",sans-serif;--font-vurgu:"Tenor Sans",sans-serif;--zemin:#1C1C1C',
    reel_pre='hue=s=0.3,eq=contrast=1.1,', css=CSS, slides=[s1, s2, s3, s4, s5], post=post,
    reel=[('ca4c06ec.png', ov('BİR FİNCAN MOLA', 'Çarşı Caddesi')),
          ('69300e5c.png', ov('TAZE KAVRULMUŞ', 'Buenos granos de café')),
          ('644e0b2c.png', ov('TÜRK KAHVESİ', None, 'Köpüğü bol, yanında lokum.')),
          ('d6f60af2.png', ov('BUZLU MU OLSUN?', 'Soğuk bar')),
          ('ca4c06ec.png', ov('UĞRAYIN', ADR, TEL))],
    page=dict(
        vars='  color-scheme: light;\n  --bg: #FFFFFF;\n  --panel: #EFE6DA;\n  --line: #1C1C1C;\n  --text: #1C1C1C;\n  --muted: #4a4a4a;\n  --accent: #1C1C1C;\n  --accent-ink: #FFFFFF;\n  --display: "Alfa Slab One", Rockwell, serif;\n  --body: "Rethink Sans", sans-serif;\n  --vurgu: "Tenor Sans", sans-serif;',
        extra_css='.eyebrow, .meta, h3 { font-family: var(--vurgu); font-weight: 400; }\nh1 em { font-style: normal; background: #C8A27A; padding: 0 .2em; box-decoration-break: clone; -webkit-box-decoration-break: clone; }\n.shot { border: 3px solid #1C1C1C; border-radius: 4px; }\n.cap { border: 3px solid #1C1C1C; border-radius: 4px; box-shadow: 6px 6px 0 #1C1C1C; }\n.copy { border-radius: 4px; }\n.dots button[aria-current="true"] { background: #C8A27A; outline: 2px solid #1C1C1C; }\n',
        motif='',
        lede='Haftalık paylaşımların nasıl görüneceğini göstermek için hazırladığımız kısa bir reels, beş karelik bir karusel ve tek gönderi; logonuzdaki kalın slab yazı ve kraft etiket diliyle.',
        reel_meta='15 sn · dikey',
        reel_note='Flat white, taze kavrulmuş çekirdek, Türk kahvesi ve soğuk içecekler; 5 sahnede Buegros. Video sessizdir; müzik Instagram’da paylaşırken eklenir.',
        alts=['Bir fincan mola. Çarşı Caddesi, Fevzipaşa.', 'Taze kavrulmuş çekirdek.', 'Türk kahvesi de var. Köpüğü bol, yanında su ve lokum.', 'Buzlu mu olsun? White chocolate mocha ve ev yapımı limonata.', f'Uğrayın, kahveniz hazır. {ADR} · 10:30’dan itibaren · {TEL}'],
        post_alt='Bugün buzlu mu, sıcak mı? Yorumlarda söyle, gelince hazırlayalım.',
        post_note='Telefon, adres ve menüdeki içecekler Google Haritalar kaydınızdan alındı.',
        music=[('Lo-fi kafe', 'Aramaya “lofi coffee” yazın. Sakin ve modern.'), ('Klasik rock (Freddie’ye selam)', 'Aramaya “classic rock instrumental” yazın. Müdavimleriniz anlar.'), ('Bossa nova', 'Aramaya “bossa nova cafe” yazın. Hafif ve sıcak.')],
        caps=[('reel', 'Reels', f'Bir fincan mola. ☕️\nFlat white, Türk kahvesi, mocha ve limonata; Çarşı Caddesi’nde.\n\n📍 Çarşı Cd. No:84, Fevzipaşa\n📞 {TEL}\n\n#Buegros #Çanakkale #kahve #flatwhite #specialtycoffee'),
              ('kar', 'Karusel', f'Çarşı Caddesi’nde bir fincan mola. 🤍\nTaze kavrulmuş çekirdekler, köpüklü Türk kahvesi ve serin içecekler.\nBir sonraki kahve molan için kaydet. 👇\n\n📍 {ADR}\n⏰ 10:30’dan itibaren\n📞 {TEL}\n\n#Buegros #Çanakkale #çanakkalekahve #türkkahvesi'),
              ('post', 'Tek gönderi', 'Bugün buzlu mu, sıcak mı? 🧊☕️\nYorumlarda söyle, gelince hazırlayalım.\n\n📍 Çarşı Cd. No:84\n\n#Buegros #Çanakkale #kahvemolası')],
    ),
)
