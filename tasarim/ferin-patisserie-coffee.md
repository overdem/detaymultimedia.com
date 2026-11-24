# ferin | patisserie & coffee · Tasarım sistemi

> Bu dosya ferin | patisserie & coffee için üretilen tüm içeriklerin (karusel, post, reels, sunum sayfası) tek kaynağıdır. Yeni iş yaparken buradaki palet ve fontların dışına çıkma; değişiklik gerekiyorsa önce bu dosyayı güncelle.

- **Kategori:** Butik pastane / kahve · Kemalpaşa, Dibek Sk.
- **Sunum sayfası:** https://sunum.detaymultimedia.com/ferin-patisserie-coffee-ornek/
- **Kaynak:** Logo: ferin.com.tr/assets/images/ferin-logo.png (bordo 'fJ' monogram + klasik serif 'FÈRIN PATISSERIE & COFFEE'). 96×96 ölçüm: bordo #4A1B1B. Fildişi, gül kurusu ve altın kırıntısı tonları butik iç mekândan türetildi (öneri).
- **Son güncelleme:** 24.11.2026

## Marka gözlemi

Tarihi Kemalpaşa sokaklarında butik pastane; tatlılar Büşra Hanım'ın kendi elinden; kirazlı tart ve focaccia yorumlarda öne çıkıyor; Google 4,7 (123). Ton: zarif, sakin, el yapımı.

## Renk paleti

| Token | Hex | Rol |
|---|---|---|
| `bordo` | `#4A1B1B` | Logo: başlık, gövde, koyu zemin |
| `fildisi` | `#F7F1E8` | Ana açık zemin |
| `gul` | `#C9928A` | Gül kurusu: ince çizgi, büyük vurgu (öneri) |
| `kaymak` | `#EDE2D3` | İkincil zemin, kart |
| `altin` | `#A8834F` | Altın kırıntısı: ayrıntı (büyük boyutta) |

**Oranlar:** %55 fildişi/kaymak, %30 bordo, %10 gül kurusu, %5 altın.

**Kontrol edilmiş yazı/zemin çiftleri (WCAG kontrast oranı):**

- `bordo` yazı / `fildisi` zemin → **12.8:1** (AA ✓) — gövde
- `bordo` yazı / `kaymak` zemin → **11.2:1** (AA ✓) — kart gövde
- `fildisi` yazı / `bordo` zemin → **12.8:1** (AA ✓) — koyu kare
- `gul` yazı / `bordo` zemin → **5.4:1** (AA ✓) — büyük vurgu
- `altin` yazı / `fildisi` zemin → **3.1:1** (yalnız büyük başlık ✓) — büyük ayrıntı

## Font sistemi

| Rol | Font | Ağırlık / stil | Nerede |
|---|---|---|---|
| Başlık | **EB Garamond** | 500 / 600 | Logodaki klasik serif 'FÈRIN' karşılığı, büyük harf geniş aralık |
| Gövde | **Be Vietnam Pro** | 400 / 600 | Menü, açıklama |
| Vurgu | **Parisienne** | 400 | Kısa not: 'el yapımı' |

Google Fonts (Türkçe karakterler ğ ş ı İ ç ö ü kontrol edildi):

```
https://fonts.googleapis.com/css2?family=EB+Garamond:wght@500;600&family=Be+Vietnam+Pro:wght@400;600&family=Parisienne&display=swap
```

**Ölçek (1080×1350 kare için):**

- Kapak başlığı: 110–150 px EB Garamond 500, büyük harf, +12%
- Gövde: 29 px Be Vietnam Pro 400
- Vurgu: 76–96 px Parisienne, gül kurusu/bordo

**Tipografi kuralları:**

- Başlık büyük harf, geniş harf aralığı (logodaki gibi).
- Parisienne kare başına bir kez.
- Bol boşluk; ortalı, sakin.

## Logo ve imza

- Web sitesindeki 'fJ' monogram + yazı; sunumda monogram yerine yazı-imza 'FERİN' EB Garamond + 'PATISSERIE & COFFEE'. Vektör logo varsa onunla değiştirilir.

## Görsel dil ve kompozisyon

- Motif: ince çift çerçeve (0.5 px + 2 px) ve oval fotoğraf penceresi, pasta kutusu kurdelesi gibi ince yatay çizgi.
- Fotoğraflar: tart, vitrin, focaccia; mermer ve porselen.
- Reels: yakın plan, yavaş.

## Fotoğraf yönü (Higgsfield prompt eki)

```
elegant patisserie, deep burgundy and warm ivory tones, soft window light, photorealistic, no people, no text, no logos, no letters
```

## Sunum sayfası CSS değişkenleri

```css
:root {
  --bordo: #4A1B1B;
  --fildisi: #F7F1E8;
  --gul: #C9928A;
  --kaymak: #EDE2D3;
  --altin: #A8834F;
  --font-baslik: 'EB Garamond', serif;
  --font-govde: 'Be Vietnam Pro', sans-serif;
  --font-vurgu: 'Parisienne', cursive;
}
```

## Yapma

- Parlak pembe/şeker renkleri kullanma.
- Kalın grotesk başlık kullanma.
- Şu fontları kullanma (standart/aşırı kullanılmış): Inter, Manrope, Fraunces, Playfair Display, Cormorant / Cormorant Garamond, DM Serif Display, DM Sans, Space Grotesk, Caveat, Pacifico, Anton, Bebas Neue, Archivo / Archivo Black, Jost, Nunito, Poppins, Montserrat, Roboto, Open Sans, Lato, Lora, Outfit, Plus Jakarta Sans, Raleway, Oswald, Work Sans, Instrument Sans / Instrument Serif, Arial / Helvetica / system-ui.
