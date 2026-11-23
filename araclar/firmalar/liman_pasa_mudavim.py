# tasarim/liman-pasa-mudavim.md — gece/altın, Marcellus + Pinyon Script + Spectral, ince altın oval motif
TEL = '0532 430 77 43'; ADR = 'Eski Balıkhane Sk. No:7/1 · Kemalpaşa'
CSS = """
.s{background:var(--gece);color:var(--fildisi);font-family:var(--font-govde);text-align:center}
.fade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(11,11,11,.55) 0%,rgba(11,11,11,0) 22%,rgba(11,11,11,0) 45%,rgba(11,11,11,.92) 78%,#0B0B0B 100%)}
.oval{position:absolute;border:2px solid var(--pasa-altin);border-radius:50%}
.lbl{position:absolute;left:0;right:0;top:78px;font:400 20px var(--font-baslik);letter-spacing:.32em;color:var(--fildisi);opacity:.9}
.blk{position:absolute;left:80px;right:80px;bottom:110px}
.scr{font:400 128px/1 var(--font-vurgu);color:var(--pasa-altin)}
.cap{font:400 64px/1.1 var(--font-baslik);letter-spacing:.2em;text-transform:none;margin-top:18px}
.bd{font:400 30px/1.45 var(--font-govde);margin-top:26px;color:var(--fildisi)}
.sm{font-size:24px;color:var(--duman);letter-spacing:.06em}
.rule{width:220px;margin:30px auto 0;border-top:1px solid var(--pasa-altin);border-bottom:1px solid var(--pasa-altin);height:6px}
.mask{position:absolute;border-radius:50%;background-size:cover;background-position:center}
.r .lbl{top:64px;font-size:15px}
.r .blk{left:50px;right:50px;bottom:120px}
.r .scr{font-size:96px}.r .cap{font-size:46px}.r .bd{font-size:24px}
"""
def s1(P): return f"""<div class="s"><div class="ph" style="background-image:url('{P('39c904c6.png')}')"></div><div class="fade"></div>
<div class="oval" style="left:60px;top:46px;width:960px;height:1258px;opacity:.55"></div>
<div class="lbl">LİMAN PAŞA MÜDAVİM · ESKİ BALIKHANE</div>
<div class="blk"><div class="scr">gün batımı</div><div class="cap">KİLİTBAHİR’E KARŞI</div><div class="rule"></div><div class="bd">Boğaz kıyısında, liman başında bir akşam.</div></div></div>"""
def s2(P): return f"""<div class="s"><div class="mask" style="left:150px;top:96px;width:780px;height:900px;background-image:url('{P('d6b21a06.png')}')"></div>
<div class="oval" style="left:130px;top:76px;width:820px;height:940px"></div>
<div class="blk" style="bottom:96px"><div class="cap" style="font-size:54px">AKŞAMIN İLK DURAĞI</div><div class="scr" style="margin-top:8px">mezeler</div><div class="bd sm" style="margin-top:14px">HAYDARİ · FAVA · MARİNE HAMSİ · AHTAPOT</div></div></div>"""
def s3(P): return f"""<div class="s"><div class="ph" style="background-image:url('{P('96c295af.png')}')"></div><div class="fade"></div>
<div class="lbl">02 · IZGARADAN</div>
<div class="blk"><div class="cap" style="font-size:76px">BALIK PİRZOLA</div><div class="rule"></div><div class="bd">Menünün en sevilenlerinden; limon ve roka eşliğinde.</div></div></div>"""
def s4(P): return f"""<div class="s" style="background:var(--liman)"><div class="ph" style="background-image:url('{P('d71dfec0.png')}')"></div><div class="fade" style="background:linear-gradient(180deg,rgba(19,48,63,.0) 40%,rgba(19,48,63,.9) 75%,#13303F 100%)"></div>
<div class="lbl">03 · AKŞAM</div>
<div class="blk"><div class="cap">CANLI MÜZİK</div><div class="scr" style="font-size:112px;margin-top:6px">eşliğinde</div><div class="bd">Liman ışıkları altında uzayan bir akşam.</div></div></div>"""
def s5(P): return f"""<div class="s"><div class="oval" style="left:150px;top:150px;width:780px;height:1050px"></div><div class="oval" style="left:166px;top:166px;width:748px;height:1018px;opacity:.45;border-width:1px"></div>
<div style="position:absolute;left:200px;right:200px;top:300px">
<div style="font:400 22px var(--font-baslik);letter-spacing:.36em;color:var(--duman)">LİMAN PAŞA MÜDAVİM</div>
<div class="scr" style="margin-top:70px">rezervasyon</div>
<div class="cap" style="font-size:52px">MASANIZI AYIRTIN</div><div class="rule"></div>
<div style="font:500 50px var(--font-govde);margin-top:56px;color:var(--pasa-altin);letter-spacing:.04em">{TEL}</div>
<div class="bd" style="font-size:26px;margin-top:20px;color:var(--fildisi)">Eski Balıkhane Sk. No:7/1<br>Kemalpaşa · Çanakkale</div></div></div>"""
def post(P): return f"""<div class="s"><div class="ph" style="background-image:url('{P('d71dfec0.png')}');background-position:50% 40%"></div><div class="fade"></div>
<div class="oval" style="left:60px;top:46px;width:960px;height:1258px;opacity:.55"></div>
<div class="lbl">LİMAN PAŞA MÜDAVİM</div>
<div class="blk"><div class="scr">bu akşam</div><div class="cap" style="font-size:60px">CANLI MÜZİK</div><div class="rule"></div><div class="bd">Akşam yemeği, canlı müzik eşliğinde.<br>Rezervasyon {TEL}</div></div></div>"""
def ov(scr=None, cap=None, bd=None, lbl='LİMAN PAŞA MÜDAVİM', grad=True):
    g = '<div class="fade"></div>' if grad else ''
    a = f'<div class="scr">{scr}</div>' if scr else ''
    c = f'<div class="cap">{cap}</div>' if cap else ''
    b = f'<div class="rule"></div><div class="bd">{bd}</div>' if bd else ''
    return f'<div class="s r" style="background:transparent">{g}<div class="lbl">{lbl}</div><div class="blk">{a}{c}{b}</div></div>'
CFG = dict(
    slug='liman-pasa-mudavim', name='Liman Paşa Müdavim',
    fonts_url='https://fonts.googleapis.com/css2?family=Marcellus&family=Pinyon+Script&family=Spectral:wght@400;500&display=swap',
    tokens='--gece:#0B0B0B;--pasa-altin:#DDB032;--fildisi:#F5F0E4;--liman:#13303F;--duman:#8C8C8C;--font-baslik:"Marcellus",serif;--font-vurgu:"Pinyon Script",cursive;--font-govde:"Spectral",Georgia,serif;--zemin:#0B0B0B',
    css=CSS, slides=[s1, s2, s3, s4, s5], post=post,
    reel=[('39c904c6.png', ov('gün batımı', 'KİLİTBAHİR’E KARŞI')),
          ('d6b21a06.png', ov('mezeler', 'AKŞAMIN İLK DURAĞI')),
          ('96c295af.png', ov(None, 'BALIK PİRZOLA', 'Izgaradan, limon ve roka ile.')),
          ('d71dfec0.png', ov('eşliğinde', 'CANLI MÜZİK')),
          ('39c904c6.png', ov('rezervasyon', 'MASANIZI AYIRTIN', f'{TEL}<br>Eski Balıkhane · Kemalpaşa'))],
    page=dict(
        vars='  color-scheme: dark;\n  --bg: #0B0B0B;\n  --panel: #13303F;\n  --line: #3b3526;\n  --text: #F5F0E4;\n  --muted: #a9a394;\n  --accent: #DDB032;\n  --accent-ink: #0B0B0B;\n  --display: "Marcellus", Georgia, serif;\n  --body: "Spectral", Georgia, serif;\n  --vurgu: "Pinyon Script", cursive;',
        extra_css='h1 { letter-spacing: .04em; }\nh1 em { font-family: var(--vurgu); font-style: normal; font-size: 1.25em; display: block; margin-top: 6px; }\n.motif { width: 120px; height: 160px; margin: 0 auto; border: 1px solid var(--accent); border-radius: 50%; display: grid; place-items: center; }\n.motif span { font: 400 11px var(--display); letter-spacing: .3em; color: var(--accent); line-height: 1.8; }\n.rule2 { width: 120px; margin: 0 auto; border-top: 1px solid var(--accent); border-bottom: 1px solid var(--accent); height: 5px; }\n',
        motif='<div class="motif" aria-hidden="true"><span>LİMAN<br>PAŞA<br>MÜDAVİM</span></div>',
        lede='Haftalık paylaşımların nasıl görüneceğini göstermek için hazırladığımız kısa bir reels, beş karelik bir karusel ve akşam gönderisi; siyah-altın kimliğinizle.',
        reel_meta='15 sn · dikey',
        reel_note='Kilitbahir’e karşı gün batımı, mezeler, balık pirzola ve canlı müzik; 5 sahnede Liman Paşa Müdavim. Video sessizdir; müzik Instagram’da paylaşırken eklenir.',
        alts=['Gün batımı, Kilitbahir’e karşı. Boğaz kıyısında, liman başında bir akşam.', 'Akşamın ilk durağı: mezeler.', 'Balık pirzola, menünün en sevilenlerinden.', 'Canlı müzik eşliğinde, liman ışıkları altında bir akşam.', f'Rezervasyon: masanızı ayırtın. {TEL} · {ADR}'],
        post_alt=f'Bu akşam: akşam yemeği ve canlı müzik. Rezervasyon {TEL}.',
        post_note='Telefon ve adres Google Haritalar kaydınızdan alındı.',
        music=[('Akustik akşam', 'Aramaya “acoustic sunset” yazın. Gün batımı sahnesine yakışır.'), ('Türk sanat müziği enstrümantal', 'Aramaya “ud taksim” yazın. Meyhane ve meze havası.'), ('Lounge caz', 'Aramaya “lounge jazz evening” yazın. Şık ve sakin.')],
        caps=[('reel', 'Reels', f'Gün batarken liman başında. 🌅\nMezeler, balık pirzola ve canlı müzik; Kilitbahir’e karşı bir akşam.\n\n📍 Eski Balıkhane Sk. No:7/1, Kemalpaşa\n📞 Rezervasyon: {TEL}\n\n#PaşaMüdavim #Çanakkale #balık #meze #canlımüzik'),
              ('kar', 'Karusel', f'Kilitbahir’e karşı bir akşam. ⚓️\nMezelerle başlayın, balık pirzolayla devam edin, canlı müzikle uzatın.\nHafta sonu planına kaydet. 👇\n\n📍 {ADR}\n📞 {TEL}\n\n#PaşaMüdavim #Çanakkale #çanakkalebalık #meze #günbatımı'),
              ('post', 'Tek gönderi', f'Bu akşam: akşam yemeği, canlı müzik eşliğinde. 🎶\nMasanızı şimdiden ayırtın.\n\n📞 Rezervasyon: {TEL}\n📍 Eski Balıkhane, Kemalpaşa\n\n#PaşaMüdavim #Çanakkale #canlımüzik')],
        sign='<div class="rule2" aria-hidden="true"></div>',
    ),
)
