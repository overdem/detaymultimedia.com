# Rokka Kahvaltı (Rokka Brunch) · Tasarım sistemi

> Bu dosya Rokka Kahvaltı (Rokka Brunch) için üretilen tüm içeriklerin (karusel, post, reels, sunum sayfası) tek kaynağıdır. Yeni iş yaparken buradaki palet ve fontların dışına çıkma; değişiklik gerekiyorsa önce bu dosyayı güncelle.

- **Kategori:** Kahvaltı / brunch · Aynalı Çarşı
- **Sunum sayfası:** https://sunum.detaymultimedia.com/rokka-kahvalti-ornek/
- **Kaynak:** Instagram @rokkakahvalti profil logosu (21.11.2026): yuvarlak krem zemin, çizim roka/yeşillik ve lavanta dalları, adaçayı yeşili şerit üstünde beyaz kalın el yazısı 'Rokka', altında 'BRUNCH'.
- **Son güncelleme:** 21.11.2026

## Marka gözlemi

Bitkisel, illüstratif: adaçayı/zeytin yeşili + lavanta + krem. Yazı kalın, yuvarlak el yazısı. Aynalı Çarşı'da, genç ve brunch odaklı. Ton: taze, bahçe, yumuşak; 'roka' kelime oyunu.

## Renk paleti

| Token | Hex | Rol |
|---|---|---|
| `roka` | `#6F8A45` | Logo şeridi: ana renk, buton |
| `orman` | `#33472A` | Başlık ve gövde yazısı |
| `lavanta` | `#A595BE` | İkincil vurgu: etiket, çiçek |
| `krem` | `#EFE8D6` | Ana zemin |
| `yumurta` | `#F2B33D` | Kahvaltı vurgusu: yumurta sarısı, fiyat (az) |

**Oranlar:** %50 krem, %25 roka/orman, %15 lavanta, %10 yumurta.

**Kontrol edilmiş yazı/zemin çiftleri (WCAG kontrast oranı):**

- `orman` yazı / `krem` zemin → **8.3:1** (AA ✓) — başlık/gövde
- `krem` yazı / `roka` zemin → **3.2:1** (yalnız büyük başlık ✓) — şerit yazısı (büyük)
- `krem` yazı / `orman` zemin → **8.3:1** (AA ✓) — koyu kart
- `orman` yazı / `lavanta` zemin → **3.7:1** (yalnız büyük başlık ✓) — etiket
- `orman` yazı / `yumurta` zemin → **5.4:1** (AA ✓) — fiyat rozeti

## Font sistemi

| Rol | Font | Ağırlık / stil | Nerede |
|---|---|---|---|
| Başlık | **Shrikhand** | 400 | Logodaki kalın yuvarlak el yazısının karşılığı; kapak başlığı |
| Gövde | **Epilogue** | 400 / 600 | Menü, saat, rezervasyon |
| Not | **Mynerve** | 400 | El yazısı not: 'şefin önerisi', ok ile işaretleme |

Google Fonts (Türkçe karakterler ğ ş ı İ ç ö ü kontrol edildi):

```
https://fonts.googleapis.com/css2?family=Shrikhand&family=Epilogue:wght@400;600&family=Mynerve&display=swap
```

**Ölçek (1080×1350 kare için):**

- Kapak başlığı: 96–120 px Shrikhand
- Ara başlık: 48 px Epilogue 600
- Gövde: 30 px Epilogue 400
- El notu: 40–48 px Mynerve + çizim ok

**Tipografi kuralları:**

- Shrikhand yalnız kısa başlık (en fazla 3 kelime).
- 'BRUNCH' gibi alt kelimeler Epilogue 600 büyük harf, +18% aralık (logodaki gibi).
- El notları yamuk ok/daire çizimiyle birlikte.

## Logo ve imza

- Yuvarlak illüstrasyon logo sağ altta, genişliğin %18'i.
- Logodaki roka/lavanta çizimleri kare köşelerinde süs olarak kırpılmış kullanılabilir.

## Görsel dil ve kompozisyon

- Motif: çizim roka yaprakları ve lavanta dalları kenarlardan taşar; krem zemin.
- Kahvaltı tabağı kuşbakışı, masa krem/ahşap.
- Reels: kuşbakışı masa kurulumu stop-motion; yaprak çizimleri yanıp söner.

## Fotoğraf yönü (Higgsfield prompt eki)

```
Overhead Turkish breakfast brunch spread, fresh arugula, herbs, eggs, cheeses, olives, lavender sprigs on a cream linen table, soft daylight, fresh green and cream palette, no text, no logos
```

## Sunum sayfası CSS değişkenleri

```css
:root {
  --roka: #6F8A45;
  --orman: #33472A;
  --lavanta: #A595BE;
  --krem: #EFE8D6;
  --yumurta: #F2B33D;
  --font-baslik: 'Shrikhand', cursive;
  --font-govde: 'Epilogue', sans-serif;
  --font-vurgu: 'Mynerve', cursive;
}
```

## Yapma

- Koyu/siyah zemin kullanma.
- Keskin geometrik/modern minimal stil yapma; marka el çizimi.
- Lavantayı ana zemin yapma.
- Şu fontları kullanma (standart/aşırı kullanılmış): Inter, Manrope, Fraunces, Playfair Display, Cormorant / Cormorant Garamond, DM Serif Display, DM Sans, Space Grotesk, Caveat, Pacifico, Anton, Bebas Neue, Archivo / Archivo Black, Jost, Nunito, Poppins, Montserrat, Roboto, Open Sans, Lato, Lora, Outfit, Plus Jakarta Sans, Raleway, Oswald, Work Sans, Instrument Sans / Instrument Serif, Arial / Helvetica / system-ui.
