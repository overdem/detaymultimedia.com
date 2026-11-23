# Federal Kordon · Tasarım sistemi

> Bu dosya Federal Kordon için üretilen tüm içeriklerin (karusel, post, reels, sunum sayfası) tek kaynağıdır. Yeni iş yaparken buradaki palet ve fontların dışına çıkma; değişiklik gerekiyorsa önce bu dosyayı güncelle.

- **Kategori:** Kafe-restoran · Kordon, Cevat Paşa / Pirireis Cd.
- **Sunum sayfası:** https://sunum.detaymultimedia.com/federal-kordon-ornek/
- **Kaynak:** Logo dosyasına ulaşılamadı; Google'daki Instagram bağlantısı (@federalkordon) açılmıyor (23.11.2026). Palet Google Haritalar mekân fotoğrafından türetilmiş ÖNERİ: koyu ahşap bar, siyah, turuncu vurgular, duvarda beyaz plak/tabaklar, pirinç ışıklar.
- **Son güncelleme:** 23.11.2026

## Marka gözlemi

Kordon'da Boğaz'a bakan, porsiyonları cömert bir kafe-restoran; yorumlarda fettuccine Alfredo, ekşi mayalı ekmekle avokadolu ekmek üstü ve önden gelen acuka öne çıkıyor. Ton: sıcak, şehirli, cömert, akşam buluşması.

## Renk paleti

| Token | Hex | Rol |
|---|---|---|
| `komur` | `#171615` | Ana koyu zemin |
| `ceviz` | `#5B3B28` | Ahşap: ikincil koyu kart |
| `turuncu` | `#E2702B` | Vurgu: başlık kelimesi, rozet |
| `plak` | `#EEEAE2` | Açık zemin, koyu zeminde yazı |
| `pirinc` | `#B38B4F` | İnce çizgi, ayrıntı |

**Oranlar:** %50 kömür/ceviz, %30 plak, %15 turuncu, %5 pirinç.

**Kontrol edilmiş yazı/zemin çiftleri (WCAG kontrast oranı):**

- `plak` yazı / `komur` zemin → **15.1:1** (AA ✓) — gövde
- `turuncu` yazı / `komur` zemin → **5.7:1** (AA ✓) — başlık vurgu
- `plak` yazı / `ceviz` zemin → **8.3:1** (AA ✓) — kart yazısı
- `komur` yazı / `plak` zemin → **15.1:1** (AA ✓) — açık kart
- `komur` yazı / `turuncu` zemin → **5.7:1** (AA ✓) — rozet yazısı
- `pirinc` yazı / `komur` zemin → **5.8:1** (AA ✓) — ince etiket (büyük)

## Font sistemi

| Rol | Font | Ağırlık / stil | Nerede |
|---|---|---|---|
| Başlık | **Big Shoulders Display** | 800 | Dar, uzun, şehirli büyük harf başlık |
| Gövde | **Public Sans** | 400 / 600 | Menü, açıklama |
| Etiket | **IBM Plex Mono** | 500 | Menü kodu, saat, adres: bistro fişi havası |

Google Fonts (Türkçe karakterler ğ ş ı İ ç ö ü kontrol edildi):

```
https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@700;800&family=Public+Sans:wght@400;600&family=IBM+Plex+Mono:wght@500&display=swap
```

**Ölçek (1080×1350 kare için):**

- Kapak başlığı: 130–170 px Big Shoulders 800, büyük harf
- Gövde: 30 px Public Sans 400
- Etiket: 22 px IBM Plex Mono 500, +8%

**Tipografi kuralları:**

- Başlıkta tek kelime turuncu.
- Etiketler mono, köşeli parantezle: [ KORDON ] [ 08:00 ].
- Sola yaslı, dergi menüsü düzeni.

## Logo ve imza

- Logo yok/teyit edilemedi → yazı-imza: FEDERAL KORDON, Big Shoulders 800. Sunumda öneri olarak belirt; zincir markanın resmi logosu varsa ona geçilir.

## Görsel dil ve kompozisyon

- Motif: plak dairesi (ince halkalı daire), turuncu yuvarlak rozet, ince pirinç çizgiler.
- Fotoğraflar sıcak akşam ışığı, büyük porsiyon yakın plan, pencereden deniz.
- Reels: plak döner gibi dairesel geçiş, hızlı kesim.

## Fotoğraf yönü (Higgsfield prompt eki)

```
Cozy modern cafe-restaurant on the Canakkale seafront promenade, dark wood, black and warm orange accents, warm light, photorealistic, no people, no text, no logos, no letters
```

## Sunum sayfası CSS değişkenleri

```css
:root {
  --komur: #171615;
  --ceviz: #5B3B28;
  --turuncu: #E2702B;
  --plak: #EEEAE2;
  --pirinc: #B38B4F;
  --font-baslik: 'Big Shoulders Display', sans-serif;
  --font-govde: 'Public Sans', sans-serif;
  --font-vurgu: 'IBM Plex Mono', monospace;
}
```

## Yapma

- Pastel zemin kullanma.
- Federal Coffee zincirinin logosunu taklit etme.
- Şu fontları kullanma (standart/aşırı kullanılmış): Inter, Manrope, Fraunces, Playfair Display, Cormorant / Cormorant Garamond, DM Serif Display, DM Sans, Space Grotesk, Caveat, Pacifico, Anton, Bebas Neue, Archivo / Archivo Black, Jost, Nunito, Poppins, Montserrat, Roboto, Open Sans, Lato, Lora, Outfit, Plus Jakarta Sans, Raleway, Oswald, Work Sans, Instrument Sans / Instrument Serif, Arial / Helvetica / system-ui.
