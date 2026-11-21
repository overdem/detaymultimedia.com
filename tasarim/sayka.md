# Şayka Restaurant (Balık & Meze) · Tasarım sistemi

> Bu dosya Şayka Restaurant (Balık & Meze) için üretilen tüm içeriklerin (karusel, post, reels, sunum sayfası) tek kaynağıdır. Yeni iş yaparken buradaki palet ve fontların dışına çıkma; değişiklik gerekiyorsa önce bu dosyayı güncelle.

- **Kategori:** Restoran · balık & meze, Kordon
- **Sunum sayfası:** https://sunum.detaymultimedia.com/sayka-ornek/
- **Kaynak:** Instagram @sayka_restaurant profil logosu (21.11.2026): beyaz zemin, lacivert dalga, sarı-hardal yelkenli tekne, fırça yazı "Şayka", martılar.
- **Son güncelleme:** 21.11.2026

## Marka gözlemi

Logo çizgisel ve denizci: lacivert-mavi dalga şeritleri, tek sıcak renk olarak yelkenin hardal sarısı, el yazısı fırça logotip. Mekân Kordon'da, yabancı turist de alıyor. Ton: ferah, tuzlu, samimi; lüks değil ama özenli.

## Renk paleti

| Token | Hex | Rol |
|---|---|---|
| `lacivert` | `#0F4C97` | Ana renk: başlıklar, logo, buton zemini |
| `derin` | `#0A2A4F` | Koyu zemin (gece/akşam kareleri), gövde yazısı |
| `dalga` | `#6FA8D6` | İnce dalga çizgileri, ayraçlar, ikincil vurgu |
| `kopuk` | `#EAF4FB` | Açık zemin, bilgi paneli |
| `yelken` | `#E3A82B` | Tek sıcak vurgu: fiyat rozeti, 'Yeni', ok işareti |
| `tuz` | `#FFFFFF` | Fotoğraf üstü yazı, logo zemini |

**Oranlar:** %60 kopuk/tuz, %25 lacivert/derin, %10 dalga, %5 yelken. Yelken asla zemin olmaz; tek bir öğede kullanılır.

**Kontrol edilmiş yazı/zemin çiftleri (WCAG kontrast oranı):**

- `lacivert` yazı / `kopuk` zemin → **7.5:1** (AA ✓) — başlık ve gövde
- `derin` yazı / `kopuk` zemin → **12.9:1** (AA ✓) — gövde
- `tuz` yazı / `derin` zemin → **14.4:1** (AA ✓) — koyu karede yazı
- `yelken` yazı / `derin` zemin → **6.8:1** (AA ✓) — rozet koyu zeminde
- `tuz` yazı / `lacivert` zemin → **8.4:1** (AA ✓) — buton

## Font sistemi

| Rol | Font | Ağırlık / stil | Nerede |
|---|---|---|---|
| Başlık | **Young Serif** | 400 (tek ağırlık) | Kapak başlığı, yemek adları |
| Gövde | **Hanken Grotesk** | 400 gövde, 700 etiket | Açıklama, fiyat, adres, sunum sayfası metni |
| El yazısı vurgu | **Courgette** | 400 | Logodaki fırça yazıya selam: tek kelimelik vurgu ('bugün', 'taze') |

Google Fonts (Türkçe karakterler ğ ş ı İ ç ö ü kontrol edildi):

```
https://fonts.googleapis.com/css2?family=Young+Serif&family=Hanken+Grotesk:wght@400;500;700&family=Courgette&display=swap
```

**Ölçek (1080×1350 kare için):**

- Kapak başlığı: 96–120 px Young Serif, satır aralığı 1.0
- Ara başlık: 48–56 px
- Gövde: 30–34 px Hanken 400, satır aralığı 1.35
- Etiket/rozet: 24 px Hanken 700, büyük harf, harf aralığı +8%
- El yazısı vurgu: 64–80 px, en fazla 1–2 kelime

**Tipografi kuralları:**

- Başlıklar cümle düzeninde (yalnız ilk harf büyük); büyük harf sadece etiketlerde.
- Courgette bir karede en fazla bir kez, başlığın yanında ve hafif eğik (−4°).
- Fiyatlar Hanken 700 + yelken rengi rozet içinde.

## Logo ve imza

- Logo görseli müşteriden alınana kadar Instagram profil logosu referans; karelere yeniden çizme, köşede 'Şayka' fırça yazısı yerine Courgette ile 'Şayka' yazma — sadece sunum sayfasında başlık olarak kullan.
- Karelerde imza: sağ alt köşede küçük lacivert dalga çizgisi + '@sayka_restaurant' (Hanken 500, 22 px).

## Görsel dil ve kompozisyon

- Motif: 2–3 ince dalga çizgisi (dalga rengi, 3 px) kare kenarlarında; logodaki dalgaların sadeleştirilmiş hali.
- Fotoğraflar tam kare ya da üstte %70 + altta kopuk renkli bilgi paneli.
- Akşam/gün batımı karelerinde derin zemin + tuz yazı; gündüz karelerinde kopuk zemin.
- Reels geçişleri: yatay kaydırma (dalga hareketi), sert kesme yok.

## Fotoğraf yönü (Higgsfield prompt eki)

```
Dardanelles seaside, natural daylight or golden hour, fresh grilled fish and Turkish meze on white and blue ceramic plates, linen tablecloth, sea and ferry softly blurred in background, crisp clean colors, navy and white tones, no text, no logos
```

## Sunum sayfası CSS değişkenleri

```css
:root {
  --lacivert: #0F4C97;
  --derin: #0A2A4F;
  --dalga: #6FA8D6;
  --kopuk: #EAF4FB;
  --yelken: #E3A82B;
  --tuz: #FFFFFF;
  --font-baslik: 'Young Serif', Georgia, serif;
  --font-govde: 'Hanken Grotesk', sans-serif;
  --font-vurgu: 'Courgette', cursive;
}
```

## Yapma

- Kırmızı, turuncu veya altın-siyah 'lüks' görünüm kullanma.
- Yelken sarısını geniş alan olarak kullanma.
- Koyu ahşap/rustik dokular ekleme; marka ferah ve denizci.
- Şu fontları kullanma (standart/aşırı kullanılmış): Inter, Manrope, Fraunces, Playfair Display, Cormorant / Cormorant Garamond, DM Serif Display, DM Sans, Space Grotesk, Caveat, Pacifico, Anton, Bebas Neue, Archivo / Archivo Black, Jost, Nunito, Poppins, Montserrat, Roboto, Open Sans, Lato, Lora, Outfit, Plus Jakarta Sans, Raleway, Oswald, Work Sans, Instrument Sans / Instrument Serif, Arial / Helvetica / system-ui.
