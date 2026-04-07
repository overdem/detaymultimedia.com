import type { Translations } from './types';

export const tr: Translations = {
  site: {
    name: 'Detay Multimedya',
    tagline: 'Teknoloji değil, sonuç satıyoruz.',
    description:
      'Detay Multimedya — Şirketlerin operasyonel süreçlerini uçtan uca otomasyona geçiren iş ortağınız. Mühendis tutmadan kurumsal verimlilik.',
  },

  nav: {
    solutions: 'Çözümler',
    allSolutions: 'Tüm Çözümler →',
    services: 'Hizmetler',
    references: 'Referanslar',
    about: 'Hakkımızda',
    contact: 'İletişim',
    cta: 'Demo Al →',
  },

  home: {
    heroLabel: 'Kurumsal İş Otomasyonu',
    heroTitle: ['Operasyonunuzu', 'otomasyona geçiriyoruz.', 'Mühendis olmadan.'],
    heroSub:
      'Şirketinizdeki tekrarlayan, zaman çalan süreçleri tespit edip otomasyona geçiriyoruz. Teknoloji değil, sonuç satıyoruz. 1997\'den bu yana kurumsal projeler yönetiyoruz.',
    ctaPrimary: 'Demo Talep Et →',
    ctaSecondary: 'Çözümleri İncele',
    statsValue1: '27',
    statsLabel1: 'Yıllık Deneyim',
    statsValue2: '%65',
    statsLabel2: 'Ort. Manuel İş Azalması',
    statsValue3: '48s',
    statsLabel3: 'İlk Geri Dönüş',
    trustLabel: '27 Yıllık Deneyim',
    trustDesc: 'Shell, Procter & Gamble, Bayer ve Anadolu Group dahil kurumsal markalarla çalışma deneyimi — 1997\'den bu yana',
    whyLabel: 'Neden Otomasyon?',
    whyTitle: 'Şirketinizde bu sorunlardan kaçı var?',
    pains: [
      {
        title: 'İnsan Hatası Riski',
        desc: 'Manuel veri girişi, kopyala-yapıştır süreçleri, e-posta zincirlerinde kaybolan bilgiler. Her gün küçük hatalar, büyük sonuçlar.',
        stat: "Hataların %80'i tekrarlayan görevlerde oluşur",
      },
      {
        title: 'Ölçeklenemeyen Süreçler',
        desc: 'Takım büyüdükçe süreçler karmaşıklaşıyor. Yeni kişi = yeni eğitim = yeni hata riski. Otomasyon sistemi siz büyüdükçe büyür.',
        stat: "Şirketlerin %67'si manuel süreç yüzünden ölçeklenemiyor",
      },
      {
        title: 'Görünmez Zaman Kayıpları',
        desc: 'Haftalık kaç saat rapor derleniyor? Kaç saat veri aktarılıyor? Kaç saat "bu mail gitti mi?" diye soruluyor?',
        stat: "Çalışanlar zamanlarının %40'ını tekrarlayan görevlere harcıyor",
      },
    ],
    sectorsLabel: 'Sektörler',
    sectorsTitle: 'Sektörünüze Özel Otomasyon',
    sectorsSub:
      'Aynı teknolojiyi farklı sektörler için farklı şekilde yapılandırıyoruz. Lojistik firmasının sorunu ile hukuk bürosunun sorunu farklı — çözümümüz de farklı olmalı.',
    sectorsMissing: 'Sektörünüzü görmüyor musunuz?',
    sectorsMissingCta: 'İletişime geçin →',
    processLabel: 'Süreç',
    processTitle: 'Nasıl Çalışıyoruz?',
    processSub: 'İlk görüşmeden canlıya geçişe kadar her adımda yanınızdayız.',
    steps: [
      {
        number: '01',
        title: 'Analiz',
        desc: 'Süreçlerinizi dinliyoruz. Nerede zaman kaybedildiğini, hangi adımın tekrarlandığını tespit ediyoruz.',
        duration: '1–3 gün',
      },
      {
        number: '02',
        title: 'Tasarım',
        desc: 'Size özel otomasyon haritası çıkarıyoruz. Hangi araç, hangi entegrasyon, hangi öncelik sırası.',
        duration: '3–5 gün',
      },
      {
        number: '03',
        title: 'Uygulama',
        desc: 'Sistemi kuruyoruz, test ediyoruz, ekibinizi alıştırıyoruz. Siz sadece onay veriyorsunuz.',
        duration: '1–4 hafta',
      },
      {
        number: '04',
        title: 'Optimizasyon',
        desc: 'Sistem canlıya geçtikten sonra ölçüp iyileştiriyoruz. Tek seferlik proje değil, süregelen ortaklık.',
        duration: 'Süregelen',
      },
    ],
    referencesLabel: 'Referanslar',
    referencesTitle: 'Sonuçlarla Konuşuyoruz',
    referencesAll: 'Tüm Referanslar →',
  },

  ctaBanner: {
    label: 'Başlayalım',
    title: 'Operasyonunuzu otomasyona geçirmeye hazır mısınız?',
    subtitle:
      '48 saat içinde geri dönüş garantisiyle ücretsiz analiz randevusu alın.',
    cta: 'Demo Randevusu Al →',
  },

  solutionsHub: {
    label: 'Çözümler',
    title: 'Sektörünüze Özel Otomasyon Çözümleri',
    subtitle:
      'Aynı teknolojiyi farklı sektörler için farklı şekilde yapılandırıyoruz.',
    inspect: 'İncele →',
    noSectorTitle: 'Sektörünüz listede yok mu?',
    noSectorSub: 'Büyük ihtimalle çözümümüz var. Konuşalım.',
    noSectorCta: 'Bizimle konuşun →',
  },

  sectorPage: {
    label: 'Otomasyonu',
    ctaDemo: 'Sektörü İçin Demo Al →',
    problemsLabel: 'Tanıdık mı geliyor?',
    problemsTitle: 'Sektöründe Gördüğümüz Sorunlar',
    solutionLabel: 'Otomasyon Haritası',
    solutionTitle: 'Sorundan Çıktıya',
    solutionSub:
      'Her manuel sürecin karşısına bir otomasyon çıktısı koyuyoruz.',
    techLabel: 'Altyapı',
    techTitle: 'Sistemi Biz Kuruyoruz, Siz Kullanıyorsunuz',
    techSub:
      'Hangi teknolojiyi kullandığımız değil, ne sonuç aldığınız önemli. Ama merak edenler için:',
    referencesLabel: 'Referanslar',
    referencesTitle: 'Sektöründen Vakalar',
    noCaseText: 'Bu sektörde yeni projeler başlatıyoruz.',
    noCaseCta: 'İlk Referansınız Siz Olun →',
    ctaSuffix: 'sektörü için özel analiz talep edin',
    ctaSubtitle:
      'Süreçlerinizi inceleyip size özel otomasyon haritası çıkarıyoruz. Ücretsiz.',
    ctaBtn: 'Analizi Talep Et →',
    problemCol: 'Mevcut Sorun',
    outcomeCol: 'Otomasyon Çıktısı',
    problemBadge: 'Sorun',
    outcomeBadge: 'Çıktı',
  },

  services: {
    metaTitle: 'Hizmetler',
    metaDesc:
      'İş akışı otomasyonu, veri entegrasyonu, raporlama ve süreç analizi hizmetlerimiz.',
    heroLabel: 'Hizmetler',
    heroTitle: 'Ne Yapıyoruz?',
    heroSub:
      'Teknolojiyi araç olarak kullanıyoruz. Sunduğumuz şey teknoloji değil, sonuç.',
    categories: [
      {
        title: 'Süreç Analizi & Otomasyon Haritalaması',
        desc: 'Şirketinizdeki mevcut süreçleri gözlemleyip hangilerinin otomasyona uygun olduğunu tespit ediyoruz. Öncelik sırası, tahmini kazanım ve uygulama planı çıkarıyoruz.',
        useCases: [
          'Operasyon süreç denetimi',
          'Zaman-kayıp analizi',
          'Otomasyon ROI hesabı',
          'Yol haritası oluşturma',
        ],
        duration: '3–5 gün',
        sectors: ['Üretim', 'Lojistik', 'Profesyonel Hizmetler'],
      },
      {
        title: 'İş Akışı Otomasyonu',
        desc: 'Tekrarlayan adımları otomatik hale getiriyoruz. E-posta bildirimleri, form işlemleri, onay akışları, görev atamaları — insan müdahalesi olmadan.',
        useCases: [
          'Onay & bildirim akışları',
          'Form → CRM entegrasyonu',
          'Otomatik görev ataması',
          'Durum güncelleme bildirimleri',
        ],
        duration: '1–2 hafta',
        sectors: ['Tüm sektörler'],
      },
      {
        title: 'Veri Entegrasyonu & Senkronizasyonu',
        desc: 'Farklı sistemlerdeki verileri birleştiriyoruz. ERP, CRM, muhasebe, e-ticaret platformları — hepsi birbiriyle konuşsun.',
        useCases: [
          'ERP ↔ CRM senkronizasyonu',
          'E-ticaret ↔ stok sistemi',
          'Muhasebe otomatik aktarımı',
          'Çoklu platform veri havuzu',
        ],
        duration: '1–3 hafta',
        sectors: ['Perakende', 'Üretim', 'Lojistik'],
      },
      {
        title: 'Raporlama & Karar Destek Sistemleri',
        desc: 'Dağınık verileri otomatik raporlara dönüştürüyoruz. Her sabah güncel operasyon özeti, haftalık performans panosu — manuel toplama yok.',
        useCases: [
          'Otomatik haftalık/aylık rapor',
          'Yönetici dashboard',
          'Anomali uyarı sistemi',
          'KPI takip paneli',
        ],
        duration: '1–2 hafta',
        sectors: ['Tüm sektörler'],
      },
      {
        title: 'İletişim & Müşteri Süreçleri Otomasyonu',
        desc: 'Müşteri iletişimindeki manuel adımları otomatikleştiriyoruz. Karşılama mesajları, takip e-postaları, anket gönderimi, randevu hatırlatmaları.',
        useCases: [
          'Müşteri karşılama akışı',
          'Otomatik takip e-postası',
          'Randevu hatırlatma',
          'NPS & anket otomasyonu',
        ],
        duration: '3–7 gün',
        sectors: ['Sağlık', 'Gayrimenkul', 'Konaklama'],
      },
      {
        title: 'Sürekli Optimizasyon & Destek',
        desc: 'Sistemi kurduktan sonra bırakmıyoruz. Aylık inceleme, performans ölçümü, iyileştirme önerileri ve teknik destek.',
        useCases: [
          'Aylık sistem incelemesi',
          'Performans raporlama',
          'Yeni süreç ekleme',
          'Teknik destek & bakım',
        ],
        duration: 'Süregelen',
        sectors: ['Tüm sektörler'],
      },
    ],
  },

  references: {
    metaTitle: 'Referanslar',
    metaDesc: 'Detay Multimedya müşteri vaka çalışmaları ve başarı hikayeleri.',
    heroLabel: 'Referanslar',
    heroTitle: 'Sonuçlarla Konuşuyoruz',
    heroSub: 'Her vaka, gerçek bir şirketteki gerçek bir sorunun çözümü.',
    statsBar: '8 sektör · Onlarca proje · Ortalama %65 manuel iş azalması',
    readMore: 'Detaylı Oku →',
    emptyCta: 'Siz de Referansımız Olun →',
  },

  about: {
    metaTitle: 'Hakkımızda',
    metaDesc:
      'Detay Multimedya hakkında — kimiz, ne yapıyoruz, neden farklıyız.',
    heroLabel: 'Hakkımızda',
    heroTitle: 'Şirketinizin Operasyonel Ortağıyız',
    heroSub:
      'Teknoloji satan bir ajans değiliz. Şirketinizin içindeki tekrarlayan, zaman çalan süreçleri tespit edip otomasyona geçiren bir operasyonel ortağız.',
    missionLabel: 'Misyon',
    missionTitle: 'Neden Varız?',
    missionText:
      'Kurumsal şirketlerin otomasyon projelerinde harcadığı bütçeyi, büyüme aşamasındaki şirketler de karşılayabilmeli. Bunu mümkün kılmak için sektörü bilen, iş dilini anlayan ve teknolojiyi araç olarak kullanan bir ekip kurduk.',
    valuesLabel: 'İlkeler',
    values: [
      {
        title: 'Sonuç Odaklılık',
        desc: 'Hangi teknolojiyi kullandığımız değil, müşterimizin ne kazandığı önemli. Her proje ölçülebilir çıktıyla başlar.',
      },
      {
        title: 'Sektör Dili',
        desc: 'Lojistik firmasıyla lojistik dilinde, hukuk bürosuyla hukuk dilinde konuşuruz. Jargon yok, iş dili var.',
      },
      {
        title: 'Süregelen Ortaklık',
        desc: 'Proje teslim edip çıkmıyoruz. Sistem büyüdükçe, şirket büyüdükçe yanındayız.',
      },
      {
        title: 'Sadelik',
        desc: 'Karmaşık çözümler bakımı zor, öğrenmesi zor. En iyi otomasyon, ekibinizin benimsediği otomasyon.',
      },
    ],
  },

  contact: {
    metaTitle: 'İletişim & Demo Talebi',
    metaDesc:
      'Detay Multimedya ile iletişime geçin. 48 saat içinde geri dönüş garantisi.',
    heroLabel: 'Demo Talebi',
    heroTitle: 'Süreci Birlikte Değerlendirelim',
    heroSub:
      'Şirketinizin hangi süreçlerini otomasyona geçirebileceğimizi 30 dakikalık bir görüşmede konuşalım.',
    formName: 'Ad Soyad',
    formCompany: 'Şirket Adı',
    formSector: 'Sektör',
    formSize: 'Şirket Büyüklüğü',
    formProcess: 'En Çok Zaman Kaybettiğiniz Süreç',
    formProcessPlaceholder:
      'Örn: Her hafta satış raporlarını manuel olarak Excel\'e giriyoruz...',
    formPhone: 'Telefon veya E-posta',
    formSubmit: 'Gönder — 48s içinde dönelim',
    formSuccess:
      '✓ Talebiniz alındı. En geç 48 saat içinde size dönüş yapacağız.',
    sizes: ['1–10', '10–50', '50–200', '200+'],
    responseNote: '48 saat içinde geri dönüş garantisi',
  },

  footer: {
    solutionsCol: 'Çözümler',
    companyCol: 'Şirket',
    contactCol: 'İletişim',
    tagline: 'Teknoloji değil, sonuç satıyoruz.\nMühendis tutmadan, kurumsal verimlilik.',
    blog: 'Blog',
    kvkk: 'KVKK',
    privacy: 'Gizlilik Politikası',
    terms: 'Kullanım Koşulları',
    rights: 'Tüm hakları saklıdır.',
  },

  sectors: [
    {
      slug: 'uretim',
      name: 'Üretim & Tedarik',
      icon: '⬡',
      summary: 'Üretim planlaması, stok yönetimi ve tedarikçi iletişimini otomasyona geçirin.',
      headline: 'Üretim hattınızda her gün kaç saatiniz kağıt işlerine gidiyor?',
      subline:
        'Sipariş takibi, stok uyarıları, tedarikçi bildirimleri ve üretim raporlarını otomasyona alıyoruz. Ekibiniz üretmeye odaklanır.',
      problems: [
        'Stok seviyeleri hâlâ manuel mi takip ediliyor?',
        'Tedarikçilere sipariş durumu e-postayla mı bildiriliyor?',
        'Üretim planı Excel\'de mi tutuluyor?',
        'Kalite kontrol kayıtları kâğıt formda mı?',
        'Haftalık üretim raporu hazırlamak 2+ saat mi alıyor?',
      ],
      solutions: [
        { problem: 'Manuel stok takibi', outcome: 'Otomatik stok uyarısı ve yenileme tetikleyicisi' },
        { problem: 'Tedarikçi e-posta bildirimleri', outcome: 'Sistem tabanlı otomatik sipariş bildirimi' },
        { problem: 'Excel üretim planı', outcome: 'Gerçek zamanlı üretim panosu' },
        { problem: 'Manuel raporlama', outcome: 'Haftalık otomatik üretim özet raporu' },
      ],
      metaDescription:
        'Üretim ve tedarik sektörü için iş otomasyonu. Stok takibi, tedarikçi bildirimleri ve üretim raporlarını otomatikleştirin.',
    },
    {
      slug: 'lojistik',
      name: 'Lojistik & Nakliye',
      icon: '◈',
      summary: 'Sevkiyat takibi, müşteri bildirimleri ve sürücü raporlarını otomatikleştirin.',
      headline: 'Sevkiyatı hâlâ telefonla mı takip ediyorsunuz?',
      subline:
        'Müşteri "kargom nerede?" diye aramadan önce sistem bildirim gönderiyor. Operasyon ekibiniz telefon yerine planlama yapıyor.',
      problems: [
        'Müşteriler sevkiyat durumu için sizi mi arıyor?',
        'Sürücü raporları günün sonunda mı toplanıyor?',
        'Gecikme bildirimi manuel olarak mı yapılıyor?',
        'Araç takip verisi sisteme manuel mi giriliyor?',
        'Faturalandırma teslimat teyidini bekliyor mu?',
      ],
      solutions: [
        { problem: 'Müşteri telefon sorguları', outcome: 'Otomatik sevkiyat durum bildirimleri (SMS/e-posta)' },
        { problem: 'Manuel sürücü raporlaması', outcome: 'Mobil uygulama üzerinden anlık güncelleme' },
        { problem: 'Gecikme bildirimleri', outcome: 'Eşik aşıldığında otomatik uyarı ve bildirim' },
        { problem: 'Manuel faturalandırma', outcome: 'Teslimat teyidi sonrası otomatik fatura oluşturma' },
      ],
      metaDescription:
        'Lojistik ve nakliye sektörü için süreç otomasyonu. Sevkiyat takibi, müşteri bildirimleri ve raporlamayı otomatikleştirin.',
    },
    {
      slug: 'hukuk',
      name: 'Hukuk & Danışmanlık',
      icon: '◻',
      summary: 'Sözleşme yönetimi, müvekkil takibi ve belge süreçlerini hızlandırın.',
      headline: 'Müvekkil takibi için kaç farklı araç kullanıyorsunuz?',
      subline:
        'Sözleşme son tarihleri, müvekkil hatırlatmaları ve belge akışını tek bir otomatik sistemde topluyoruz.',
      problems: [
        'Sözleşme tarihleri takvimde mi takip ediliyor?',
        'Müvekkil randevu hatırlatmaları manuel mi gönderiliyor?',
        'Dava belgelerine erişim e-posta zincirlerinde mi?',
        'Fatura takibi ayrı bir sistemde mi?',
        'Yeni müvekkil onboarding süreci standart mı?',
      ],
      solutions: [
        { problem: 'Manuel takvim takibi', outcome: 'Otomatik son tarih uyarısı ve hatırlatma akışı' },
        { problem: 'Manuel randevu hatırlatması', outcome: 'Otomatik SMS/e-posta hatırlatma sistemi' },
        { problem: 'Dağınık belge yönetimi', outcome: 'Merkezi belge arşivi ve erişim otomasyonu' },
        { problem: 'Manuel onboarding', outcome: 'Standart müvekkil karşılama ve belge toplama akışı' },
      ],
      metaDescription:
        'Hukuk büroları ve danışmanlık firmaları için süreç otomasyonu. Sözleşme takibi, müvekkil yönetimi ve belge akışını otomatikleştirin.',
    },
    {
      slug: 'perakende',
      name: 'Perakende & E-Ticaret',
      icon: '◇',
      summary: 'Sipariş, stok ve müşteri hizmetleri süreçlerini entegre edin.',
      headline: 'Sipariş yönetiminde kaç sistem arasında geçiş yapıyorsunuz?',
      subline:
        'E-ticaret platformu, stok sistemi ve muhasebe birbirine konuşuyor. Sipariş girer, sistem harekete geçer.',
      problems: [
        'Stok güncelleme birden fazla platformda manuel mi yapılıyor?',
        'İade süreçleri e-posta zinciriyle mi yönetiliyor?',
        'Müşteri soruları tek noktada mı toplanıyor?',
        'Kargo bildirimleri otomatik mi gönderiliyor?',
        'Satış raporları birden fazla kaynaktan mı derleniyor?',
      ],
      solutions: [
        { problem: 'Çoklu platform stok yönetimi', outcome: 'Merkezi stok senkronizasyonu (gerçek zamanlı)' },
        { problem: 'Manuel iade süreci', outcome: 'Otomatik iade onay ve iade akışı' },
        { problem: 'Dağınık müşteri soruları', outcome: 'Birleşik müşteri iletişim merkezi' },
        { problem: 'Manuel satış raporlaması', outcome: 'Günlük/haftalık otomatik satış özeti' },
      ],
      metaDescription:
        'Perakende ve e-ticaret için süreç otomasyonu. Stok senkronizasyonu, sipariş yönetimi ve raporlamayı otomatikleştirin.',
    },
    {
      slug: 'saglik',
      name: 'Sağlık & Klinik',
      icon: '○',
      summary: 'Hasta randevu, hatırlatma ve raporlama süreçlerini otomasyona alın.',
      headline: 'Randevu hatırlatmaları hâlâ sekreter tarafından mı yapılıyor?',
      subline:
        'Hasta iletişimi, randevu yönetimi ve klinik raporlamasını otomasyona geçiriyoruz. Ekibiniz hastaya odaklanır.',
      problems: [
        'Randevu hatırlatmaları manuel olarak mı aranıyor?',
        'No-show oranınız yüksek mi?',
        'Hasta dosyalarına erişim zaman alıyor mu?',
        'Sigorta ve fatura süreçleri manuel mi işleniyor?',
        'Periyodik kontrol davetleri nasıl gönderiliyor?',
      ],
      solutions: [
        { problem: 'Manuel randevu hatırlatması', outcome: 'Otomatik SMS/WhatsApp hatırlatma (24s ve 2s öncesi)' },
        { problem: 'Yüksek no-show oranı', outcome: 'Hatırlatma + onay sistemiyle doluluk optimizasyonu' },
        { problem: 'Manuel sigorta işlemleri', outcome: 'Sigorta form otomasyonu ve takip sistemi' },
        { problem: 'Periyodik kontrol takibi', outcome: 'Otomatik hasta geri çağırma kampanyası' },
      ],
      metaDescription:
        'Klinik ve sağlık kurumları için süreç otomasyonu. Randevu yönetimi, hasta iletişimi ve raporlamayı otomatikleştirin.',
    },
    {
      slug: 'gayrimenkul',
      name: 'Gayrimenkul & İnşaat',
      icon: '▣',
      summary: 'Portföy yönetimi, müşteri takibi ve sözleşme süreçlerini kolaylaştırın.',
      headline: 'Portföyünüzdeki her ilanı hangi sistemde takip ediyorsunuz?',
      subline:
        'Müşteri sorguları, ilan yönetimi ve sözleşme süreçlerini tek bir akışta topluyoruz.',
      problems: [
        'Gelen talep formu sorguları tek noktada mı toplanıyor?',
        'İlan güncellemeleri birden fazla platformda manuel mi yapılıyor?',
        'Müşteri takip e-postaları kişiye özel mi gönderilmeli ama vakit mi yok?',
        'Kira/taksit hatırlatmaları manuel mi yapılıyor?',
        'Sözleşme süreci belge toplamakla mı geçiyor?',
      ],
      solutions: [
        { problem: 'Dağınık müşteri talepleri', outcome: 'Merkezi talep toplama ve otomatik yönlendirme' },
        { problem: 'Çoklu platform ilan yönetimi', outcome: 'Tek noktadan çoklu platform ilan senkronizasyonu' },
        { problem: 'Manuel kira hatırlatması', outcome: 'Otomatik kira hatırlatma ve gecikme bildirimi' },
        { problem: 'Manuel sözleşme takibi', outcome: 'Sözleşme son tarihi uyarısı ve yenileme akışı' },
      ],
      metaDescription:
        'Gayrimenkul ve inşaat sektörü için süreç otomasyonu. Portföy yönetimi, müşteri takibi ve sözleşme süreçlerini otomatikleştirin.',
    },
    {
      slug: 'konaklama',
      name: 'Otelcilik & Konaklama',
      icon: '▨',
      summary: 'Rezervasyon, misafir iletişimi ve operasyon raporlarını otomatikleştirin.',
      headline: 'Check-in öncesi misafirlere ulaşmak için kaç e-posta yazılıyor?',
      subline:
        'Misafir karşılama akışı, rezervasyon bildirimleri ve operasyon raporlamasını otomasyona geçiriyoruz.',
      problems: [
        'Rezervasyon onayları ve hatırlatmaları manuel mi gönderiliyor?',
        'Misafir öncesi bilgi formu e-postayla mı toplanıyor?',
        'Farklı kanallardan gelen rezervasyonlar tek noktada mı?',
        'Operasyon raporları sabah toplantısı için manuel mi hazırlanıyor?',
        'Misafir sonrası değerlendirme istekleri nasıl gönderiliyor?',
      ],
      solutions: [
        { problem: 'Manuel rezervasyon bildirimleri', outcome: 'Otomatik onay, hatırlatma ve karşılama akışı' },
        { problem: 'Dağınık kanal yönetimi', outcome: 'Merkezi rezervasyon yönetim sistemi' },
        { problem: 'Manuel sabah raporu', outcome: 'Günlük otomatik doluluk ve operasyon özeti' },
        { problem: 'Manuel değerlendirme isteği', outcome: 'Check-out sonrası otomatik yorum toplama akışı' },
      ],
      metaDescription:
        'Otel ve konaklama tesisleri için süreç otomasyonu. Rezervasyon yönetimi, misafir iletişimi ve raporlamayı otomatikleştirin.',
    },
    {
      slug: 'egitim',
      name: 'Eğitim & Kurumlar',
      icon: '▦',
      summary: 'Öğrenci kayıt, bildirim ve raporlama süreçlerini dijitalleştirin.',
      headline: 'Kayıt sezonu geldiğinde kaç kişi manuel form işliyor?',
      subline:
        'Öğrenci kayıt akışı, bildirimler ve kurumsal raporlamanın tamamını otomasyona geçiriyoruz.',
      problems: [
        'Kayıt formları e-posta veya kâğıtla mı toplanıyor?',
        'Ödeme hatırlatmaları manuel mi gönderiliyor?',
        'Veli bildirimleri kişiye özel ama zaman alıcı mı?',
        'Sınav ve program değişiklikleri SMS/e-postayla mı duyuruluyor?',
        'Dönem sonu raporları manuel olarak mı hazırlanıyor?',
      ],
      solutions: [
        { problem: 'Manuel kayıt formu işleme', outcome: 'Otomatik kayıt akışı ve onay bildirimi' },
        { problem: 'Manuel ödeme hatırlatması', outcome: 'Otomatik ödeme hatırlatma ve gecikme bildirimi' },
        { problem: 'Toplu veli bildirimleri', outcome: 'Segmentli otomatik bildirim sistemi' },
        { problem: 'Manuel dönem raporu', outcome: 'Otomatik dönem sonu performans raporu' },
      ],
      metaDescription:
        'Eğitim kurumları için süreç otomasyonu. Öğrenci kayıt yönetimi, veli bildirimleri ve raporlamayı otomatikleştirin.',
    },
  ],
};
