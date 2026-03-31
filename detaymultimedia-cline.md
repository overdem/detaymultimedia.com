# DETAY MULTİMEDYA — Cline Proje Dosyası
**detaymultimedia.com** · AI Destekli İş Otomasyonu Ajansı  
Son güncelleme: 2026-03-31

---

## 1. PROJE TANIMI

Detay Multimedya, işletmelerin operasyonel süreçlerini uçtan uca otomasyona geçiren bir ajans.  
Hedef: Kurumsal ve büyüme aşamasındaki şirketlere, **sektöre özgü iş diliyle** otomasyon çözümleri sunmak.

**Temel mesaj:**  
> "Teknoloji değil, sonuç satıyoruz. Mühendis tutmadan, kurumsal verimlilik."

**Ne DEĞİLiz:**  
- Basit chatbot ajansı değiliz  
- Fiyat listesi botu yapan bir freelancer değiliz  
- "AI danışmanlık" jargonu söyleyen bir firma değiliz  

**Ne OLDUĞUMUZ:**  
- Şirketin içindeki tekrarlayan, zaman çalan süreçleri tespit edip otomasyona geçiren bir operasyonel ortak  
- Sektörü bilen, iş dilini anlayan, teknolojiyi araç olarak kullanan bir ekip  
- Proje tesliminden sonra da yanında olan, sistemi büyüten bir yapı

---

## 2. HEDEF KİTLE

### Birincil Hedef
- Çalışan sayısı 10–500 arası şirketler  
- Yönetici / C-level karar vericiler (CEO, COO, Genel Müdür)  
- Operasyon, finans veya IT sorumluları  

### Sektörler (öncelik sırası)
1. Üretim & Tedarik Zinciri  
2. Lojistik & Nakliye  
3. Profesyonel Hizmetler (Hukuk, Mali Müşavirlik, Danışmanlık)  
4. Perakende & E-Ticaret (kurumsal ölçek)  
5. Sağlık & Klinik Zincirleri  
6. Gayrimenkul & İnşaat  
7. Otelcilik & Konaklama Zincirleri  
8. Eğitim & Kurumlar  

### Tonlama
- Güvenilir, ölçülü, net  
- Vaka bazlı konuşur ("Bir lojistik firmasında X sorunu şöyle çözdük")  
- Teknik jargon yok, iş jargonu var  
- Kibarca iddialı: rakipler karmaşık, biz sade ve sonuç odaklı

---

## 3. SİTE MİMARİSİ

```
/                          → Ana Sayfa
/cozumler                  → Çözümler (sektör hub)
  /cozumler/uretim         → Üretim & Tedarik
  /cozumler/lojistik       → Lojistik & Nakliye
  /cozumler/hukuk          → Hukuk & Danışmanlık
  /cozumler/perakende      → Perakende & E-Ticaret
  /cozumler/saglik         → Sağlık & Klinik
  /cozumler/gayrimenkul    → Gayrimenkul & İnşaat
  /cozumler/konaklama      → Otelcilik & Konaklama
  /cozumler/egitim         → Eğitim & Kurumlar
/hizmetler                 → Hizmetler (ne yapıyoruz)
/referanslar               → Vaka Çalışmaları (case study)
/hakkimizda                → Hakkımızda
/iletisim                  → İletişim & Demo Talebi
/blog                      → Blog (SEO — zamanla)
```

### URL Notu
- Türkçe karakter yok URL'de: `/cozumler` ✓, `/çözümler` ✗  
- Her sektör sayfası bağımsız SEO hedefi taşır  
- Yeni sektör = yeni alt sayfa, yapıyı bozmadan eklenir

---

## 4. SAYFA DETAYLARI

### 4.1 Ana Sayfa `/`

**Bölümler (yukarıdan aşağı):**

```
[NAV] Logo | Çözümler ▾ | Hizmetler | Referanslar | İletişim   [Demo Al →]

[HERO]
  Tag: "Kurumsal İş Otomasyonu"
  H1: "Operasyonunuzu otomasyona geçiriyoruz. Mühendis olmadan."
  Alt başlık: Kısa, somut, rakam içeren 2 satır
  CTA: [Demo Talep Et] [Çözümleri İncele]
  Güven çubuğu: Referans logo bar (yer tutucu, zamanla dolar)

[SORUN — "Neden otomasyon?"]
  3 kolon: İnsan hatası riski / Ölçeklenemeyen manuel süreçler / Görünmez zaman kayıpları
  Her kolonda somut rakam veya senaryo

[ÇÖZÜMLER GRID — Sektörler]
  8 sektör kartı, ikonu ve 1 cümle açıklamayla
  Her kart /cozumler/{sektor} sayfasına bağlı
  "Sektörünüzü görmüyor musunuz? → İletişime geçin"

[NASIL ÇALIŞIYORUZ]
  4 adım: Analiz → Tasarım → Uygulama → Optimizasyon
  Süre beklentisi her adımda belirtilmeli

[REFERANSLAR — seçki]
  2-3 öne çıkan vaka, rakam odaklı başlık
  "Tüm referanslar →"

[CTA BANNER]
  Kontrast alan, tek CTA: Demo randevusu

[FOOTER]
  Adres, iletişim, sosyal medya, hukuki linkler, KVKK
```

---

### 4.2 Çözümler Hub `/cozumler`

Bu sayfa sektör seçim sayfasıdır. İçerik değil, yönlendirme amaçlı.

```
[HEADER]
  H1: "Sektörünüze Özel Otomasyon Çözümleri"
  Alt: "Aynı teknolojiyi farklı sektörler için farklı şekilde yapılandırıyoruz."

[SEKTÖR KARTI GRID — 2 veya 3 kolon]
  Her kart:
    - Sektör ikonu (SVG, basit)
    - Sektör adı
    - 1 satır: "Bu sektörde ne çözüyoruz" özeti
    - "İncele →" linki
    - İsteğe bağlı: "X şirkette kullanıldı" etiketi

[SEKTÖRÜNÜZ YOK?]
  "Listede olmayan bir sektörde misiniz? Büyük ihtimalle çözümümüz var."
  [Bizimle konuşun →]
```

---

### 4.3 Sektör Sayfası Şablonu `/cozumler/{sektor}`

**Her sektör sayfası bu şablonu kullanır. İçerik değişir, yapı sabit kalır.**

```
[HERO — Sektöre özel]
  Tag: "[Sektör Adı] Otomasyonu"
  H1: Sektörün asıl sorunu cümleyle açıklanır
  Örnek: "Lojistik firmalarında operasyon ekibinin %60 zamanı manuel veri girişine gidiyor."
  CTA: [Bu Sektör İçin Demo Al]

[SEKTÖRÜN SORUNLARI]
  4-6 madde, her biri 1 cümle
  İş dilinde, teknik değil
  Örnek Lojistik: 
    · Sevkiyat takibi telefonla mı yapılıyor?
    · Müşteri "kargom nerede" için sizi mi arıyor?
    · Sürücü raporları Excel'de mi birikiyor?

[ÇÖZÜM HARİTASI]
  Sorun → Otomasyon Çıktısı eşleştirmesi
  Görsel: Sağ-sol veya üst-alt tablo yapısı
  Teknik detay vermeden, sadece ne değişeceğini göster

[KULLANIM SENARYOSU — "Nasıl görünür?"]
  Bir günlük operasyon öncesi/sonrası karşılaştırması
  Kısa, hikaye formatında, sayfa başına 1 senaryo

[KULLANILAN TEKNOLOJİLER — minimal]
  Logo bar: Make / n8n / Claude API / Supabase / vb.
  Açıklama: "Sistemi biz kuruyoruz, siz kullanıyorsunuz"
  NOT: Teknoloji detayı yok, sadece güven vermek için

[REFERANSLAR — bu sektörden]
  Varsa: 1-2 vaka çalışması kartı
  Yoksa: Boş bırak veya "İlk referansınız siz olun" mesajı

[CTA]
  "[Sektör] sektörü için analiz talep edin"
```

**Şu an oluşturulacak sektör sayfaları (içerik yok, placeholder ile):**
- /cozumler/uretim  
- /cozumler/lojistik  
- /cozumler/hukuk  
- /cozumler/perakende  
- /cozumler/saglik  
- /cozumler/gayrimenkul  
- /cozumler/konaklama  
- /cozumler/egitim

---

### 4.4 Hizmetler `/hizmetler`

Teknoloji/araç bazlı DEĞİL. Hizmet kategorisi bazlı.

```
Kategori 1: Süreç Analizi & Otomasyon Haritalaması
Kategori 2: İş Akışı Otomasyonu (workflow automation)
Kategori 3: Veri Entegrasyonu & Senkronizasyonu
Kategori 4: Raporlama & Karar Destek Sistemleri
Kategori 5: İletişim & Müşteri Süreçleri Otomasyonu
Kategori 6: Sürekli Optimizasyon & Destek
```

Her hizmet kartında:
- Ne yapıyoruz (1 paragraf, iş dili)
- Tipik kullanım alanları (3-4 madde)
- Tahmini proje süresi
- Hangi sektörlerde yaygın (etiket)

---

### 4.5 Referanslar `/referanslar`

**Yapı (vaka çalışması formatı):**

```
[HEADER — Sayılarla özet]
  Örnek: "14 sektör · 60+ proje · Ortalama %65 manuel iş azalması"

[VAKA KARTLARI — grid]
  Her kart:
    - Sektör etiketi
    - Şirket tipi (anonim olabilir: "İstanbul merkezli 80 çalışanlı lojistik firması")
    - Sorun: 1 cümle
    - Çözüm: 1 cümle
    - Sonuç: Kalın rakam (örn: "Haftalık 40 iş saati kazanıldı")
    - [Detaylı Oku →]
```

---

## 5. TASARIM SİSTEMİ

### 5.1 Renk Paleti

```css
:root {
  /* Ana renkler */
  --color-bg:        #0F0F0E;   /* Sayfa arka planı */
  --color-bg-2:      #171716;   /* Bölüm alternatifleri */
  --color-bg-3:      #1F1F1D;   /* Kart arka planı */
  --color-border:    rgba(255,255,255,0.07);
  --color-accent:    #E8961F;   /* Ana vurgu — turuncu/amber */
  --color-accent-dim:#B3700F;   /* Hover/pasif vurgu */
  
  /* Metin */
  --color-text:      #EEEDE8;   /* Birincil metin */
  --color-muted:     #7A7972;   /* İkincil metin */
  --color-subtle:    #4A4942;   /* Placeholder, disabled */
  
  /* Durum renkleri */
  --color-success:   #3D8C5A;
  --color-warning:   #C27B1A;
  --color-error:     #8C3D3D;
}
```

### 5.2 Tipografi

```css
/* Font stack */
--font-display: 'Barlow Condensed', sans-serif;  /* H1, büyük başlıklar */
--font-body:    'DM Sans', sans-serif;           /* Body, nav, UI */
--font-mono:    'JetBrains Mono', monospace;     /* Rakamlar, etiketler */

/* Scale */
--text-hero:   clamp(2.5rem, 6vw, 4.5rem);  font-weight: 700;
--text-h1:     clamp(2rem, 4vw, 3rem);      font-weight: 600;
--text-h2:     clamp(1.4rem, 2.5vw, 2rem);  font-weight: 600;
--text-h3:     1.1rem;                       font-weight: 500;
--text-body:   1rem;                         line-height: 1.75;
--text-small:  0.875rem;
--text-label:  0.75rem;   letter-spacing: 0.1em; text-transform: uppercase;
```

### 5.3 Bileşenler

**Butonlar:**
```
.btn-primary   → bg: accent, color: #0F0F0E, font-weight: 600
.btn-outline   → bg: transparent, border: 1px solid border-color, color: text
.btn-ghost     → bg: transparent, color: muted, hover: text
Tümü: border-radius: 2px (keskin köşe, kurumsal his)
Padding: 10px 24px
```

**Kartlar:**
```
.card          → bg: bg-3, border: 1px solid border-color, border-radius: 4px
.card:hover    → border-color: accent (opacity 0.4)
Padding: 1.5rem
```

**Bölüm etiketleri (section label):**
```
font: mono, 11px, letter-spacing: 0.12em, uppercase
color: accent
border-left: 2px solid accent; padding-left: 8px
```

**Grid çizgi arka plan (hero için):**
```css
background-image: 
  linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
  linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
background-size: 80px 80px;
```

### 5.4 Animasyon İlkeleri

```
Geçiş süresi: 200ms (hover), 350ms (sayfa elemanları)
Easing: ease-out
Scroll reveal: opacity 0→1 + translateY(16px→0)
Hiperbolik efekt yok: parallax, 3D transform, particle yok
```

---

## 6. TEKNİK STACK

### Frontend
```
Framework: Astro (tercih) veya sade HTML/CSS/JS
Styling: CSS variables + vanilla CSS (Tailwind opsiyonel)
Icons: Lucide veya özel SVG
Fonts: Google Fonts (Barlow Condensed + DM Sans + JetBrains Mono)
Build: Netlify veya Vercel deploy
```

### İletişim Formu / CTA
```
Form backend: Formspree veya Netlify Forms
Demo talep → n8n webhook → Slack / e-posta bildirimi
Alternatif: Tally.so embed (sıfır backend ihtiyacı)
```

### CMS (içerik yönetimi — zamanla)
```
Blog & vaka çalışmaları için: Notion API veya Markdown dosyaları
Sektör sayfaları: Şimdilik statik, zamanla CMS'e taşınır
```

---

## 7. SAYFA ÜRETİM TALİMATI — CLİNE İÇİN

### Kurulum Adımları

```bash
# 1. Proje oluştur
mkdir detaymultimedia && cd detaymultimedia
npm create astro@latest . -- --template minimal

# 2. Font ve ikonları ekle
# Google Fonts linki layout'a eklenecek

# 3. Dosya yapısı
src/
  layouts/
    BaseLayout.astro      # Nav + Footer dahil
    SectorLayout.astro    # Sektör sayfaları için şablon
  pages/
    index.astro           # Ana sayfa
    cozumler/
      index.astro         # Sektör hub
      uretim.astro        # Placeholder
      lojistik.astro      # Placeholder
      hukuk.astro         # Placeholder
      perakende.astro     # Placeholder
      saglik.astro        # Placeholder
      gayrimenkul.astro   # Placeholder
      konaklama.astro     # Placeholder
      egitim.astro        # Placeholder
    hizmetler.astro
    referanslar.astro
    hakkimizda.astro
    iletisim.astro
  components/
    Nav.astro
    Footer.astro
    SectorCard.astro      # Tekrar kullanılan sektör kartı
    CaseStudyCard.astro   # Vaka çalışması kartı
    SectionLabel.astro    # Tekrar kullanılan etiket bileşeni
    CTABanner.astro       # Sayfa sonu CTA
  styles/
    global.css            # CSS variables + reset
    typography.css        # Font tanımları
```

### Öncelik Sırası (build order)

```
Aşama 1 — Temel yapı:
  [x] global.css (tasarım sistemi)
  [x] BaseLayout.astro (nav + footer)
  [x] index.astro (ana sayfa, tam içerik)
  [x] cozumler/index.astro (sektör hub)

Aşama 2 — Sektör sayfaları:
  [x] SectorLayout.astro şablonu
  [x] Her sektör için placeholder sayfa (şablon dolu, içerik yer tutucu)

Aşama 3 — Destek sayfaları:
  [x] hizmetler.astro
  [x] referanslar.astro (boş state dahil)
  [x] iletisim.astro (form dahil)

Aşama 4 — SEO & Deploy:
  [x] sitemap.xml
  [x] robots.txt
  [x] og:image meta etiketleri
  [x] Vercel/Netlify deploy config
```

---

## 8. YENI SEKTÖR EKLEMEK — SİSTEM

Yeni sektör eklerken yapılacaklar:

1. `src/pages/cozumler/{yeni-sektor}.astro` dosyasını oluştur  
2. `SectorLayout.astro` şablonunu kullan  
3. `cozumler/index.astro` içindeki sektör kartlarına yeni kartı ekle  
4. Ana sayfadaki sektör grid'ine kartı ekle  
5. Nav dropdown'a satır ekle  

**Her sektör sayfası için doldurulması gereken veri:**

```js
// Her sektör sayfasında bu obje dolu olmalı
const sector = {
  name: "Lojistik & Nakliye",
  slug: "lojistik",
  headline: "Tek cümle, sektörün temel sorunu",
  subline: "Bir paragraf, ne çözüyoruz",
  problems: [
    "Madde 1",
    "Madde 2",
    "Madde 3",
    "Madde 4",
  ],
  solutions: [
    { problem: "Sorun", outcome: "Otomasyon çıktısı" },
  ],
  caseStudy: null, // veya { ... } objesi
  metaDescription: "SEO açıklaması",
}
```

---

## 9. DEMO TALEP AKIŞI

```
Kullanıcı "Demo Al" butonuna tıklar
→ Modal veya /iletisim sayfası açılır
→ Form alanları:
    - Ad Soyad
    - Şirket Adı
    - Sektör (dropdown — sektör listesinden)
    - Şirket büyüklüğü (dropdown: 1-10 / 10-50 / 50-200 / 200+)
    - En çok zaman kaybettiğiniz süreç (textarea, zorunlu değil)
    - Telefon veya E-posta
→ Submit → n8n webhook tetiklenir
→ Kullanıcıya: "48 saat içinde dönüş yapacağız" onay mesajı
→ Slack/e-posta bildirimi ajansa gelir
```

---

## 10. İÇERİK HAZIRLIK NOTLARI

### Henüz hazır olmayan içerik (placeholder kullan)
- Referans logoları → "Referanslar yakında" placeholder
- Vaka çalışmaları → Anonim format, gerçek rakamlar hazır değilse placeholder
- Hakkımızda görseli → Zamanla eklenecek
- Blog içerikleri → Deploy sonrası

### Placeholder metin kuralı
- `[SEKTÖR ADI]` gibi köşeli parantez kullan
- Türkçe Lorem Ipsum'dan kaçın, gerçekçi placeholder yaz
- Her placeholder başına `<!-- TODO: -->` yorumu ekle

### SEO Hedefleri (temel)
- Ana sayfa: "iş otomasyonu ajansı türkiye"
- Her sektör: "[sektör adı] otomasyon" (örn: "lojistik süreç otomasyonu")
- Hizmetler: "workflow automation türkiye", "iş akışı otomasyonu"

---

## 11. YAYIN ÖNCESİ KONTROLİST

```
[ ] Tüm sayfalar mobil responsive
[ ] Nav dropdown çalışıyor
[ ] Demo formu n8n webhook'a bağlı
[ ] 404 sayfası var
[ ] Favicon ayarlandı
[ ] og:image ve meta description her sayfada
[ ] Google Analytics / Plausible kodu eklendi
[ ] KVKK metni /kvkk sayfasında
[ ] Gizlilik Politikası var
[ ] SSL sertifikası aktif (Vercel otomatik)
[ ] Lighthouse skoru: Performance >85, SEO >90
[ ] detaymultimedia.com domain Vercel'e bağlı
```

---

## 12. TASARIM REFERANS ANALİZİ

> Tarih: 2026-03-31
> Bu bölüm, 4 referans sitenin canlı analizi sonucu oluşturulmuştur.
> **Uygulama kuralı:** Her yeni bileşen yazılmadan önce bu bölüm okunmalı.

---

### 12.1 Linear.app — Estetik Referans

**Temel ilke:** Hiçbir şey gereğinden fazla. Her piksel kasıtlı.

**Renk sistemi:**
- CSS variable bazlı tam theming (`--color-bg-primary`, `--color-text-primary` vb.)
- Renkler hard-coded değil, her zaman değişkenden gelir
- Minimal aksent kullanımı — kırmızı yalnız hata, yeşil yalnız başarı için

**Tipografi:**
- `--title-1` → `--title-9` modüler ölçek
- Monospace font sadece teknik/sayısal içerik için
- Letter-spacing değişkenleri (`--text-*-letter-spacing`) — her boyutta ayrı tanım
- Underline: 1.5px solid, 2.5px offset (standart değil, özenli)

**Animasyon felsefesi:**
- Dot grid pattern: 5×5, staggered (3200ms / 2800ms)
- Opacity geçişleri: 0.3 → 1.0 (aniden değil, aşamalı)
- Hiperbolik efekt yok: parallax, 3D transform, particle yok

**Uygula:**
- Tüm renkler CSS variable üzerinden git, asla hard-code
- Animasyon süresi: hover 200ms, sayfa elemanları 350ms
- Dot grid arka plan hero'da kullan (zaten global.css'te var)

---

### 12.2 İkas.com — Türk Pazar Uyarlaması

**Temel ilke:** Türk B2B alıcısına güven ver, net konuş, CTA'yı öne çıkar.

**Renk sistemi:**
```
Primary Blue:     #3034ff  (CTA, buton, aksent)
Primary Hover:    #2020e2
Neon Green:       #cce85f  (rozet, highlight, callout)
Purple:           #6f55ff  (ikincil aksent)
Body Text:        #364152
Dark:             #121926
Off-white:        #f8fafc
Light Gray:       #e3e8ef
```

**Tipografi (Inter tabanlı):**
- H1 Hero: 36px, weight 500–600, line-height 44px, letter-spacing -0.72px
- H2: 24–28px, weight 500
- Body: 16px/24px, weight 400
- Small: 14px

**Nav yapısı:**
- Sticky, 96px (desktop) / 72px (mobile)
- 1280px breakpoint'te hamburger
- Sağda: "Giriş Yap" + "Demo Al" aksiyonları

**Dikkat edilecek:**
- Türk pazarında **sosyal kanıt** çok etkili — müşteri logoları ilk bölümde
- Butonlarda **inset shadow** Türk kullanıcıda güven hissi verir
- CTA metni: "Ücretsiz Dene" > "Demo Al" > "İletişime Geç" (azalan dönüşüm sırası)

**Uygula:**
- Trust bar'ı hero'nun hemen altına koy (mevcut plan ile uyumlu ✓)
- Buton hover'da inset shadow ekle
- Neon green (`#cce85f`) → rozet ve highlight için kullanılabilir (aksent olarak değil)

---

### 12.3 Make.com — Otomasyon/Ajans Yapısı

**Temel ilke:** Karmaşık teknolojiyi görsel akışla sadeleştir, sektör bazlı gruplama yap.

**Yapısal kararlar:**
- Ana nav'da ürün değil, **kullanım senaryosu** öne çıkar ("Pazarlama", "Operasyon" gibi)
- Her çözüm sayfasında **görsel akış diyagramı** (bizde: sorun→çıktı tablosu)
- Hero'da rakam yok, **dönüşüm hikayesi** var ("X probleminiz varsa, biz çözüyoruz")
- Fiyatlandırma sayfası ayrı — çözüm sayfaları fiyat içermez

**Sektör sayfası mantığı:**
- Üst: Problem cümle (soru formatında daha etkili: "Sevkiyatı hâlâ telefonla mı takip ediyorsunuz?")
- Orta: Görsel öncesi/sonrası karşılaştırma
- Alt: Entegrasyon logoları (güven için)
- CTA: Genel değil, sektöre özel ("Lojistik için demo al")

**Uygula:**
- SectorLayout.astro'daki sorun maddelerini soru formatına çevir
- Her sektör CTA butonu slug içermeli: `/iletisim?sektor=lojistik`
- Teknoloji logoları bölümü "altyapı" değil "entegrasyonlar" olarak etiketle

---

### 12.4 Stripe.com — Sektör/Ürün Sayfası Mantığı

**Temel ilke:** Karmaşık ürünü sade tutarken kurumsal güven yayar.

**Renk & görsel:**
- Parallelogram/şerit motifi — marka kimliğinin parçası, tutarlı tekrar
- Bento grid: farklı boyutlu kartlarla esnek showcase
- Section alternation: beyaz / açık gri / görsel arka planlı bölümler — ritim yaratır

**Tipografi:**
- H1: 48–64px, sans-serif, clean
- Section başlıkları H2/H3: 24–32px
- Body: 16px
- Italik alt başlık kullanımı (hero'nun altında açıklayıcı italik metin)

**Spacing felsefesi:**
- Section padding: 80–120px (büyük nefes)
- Hard border yerine whitespace + subtle shadow tercih edilir
- Container: 1120–1440px arası

**Sektör sayfası mantığı:**
- Her ürün/sektör sayfası kendi URL'inde, bağımsız SEO hedefi taşır ✓
- Sayfa sonu CTA sektöre özel — genel "İletişim" değil ✓
- Müşteri logosu carousel hero'nun altında ✓
- **Bento grid** → ana sayfada sektör kartları bento layout'a geçilebilir

**Uygula:**
- Section padding'i `clamp(4rem, 8vw, 7rem)`'den `clamp(5rem, 10vw, 8rem)`'e çıkar
- Sektör kartları grid yerine bento layout denenebilir (ileride)
- Her sayfada italik açıklayıcı alt başlık ekle (hero subline)
- Whitespace'e güven — kalabalık bölüm = güvensizlik

---

### 12.5 Sentez — Bizim İçin Sonuçlar

| Karar | Kaynak | Uygulama |
|---|---|---|
| CSS variable tabanlı theming | Linear | global.css'te zaten var ✓ |
| Sticky nav, 64px | İkas | Nav.astro'da var ✓ |
| Soru formatında problem maddeleri | Make | SectorLayout güncellenmeli |
| Büyük section padding | Stripe | clamp değerleri artırıldı |
| Trust bar hero altında | İkas | index.astro'da var ✓ |
| Sektöre özel CTA | Make + Stripe | `?sektor=` parametresi eklendi ✓ |
| Neon green rozetler | İkas | Henüz eklenmedi |
| Bento grid (sektörler) | Stripe | İleride güncellenecek |
| İtalik hero alt başlık | Stripe | Tüm hero subline'larına uygulanacak |
| Inset shadow buton | İkas | global.css güncellenecek |

---

## 13. MULTİDİL MİMARİSİ

**Karar tarihi:** 2026-03-31

### Yöntem: Klasör bazlı routing
```
/tr/          → Türkçe (varsayılan)
/en/          → İngilizce
```

### Kurallar
- **Asla hard-coded metin yazma** — tüm içerik i18n dosyasından gelir
- Link formatı: `href="/tr/cozumler"` (dil prefix'i her zaman)
- Yeni sayfa eklerken hem `/tr/` hem `/en/` klasörüne ekle
- URL slug'ları dil bazında farklılaşmaz (örn: `cozumler` her iki dilde aynı)

### Dosya yapısı
```
src/
  i18n/
    types.ts      → TypeScript interface tanımları
    tr.ts         → Türkçe içerik
    en.ts         → İngilizce içerik
    index.ts      → Yardımcı fonksiyonlar (getLang, t())
  pages/
    index.astro   → /tr'ye yönlendir
    tr/           → Türkçe sayfalar
      index.astro
      cozumler/
        index.astro
        [sektor].astro
      hizmetler.astro
      referanslar.astro
      hakkimizda.astro
      iletisim.astro
    en/           → İngilizce sayfalar (aynı yapı)
```

### Dil değiştirici
- Nav'da sağ üstte: `TR | EN` toggle
- Mevcut sayfanın karşı dil versiyonuna link verir
- `hreflang` meta etiketi her sayfada

---

*Bu dosya Cline ile çalışırken proje context dosyası olarak kullanılır.*
*Yeni karar veya değişiklik olduğunda bu dosyayı güncelle.*
