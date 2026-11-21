# Esenler Çıtır Pide · Tasarım sistemi

> Bu dosya Esenler Çıtır Pide için üretilen tüm içeriklerin (karusel, post, reels, sunum sayfası) tek kaynağıdır. Yeni iş yaparken buradaki palet ve fontların dışına çıkma; değişiklik gerekiyorsa önce bu dosyayı güncelle.

- **Kategori:** Pide / lahmacun / kebap · Esenler
- **Sunum sayfası:** https://sunum.detaymultimedia.com/esenler-citir-pide-ornek/
- **Kaynak:** Instagram @esenlercitirpide profil logosu (21.11.2026): krem yuvarlak zemin, koyu kahve kavisli 'ESENLER', şiş kebap çizimi, büyük turuncu 'ÇITIR' (kahve gölgeli), altında 'PİDE LAHMACUN KEBAP' ve şerit içinde '2012'.
- **Son güncelleme:** 21.11.2026

## Marka gözlemi

Krem + yanık turuncu + koyu kahve; kalın kama serifli 'ÇITIR', şiş ikonu, 'since 2012' şeridi: retro esnaf tabelası. Ton: iştahlı, mahalle, samimi; yüksek enerji.

## Renk paleti

| Token | Hex | Rol |
|---|---|---|
| `krem` | `#FFF0DF` | Logo zemini: ana zemin |
| `citir` | `#D06E12` | Ana marka: başlık 'ÇITIR', rozet |
| `kahve` | `#5E2E1E` | Gölge ve yazı: gövde, çizgi |
| `kor` | `#A9301C` | İkincil: acı/kebap vurgusu |
| `yesil` | `#5B7F3A` | Çok sınırlı: maydanoz/biber, taze vurgusu |

**Oranlar:** %50 krem, %25 citir, %15 kahve, %7 kor, %3 yesil.

**Kontrol edilmiş yazı/zemin çiftleri (WCAG kontrast oranı):**

- `kahve` yazı / `krem` zemin → **10.0:1** (AA ✓) — gövde/başlık
- `citir` yazı / `krem` zemin → **3.2:1** (yalnız büyük başlık ✓) — büyük başlık
- `krem` yazı / `kahve` zemin → **10.0:1** (AA ✓) — koyu şerit
- `krem` yazı / `kor` zemin → **6.0:1** (AA ✓) — fiyat rozeti
- `krem` yazı / `citir` zemin → **3.2:1** (yalnız büyük başlık ✓) — rozet içi (büyük)

## Font sistemi

| Rol | Font | Ağırlık / stil | Nerede |
|---|---|---|---|
| Başlık | **Rokkitt** | 900 | Logodaki kalın kama serifin karşılığı; 'ÇITIR' gibi kelimeler |
| Gövde | **Chivo** | 400 / 700 | Menü, sipariş, adres |
| Rakam | **Abril Fatface** | 400 | '2012', fiyat, adet rakamları |

Google Fonts (Türkçe karakterler ğ ş ı İ ç ö ü kontrol edildi):

```
https://fonts.googleapis.com/css2?family=Rokkitt:wght@800;900&family=Chivo:wght@400;700&family=Abril+Fatface&display=swap
```

**Ölçek (1080×1350 kare için):**

- Kapak başlığı: 130–160 px Rokkitt 900, büyük harf, 6 px kahve gölge (logodaki gibi)
- Rakam: 96–120 px Abril Fatface
- Gövde: 30 px Chivo 400
- Şerit: 24 px Chivo 700, büyük harf, +12%

**Tipografi kuralları:**

- Başlıklarda logodaki ofset gölge: kahve renkte 6 px sağ-alt, bulanıklık yok.
- '2012'den beri' şeridi kurdele şeklinde her kapakta.
- Kavisli üst yazı (rozet) kampanya karelerinde.

## Logo ve imza

- Yuvarlak krem logo, kapakta ortada büyük; iç karelerde sol üst %16.
- Şiş kebap çizimi ayrı ikon olarak kullanılabilir.

## Görsel dil ve kompozisyon

- Motif: kurdele şerit, şiş ikonu, retro rozet; krem zeminde yanık turuncu bloklar.
- Fotoğraflar sıcak, fırın/ızgara yakın plan; turuncu çerçeveli kart içinde.
- Reels: çıtırlık sesi vurgusu (ASMR kesim), rozet zıplayarak girer.

## Fotoğraf yönü (Higgsfield prompt eki)

```
Crispy Turkish pide and lahmacun, adana kebab skewers on charcoal grill, wood oven flames, close-up appetizing textures, warm orange and brown tones, neighborhood kebab shop, no text, no logos
```

## Sunum sayfası CSS değişkenleri

```css
:root {
  --krem: #FFF0DF;
  --citir: #D06E12;
  --kahve: #5E2E1E;
  --kor: #A9301C;
  --yesil: #5B7F3A;
  --font-baslik: 'Rokkitt', serif;
  --font-govde: 'Chivo', sans-serif;
  --font-vurgu: 'Abril Fatface', serif;
}
```

## Yapma

- Siyah-kırmızı-sarı 'fast food afiş' paleti kullanma; marka krem-turuncu-kahve retro.
- Modern ince sans başlık kullanma.
- Gölgeyi bulanık/yumuşak yapma.
- Şu fontları kullanma (standart/aşırı kullanılmış): Inter, Manrope, Fraunces, Playfair Display, Cormorant / Cormorant Garamond, DM Serif Display, DM Sans, Space Grotesk, Caveat, Pacifico, Anton, Bebas Neue, Archivo / Archivo Black, Jost, Nunito, Poppins, Montserrat, Roboto, Open Sans, Lato, Lora, Outfit, Plus Jakarta Sans, Raleway, Oswald, Work Sans, Instrument Sans / Instrument Serif, Arial / Helvetica / system-ui.
