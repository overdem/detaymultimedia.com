# İhsan-ı İkram Esnaf Lokantası · Tasarım sistemi

> Bu dosya İhsan-ı İkram Esnaf Lokantası için üretilen tüm içeriklerin (karusel, post, reels, sunum sayfası) tek kaynağıdır. Yeni iş yaparken buradaki palet ve fontların dışına çıkma; değişiklik gerekiyorsa önce bu dosyayı güncelle.

- **Kategori:** Esnaf lokantası · et lokantası & zeytinyağlılar, Kemalpaşa / Yalı Cd.
- **Sunum sayfası:** https://sunum.detaymultimedia.com/ihsan-i-ikram-esnaf-lokantasi-ornek/
- **Kaynak:** Instagram hesabı bulunamadı (23.11.2026). Kaynak: kendi basılı menü kartı (Google Haritalar fotoğrafı, Ağu 2026): koyu kahve-siyah kalın geometrik 'İhsan-ı İkram' yazısı, kiremit-bordo etiket içinde beyaz 'Menü', pembemsi krem kâğıt, alt satırda 'Et Lokantası & Zeytinyağlılar'. Zeytin ve bakır tonları menü içeriğinden (zeytinyağlılar, tencere) türetilmiş öneri.
- **Son güncelleme:** 23.11.2026

## Marka gözlemi

Menü kartındaki yazı modern ve kalın, kâğıt sıcak ve sade: geleneksel esnaf lokantası ama tozlu değil. 06:30'dan gece 04:30'a kadar açık; çorba, sulu yemek, zeytinyağlı ve et yemekleri. Ton: doyurucu, samimi, her saat açık, ev yemeği.

## Renk paleti

| Token | Hex | Rol |
|---|---|---|
| `murekkep` | `#2E2420` | Yazı-logo rengi: başlık, gövde |
| `etiket` | `#7A3B2E` | 'Menü' etiketi: vurgu blok, şerit, buton |
| `kagit` | `#F5E8E1` | Menü kâğıdı: ana açık zemin |
| `zeytin` | `#5E6B34` | Zeytinyağlılar: ikincil vurgu, küçük etiket |
| `bakir` | `#C9853F` | Tencere/bakır: ince çizgi, saat rozeti (koyu zeminde) |

**Oranlar:** %55 kağıt, %25 mürekkep, %12 etiket, %5 zeytin, %3 bakır.

**Kontrol edilmiş yazı/zemin çiftleri (WCAG kontrast oranı):**

- `murekkep` yazı / `kagit` zemin → **12.6:1** (AA ✓) — gövde
- `kagit` yazı / `etiket` zemin → **7.0:1** (AA ✓) — etiket/şerit yazısı
- `kagit` yazı / `murekkep` zemin → **12.6:1** (AA ✓) — koyu kart
- `etiket` yazı / `kagit` zemin → **7.0:1** (AA ✓) — başlık vurgu kelimesi
- `zeytin` yazı / `kagit` zemin → **4.8:1** (AA ✓) — küçük etiket
- `bakir` yazı / `murekkep` zemin → **5.0:1** (AA ✓) — saat rozeti (büyük)

## Font sistemi

| Rol | Font | Ağırlık / stil | Nerede |
|---|---|---|---|
| Başlık | **Lexend** | 800 / 600 | Menüdeki kalın geometrik 'İhsan-ı İkram' yazısının karşılığı |
| Gövde | **Karla** | 400 / 700 | Yemek adı, açıklama, adres |
| Tebeşir | **Patrick Hand** | 400 | Günün yemeği tahtası notu: 'bugün tencerede', fiyat değil |

Google Fonts (Türkçe karakterler ğ ş ı İ ç ö ü kontrol edildi):

```
https://fonts.googleapis.com/css2?family=Lexend:wght@600;800&family=Karla:wght@400;700&family=Patrick+Hand&display=swap
```

**Ölçek (1080×1350 kare için):**

- Kapak başlığı: 96–120 px Lexend 800, sıkı satır
- Etiket: 26 px Lexend 600, kiremit kutu içinde beyaz
- Gövde: 30 px Karla 400
- Tebeşir notu: 44 px Patrick Hand, −3°

**Tipografi kuralları:**

- Menü kartındaki gibi: kalın başlık + yanında kiremit kutuda tek kelime etiket ('Menü', 'Bugün', 'Sıcak').
- Yemek listeleri iki sütun menü düzeninde, ince mürekkep çizgilerle.
- Patrick Hand yalnız kısa not; kare başına bir kez.

## Logo ve imza

- Logo dosyası yok → yazı-imza: 'İhsan-ı İkram' Lexend 800 + kiremit 'Esnaf Lokantası' etiketi. Sunumda kimlik önerisi olarak belirt.
- İmza: alt şeritte 0551 160 66 49 · Yalı Cd. Kemalpaşa.

## Görsel dil ve kompozisyon

- Motif: menü kartı (krem kâğıt, ince çerçeve, iki sütun), kiremit etiket kutusu, saat rozeti (06:30–04:30).
- Fotoğraflar sıcak, buharlı, benmari/tencere yakın plan; kâğıt kenarlı kart içinde.
- Reels: tencere kapağı açılır, kepçe; etiket kutusu soldan kayar.

## Fotoğraf yönü (Higgsfield prompt eki)

```
Warm traditional Turkish tradesmen's restaurant, homey light, deep brown and brick red tones with cream, photorealistic, no people, no text, no logos, no letters
```

## Sunum sayfası CSS değişkenleri

```css
:root {
  --murekkep: #2E2420;
  --etiket: #7A3B2E;
  --kagit: #F5E8E1;
  --zeytin: #5E6B34;
  --bakir: #C9853F;
  --font-baslik: 'Lexend', sans-serif;
  --font-govde: 'Karla', sans-serif;
  --font-vurgu: 'Patrick Hand', cursive;
}
```

## Yapma

- Neon/parlak renk ve modern kafe estetiği kullanma.
- Fiyat yazma (menü fiyatları değişiyor).
- Puan/yorum sayısını içerikte kullanma.
- Şu fontları kullanma (standart/aşırı kullanılmış): Inter, Manrope, Fraunces, Playfair Display, Cormorant / Cormorant Garamond, DM Serif Display, DM Sans, Space Grotesk, Caveat, Pacifico, Anton, Bebas Neue, Archivo / Archivo Black, Jost, Nunito, Poppins, Montserrat, Roboto, Open Sans, Lato, Lora, Outfit, Plus Jakarta Sans, Raleway, Oswald, Work Sans, Instrument Sans / Instrument Serif, Arial / Helvetica / system-ui.
