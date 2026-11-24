# Veranda Coffee Company · Tasarım sistemi

> Bu dosya Veranda Coffee Company için üretilen tüm içeriklerin (karusel, post, reels, sunum sayfası) tek kaynağıdır. Yeni iş yaparken buradaki palet ve fontların dışına çıkma; değişiklik gerekiyorsa önce bu dosyayı güncelle.

- **Kategori:** Kahve dükkanı · Kordon (Yalı Cd.) + Yeni Kordon + Kepez Bahçe
- **Sunum sayfası:** https://sunum.detaymultimedia.com/veranda-coffee-company-ornek/
- **Kaynak:** Logo: menu.coffeeveranda.com kapak (kraft zemin üzerinde koyu kahve daire içinde ince el çizimi 'VERANDA' + turuncu fincan). 96×96 ölçüm: kraft #B9925A çevresi, çizgi #3E2B22, fincan #E7611D. Siyah #1C1A18 Kordon şubesinin 'şık, siyah ağırlıklı' iç mekânından (Google yorumu).
- **Son güncelleme:** 24.11.2026

## Marka gözlemi

Kordon'da deniz manzaralı kahve; Ruby cheesecake ve 'Boğaz'a karşı kahvaltı' menünün öne çıkanları; üç şube (Kordon, Yeni Kordon, Kepez Bahçe). Ton: sıcak, el yapımı, deniz kenarı.

## Renk paleti

| Token | Hex | Rol |
|---|---|---|
| `kraft` | `#B9925A` | Logo zemini: büyük alan, bant |
| `murekkep` | `#3E2B22` | Logo çizgisi: başlık, gövde |
| `fincan` | `#E7611D` | Logodaki turuncu fincan: tek vurgu, rozet |
| `krem` | `#F4EBDD` | Açık zemin, kart |
| `siyah` | `#1C1A18` | İç mekân siyahı: koyu kare |

**Oranlar:** %40 krem, %25 kraft, %20 mürekkep/siyah, %10 fincan turuncusu (yalnız vurgu).

**Kontrol edilmiş yazı/zemin çiftleri (WCAG kontrast oranı):**

- `murekkep` yazı / `krem` zemin → **11.3:1** (AA ✓) — gövde
- `murekkep` yazı / `kraft` zemin → **4.7:1** (AA ✓) — başlık / bant
- `krem` yazı / `siyah` zemin → **14.7:1** (AA ✓) — koyu kare gövde
- `fincan` yazı / `siyah` zemin → **5.1:1** (AA ✓) — büyük başlık vurgu
- `krem` yazı / `murekkep` zemin → **11.3:1** (AA ✓) — koyu kart
- `siyah` yazı / `fincan` zemin → **5.1:1** (AA ✓) — rozet yazısı

## Font sistemi

| Rol | Font | Ağırlık / stil | Nerede |
|---|---|---|---|
| Başlık | **Amatic SC** | 700 | Logodaki ince, el çizimi büyük harf 'VERANDA' karşılığı |
| Gövde | **Mulish** | 400 / 700 | Menü, açıklama, iletişim |
| Vurgu | **Kaushan Script** | 400 | Kısa sıcak not: 'Boğaz'a karşı' |

Google Fonts (Türkçe karakterler ğ ş ı İ ç ö ü kontrol edildi):

```
https://fonts.googleapis.com/css2?family=Amatic+SC:wght@700&family=Mulish:wght@400;700&family=Kaushan+Script&display=swap
```

**Ölçek (1080×1350 kare için):**

- Kapak başlığı: 150–210 px Amatic SC 700, büyük harf, +4%
- Gövde: 30 px Mulish 400
- Vurgu: 64–84 px Kaushan Script, fincan turuncusu

**Tipografi kuralları:**

- Başlık her zaman büyük harf, el çizimi hissi korunur.
- Kaushan Script kare başına bir kez.
- Turuncu yalnız vurgu ve tek rozet; zemin olarak kullanılmaz.
- Turuncu açık zeminde yazı rengi olarak kullanılmaz (2,9:1); açık karede turuncu yalnız rozet zemini, üstünde siyah yazı.

## Logo ve imza

- Logo dosyası menü kapağından; sunumda daire + 'VERANDA' yazı-imza (Amatic SC, mürekkep) ve küçük turuncu fincan noktası. Elinizde vektör logo varsa onunla değiştirilir.

## Görsel dil ve kompozisyon

- Motif: logodaki ince çift daire (fotoğraf daire çerçeve / rozet), kraft kâğıt dokusu (hafif gren).
- Fotoğraflar: Kordon, deniz, siyah masa, Ruby cheesecake.
- Reels: deniz kenarından yavaş yakınlaşma.

## Fotoğraf yönü (Higgsfield prompt eki)

```
warm kraft brown and black tones with a touch of burnt orange, seaside light, photorealistic, no people, no text, no logos, no letters
```

## Sunum sayfası CSS değişkenleri

```css
:root {
  --kraft: #B9925A;
  --murekkep: #3E2B22;
  --fincan: #E7611D;
  --krem: #F4EBDD;
  --siyah: #1C1A18;
  --font-baslik: 'Amatic SC', sans-serif;
  --font-govde: 'Mulish', sans-serif;
  --font-vurgu: 'Kaushan Script', cursive;
}
```

## Yapma

- Turuncuyu büyük zemin yapma.
- Soğuk mavi/gri palet kullanma.
- Çok kalın blok font kullanma; logo ince ve el çizimi.
- Şu fontları kullanma (standart/aşırı kullanılmış): Inter, Manrope, Fraunces, Playfair Display, Cormorant / Cormorant Garamond, DM Serif Display, DM Sans, Space Grotesk, Caveat, Pacifico, Anton, Bebas Neue, Archivo / Archivo Black, Jost, Nunito, Poppins, Montserrat, Roboto, Open Sans, Lato, Lora, Outfit, Plus Jakarta Sans, Raleway, Oswald, Work Sans, Instrument Sans / Instrument Serif, Arial / Helvetica / system-ui.
