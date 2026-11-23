"""Teklif içerik üreticisi: firma tasarım dosyasına (tasarim/<slug>.md) göre
karusel + post (1080x1350), reels (720x1280, ffmpeg zoompan + xfade) ve sunum sayfası.

Kullanım: python3 araclar/sunum.py <firma-slug> <ham-foto-klasörü> <çıktı-klasörü>
Firma ayarları araclar/firmalar/<slug_alt_cizgi>.py içinde (CFG sözlüğü).
"""
import html as H, importlib.util, json, os, subprocess, sys, shutil
from pathlib import Path
from playwright.sync_api import sync_playwright

REPO = Path(__file__).resolve().parent.parent

def doc(cfg, body, w, h, transparent=False, photos=None):
    bg = 'transparent' if transparent else 'var(--zemin, #000)'
    return f"""<!doctype html><html lang="tr"><head><meta charset="utf-8">
<link href="{cfg['fonts_url']}" rel="stylesheet"><style>
:root{{{cfg['tokens']}}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:{w}px;height:{h}px;overflow:hidden;background:{bg}}}
.s{{position:relative;width:{w}px;height:{h}px;overflow:hidden}}
.ph{{position:absolute;inset:0;background-size:cover;background-position:center}}
{cfg['css']}
</style></head><body>{body}</body></html>"""

def photo_url(photos, name):
    return 'file://' + str(Path(photos) / name)

def render_all(cfg, photos, out):
    out = Path(out); out.mkdir(parents=True, exist_ok=True)
    tmp = out / '_html'; tmp.mkdir(exist_ok=True)
    P = lambda n: photo_url(photos, n)
    jobs = []
    for i, s in enumerate(cfg['slides'], 1):
        jobs.append((f'karusel_{i}', s(P), 1080, 1350, False))
    jobs.append(('post', cfg['post'](P), 1080, 1350, False))
    for i, (ph, ov) in enumerate(cfg['reel'], 1):
        jobs.append((f'reel_ov_{i}', ov, 720, 1280, True))
    with sync_playwright() as p:
        b = p.chromium.launch()
        for name, body, w, h, tr in jobs:
            f = tmp / f'{name}.html'
            f.write_text(doc(cfg, body, w, h, tr), encoding='utf-8')
            pg = b.new_page(viewport={'width': w, 'height': h})
            pg.goto('file://' + str(f)); pg.wait_for_load_state('networkidle')
            pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(250)
            pg.screenshot(path=str(out / f'{name}.png'), omit_background=tr)
            pg.close()
        b.close()

def reel(cfg, photos, out, per=3.4, xf=0.5):
    out = Path(out); clips = []
    for i, (ph, ov) in enumerate(cfg['reel'], 1):
        c = out / f'_clip{i}.mp4'; n = int(per * 30)
        zin = i % 2 == 1
        z = "min(zoom+0.0011,1.15)" if zin else "if(eq(on,0),1.15,max(zoom-0.0011,1.0))"
        vf = (f"[0:v]scale=1440:2560:force_original_aspect_ratio=increase,crop=1440:2560,{cfg.get('reel_pre', '')}"
              f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=720x1280:fps=30,format=yuv420p[bg];"
              f"[1:v]format=rgba,fade=in:st=0.25:d=0.45:alpha=1[ov];[bg][ov]overlay=0:0:shortest=1,format=yuv420p")
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-loop', '1', '-t', str(per), '-i', str(Path(photos) / ph),
                        '-loop', '1', '-t', str(per), '-i', str(out / f'reel_ov_{i}.png'),
                        '-filter_complex', vf, '-t', str(per), '-r', '30', '-c:v', 'libx264', '-crf', '20', str(c)], check=True)
        clips.append(c)
    args = []; [args.extend(['-i', str(c)]) for c in clips]
    fc = []; last = '[0:v]'; off = 0
    for k in range(1, len(clips)):
        off += per - xf
        lab = f'[v{k}]'
        fc.append(f"{last}[{k}:v]xfade=transition=fade:duration={xf}:offset={off:.2f}{lab}")
        last = lab
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', *args, '-filter_complex', ';'.join(fc), '-map', last,
                    '-c:v', 'libx264', '-crf', '23', '-preset', 'slow', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', '-an',
                    str(out / 'reel.mp4')], check=True)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-ss', '1.2', '-i', str(out / 'reel.mp4'), '-frames:v', '1', '-q:v', '3',
                    str(out / 'reel_poster.jpg')], check=True)
    for c in clips: c.unlink()

def page(cfg):
    pg = cfg['page']; slug = cfg['slug']
    figs = []
    for i, alt in enumerate(pg['alts'], 1):
        lazy = '' if i == 1 else ' loading="lazy"'
        figs.append(f'      <figure><img class="shot" src="img/karusel_{i}.jpg" alt="Kare {i}: {H.escape(alt)}" width="1080" height="1350"{lazy}></figure>')
    music = '\n'.join(f'      <li><b>{H.escape(a)}</b><span>{H.escape(b)}</span></li>' for a, b in pg['music'])
    caps = []
    for key, title, txt in pg['caps']:
        caps.append(f'''    <div class="cap">
      <div class="cap-top"><h3>{title}</h3><button class="copy" type="button" data-copy="cap-{key}">Kopyala</button></div>
      <pre id="cap-{key}">{H.escape(txt)}</pre>
    </div>''')
    tpl = (REPO / 'araclar' / 'sayfa_sablon.html').read_text(encoding='utf-8')
    rep = {
        '{{SLUG}}': slug, '{{NAME}}': H.escape(cfg['name']), '{{FONTS}}': cfg['fonts_url'],
        '{{VARS}}': pg['vars'], '{{EXTRA_CSS}}': pg.get('extra_css', ''), '{{MOTIF}}': pg.get('motif', ''),
        '{{LEDE}}': pg['lede'], '{{REEL_META}}': pg['reel_meta'], '{{REEL_NOTE}}': pg['reel_note'],
        '{{N}}': str(len(pg['alts'])), '{{FIGS}}': '\n'.join(figs), '{{POST_ALT}}': H.escape(pg['post_alt']),
        '{{POST_NOTE}}': pg['post_note'], '{{MUSIC}}': music, '{{CAPS}}': '\n\n'.join(caps),
        '{{SIGN}}': pg.get('sign', ''),
    }
    for k, v in rep.items(): tpl = tpl.replace(k, v)
    return tpl

def load(slug):
    f = REPO / 'araclar' / 'firmalar' / (slug.replace('-', '_') + '.py')
    spec = importlib.util.spec_from_file_location('cfg', f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.CFG

def main(slug, photos, out, skip_reel=False):
    cfg = load(slug); out = Path(out)
    render_all(cfg, photos, out)
    if not skip_reel: reel(cfg, photos, out)
    dst = REPO / 'sunum' / f'{slug}-ornek'; (dst / 'img').mkdir(parents=True, exist_ok=True); (dst / 'video').mkdir(exist_ok=True)
    from PIL import Image
    for f in sorted(out.glob('karusel_*.png')) + [out / 'post.png']:
        Image.open(f).convert('RGB').save(dst / 'img' / (f.stem + '.jpg'), quality=88, optimize=True, progressive=True)
    for old in (dst / 'img').glob('karusel_*.jpg'):
        if not (out / (old.stem + '.png')).exists(): old.unlink()
    if (out / 'reel.mp4').exists():
        shutil.copy(out / 'reel.mp4', dst / 'video' / 'reel.mp4'); shutil.copy(out / 'reel_poster.jpg', dst / 'img' / 'reel_poster.jpg')
    (dst / 'index.html').write_text(page(cfg), encoding='utf-8')
    print('ok', dst)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], '--no-reel' in sys.argv)
