# Şevket Steakhouse (Şevk-ET) · Tasarım sistemi

> Bu dosya Şevket Steakhouse (Şevk-ET) için üretilen tüm içeriklerin (karusel, post, reels, sunum sayfası) tek kaynağıdır. Yeni iş yaparken buradaki palet ve fontların dışına çıkma; değişiklik gerekiyorsa önce bu dosyayı güncelle.

- **Kategori:** Restoran · steakhouse / kasap
- **Sunum sayfası:** https://sunum.detaymultimedia.com/sevket-24-kasim/
- **Kaynak:** sevketsteakhouse.com (21.11.2026): siyah-beyaz boğa kafatası logo 'Şevk-ET STEAKHOUSE', üst menü haki altın şerit, 'Dededen Toruna' sloganı; Instagram @sevketkasapsteakhouse profili siyah-beyaz usta portresi.
- **Son güncelleme:** 21.11.2026

## Marka gözlemi

Siyah, beyaz ve haki-altın üçlüsü. Logo kalın, dar, ağır harfli; 'ET' kısmı altın. '100 yıllık ustalık, 3. nesil', 'kendi yetiştirdiğimiz besiler' anlatısı güçlü. Ton: ciddi, erkeksi, zanaat; parlak lüks değil, kasap tezgâhı dürüstlüğü.

## Renk paleti

| Token | Hex | Rol |
|---|---|---|
| `kömür` | `#111111` | Ana zemin |
| `kul` | `#2B2B2B` | İkincil koyu zemin, kart |
| `haki` | `#AE9A64` | Marka vurgusu: 'ET', çizgiler, rozet |
| `kemik` | `#F3EEE3` | Açık zemin / yazı |
| `kesim` | `#8E2A1E` | Çok sınırlı: et/ateş vurgusu, 'yeni' noktası |

**Oranlar:** %65 kömür/kul, %20 kemik, %12 haki, %3 kesim.

**Kontrol edilmiş yazı/zemin çiftleri (WCAG kontrast oranı):**

- `kemik` yazı / `kömür` zemin → **16.3:1** (AA ✓) — gövde ve başlık
- `haki` yazı / `kömür` zemin → **6.8:1** (AA ✓) — vurgu kelime, büyük başlık
- `kömür` yazı / `haki` zemin → **6.8:1** (AA ✓) — rozet içi yazı
- `kemik` yazı / `kul` zemin → **12.2:1** (AA ✓) — kart yazısı
- `kömür` yazı / `kemik` zemin → **16.3:1** (AA ✓) — açık karede yazı

## Font sistemi

| Rol | Font | Ağırlık / stil | Nerede |
|---|---|---|---|
| Başlık | **Big Shoulders Display** | 900 kapak, 700 ara başlık | Logodaki dar-kalın harflerin karşılığı; tüm büyük harf başlıklar |
| Gövde | **Schibsted Grotesk** | 400 gövde, 600 etiket | Açıklama, gramaj, fiyat, sayfa metni |
| İmza | **Gelasio** | 400 italik | 'Dededen Toruna', usta sözü, alıntılar |

Google Fonts (Türkçe karakterler ğ ş ı İ ç ö ü kontrol edildi):

```
https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@700;900&family=Schibsted+Grotesk:wght@400;600&family=Gelasio:ital@1&display=swap
```

**Ölçek (1080×1350 kare için):**

- Kapak başlığı: 140–180 px Big Shoulders 900, büyük harf, harf aralığı −1%
- Ara başlık: 64–72 px 700
- Gövde: 30–32 px Schibsted 400, satır aralığı 1.4
- Etiket: 22–24 px Schibsted 600, büyük harf, harf aralığı +12%
- İmza: 44–56 px Gelasio italik

**Tipografi kuralları:**

- Başlıkta logodaki gibi bir kelime parçası haki ile vurgulanır (ŞEVK + ET, KUZU + ETİ gibi).
- Gramaj/fiyat her zaman Schibsted 600 + haki ince çerçeve.
- Gelasio italik yalnız alıntı/slogan, kare başına bir kez.

## Logo ve imza

- Boğa kafatası logo siyah-beyaz; koyu zeminde beyaz versiyon, sol üst ya da alt ortada, kare genişliğinin %14'ü.
- Logo dosyası müşteriden alınana kadar 'ŞEVK-ET' yazısını Big Shoulders 900 ile, 'ET' haki olacak şekilde yaz.

## Görsel dil ve kompozisyon

- Motif: kasap kesim şeması çizgileri (haki, 2 px) ve numaralı bölgeler; menü/kesim karelerinde.
- Fotoğraflar koyu zemin üstünde, düşük anahtar ışık; kenarlarda 40 px kömür pay.
- Reels: ateş/kızgın demir anları, kısa sert kesmeler, haki ince ilerleme çizgisi altta.

## Fotoğraf yönü (Higgsfield prompt eki)

```
Dark low-key steakhouse photography, dry-aged steak on black slate and cast iron, wood fire glow, coarse salt, dramatic side light, deep blacks with warm highlights, butcher craft details, no text, no logos
```

## Sunum sayfası CSS değişkenleri

```css
:root {
  --kömür: #111111;
  --kul: #2B2B2B;
  --haki: #AE9A64;
  --kemik: #F3EEE3;
  --kesim: #8E2A1E;
  --font-baslik: 'Big Shoulders Display', Impact, sans-serif;
  --font-govde: 'Schibsted Grotesk', sans-serif;
  --font-vurgu: 'Gelasio', Georgia, serif;
}
```

## Yapma

- Altın parıltı/gradyan, lüks otel estetiği kullanma; haki mat kalmalı.
- Pastel ya da açık renk ağırlıklı kare yapma.
- Kesim kırmızısını zemin olarak kullanma.
- Şu fontları kullanma (standart/aşırı kullanılmış): Inter, Manrope, Fraunces, Playfair Display, Cormorant / Cormorant Garamond, DM Serif Display, DM Sans, Space Grotesk, Caveat, Pacifico, Anton, Bebas Neue, Archivo / Archivo Black, Jost, Nunito, Poppins, Montserrat, Roboto, Open Sans, Lato, Lora, Outfit, Plus Jakarta Sans, Raleway, Oswald, Work Sans, Instrument Sans / Instrument Serif, Arial / Helvetica / system-ui.
