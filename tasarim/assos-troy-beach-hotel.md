# Assos Troy Beach Hotel · Tasarım sistemi

> Bu dosya Assos Troy Beach Hotel için üretilen tüm içeriklerin (karusel, post, reels, sunum sayfası) tek kaynağıdır. Yeni iş yaparken buradaki palet ve fontların dışına çıkma; değişiklik gerekiyorsa önce bu dosyayı güncelle.

- **Kategori:** Konaklama · Behram / Kadırga Koyu + Troy Port Hotel (Assos Antik Liman)
- **Sunum sayfası:** https://sunum.detaymultimedia.com/assos-troy-beach-hotel-ornek/
- **Kaynak:** Logo: troybeachhotel.com SVG (bakır gradyan 'ASSOS TROY BEACH HOTEL', #D99983 → #966638); site metin rengi #5A422B. Deniz mavisi ve çim yeşili Kadırga Koyu fotoğraflarından (site 'Mavi ve Yeşilin Buluştuğu Nokta').
- **Son güncelleme:** 24.11.2026

## Marka gözlemi

Kadırga Koyu'nda denize sıfır, havuzlu ve plajlı otel; Google 4,9 (1.371); kardeş otel Troy Port, Assos Antik Liman'da yıl boyu açık. Ton: Ege, sıcak, ferah.

## Renk paleti

| Token | Hex | Rol |
|---|---|---|
| `bakir` | `#966638` | Logo koyu bakır: başlık vurgu, çizgi |
| `pembe_bakir` | `#D99983` | Logo açık bakır: büyük vurgu, rozet |
| `toprak` | `#5A422B` | Metin: gövde, başlık |
| `deniz` | `#1F5F73` | Kadırga Koyu denizi: koyu zemin |
| `kum` | `#F8F1EA` | Açık zemin |

**Oranlar:** %45 kum, %25 deniz, %15 toprak, %15 bakır tonları.

**Kontrol edilmiş yazı/zemin çiftleri (WCAG kontrast oranı):**

- `toprak` yazı / `kum` zemin → **8.3:1** (AA ✓) — gövde
- `kum` yazı / `deniz` zemin → **6.4:1** (AA ✓) — koyu kare
- `bakir` yazı / `kum` zemin → **4.4:1** (yalnız büyük başlık ✓) — büyük başlık
- `pembe_bakir` yazı / `deniz` zemin → **3.0:1** (yalnız büyük başlık ✓) — büyük vurgu
- `kum` yazı / `toprak` zemin → **8.3:1** (AA ✓) — koyu kart

## Font sistemi

| Rol | Font | Ağırlık / stil | Nerede |
|---|---|---|---|
| Başlık | **Castoro** | 400 (+italik) | Logodaki klasik serif 'TROY' karşılığı |
| Gövde | **Mukta** | 400 / 600 | Açıklama, iletişim |
| Vurgu | **Alex Brush** | 400 | Kısa not: 'Assos' |

Google Fonts (Türkçe karakterler ğ ş ı İ ç ö ü kontrol edildi):

```
https://fonts.googleapis.com/css2?family=Castoro&family=Mukta:wght@400;600&family=Alex+Brush&display=swap
```

**Ölçek (1080×1350 kare için):**

- Kapak başlığı: 120–170 px Castoro, büyük harf, +10%
- Gövde: 30 px Mukta 400
- Vurgu: 80–100 px Alex Brush, açık bakır

**Tipografi kuralları:**

- Başlık büyük harf, geniş aralık; logodaki gibi bakır gradyan yalnız kapakta.
- Alex Brush kare başına bir kez.
- Gövde Mukta, sol hizalı ya da ortalı.

## Logo ve imza

- Web sitesindeki bakır gradyanlı logo; sunumda yazı-imza 'ASSOS / TROY / BEACH HOTEL' Castoro, bakır gradyan.

## Görsel dil ve kompozisyon

- Motif: antik liman taşına gönderme yapan ince yatay taş sırası çizgisi; fotoğraflar yumuşak köşeli (18 px).
- Fotoğraflar: kabanalar, havuz, Antik Liman.
- Reels: deniz → havuz → liman; sakin geçiş.

## Fotoğraf yönü (Higgsfield prompt eki)

```
Aegean coast at Assos, terracotta copper and sea blue tones, warm natural light, photorealistic, no people, no text, no logos, no letters
```

## Sunum sayfası CSS değişkenleri

```css
:root {
  --bakir: #966638;
  --pembe_bakir: #D99983;
  --toprak: #5A422B;
  --deniz: #1F5F73;
  --kum: #F8F1EA;
  --font-baslik: 'Castoro', serif;
  --font-govde: 'Mukta', sans-serif;
  --font-vurgu: 'Alex Brush', cursive;
}
```

## Yapma

- Neon turkuaz ve tropikal renk kullanma.
- Bakırı küçük gövde yazısında kullanma (kontrast).
- Şu fontları kullanma (standart/aşırı kullanılmış): Inter, Manrope, Fraunces, Playfair Display, Cormorant / Cormorant Garamond, DM Serif Display, DM Sans, Space Grotesk, Caveat, Pacifico, Anton, Bebas Neue, Archivo / Archivo Black, Jost, Nunito, Poppins, Montserrat, Roboto, Open Sans, Lato, Lora, Outfit, Plus Jakarta Sans, Raleway, Oswald, Work Sans, Instrument Sans / Instrument Serif, Arial / Helvetica / system-ui.
