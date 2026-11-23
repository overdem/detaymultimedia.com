# tasarim/lahmacun-time-ocakbasi.md — gece/tabure pembesi/petrol/ocak/ampul, Unbounded 900 + Readex Pro + Kalam, ip ampul + saat kadranı motifi (logo yok: yazı-logo önerisi)
import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from motif import bulbs
TEL = '0538 093 67 17'; ADR = 'Kemalyeri Sk. No:9 · Kemalpaşa'
CSS = """
.s{background:var(--gece);color:var(--ampul);font-family:var(--font-govde)}
.t{font:900 112px/.98 var(--font-baslik);text-transform:uppercase;color:var(--ampul)}
.t em{font-style:normal;color:var(--tabure)}
.bd{font:400 30px/1.45 var(--font-govde);color:var(--ampul)}
.note{font:700 50px/1.1 var(--font-vurgu);color:var(--tabure);transform:rotate(-5deg);display:inline-block;background:var(--gece);padding:8px 26px 4px;border-radius:999px}
.clock{position:absolute;width:230px;height:230px;border-radius:50%;background:var(--tabure);color:var(--gece);display:flex;flex-direction:column;align-items:center;justify-content:center;border:8px solid var(--ampul)}
.clock b{font:900 52px var(--font-baslik)}.clock span{font:700 22px var(--font-baslik);letter-spacing:.12em}
.clock:before{content:"";position:absolute;left:50%;top:22px;width:6px;height:60px;background:var(--gece);transform:translateX(-50%)}
.pic{position:absolute;background-size:cover;background-position:center;border-radius:36px}
.dark{position:absolute;inset:0;background:linear-gradient(180deg,rgba(27,29,51,0) 40%,rgba(27,29,51,.95) 80%,#1B1D33 100%)}
.num{font:900 30px var(--font-baslik);color:var(--petrol);background:var(--ampul);display:inline-block;padding:8px 18px;border-radius:999px}
.r .t{font-size:78px}.r .bd{font-size:24px}.r .note{font-size:40px}
"""
B = bulbs('#FFE3A3', 13, 1080, 30, 36, 9)
def s1(P): return f"""<div class="s"><div style="position:absolute;left:0;top:0">{B}</div>
<div class="pic" style="left:70px;right:70px;top:150px;height:760px;background-image:url('{P('a30665e4.png')}')"></div>
<div class="clock" style="right:40px;top:110px"><span>SAYI</span><b>01</b></div>
<div style="position:absolute;left:80px;right:80px;top:950px"><div class="t" style="font-size:104px">LAHMACUN<br><em>TIME</em></div><div class="bd" style="margin-top:16px;color:#c9d2ff">Kemalpaşa · ocakbaşı</div></div></div>"""
def item(P, ph, no, t, bd, note):
    return f"""<div class="s"><div class="ph" style="background-image:url('{P(ph)}')"></div><div class="dark"></div>
<div style="position:absolute;left:0;top:0">{B}</div>
<div style="position:absolute;left:80px;right:80px;bottom:100px"><span class="num">{no}</span><div class="t" style="margin-top:22px">{t}</div><div class="bd" style="margin-top:18px">{bd}</div></div>
<div style="position:absolute;right:70px;top:150px"><span class="note">{note}</span></div></div>"""
def s2(P): return item(P, 'a30665e4.png', '01', 'İnce hamur,<br><em>çıtır</em> kenar', 'Antep usulü lahmacun; yeşillik, limon ve ezme yanında.', 'acılı mı?')
def s3(P): return item(P, '106fe7e7.png', '02', 'Ocaktan<br><em>sıcak</em>', 'Kanat, adana, beyti; közde biber ve domatesle.', 'közden yeni!')
def s4(P): return item(P, '76e37b79.png', '03', 'Üstü açık<br><em>bahçe</em>', 'Ampuller yanınca bahçede yer bulun.', 'akşama burada')
def s5(P): return f"""<div class="s" style="background:var(--petrol)"><div style="position:absolute;left:0;top:0">{bulbs('#FFE3A3', 13, 1080, 30, 36, 9)}</div>
<div class="clock" style="left:425px;top:170px;width:230px;height:230px"><span>AÇILIŞ</span><b>11:00</b></div>
<div style="position:absolute;left:70px;right:70px;top:470px;text-align:center"><div class="t" style="font-size:96px">LAHMACUN<br><em style="color:var(--gece)">VAKTİ</em></div>
<div style="margin-top:56px;background:var(--gece);border-radius:30px;padding:40px 30px"><div style="font:900 58px var(--font-baslik);color:var(--ampul)">{TEL}</div><div class="bd" style="margin-top:16px">{ADR}</div></div></div></div>"""
def post(P): return f"""<div class="s"><div class="ph" style="background-image:url('{P('a30665e4.png')}');background-size:150%;background-position:30% 40%"></div><div class="dark"></div>
<div class="clock" style="right:60px;top:60px"><span>ÖĞLE</span><b>12:00</b></div>
<div style="position:absolute;left:80px;right:80px;bottom:110px"><div class="t">Öğle arası,<br><em>lahmacun</em> vakti</div><div style="margin-top:24px"><span class="note" style="font-size:44px">bahçede ya da paket</span></div></div></div>"""
def ov(t, bd=None, note=None):
    b = f'<div class="bd" style="margin-top:14px">{bd}</div>' if bd else ''
    n = f'<div style="margin-top:18px"><span class="note">{note}</span></div>' if note else ''
    return f'<div class="s r" style="background:transparent"><div class="dark"></div><div style="position:absolute;left:0;top:0;transform:scale(.667);transform-origin:0 0">{B}</div><div style="position:absolute;left:50px;right:50px;bottom:130px">{"<div class=t>"+t+"</div>"}{b}{n}</div></div>'
CFG = dict(
    slug='lahmacun-time-ocakbasi', name='Lahmacun Time Ocakbaşı',
    fonts_url='https://fonts.googleapis.com/css2?family=Unbounded:wght@700;900&family=Readex+Pro:wght@400;600&family=Kalam:wght@400;700&display=swap',
    tokens='--tabure:#E0457B;--petrol:#12807F;--ocak:#E7742B;--gece:#1B1D33;--ampul:#FFE3A3;--font-baslik:"Unbounded",sans-serif;--font-govde:"Readex Pro",sans-serif;--font-vurgu:"Kalam",cursive;--zemin:#1B1D33',
    css=CSS, slides=[s1, s2, s3, s4, s5], post=post,
    reel=[('a30665e4.png', ov('LAHMACUN<br><em>TIME</em>', 'Kemalpaşa · ocakbaşı')),
          ('a30665e4.png', ov('İnce hamur,<br><em>çıtır</em> kenar', None, 'acılı mı?')),
          ('106fe7e7.png', ov('Ocaktan<br><em>sıcak</em>', 'Kanat, adana, beyti')),
          ('76e37b79.png', ov('Üstü açık<br><em>bahçe</em>')),
          ('76e37b79.png', ov('<em>11:00</em>’den<br>itibaren', f'{TEL}<br>{ADR}'))],
    page=dict(
        vars='  color-scheme: dark;\n  --bg: #1B1D33;\n  --panel: #24274a;\n  --line: #3a3e66;\n  --text: #FFE3A3;\n  --muted: #c9c3d8;\n  --accent: #E0457B;\n  --accent-ink: #1B1D33;\n  --display: "Unbounded", sans-serif;\n  --display-w: 900;\n  --body: "Readex Pro", sans-serif;\n  --vurgu: "Kalam", cursive;',
        extra_css='h1 { text-transform: uppercase; font-size: clamp(26px, 7.4vw, 38px); }\nh1 em { font-style: normal; color: #E0457B; }\nh2 { font-size: 20px; text-transform: uppercase; }\n.motif { display: flex; justify-content: center; gap: 14px; }\n.motif i { width: 10px; height: 10px; border-radius: 50%; background: #FFE3A3; box-shadow: 0 0 10px #FFE3A3; }\n.kimlik { font-family: var(--vurgu); color: #E0457B; font-size: 18px; margin: 0; }\n',
        motif='<div class="motif" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>',
        lede='Haftalık paylaşımların nasıl görüneceğini göstermek için hazırladığımız kısa bir reels, beş karelik dergi tarzı bir karusel ve tek gönderi. Logonuz olmadığı için “LAHMACUN TIME” yazısı ve saat rozeti bir kimlik önerisidir; renkler mekânınızdaki pembe taburelerden ve ampullerden alındı.',
        reel_meta='15 sn · dikey',
        reel_note='İnce hamurlu lahmacun, ocaktan kebap, açık bahçe ve iletişim; 5 sahnede Lahmacun Time. Video sessizdir; müzik Instagram’da paylaşırken eklenir.',
        alts=['Lahmacun Time, Sayı 01. Kemalpaşa, ocakbaşı.', '01. İnce hamur, çıtır kenar. Antep usulü lahmacun.', '02. Ocaktan sıcak. Kanat, adana, beyti.', '03. Üstü açık bahçe.', f'Lahmacun vakti. Açılış 11:00 · {TEL} · {ADR}'],
        post_alt='Öğle arası, lahmacun vakti. Bahçede ya da paket.',
        post_note='Telefon, adres ve açılış saati Google Haritalar kaydınızdan alındı.',
        music=[('Modern Anadolu', 'Aramaya “anatolian groove” yazın. Ocakbaşına yakışır.'), ('Akustik bağlama', 'Aramaya “baglama instrumental” yazın. Sıcak ve yerel.'), ('Upbeat', 'Aramaya “upbeat cooking” yazın. Hızlı kesimler için.')],
        caps=[('reel', 'Reels', f'İnce hamur, çıtır kenar. 🔥\nAntep usulü lahmacun, ocaktan kebap ve üstü açık bahçe.\n\n📍 Kemalyeri Sk. No:9, Kemalpaşa\n📞 {TEL}\n\n#LahmacunTime #Çanakkale #lahmacun #ocakbaşı #kebap'),
              ('kar', 'Karusel', f'Lahmacun Time, Sayı 01. 📰\n01 İnce hamur, çıtır kenar · 02 Ocaktan sıcak · 03 Üstü açık bahçe.\nÖğle arası için kaydet. 👇\n\n📍 {ADR}\n⏰ 11:00’den itibaren\n📞 {TEL}\n\n#LahmacunTime #Çanakkale #çanakkalelahmacun #ocakbaşı'),
              ('post', 'Tek gönderi', f'Öğle arası, lahmacun vakti. 🌿🍋\nBahçede ya da paket; sen seç.\n\n📞 {TEL}\n📍 Kemalpaşa\n\n#LahmacunTime #lahmacun #Çanakkale')],
    ),
)
