# Kuzey Çiçekçilik · Tasarım sistemi

> Bu dosya Kuzey Çiçekçilik için üretilen tüm içeriklerin (karusel, post, reels, sunum sayfası) tek kaynağıdır. Yeni iş yaparken buradaki palet ve fontların dışına çıkma; değişiklik gerekiyorsa önce bu dosyayı güncelle.

- **Kategori:** Çiçekçi · Kepez
- **Sunum sayfası:** https://sunum.detaymultimedia.com/kuzey-cicekcilik-ornek/
- **Kaynak:** Logo yok. Google Haritalar dükkân fotoğrafı (21.11.2026): sarı tabela üzerinde siyah kalın büyük harf 'KUZEY ÇİÇEKÇİLİK'. Instagram @kuzeycicekcilik17 profili: sahibinin kırmızı gül buketli fotoğrafı.
- **Son güncelleme:** 21.11.2026

## Marka gözlemi

Marka kimliği tabeladan ibaret: canlı sarı + siyah kalın harf, mahalle dükkânı netliği. Ürün dili kırmızı gül ve yeşil yaprak. Ton: enerjik, ulaşılabilir, hızlı sipariş; butik/pastel değil.

## Renk paleti

| Token | Hex | Rol |
|---|---|---|
| `tabela` | `#F5C31C` | Marka rengi: zemin blokları, şerit, rozet |
| `murekkep` | `#151515` | Başlık ve gövde yazısı |
| `gul` | `#C8102E` | Ürün vurgusu: gül, kalp, özel gün etiketi |
| `yaprak` | `#2F6B3A` | İkincil: yeşillik, 'aynı gün teslim' etiketi |
| `kagit` | `#FFFBEA` | Açık zemin, bilgi kartı |

**Oranlar:** %40 kagit, %30 tabela, %20 murekkep, %7 gul, %3 yaprak.

**Kontrol edilmiş yazı/zemin çiftleri (WCAG kontrast oranı):**

- `murekkep` yazı / `tabela` zemin → **11.0:1** (AA ✓) — tabela şeridi yazısı
- `murekkep` yazı / `kagit` zemin → **17.6:1** (AA ✓) — gövde
- `kagit` yazı / `gul` zemin → **5.7:1** (AA ✓) — özel gün rozeti
- `kagit` yazı / `yaprak` zemin → **6.2:1** (AA ✓) — teslimat etiketi
- `tabela` yazı / `murekkep` zemin → **11.0:1** (AA ✓) — koyu şerit üstü

## Font sistemi

| Rol | Font | Ağırlık / stil | Nerede |
|---|---|---|---|
| Başlık | **Bricolage Grotesque** | 800 büyük harf | Tabeladaki kalın büyük harfin karşılığı; kapak ve fiyat |
| Gövde | **Albert Sans** | 400 / 600 | Açıklama, adres, sipariş bilgisi |
| Çiçek adı | **Yeseva One** | 400 | Çiçek/buket adı, 'Anneler Günü' gibi özel gün başlığı |

Google Fonts (Türkçe karakterler ğ ş ı İ ç ö ü kontrol edildi):

```
https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@700;800&family=Albert+Sans:wght@400;600&family=Yeseva+One&display=swap
```

**Ölçek (1080×1350 kare için):**

- Kapak başlığı: 110–140 px Bricolage 800, büyük harf
- Buket adı: 64–80 px Yeseva One
- Gövde: 30–32 px Albert 400
- Fiyat: 72 px Bricolage 800 + '₺' 40 px
- Etiket: 22 px Albert 600, büyük harf, +10%

**Tipografi kuralları:**

- Tabela hissi: her karede bir yerde sarı zemin üstünde siyah büyük harf şerit (yükseklik 120–160 px).
- Yeseva One yalnız ürün/gün adı için; gövde metni asla.
- WhatsApp sipariş numarası her satış karesinde Albert 600 ile.

## Logo ve imza

- Logo yok → 'KUZEY ÇİÇEKÇİLİK' Bricolage 800, siyah, sarı şerit içinde 'yazı-logo' olarak kullan; sunumda yeni logo önerisi bonus olarak sunulabilir.
- İmza: sarı şerit + '@kuzeycicekcilik17 · 0542 678 81 09'.

## Görsel dil ve kompozisyon

- Motif: tabela şeridi (tam genişlik sarı bant) ve yuvarlak sarı fiyat damgası.
- Fotoğraflar kâğıt zeminde, beyaz çerçevesiz, ürün merkezde; arka plan sade.
- Reels: ürünün elden ele geçişi, sarı şerit alttan yukarı kayarak giriş.

## Fotoğraf yönü (Higgsfield prompt eki)

```
Bright florist shop photography, red roses and seasonal bouquets wrapped in kraft paper, clean warm daylight, neighborhood flower shop in Çanakkale, vivid true colors, shallow depth of field, no text, no logos
```

## Sunum sayfası CSS değişkenleri

```css
:root {
  --tabela: #F5C31C;
  --murekkep: #151515;
  --gul: #C8102E;
  --yaprak: #2F6B3A;
  --kagit: #FFFBEA;
  --font-baslik: 'Bricolage Grotesque', sans-serif;
  --font-govde: 'Albert Sans', sans-serif;
  --font-vurgu: 'Yeseva One', Georgia, serif;
}
```

## Yapma

- Pastel pembe/lila butik estetiği kullanma; marka sarı-siyah.
- İnce zarif serif ile kapak yapma.
- Sarıyı açık sarıya (limon/krem) çekme.
- Şu fontları kullanma (standart/aşırı kullanılmış): Inter, Manrope, Fraunces, Playfair Display, Cormorant / Cormorant Garamond, DM Serif Display, DM Sans, Space Grotesk, Caveat, Pacifico, Anton, Bebas Neue, Archivo / Archivo Black, Jost, Nunito, Poppins, Montserrat, Roboto, Open Sans, Lato, Lora, Outfit, Plus Jakarta Sans, Raleway, Oswald, Work Sans, Instrument Sans / Instrument Serif, Arial / Helvetica / system-ui.
