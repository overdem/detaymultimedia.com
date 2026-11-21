# Liman Paşa Müdavim · Tasarım sistemi

> Bu dosya Liman Paşa Müdavim için üretilen tüm içeriklerin (karusel, post, reels, sunum sayfası) tek kaynağıdır. Yeni iş yaparken buradaki palet ve fontların dışına çıkma; değişiklik gerekiyorsa önce bu dosyayı güncelle.

- **Kategori:** Restoran · balık & et, Eski Balıkhane
- **Sunum sayfası:** https://sunum.detaymultimedia.com/liman-pasa-mudavim-ornek/
- **Kaynak:** Instagram @liman_pasamudavim profil logosu (21.11.2026): beyaz zemin üstünde siyah oval, altın el yazısı 'Paşa' + küçük 'Müdavim', altında aralıklı büyük harf 'LİMAN'.
- **Son güncelleme:** 21.11.2026

## Marka gözlemi

Siyah oval + altın script + aralıklı serif büyük harf: klasik meyhane/liman lokantası şıklığı. 'Müdavim' kelimesi sadakat anlatısı veriyor. Ton: gece, rakı sofrası, saygın.

## Renk paleti

| Token | Hex | Rol |
|---|---|---|
| `gece` | `#0B0B0B` | Ana zemin (logo ovali) |
| `pasa-altin` | `#DDB032` | Logo script rengi: vurgu, çizgi, başlık kelimesi |
| `fildisi` | `#F5F0E4` | Yazı, açık kart |
| `liman` | `#13303F` | İkincil koyu: deniz/gece mavisi kart |
| `duman` | `#8C8C8C` | İkincil gövde, ayrıntı |

**Oranlar:** %60 gece/liman, %25 fildisi, %10 pasa-altin, %5 duman.

**Kontrol edilmiş yazı/zemin çiftleri (WCAG kontrast oranı):**

- `fildisi` yazı / `gece` zemin → **17.3:1** (AA ✓) — gövde
- `pasa-altin` yazı / `gece` zemin → **9.7:1** (AA ✓) — vurgu/başlık
- `fildisi` yazı / `liman` zemin → **12.1:1** (AA ✓) — kart yazısı
- `gece` yazı / `fildisi` zemin → **17.3:1** (AA ✓) — açık kart
- `duman` yazı / `gece` zemin → **5.9:1** (AA ✓) — ikincil bilgi (büyük)

## Font sistemi

| Rol | Font | Ağırlık / stil | Nerede |
|---|---|---|---|
| Başlık | **Marcellus** | 400 | 'LİMAN' gibi aralıklı büyük harf başlıklar |
| Script | **Pinyon Script** | 400 | Logodaki altın 'Paşa' yazısının karşılığı; tek kelime/isim |
| Gövde | **Spectral** | 400 / 500 | Menü, açıklama, rezervasyon |

Google Fonts (Türkçe karakterler ğ ş ı İ ç ö ü kontrol edildi):

```
https://fonts.googleapis.com/css2?family=Marcellus&family=Pinyon+Script&family=Spectral:wght@400;500&display=swap
```

**Ölçek (1080×1350 kare için):**

- Kapak başlığı: 72–96 px Marcellus büyük harf, harf aralığı +24%
- Script: 110–140 px Pinyon Script, altın
- Gövde: 30 px Spectral 400
- Etiket: 20 px Marcellus, +30%

**Tipografi kuralları:**

- Kapak düzeni logodan: üstte script altın kelime, altında aralıklı büyük harf satır.
- Pinyon Script kare başına en fazla bir kez.
- Tüm metinler ortalı; liman/gece ciddiyeti.

## Logo ve imza

- Siyah oval logo, fildişi zeminde ya da siyah karede altın kontur ile; genişliğin %22'si.
- Logo ovali şeklinde fotoğraf maskesi kullanılabilir.

## Görsel dil ve kompozisyon

- Motif: ince altın oval çerçeve, kare ortasında; çift ince altın çizgi ayraç.
- Fotoğraflar akşam ışığı, sofra; kenarlarda gece payı.
- Reels: yavaş tempolu, mum/ışık yansımaları; altın çizgi soldan sağa açılır.

## Fotoğraf yönü (Higgsfield prompt eki)

```
Evening harbor restaurant in Çanakkale, raki table with meze and grilled fish, candlelight and warm bulbs, dark navy sea and boats in background, elegant classic atmosphere, deep blacks and warm gold highlights, no text, no logos
```

## Sunum sayfası CSS değişkenleri

```css
:root {
  --gece: #0B0B0B;
  --pasa-altin: #DDB032;
  --fildisi: #F5F0E4;
  --liman: #13303F;
  --duman: #8C8C8C;
  --font-baslik: 'Marcellus', serif;
  --font-vurgu: 'Pinyon Script', cursive;
  --font-govde: 'Spectral', Georgia, serif;
}
```

## Yapma

- Açık/pastel zeminli karusel yapma.
- Modern grotesk başlık kullanma.
- Altını parlak gradyan/metal efekt yapma.
- Şu fontları kullanma (standart/aşırı kullanılmış): Inter, Manrope, Fraunces, Playfair Display, Cormorant / Cormorant Garamond, DM Serif Display, DM Sans, Space Grotesk, Caveat, Pacifico, Anton, Bebas Neue, Archivo / Archivo Black, Jost, Nunito, Poppins, Montserrat, Roboto, Open Sans, Lato, Lora, Outfit, Plus Jakarta Sans, Raleway, Oswald, Work Sans, Instrument Sans / Instrument Serif, Arial / Helvetica / system-ui.
