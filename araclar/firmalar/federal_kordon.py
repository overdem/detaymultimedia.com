# tasarim/federal-kordon.md — kömür/ceviz/turuncu/plak/pirinç (öneri), Big Shoulders Display + Public Sans + IBM Plex Mono, plak dairesi motifi
TEL = '0545 322 17 17'; ADR = 'Pirireis Cd. No:1/5 · Cevat Paşa'
PH = dict(makarna='44d20117.png', avokado='bc1fc780.png', ic='46aac0a3.png')
CSS = """
.s{background:var(--komur);color:var(--plak);font-family:var(--font-govde)}
.t{font:800 150px/.9 var(--font-baslik);text-transform:uppercase;letter-spacing:.01em}
.t em{font-style:normal;color:var(--turuncu)}
.bd{font:400 30px/1.45 var(--font-govde)}
.mono{font:500 22px var(--font-vurgu);letter-spacing:.08em;text-transform:uppercase}
.rec{position:absolute;border-radius:50%;background-size:cover;background-position:center}
.ring{position:absolute;border-radius:50%;border:2px solid var(--pirinc)}
.band{position:absolute;left:0;right:0;bottom:0;background:var(--komur);padding:44px 70px 70px;border-top:6px solid var(--turuncu)}
.dot{display:inline-block;width:150px;height:150px;border-radius:50%;background:var(--turuncu);color:var(--komur);font:800 44px/150px var(--font-baslik);text-align:center}
.r .t{font-size:100px}.r .bd{font-size:24px}.r .mono{font-size:17px}
"""
def s1(P): return f"""<div class="s"><div class="mono" style="position:absolute;left:70px;top:70px;color:var(--pirinc)">[ Kordon · Cevat Paşa ]</div>
<div class="rec" style="left:190px;top:170px;width:700px;height:700px;background-image:url('{P(PH['ic'])}')"></div>
<div class="ring" style="left:170px;top:150px;width:740px;height:740px"></div><div class="ring" style="left:150px;top:130px;width:780px;height:780px;opacity:.5"></div>
<div class="rec" style="left:500px;top:480px;width:80px;height:80px;background:var(--turuncu)"></div>
<div style="position:absolute;left:70px;right:70px;bottom:80px"><div class="t">Federal<br><em>Kordon</em></div><div class="bd" style="margin-top:16px">Boğaz’a karşı kahve, kahvaltı ve akşam yemeği.</div></div></div>"""
def dish(P, ph, no, t, bd):
    return f"""<div class="s"><div class="ph" style="background-image:url('{P(ph)}');bottom:380px"></div>
<div class="band"><div class="mono" style="color:var(--pirinc)">[ {no} ]</div><div class="t" style="font-size:112px;margin-top:10px">{t}</div><div class="bd" style="margin-top:14px">{bd}</div></div></div>"""
def s2(P): return dish(P, PH['makarna'], '01 · Akşam', 'Fettuccine <em>Alfredo</em>', 'Kremalı, bol parmesanlı; tabak dolu gelir.')
def s3(P): return dish(P, PH['avokado'], '02 · Sabah', 'Avokadolu <em>ekmek</em>', 'Ekşi mayalı ekmek üstünde; yanında acuka.')
def s4(P): return f"""<div class="s"><div class="ph" style="background-image:url('{P(PH['ic'])}')"></div><div class="ph" style="background:linear-gradient(180deg,rgba(23,22,21,0) 45%,rgba(23,22,21,.95) 85%)"></div>
<div style="position:absolute;left:70px;right:70px;bottom:80px"><div class="mono" style="color:var(--pirinc)">[ 03 · Manzara ]</div><div class="t" style="margin-top:10px;font-size:130px">Boğaz’a <em>karşı</em></div><div class="bd" style="margin-top:14px">Kordon’da buluşmak için bir masa.</div></div></div>"""
def s5(P): return f"""<div class="s" style="background:var(--ceviz)"><div class="ring" style="left:-260px;top:-260px;width:900px;height:900px"></div><div class="ring" style="left:-200px;top:-200px;width:780px;height:780px;opacity:.6"></div>
<div style="position:absolute;right:70px;top:110px"><span class="dot">08:00</span></div>
<div style="position:absolute;left:70px;right:70px;top:620px"><div class="t" style="font-size:120px">Kordon’da<br><em>görüşelim</em></div>
<div class="mono" style="margin-top:50px;font-size:26px;line-height:1.9">[ {TEL} ]<br>[ {ADR} ]<br>[ Her gün 08:00’den itibaren ]</div></div></div>"""
def post(P): return f"""<div class="s"><div class="ph" style="background-image:url('{P(PH['avokado'])}');background-size:120%;background-position:50% 60%"></div><div class="ph" style="background:linear-gradient(180deg,rgba(23,22,21,.85) 0%,rgba(23,22,21,0) 35%)"></div>
<div style="position:absolute;left:70px;right:70px;top:70px"><div class="mono" style="color:var(--pirinc)">[ Günaydın Kordon ]</div><div class="t" style="margin-top:12px;font-size:120px">Kahvaltı <em>hazır</em></div></div></div>"""
def ov(t, mono=None, bd=None):
    m = f'<div class="mono" style="color:var(--pirinc)">[ {mono} ]</div>' if mono else ''
    b = f'<div class="bd" style="margin-top:12px">{bd}</div>' if bd else ''
    return f'<div class="s r" style="background:transparent"><div style="position:absolute;left:0;right:0;bottom:0;padding:34px 44px 120px;background:linear-gradient(180deg,rgba(23,22,21,0),rgba(23,22,21,.92) 30%);border-bottom:6px solid var(--turuncu)">{m}<div class="t" style="margin-top:8px">{t}</div>{b}</div></div>'
CFG = dict(
    slug='federal-kordon', name='Federal Kordon',
    fonts_url='https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@700;800&family=Public+Sans:wght@400;600&family=IBM+Plex+Mono:wght@500&display=swap',
    tokens='--komur:#171615;--ceviz:#5B3B28;--turuncu:#E2702B;--plak:#EEEAE2;--pirinc:#B38B4F;--font-baslik:"Big Shoulders Display",sans-serif;--font-govde:"Public Sans",sans-serif;--font-vurgu:"IBM Plex Mono",monospace;--zemin:#171615',
    css=CSS, slides=[s1, s2, s3, s4, s5], post=post,
    reel=[(PH['ic'], ov('Federal <em>Kordon</em>', 'Boğaz’a karşı')),
          (PH['makarna'], ov('Fettuccine <em>Alfredo</em>', '01 · Akşam')),
          (PH['avokado'], ov('Avokadolu <em>ekmek</em>', '02 · Sabah', 'Ekşi mayalı, yanında acuka')),
          (PH['ic'], ov('Kordon’da <em>görüşelim</em>', TEL, 'Her gün 08:00’den itibaren'))],
    page=dict(
        vars='  color-scheme: dark;\n  --bg: #171615;\n  --panel: #241f1c;\n  --line: #3d342d;\n  --text: #EEEAE2;\n  --muted: #c2b9ad;\n  --accent: #E2702B;\n  --accent-ink: #171615;\n  --display: "Big Shoulders Display", sans-serif;\n  --display-w: 800;\n  --body: "Public Sans", sans-serif;\n  --vurgu: "IBM Plex Mono", monospace;',
        extra_css='h1 { text-transform: uppercase; font-size: clamp(36px, 11vw, 54px); line-height: 1; }\nh1 em { font-style: normal; color: #E2702B; }\nh2 { text-transform: uppercase; font-size: 30px; }\n.eyebrow, .meta, h3 { font-family: var(--vurgu); font-weight: 500; }\n.motif { width: 64px; height: 64px; margin: 0 auto; border-radius: 50%; border: 2px solid #B38B4F; box-shadow: inset 0 0 0 10px #171615, inset 0 0 0 12px #B38B4F, inset 0 0 0 24px #171615, inset 0 0 0 32px #E2702B; }\n.kimlik { font-family: var(--vurgu); font-size: 12px; color: #c2b9ad; margin: 0; }\n',
        motif='<div class="motif" aria-hidden="true"></div>',
        lede='Haftalık paylaşımların nasıl görüneceğini göstermek için hazırladığımız kısa bir reels, beş karelik bir karusel ve tek gönderi. Renkler mekânınızdaki koyu ahşap, turuncu vurgular ve duvardaki plaklardan alınmış bir öneri.',
        reel_meta='12 sn · dikey',
        reel_note='Boğaz’a bakan masa, fettuccine Alfredo, avokadolu ekmek üstü ve iletişim; 4 sahnede Federal Kordon. Video sessizdir; müzik Instagram’da paylaşırken eklenir.',
        alts=['Federal Kordon: Boğaz’a karşı kahve, kahvaltı ve akşam yemeği.', '01 · Akşam: fettuccine Alfredo, kremalı ve bol parmesanlı.', '02 · Sabah: ekşi mayalı ekmek üstünde avokado, yanında acuka.', '03 · Manzara: Boğaz’a karşı, Kordon’da buluşmak için bir masa.', f'Kordon’da görüşelim: {TEL} · {ADR} · Her gün 08:00’den itibaren'],
        post_alt='Günaydın Kordon: kahvaltı hazır.',
        post_note='Telefon, adres ve açılış saati Google Haritalar kaydınızdan; öne çıkan tabaklar misafir yorumlarından alındı.',
        music=[('Lo-fi akşam', 'Aramaya “lofi evening” yazın. Kordon akşamına sakin bir eşlik.'), ('Funk / soul', 'Aramaya “soul groove” yazın. Plak duvarına yakışır.'), ('İtalyan kafe', 'Aramaya “italian cafe jazz” yazın. Makarna sahnesi için.')],
        caps=[('reel', 'Reels', f'Boğaz’a karşı bir masa. 🌊\nSabah avokadolu ekmek üstü, akşam fettuccine Alfredo.\n\n📍 Pirireis Cd. No:1/5, Cevat Paşa\n📞 {TEL}\n\n#FederalKordon #Çanakkale #kordon #kahvaltı #makarna'),
              ('kar', 'Karusel', f'Kordon’da bir gün. ☕️🍝\n01 Fettuccine Alfredo · 02 Avokadolu ekmek üstü · 03 Boğaz manzarası.\nBuluşma planına kaydet. 👇\n\n📍 {ADR}\n⏰ Her gün 08:00’den itibaren\n📞 {TEL}\n\n#FederalKordon #Çanakkale #çanakkalekafe #kordonboyu'),
              ('post', 'Tek gönderi', f'Günaydın Kordon, kahvaltı hazır. 🥑\nEkşi mayalı ekmek, avokado ve yanında acuka.\n\n📍 Pirireis Cd. No:1/5\n\n#FederalKordon #günaydın #Çanakkale')],
        sign='<p class="kimlik">Logonuza ulaşamadık; “FEDERAL KORDON” yazısı bir öneridir, resmi logonuzla değiştiririz.</p>',
    ),
)
