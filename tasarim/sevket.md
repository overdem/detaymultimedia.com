# Şevket Steakhouse (Şevk-ET) · Tasarım sistemi

> Bu dosya Şevket Steakhouse (Şevk-ET) için üretilen tüm içeriklerin (karusel, post, reels, sunum sayfası) tek kaynağıdır. Yeni iş yaparken buradaki palet ve fontların dışına çıkma; değişiklik gerekiyorsa önce bu dosyayı güncelle.

- **Kategori:** Restoran · steakhouse / kasap
- **Sunum sayfası:** https://sunum.detaymultimedia.com/sevket-24-kasim/ · https://sunum.detaymultimedia.com/sevket-mac-21-kasim/
- **Kaynak:** Onaylı marka sistemi: proje dokümanı canakkale/sevket/SEVKET.md (20.11.2026, Özdem 'daha pro' isteğiyle onayladı) — renkler, yerleşim ve kurallar oradan. Logo: sevketsteakhouse.com ve kendi gönderilerindeki boğa kafatası 'Şevk-ET'. 21.11.2026: yalnız fontlar standart olmayanlarla değiştirildi (Playfair Display → Brygada 1918, Montserrat → Gabarito).
- **Son güncelleme:** 21.11.2026

## Marka gözlemi

Kömür siyahı zemin, ince altın çerçeve, serif başlık + altın italik vurgu kelimesi, geniş aralıklı büyük harf etiketler. 3. nesil / 100 yıllık ustalık / kendi besisi anlatısı; slogan 'Dededen Toruna'. Ton: premium ama samimi steakhouse; maç günleri ve fasıl de var. Ayrıntılar ve onaylı işler için SEVKET.md.

## Renk paleti

| Token | Hex | Rol |
|---|---|---|
| `komur` | `#0D0A08` | Ana zemin |
| `panel` | `#17120E` | Panel / kart zemini |
| `cizgi` | `#3A2E22` | İnce ayraç çizgileri, panel kenarı |
| `krem` | `#F4ECDE` | Başlık ve gövde yazısı |
| `altin` | `#CBA46A` | Çerçeve, kicker satırı, italik vurgu kelimesi, indirim halkası |

**Oranlar:** %75 komur/panel, %15 krem, %8 altin, %2 cizgi. Maç hikâyelerinde kulüp renkleri yalnız ince şerit olarak eklenir (GS #FDB913/#A90432, FB #FFED00/#00205B).

**Kontrol edilmiş yazı/zemin çiftleri (WCAG kontrast oranı):**

- `krem` yazı / `komur` zemin → **16.8:1** (AA ✓) — başlık/gövde
- `altin` yazı / `komur` zemin → **8.5:1** (AA ✓) — kicker, vurgu kelimesi
- `krem` yazı / `panel` zemin → **15.9:1** (AA ✓) — panel yazısı
- `komur` yazı / `altin` zemin → **8.5:1** (AA ✓) — altın rozet içi
- `altin` yazı / `panel` zemin → **8.0:1** (AA ✓) — panelde altın vurgu

## Font sistemi

| Rol | Font | Ağırlık / stil | Nerede |
|---|---|---|---|
| Başlık | **Brygada 1918** | 500; vurgu kelimesi 500 italik + altın | Serif başlık, dev '%10', alıntı/slogan |
| Etiket / metin | **Gabarito** | 400 metin, 500–600 büyük harf etiket | Kicker, alt bilgi, adres, rezervasyon; büyük harf geniş aralıklı |

Google Fonts (Türkçe karakterler ğ ş ı İ ç ö ü kontrol edildi):

```
https://fonts.googleapis.com/css2?family=Brygada+1918:ital,wght@0,500;0,600;1,500&family=Gabarito:wght@400;500;600&display=swap
```

**Ölçek (1080×1350 kare için):**

- Başlık (post 1728×2304): 150–190 px Brygada 500, vurgu kelimesi italik altın
- Başlık (1080×1350 / hikâye 1080×1920): 96–120 px
- Kicker: 26–30 px Gabarito 600, büyük harf, +30% aralık, iki yanında 40 px altın çizgi
- Gövde: 30–34 px Gabarito 400
- Alt bilgi: 20–22 px Gabarito 500, büyük harf, +25%: 'ŞEVKET STEAKHOUSE · 01/06 · ÇANAKKALE'
- İndirim: dev '%10' Brygada 600, koyu daire + çift altın halka

**Tipografi kuralları:**

- Her başlıkta tek bir kelime italik + altın (Playfair yerine Brygada 1918 italik).
- Etiketler her zaman büyük harf ve geniş aralıklı Gabarito.
- Yazılar fotoğraflara sonradan Python ile basılır (Türkçe karakterler doğru çıksın).

## Logo ve imza

- Beyaz boğa kafatası logo üst ortada (SEVKET.md'deki 01_referans/logo_beyaz_maske.png; orijinal dosya müşteriden istenmeli).
- Kenardan 64 px (post) / 48 px (hikâye) içeride ince altın çerçeve her karede.

## Görsel dil ve kompozisyon

- Onaylı yerleşim: üstte logo, altın kicker satırı, serif başlık, altta alt bilgi; fotoğrafların üst %45–60'ı karanlık boş alan (yazı için).
- Mekân referansı: parlak turuncu-kahve ahşap masa, çapraz sırtlı ahşap sandalyeler, bir turkuaz sandalye, sıcak sarkıt lambalar.
- Boyutlar: post/karusel 1728×2304 (3:4); hikâye/reels 1080×1920.

## Fotoğraf yönü (Higgsfield prompt eki)

```
Photorealistic editorial food photograph, premium steakhouse advertising, full-frame camera, 50mm, f/2, natural colors, real photo. Location: the real restaurant from image 1, same glossy orange-brown wooden table, warm pendant lamps softly blurred far in the background, night. In the lower 45 percent of the frame: [YEMEK]. The upper 55 percent of the frame is dark, calm, out-of-focus restaurant background with only a few soft warm bokeh lights, empty negative space. Low-key warm side light. Absolutely no text, no letters, no logo, no signs, no TV screen, no watermark, no people.
```

## Sunum sayfası CSS değişkenleri

```css
:root {
  --komur: #0D0A08;
  --panel: #17120E;
  --cizgi: #3A2E22;
  --krem: #F4ECDE;
  --altin: #CBA46A;
  --font-baslik: 'Brygada 1918', Georgia, serif;
  --font-govde: 'Gabarito', sans-serif;
}
```

## Yapma

- İnsan, alkol (burgerin yanında limonata), kulüp logosu kullanma; kulüp renkleri yalnız ince şerit.
- Yırtık kâğıt etiket / el yazısı stile dönme (Özdem beğenmedi).
- Altını parlak metalik gradyan yapma.
- Playfair Display ve Montserrat'ı artık kullanma; yerlerine Brygada 1918 ve Gabarito.
- Şu fontları kullanma (standart/aşırı kullanılmış): Inter, Manrope, Fraunces, Playfair Display, Cormorant / Cormorant Garamond, DM Serif Display, DM Sans, Space Grotesk, Caveat, Pacifico, Anton, Bebas Neue, Archivo / Archivo Black, Jost, Nunito, Poppins, Montserrat, Roboto, Open Sans, Lato, Lora, Outfit, Plus Jakarta Sans, Raleway, Oswald, Work Sans, Instrument Sans / Instrument Serif, Arial / Helvetica / system-ui.
