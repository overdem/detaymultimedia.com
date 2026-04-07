# Görev: 8 Sektör Blog & SEO Sayfaları

## Genel Yapı

Her sektör için iki sayfa oluşturulacak:

1. `/tr/blog/[sektor]-otomasyon` — SEO odaklı, yapılandırılmış, 700-900 kelime
2. `/tr/blog/[sektor]-vaka-rehberi` — Derinlemesine rehber, 1200-1500 kelime

Toplam 16 sayfa. Önce şablonu kur, sonra her sektörü üret.

---

## DOSYA YAPISI

```
src/
  pages/
    tr/
      blog/
        index.astro                        ← Blog ana sayfa
        lojistik-otomasyon.astro
        lojistik-surecler-rehberi.astro
        uretim-otomasyon.astro
        uretim-surecler-rehberi.astro
        hukuk-otomasyon.astro
        hukuk-surecler-rehberi.astro
        perakende-otomasyon.astro
        perakende-surecler-rehberi.astro
        saglik-otomasyon.astro
        saglik-surecler-rehberi.astro
        gayrimenkul-otomasyon.astro
        gayrimenkul-surecler-rehberi.astro
        konaklama-otomasyon.astro
        konaklama-surecler-rehberi.astro
        egitim-otomasyon.astro
        egitim-surecler-rehberi.astro
  layouts/
    BlogLayout.astro                       ← Blog sayfaları için layout
  components/
    BlogCTA.astro                          ← Her blog sonundaki CTA
    RelatedPosts.astro                     ← İlgili yazılar bileşeni
```

---

## BlogLayout.astro — ŞABLON

```astro
---
interface Props {
  title: string;
  description: string;
  sector: string;
  readTime: string;
  publishDate: string;
  type: 'seo' | 'rehber';
}
const { title, description, sector, readTime, publishDate, type } = Astro.props;
---
```

Layout yapısı:
- BaseLayout'u extend et
- Sol: İçerik (max-width 720px)
- Sağ: Sticky sidebar — sektör CTA kartı, ilgili yazılar
- Üst: Breadcrumb → Ana Sayfa / Blog / [Başlık]
- Alt: BlogCTA bileşeni + RelatedPosts

---

## TİP 1 — SEO SAYFASI ŞABLONU

Her sektör için yapı:

```
[BREADCRUMB]
Ana Sayfa → Blog → [Sektör] Otomasyonu

[SECTION ETİKETİ]
[Sektör] · Otomasyon Rehberi

[H1]
[Sektör] Firmalarında Süreç Otomasyonu:
Neden Kaçınılmaz Hale Geldi?

[GİRİŞ — 100 kelime]
Rakam ve somut senaryo ile başla.
"Türkiye'deki [sektör] firmalarının %X'i..."

[H2] [Sektör]'de En Çok Zaman Kaybettiren 5 Süreç
  Her madde: Sorun + neden olduğu kayıp + 1 cümle çözüm

[H2] Otomasyon Hangi Süreçleri Değiştirir?
  Tablo: Süreç | Önce | Sonra | Kazanım

[H2] Nereden Başlamalı?
  3 adım — analiz, önceliklendirme, uygulama

[CTA KUTUSU]
"[Sektör] sektörü için ücretsiz süreç analizi"
→ /tr/iletisim

[İLGİLİ]
→ Derinlemesine rehbere link
→ Sektör çözüm sayfasına link (/tr/cozumler/[sektor])
```

---

## TİP 2 — DERİNLEMESİNE REHBERİ ŞABLONU

```
[BREADCRUMB]
Ana Sayfa → Blog → [Sektör] Süreçler Rehberi

[SECTION ETİKETİ]
Pratik Rehber · [Sektör]

[H1]
[Sektör] İşletmelerinde İş Akışı Otomasyonu:
Adım Adım Uygulama Rehberi

[GİRİŞ — 150 kelime]
Kimin için yazıldı, ne öğrenecekler, neden şimdi

[H2] [Sektör]'ün Operasyonel Gerçeği
  Sektöre özgü zorluklar, rakamlarla

[H2] Hangi Süreçler Otomasyona Hazır?
  Öncelik matrisi: Etki (yüksek/düşük) × Zorluk (kolay/zor)
  4 kadranda sınıflandırılmış süreçler

[H2] Araçlar ve Entegrasyonlar
  Sektörde yaygın kullanılan yazılımlar
  Bunlarla nasıl entegre olunur
  Teknik detay yok — "ne sağlar" odaklı

[H2] Gerçek Senaryo: Bir Haftada Ne Değişir?
  Pazartesi sabahı → Cuma akşamı
  Önce/sonra karşılaştırması, hikaye formatında

[H2] Sık Yapılan Hatalar
  3-4 madde, her biri "Hata → Neden Olur → Nasıl Önlenir"

[H2] Nereden Başlamalısınız?
  Öz değerlendirme soruları (5 soru)
  Cevaplara göre yönlendirme

[CTA KUTUSU — accent arka plan]
"Süreçlerinizi birlikte haritalayalım"
30 dakika ücretsiz analiz
→ Demo Randevusu Al

[İLGİLİ]
→ SEO sayfasına link
→ Sektör çözüm sayfasına link
```

---

## 8 SEKTÖR İÇERİK REHBERİ

### 1. Lojistik & Nakliye
**SEO anahtar kelime:** "lojistik süreç otomasyonu"
**Ana sorunlar:** Sevkiyat takibi, sürücü raporları, müşteri bildirimleri, fatura işlemleri
**Somut rakam:** Türkiye'de lojistik firmalarının %70'i sevkiyat güncellemelerini hâlâ telefonla yapıyor
**Senaryo:** 120 araçlı nakliye firması, günde 40 telefon görüşmesi sadece "kargom nerede" için

### 2. Üretim & Tedarik
**SEO anahtar kelime:** "üretim otomasyon sistemi"
**Ana sorunlar:** Sipariş takibi, stok uyarıları, tedarikçi iletişimi, üretim raporları
**Somut rakam:** Üretim firmalarında veri girişi hatalarının %80'i manuel süreçlerden kaynaklanıyor
**Senaryo:** 3 ayrı sistemde tutulan sipariş, stok ve fatura verisi — entegrasyon yok

### 3. Hukuk & Danışmanlık
**SEO anahtar kelime:** "hukuk bürosu süreç otomasyonu"
**Ana sorunlar:** Sözleşme takibi, duruşma hatırlatmaları, müvekkil bildirimleri, belge yönetimi
**Somut rakam:** Hukuk bürolarında avukatların zamanının %35'i idari işlere gidiyor
**Senaryo:** 5 avukatlı büro, 200 aktif dosya — hangi duruşma ne zaman kim takip ediyor?

### 4. Perakende & E-Ticaret
**SEO anahtar kelime:** "e-ticaret operasyon otomasyonu"
**Ana sorunlar:** Sipariş yönetimi, stok senkronizasyonu, müşteri bildirimleri, iade süreci
**Somut rakam:** E-ticaret firmalarında müşteri hizmetleri sorgularının %60'ı sipariş durumu sorusu
**Senaryo:** 500 günlük sipariş, 3 kanal (web, marketplace, mağaza) — stok tutarsızlığı

### 5. Sağlık & Klinik
**SEO anahtar kelime:** "klinik randevu otomasyonu"
**Ana sorunlar:** Randevu yönetimi, hasta hatırlatmaları, raporlama, sigorta takibi
**Somut rakam:** Hatırlatma yapılmayan randevularda %30 gelmeme oranı
**Senaryo:** 3 doktorlu klinik, resepsiyon telefondan ayrılamıyor çünkü randevu sorguları geliyor

### 6. Gayrimenkul & İnşaat
**SEO anahtar kelime:** "gayrimenkul süreç otomasyonu"
**Ana sorunlar:** İlan yönetimi, müşteri takibi, görüntüleme randevuları, sözleşme süreci
**Somut rakam:** Gayrimenkul danışmanları zamanlarının %45'ini idari işlere harcıyor
**Senaryo:** 200 aktif ilan, her ilanın WhatsApp soruları, görüntüleme takibi — Excel'de

### 7. Otelcilik & Konaklama
**SEO anahtar kelime:** "otel operasyon otomasyonu"
**Ana sorunlar:** Rezervasyon yönetimi, misafir iletişimi, temizlik koordinasyonu, raporlama
**Somut rakam:** Otellerde check-in/check-out süreçleri ortalama 12 dakika alıyor
**Senaryo:** 40 odalı butik otel, 3 kanal üzerinden rezervasyon — çakışmalar kaçınılmaz

### 8. Eğitim & Kurumlar
**SEO anahtar kelime:** "eğitim kurumu süreç otomasyonu"
**Ana sorunlar:** Kayıt süreçleri, devam takibi, veli bildirimleri, ödeme hatırlatmaları
**Somut rakam:** Özel okullarda idari personelin %50 zamanı manuel bildirim ve takibe gidiyor
**Senaryo:** 300 öğrencili okul — devamsızlık bildirimi hâlâ telefonla yapılıyor

---

## BLOG ANA SAYFA — `/tr/blog/index.astro`

```
[HEADER]
Section etiketi: Blog & Rehberler
Başlık: Otomasyon hakkında bilmeniz gerekenler
Alt: "Sektöre özgü rehberler, pratik içerikler,
     gerçek senaryolar."

[FİLTRE ÇUBUĞU]
Tümü | Lojistik | Üretim | Hukuk | Perakende |
Sağlık | Gayrimenkul | Konaklama | Eğitim

[KART GRİD — 2 kolon]
Her kart:
  - Sektör etiketi (accent rengi)
  - Tip etiketi: "SEO Rehberi" veya "Derinlemesine"
  - Başlık
  - 2 satır özet
  - Okuma süresi
  - Devamını Oku →

[SAYFALAMA]
İlk yüklemede 8 kart, "Daha Fazla Göster" butonu
```

---

## META TAG KURALI

Her sayfa için:
```astro
---
const meta = {
  title: "[Başlık] — Detay Multimedya Blog",
  description: "[150 karakter, anahtar kelime içeren özet]",
  canonical: "https://detaymultimedia.com/tr/blog/[slug]"
}
---
```

---

## ÖNCE BUNLARI YAP — ÖNCELİK SIRASI

```
1. BlogLayout.astro şablonu
2. BlogCTA.astro bileşeni
3. blog/index.astro — ana sayfa (içerik placeholder)
4. lojistik-otomasyon.astro — tam içerik
5. lojistik-surecler-rehberi.astro — tam içerik
6. Diğer 6 sektör — aynı şablonla, sektör verisini değiştirerek
```

Lojistik sayfaları tam içerikle üret, diğerleri için
içerik yapısı aynı kalacak sadece sektör verisi değişecek.

---

## TASARIM NOTLARI

- Blog sayfaları beyaz/açık arka plan OLMAYACAK
- Site ile aynı dark tema devam edecek
- Makale içi başlıklar H2/H3 hiyerarşisi — Barlow Condensed
- Body metin: DM Sans, 17px, line-height 1.8, --color-muted
- İçerik max-width: 680px, ortalı
- Kod/veri blokları: JetBrains Mono, --color-bg-3 arka plan
- CTA kutuları: --color-accent border-left 4px veya
  tam accent arka plan (son CTA)
- Mobilde sidebar gizlenecek, içerik tam genişlik
