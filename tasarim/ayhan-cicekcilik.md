# Ayhan Çiçekçilik · Tasarım sistemi

> Bu dosya Ayhan Çiçekçilik için üretilen tüm içeriklerin (karusel, post, reels, sunum sayfası) tek kaynağıdır. Yeni iş yaparken buradaki palet ve fontların dışına çıkma; değişiklik gerekiyorsa önce bu dosyayı güncelle.

- **Kategori:** Çiçekçi & peyzaj · Cevat Paşa
- **Sunum sayfası:** https://sunum.detaymultimedia.com/ayhan-cicekcilik-ornek/
- **Kaynak:** Instagram @ayhan_cicekcilik profil logosu (21.11.2026): beyaz zemin, zeytin yeşili küçük harf el yazısı 'ayhan', altında ince büyük harf 'ÇİÇEKÇİLİK & PEYZAJ DÜZENLEME'; site ayhancicekcilik.com.
- **Son güncelleme:** 21.11.2026

## Marka gözlemi

Zeytin yeşili tek renk, zarif küçük harf yazı + ince büyük harf alt satır: köklü, sakin, butik. Peyzaj işi de var. Ton: zarif, doğal, güven veren; renk ürünlerden gelsin.

## Renk paleti

| Token | Hex | Rol |
|---|---|---|
| `zeytin` | `#3F5A2E` | Logo rengi: başlık, çizgiler |
| `adacayi` | `#8A9472` | İkincil: ayraç, etiket zemini |
| `kirli-beyaz` | `#F7F5EF` | Ana zemin |
| `toprak` | `#2E2A24` | Gövde yazısı |
| `pudra` | `#E7B7B0` | Çiçek vurgusu: özel gün rozeti (az) |

**Oranlar:** %65 kirli-beyaz, %20 zeytin, %10 adacayi, %5 pudra.

**Kontrol edilmiş yazı/zemin çiftleri (WCAG kontrast oranı):**

- `zeytin` yazı / `kirli-beyaz` zemin → **7.1:1** (AA ✓) — başlık
- `toprak` yazı / `kirli-beyaz` zemin → **13.1:1** (AA ✓) — gövde
- `kirli-beyaz` yazı / `zeytin` zemin → **7.1:1** (AA ✓) — koyu şerit
- `toprak` yazı / `pudra` zemin → **8.0:1** (AA ✓) — rozet içi
- `toprak` yazı / `adacayi` zemin → **4.5:1** (yalnız büyük başlık ✓) — etiket

## Font sistemi

| Rol | Font | Ağırlık / stil | Nerede |
|---|---|---|---|
| Başlık | **Gilda Display** | 400 | Kapak ve ürün başlığı; ince, zarif serif |
| Gövde | **Red Hat Text** | 400 / 500 | Açıklama, saat, sipariş |
| El yazısı | **Italianno** | 400 | Logodaki küçük harf yazıya selam; buket adı veya tek kelime |

Google Fonts (Türkçe karakterler ğ ş ı İ ç ö ü kontrol edildi):

```
https://fonts.googleapis.com/css2?family=Gilda+Display&family=Red+Hat+Text:wght@400;500&family=Italianno&display=swap
```

**Ölçek (1080×1350 kare için):**

- Kapak başlığı: 88–110 px Gilda
- El yazısı: 96–120 px Italianno (ince olduğu için büyük)
- Gövde: 30 px Red Hat 400
- Alt satır/etiket: 20–22 px Red Hat 500, büyük harf, +20% (logodaki ince alt satır gibi)

**Tipografi kuralları:**

- Logodaki gibi: büyük zarif başlık + altında çok aralıklı ince büyük harf satır ikilisi her kapakta.
- Italianno beyaz/koyu üzerinde en az 96 px; küçük boyutta kullanma.
- Peyzaj içeriklerinde de aynı sistem, sadece fotoğraf değişir.

## Logo ve imza

- Logo bol boşlukla, kare üst ortada veya alt ortada, genişliğin %22'si; çevresine hiçbir öğe yaklaşmaz.
- Koyu zeminde kirli-beyaz tek renk versiyon.

## Görsel dil ve kompozisyon

- Motif: ince zeytin çizgi çerçeve (1.5 px) kenardan 48 px içerde; bol negatif alan.
- Fotoğraflar kare içinde kemerli (üstü yuvarlak) çerçevede.
- Reels: yavaş zoom, çapraz geçiş (crossfade), müzik akustik.

## Fotoğraf yönü (Higgsfield prompt eki)

```
Elegant florist and garden design photography, seasonal bouquets and potted plants, soft natural window light, olive green foliage, calm neutral background, refined but natural, no text, no logos
```

## Sunum sayfası CSS değişkenleri

```css
:root {
  --zeytin: #3F5A2E;
  --adacayi: #8A9472;
  --kirli-beyaz: #F7F5EF;
  --toprak: #2E2A24;
  --pudra: #E7B7B0;
  --font-baslik: 'Gilda Display', Georgia, serif;
  --font-govde: 'Red Hat Text', sans-serif;
  --font-vurgu: 'Italianno', cursive;
}
```

## Yapma

- Doygun kırmızı/sarı zemin kullanma (Kuzey Çiçekçilik'le karışmasın).
- Kalın/dar başlık fontu kullanma.
- Kareleri doldurma; boşluk markanın parçası.
- Şu fontları kullanma (standart/aşırı kullanılmış): Inter, Manrope, Fraunces, Playfair Display, Cormorant / Cormorant Garamond, DM Serif Display, DM Sans, Space Grotesk, Caveat, Pacifico, Anton, Bebas Neue, Archivo / Archivo Black, Jost, Nunito, Poppins, Montserrat, Roboto, Open Sans, Lato, Lora, Outfit, Plus Jakarta Sans, Raleway, Oswald, Work Sans, Instrument Sans / Instrument Serif, Arial / Helvetica / system-ui.
