# tasarim/ihsan-i-ikram-esnaf-lokantasi.md — mürekkep/kiremit etiket/menü kâğıdı, Lexend + Karla + Patrick Hand, menü kartı motifi
TEL = '0551 160 66 49'; ADR = 'Yalı Cd. · Kemalpaşa'
CSS = """
.s{background:var(--kagit);color:var(--murekkep);font-family:var(--font-govde)}
.wm{font:800 54px/1 var(--font-baslik);letter-spacing:-.01em}
.tag{display:inline-block;margin-left:10px;background:var(--etiket);color:var(--kagit);font:600 26px/1 var(--font-baslik);padding:10px 16px 12px;border-radius:6px;vertical-align:middle}
.t{font:800 104px/.98 var(--font-baslik);letter-spacing:-.02em}
.bd{font:400 30px/1.45 var(--font-govde)}
.note{font:400 46px/1.1 var(--font-vurgu);color:var(--etiket);transform:rotate(-3deg);display:inline-block}
.card{position:absolute;background:var(--kagit);padding:40px 44px;border:2px solid var(--murekkep);box-shadow:0 0 0 10px var(--kagit),0 0 0 12px var(--murekkep)}
.pic{position:absolute;background-size:cover;background-position:center;border:2px solid var(--murekkep)}
.col h4{font:600 24px var(--font-baslik);letter-spacing:.12em;color:var(--etiket);margin-bottom:12px;border-bottom:2px solid var(--murekkep);padding-bottom:8px}
.col div{font:400 36px/1.6 var(--font-govde)}
.clock{width:300px;height:300px;border-radius:50%;border:4px solid var(--bakir);display:flex;flex-direction:column;align-items:center;justify-content:center;color:var(--kagit);margin:0 auto}
.r .t{font-size:72px}.r .wm{font-size:38px}.r .tag{font-size:19px}.r .bd{font-size:23px}.r .note{font-size:36px}
"""
def s1(P): return f"""<div class="s"><div style="position:absolute;left:80px;top:80px"><span class="wm">İhsan-ı İkram</span> <span class="tag">Esnaf Lokantası</span><div class="bd" style="margin-top:12px;font-size:26px">Et lokantası &amp; zeytinyağlılar · Kemalpaşa</div></div>
<div class="pic" style="left:80px;right:80px;top:240px;height:860px;background-image:url('{P('6e4b6cc2.png')}')"></div>
<div style="position:absolute;left:80px;right:80px;top:1140px;display:flex;justify-content:space-between;align-items:center"><div class="t" style="font-size:76px">Bugün<br>tencerede</div><span class="note" style="font-size:58px">ne var?</span></div></div>"""
def photo(P, ph, tag, t, bd):
    return f"""<div class="s"><div class="ph" style="background-image:url('{P(ph)}')"></div>
<div class="card" style="left:70px;right:70px;bottom:80px"><span class="tag">{tag}</span><div class="t" style="font-size:84px;margin-top:20px">{t}</div><div class="bd" style="margin-top:14px">{bd}</div></div></div>"""
def s2(P): return photo(P, 'd4cdd3e9.png', 'Sıcak', 'Çorba', 'Mercimek, ezogelin, tarhana, yayla… Sabahın ilk, gecenin son kâsesi.')
def s3(P): return photo(P, 'c61c5195.png', 'Tencereden', 'İzmir köfte', 'Fırından; patates, biber ve domatesle. Yanında tereyağlı pilav.')
def s4(P): return f"""<div class="s"><div style="position:absolute;left:80px;right:80px;top:80px"><span class="wm" style="font-size:46px">İhsan-ı İkram</span> <span class="tag">Menü</span><div class="bd" style="font-size:26px;margin-top:8px">Et Lokantası &amp; Zeytinyağlılar</div></div>
<div style="position:absolute;left:80px;right:80px;top:270px;display:grid;grid-template-columns:1fr 1fr;gap:70px 56px">
<div class="col"><h4>ÇORBALAR</h4><div>Ezogelin<br>Mercimek<br>Tarhana<br>Yayla</div></div>
<div class="col"><h4>SEBZE YEMEKLERİ</h4><div>Kuru fasulye<br>Taze fasulye<br>İmambayıldı<br>Pırasa</div></div>
<div class="col"><h4>ÖZEL ET</h4><div>Sultan kebabı<br>Elbasan tava<br>Tepsi kebabı<br>Dana et kavurma</div></div>
<div class="col"><h4>KIYMALI</h4><div>İzmir köfte<br>Karnıyarık<br>Musakka<br>Kadınbudu</div></div></div>
<div style="position:absolute;left:80px;bottom:90px"><span class="note">ve daha fazlası, her gün taze</span></div></div>"""
def s5(P): return f"""<div class="s" style="background:var(--murekkep);color:var(--kagit);text-align:center"><div style="position:absolute;left:0;right:0;top:150px">
<div class="clock"><div style="font:600 24px var(--font-baslik);letter-spacing:.14em;color:var(--bakir)">AÇIK</div><div style="font:800 54px/1.1 var(--font-baslik)">06:30<br>04:30</div></div>
<div class="t" style="margin-top:60px;font-size:92px">Gece de<br>açığız</div>
<div class="bd" style="margin-top:22px;color:var(--kagit)">Sabah kahvaltıdan önce çorba,<br>gece çıkışında sıcak yemek.</div></div>
<div style="position:absolute;left:80px;right:80px;bottom:90px;border-top:2px solid var(--bakir);padding-top:30px"><span class="tag" style="font-size:30px">{TEL}</span><div class="bd" style="margin-top:14px;color:var(--kagit)">{ADR} · Çanakkale</div></div></div>"""
def post(P): return f"""<div class="s"><div class="pic" style="left:0;top:0;right:0;height:1010px;border:0;border-bottom:2px solid var(--murekkep);background-image:url('{P('6e4b6cc2.png')}');background-position:50% 70%"></div>
<div style="position:absolute;left:80px;right:80px;top:1050px"><span class="tag">Bugün</span><div class="t" style="font-size:80px;margin-top:14px">Tencereler hazır</div><div class="bd" style="margin-top:8px">İhsan-ı İkram · Yalı Cd., Kemalpaşa</div></div></div>"""
def ov(tag, t, bd=None):
    b = f'<div class="bd" style="margin-top:10px">{bd}</div>' if bd else ''
    return f'<div class="s r" style="background:transparent"><div class="card" style="left:40px;right:40px;bottom:120px;padding:28px 30px"><span class="tag">{tag}</span><div class="t" style="margin-top:14px">{t}</div>{b}</div></div>'
CFG = dict(
    slug='ihsan-i-ikram-esnaf-lokantasi', name='İhsan-ı İkram Esnaf Lokantası',
    fonts_url='https://fonts.googleapis.com/css2?family=Lexend:wght@600;800&family=Karla:wght@400;700&family=Patrick+Hand&display=swap',
    tokens='--murekkep:#2E2420;--etiket:#7A3B2E;--kagit:#F5E8E1;--zeytin:#5E6B34;--bakir:#C9853F;--font-baslik:"Lexend",sans-serif;--font-govde:"Karla",sans-serif;--font-vurgu:"Patrick Hand",cursive;--zemin:#F5E8E1',
    css=CSS, slides=[s1, s2, s3, s4, s5], post=post,
    reel=[('6e4b6cc2.png', ov('Esnaf Lokantası', 'İhsan-ı İkram', 'Bugün tencerede ne var?')),
          ('d4cdd3e9.png', ov('Sıcak', 'Çorba', 'Sabahın ilk, gecenin son kâsesi')),
          ('c61c5195.png', ov('Tencereden', 'İzmir köfte')),
          ('6e4b6cc2.png', ov('Açık', '06:30 – 04:30', f'{TEL} · {ADR}'))],
    page=dict(
        vars='  color-scheme: light;\n  --bg: #F5E8E1;\n  --panel: #fbf3ee;\n  --line: #d9c5ba;\n  --text: #2E2420;\n  --muted: #5f4d45;\n  --accent: #7A3B2E;\n  --accent-ink: #F5E8E1;\n  --display: "Lexend", sans-serif;\n  --display-w: 800;\n  --body: "Karla", sans-serif;\n  --vurgu: "Patrick Hand", cursive;',
        extra_css='h1 { letter-spacing: -.01em; }\nh1 em { font-style: normal; background: #7A3B2E; color: #F5E8E1; padding: 0 .25em; border-radius: 6px; font-size: .8em; }\n.shot { border: 2px solid #2E2420; border-radius: 4px; }\n.cap { border: 2px solid #2E2420; border-radius: 4px; }\n.kimlik { font-family: var(--vurgu); color: #7A3B2E; font-size: 20px; margin: 0; }\n',
        motif='',
        lede='Haftalık paylaşımların nasıl görüneceğini göstermek için hazırladığımız kısa bir reels, beş karelik bir karusel ve tek gönderi. Renkler ve yazı karakteri kendi menü kartınızdan alındı: koyu “İhsan-ı İkram” yazısı ve kiremit “Menü” etiketi.',
        reel_meta='12 sn · dikey',
        reel_note='Benmari, sıcak çorba, İzmir köfte ve açık olduğunuz saatler; 4 sahnede İhsan-ı İkram. Video sessizdir; müzik Instagram’da paylaşırken eklenir.',
        alts=['İhsan-ı İkram Esnaf Lokantası. Bugün tencerede ne var?', 'Sıcak: çorba. Mercimek, ezogelin, tarhana, yayla.', 'Tencereden: İzmir köfte, patates ve biberle, yanında pilav.', 'Menü: çorbalar, sebze yemekleri, özel et, kıymalı yemekler.', f'Gece de açığız: 06:30–04:30. {TEL} · {ADR}'],
        post_alt='Bugün: tencereler hazır. İhsan-ı İkram, Yalı Cd., Kemalpaşa.',
        post_note='Telefon, adres, açılış saatleri ve yemek adları Google Haritalar kaydınızdan ve menü kartınızdan alındı; fiyat kullanılmadı.',
        music=[('Mahalle esnafı', 'Aramaya “turkish folk instrumental” yazın. Sıcak ve tanıdık.'), ('Akustik sabah', 'Aramaya “acoustic morning” yazın. Çorba sabahlarına.'), ('Gece sakinliği', 'Aramaya “late night lofi” yazın. Gece çıkışı sahnesine.')],
        caps=[('reel', 'Reels', f'Bugün tencerede ne var? 🍲\nSıcak çorba, İzmir köfte ve zeytinyağlılar; sabah 06:30’dan gece 04:30’a.\n\n📍 Yalı Cd., Kemalpaşa\n📞 {TEL}\n\n#İhsanıİkram #Çanakkale #esnaflokantası #evyemeği #çorba'),
              ('kar', 'Karusel', f'Esnaf lokantası usulü, her gün taze. 🥣\nÇorbalar, sebze yemekleri, özel et ve kıymalı yemekler.\nÖğle arası için kaydet. 👇\n\n📍 {ADR}\n⏰ 06:30 – 04:30\n📞 {TEL}\n\n#İhsanıİkram #Çanakkale #çanakkaleyemek #kemalpaşa'),
              ('post', 'Tek gönderi', f'Tencereler hazır. 🍲\nBugün ne yiyelim? Yorumlara yaz.\n\n📍 Yalı Cd., Kemalpaşa\n📞 {TEL}\n\n#İhsanıİkram #esnaflokantası #Çanakkale')],
        sign='<p class="kimlik">“İhsan-ı İkram” yazı-imzası menü kartınızdan; elinizde logo dosyası varsa onunla değiştiririz.</p>',
    ),
)
