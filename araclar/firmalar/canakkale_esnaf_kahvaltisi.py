# tasarim/canakkale-esnaf-kahvaltisi.md — arduvaz/kağıt/defne, Bona Nova + Literata + Courier Prime, defne çelengi + fiş motifi
import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from motif import laurel
TEL = '0542 778 94 17'; ADR = 'Demircioğlu Cd. 87/C · İsmetpaşa'
CSS = """
.s{background:var(--kagit);color:var(--arduvaz);font-family:var(--font-govde);text-align:center}
.t{font:700 92px/1.02 var(--font-baslik);text-transform:uppercase;letter-spacing:.04em}
.sub{font:400 21px var(--font-baslik);letter-spacing:.22em;text-transform:uppercase}
.bd{font:400 30px/1.45 var(--font-govde)}
.fis{background:var(--kagit);color:var(--murekkep);font:400 27px/1.7 var(--font-vurgu);text-align:left;padding:34px 40px;border-top:3px dotted var(--arduvaz);border-bottom:3px dotted var(--arduvaz)}
.fis b{font-weight:700}
.row{display:flex;gap:10px}.row i{flex:1;border-bottom:3px dotted rgba(51,71,90,.5);transform:translateY(-10px)}
.wr{position:relative;display:inline-block}.wr svg{display:block}
.wr .in{position:absolute;left:0;right:0;top:50%;transform:translateY(-38%)}
.frame{position:absolute;background-size:cover;background-position:center}
.r .t{font-size:64px}.r .sub{font-size:16px}.r .bd{font-size:24px}.r .fis{font-size:21px;padding:22px 28px}
"""
def s1(P): return f"""<div class="s"><div class="frame" style="left:56px;top:56px;width:968px;height:720px;background-image:url('{P('b2ce1c66.png')}')"></div>
<div style="position:absolute;left:0;right:0;top:820px"><div class="t" style="font-size:96px">Günaydın<br>İsmetpaşa</div>
<div style="margin-top:10px">{laurel('#8C9A80', 200)}</div><div class="sub">Esnaf kahvaltısı · Pişi · Menemen</div></div></div>"""
def s2(P): return f"""<div class="s"><div class="ph" style="background-image:url('{P('4b657f25.png')}')"></div>
<div class="fis" style="position:absolute;left:70px;right:70px;bottom:70px">
<div style="font:700 60px var(--font-baslik);letter-spacing:.04em;color:var(--arduvaz);margin-bottom:12px">PİŞİ TABAĞI</div>
<div class="row"><span>Sıcak pişi</span><i></i><b>✓</b></div><div class="row"><span>Beyaz peynir, zeytin</span><i></i><b>✓</b></div><div class="row"><span>Gül reçeli</span><i></i><b>✓</b></div><div class="row"><span>İnce belli çay</span><i></i><b>hazır</b></div></div></div>"""
def s3(P): return f"""<div class="s" style="background:var(--murekkep);color:var(--kagit)"><div class="frame" style="left:90px;top:90px;width:900px;height:880px;background-image:url('{P('0833558a.png')}');border:14px solid var(--kagit)"></div>
<div style="position:absolute;left:60px;right:60px;top:1020px"><div class="t" style="font-size:84px">Tavada menemen</div>
<div style="width:120px;height:6px;background:var(--pisi);margin:24px auto"></div><div class="bd">Sofraya tavasıyla, dumanı üstünde gelir.</div></div></div>"""
def s4(P): return f"""<div class="s"><div style="position:absolute;left:0;right:0;top:40px"><div class="wr">{laurel('#33475A', 800)}<div class="in"><div class="t" style="font-size:74px">Bekleriz!</div><div class="sub" style="margin-top:14px;font-size:18px">Çanakkale’nin ilk<br>esnaf kahvaltıcısı</div></div></div></div>
<div class="fis" style="position:absolute;left:110px;right:110px;top:900px;font-size:30px;padding:24px 40px">
<div class="row"><span>AÇILIŞ</span><i></i><b>07:00</b></div><div class="row"><span>TELEFON</span><i></i><b>{TEL}</b></div><div class="row"><span>ADRES</span><i></i><b>Demircioğlu Cd. 87/C</b></div><div class="row"><span></span><i style="border:0"></i><b>İsmetpaşa</b></div></div>
<div class="sub" style="position:absolute;left:0;right:0;bottom:56px;color:#5f6d55">Paket kahvaltı · Pişi · Gözleme</div></div>"""
def post(P): return f"""<div class="s"><div class="frame" style="left:0;top:0;width:1080px;height:960px;background-image:url('{P('f194e2be.png')}')"></div>
<div style="position:absolute;left:0;right:0;top:960px;height:390px;padding-top:46px;border-top:6px solid var(--pisi)"><div class="t" style="font-size:80px">Çay demlendi,<br>sofra hazır</div>
<div class="sub" style="margin-top:22px">Sabah 07:00’den itibaren · İsmetpaşa</div></div></div>"""
def ov(t, sub=None, fis=None):
    s = f'<div class="sub" style="margin-top:12px">{sub}</div>' if sub else ''
    f = f'<div class="fis" style="margin-top:26px">{fis}</div>' if fis else ''
    return f"""<div class="s r" style="background:transparent"><div style="position:absolute;left:44px;right:44px;bottom:110px;background:rgba(250,248,243,.95);padding:34px 26px;border-top:4px dotted var(--arduvaz);border-bottom:4px dotted var(--arduvaz)"><div class="t">{t}</div>{s}{f}</div></div>"""
CTA_FIS = f'<div class="row"><span>AÇILIŞ</span><i></i><b>07:00</b></div><div class="row"><span>TEL</span><i></i><b>{TEL}</b></div>'
CFG = dict(
    slug='canakkale-esnaf-kahvaltisi', name='Çanakkale Esnaf Kahvaltısı',
    fonts_url='https://fonts.googleapis.com/css2?family=Bona+Nova:wght@400;700&family=Literata:wght@400;600&family=Courier+Prime:wght@400;700&display=swap',
    tokens='--arduvaz:#33475A;--murekkep:#1E2A36;--defne:#8C9A80;--kagit:#FAF8F3;--pisi:#E8A93A;--font-baslik:"Bona Nova",Georgia,serif;--font-govde:"Literata",Georgia,serif;--font-vurgu:"Courier Prime",monospace;--zemin:#FAF8F3',
    css=CSS, slides=[s1, s2, s3, s4], post=post,
    reel=[('b2ce1c66.png', ov('Günaydın<br>İsmetpaşa', 'Esnaf kahvaltısı')),
          ('4b657f25.png', ov('Pişi tabağı', 'Peynir · zeytin · reçel')),
          ('0833558a.png', ov('Tavada menemen', 'Dumanı üstünde')),
          ('f194e2be.png', ov('Çay demlendi', 'Sofra hazır')),
          ('b2ce1c66.png', ov('Bekleriz!', 'Demircioğlu Cd. 87/C · İsmetpaşa', CTA_FIS))],
    page=dict(
        vars='  color-scheme: light;\n  --bg: #FAF8F3;\n  --panel: #ffffff;\n  --line: #d9d6cc;\n  --text: #1E2A36;\n  --muted: #4f5d6b;\n  --accent: #33475A;\n  --accent-ink: #FAF8F3;\n  --display: "Bona Nova", Georgia, serif;\n  --display-w: 700;\n  --body: "Literata", Georgia, serif;\n  --vurgu: "Courier Prime", monospace;',
        extra_css='h1 { text-transform: uppercase; letter-spacing: .03em; color: var(--accent); }\nh1 em { font-style: normal; color: #6f7d63; display: block; font-size: .62em; letter-spacing: .14em; margin-top: 6px; }\n.eyebrow { color: #6f7d63; }\n.meta, .cap pre { font-family: var(--vurgu); }\n.head { border-bottom: 2px dotted var(--accent); }\n.motif svg { display: block; margin: 0 auto; }\n.dots button[aria-current="true"] { background: #E8A93A; }\n',
        motif=f'<div class="motif" aria-hidden="true">{laurel("#8C9A80", 120)}</div>',
        lede='Haftalık paylaşımların nasıl görüneceğini göstermek için hazırladığımız kısa bir reels, dört karelik bir karusel ve sabah gönderisi; logonuzdaki arduvaz, kâğıt ve defne çelengiyle.',
        reel_meta='15 sn · dikey',
        reel_note='Esnaf kahvaltısı, pişi tabağı, tavada menemen ve demlenen çay; 5 sahnede sabahınız. Video sessizdir; müzik Instagram’da paylaşırken eklenir.',
        alts=['Günaydın İsmetpaşa! Esnaf kahvaltısı, pişi, menemen.', 'Pişi tabağı: sıcak pişi, peynir, zeytin, gül reçeli; çayınız da hazır.', 'Tavada menemen, sofraya tavasıyla gelir.', f'Bekleriz! Çanakkale’nin ilk esnaf kahvaltıcısı. Açılış 07:00 · {TEL} · {ADR}'],
        post_alt='Çay demlendi, sofra hazır. Sabah 07:00’den itibaren, İsmetpaşa.',
        post_note='Telefon, adres ve açılış saati Google Haritalar kaydınızdan; “ilk esnaf kahvaltıcısı” ifadesi Instagram biyografinizden alındı.',
        music=[('Neşeli ukulele', 'Aramaya “happy ukulele morning” yazın. Güler yüzlü bir sabah.'), ('Akustik gitar', 'Aramaya “acoustic morning” yazın. Sıcak ve samimi.'), ('Mahalle havası', 'Aramaya “turkish folk instrumental” yazın. Esnaf sofrasına yakışır.')],
        caps=[('reel', 'Reels', f'Günaydın İsmetpaşa! ☀️\nEsnaf kahvaltısı, sıcak pişi, tavada menemen ve demli çay.\n\n📍 Demircioğlu Cd. 87/C, İsmetpaşa\n📞 {TEL}\n\n#EsnafKahvaltısı #Çanakkale #kahvaltı #pişi #menemen'),
              ('kar', 'Karusel', f'Bugünün sofrası hazır. 🍳\nPişi tabağı, menemen, peynir, zeytin, reçel ve sınırsız sohbet.\nKahvaltı planına kaydet. 👇\n\n📍 {ADR}\n⏰ Sabah 07:00’den itibaren\n📞 {TEL}\n\n#EsnafKahvaltısı #Çanakkale #çanakkalekahvaltı #ismetpaşa'),
              ('post', 'Tek gönderi', f'Çay demlendi, sofra hazır. ☕️\nGüne güzel bir kahvaltıyla başlayın.\n\n📞 {TEL}\n📍 Demircioğlu Cd. 87/C\n\n#EsnafKahvaltısı #günaydın #Çanakkale')],
    ),
)
