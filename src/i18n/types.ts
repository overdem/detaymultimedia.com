export type Lang = 'tr' | 'en';

export interface SectorData {
  slug: string;
  name: string;
  icon: string;
  summary: string;
  headline: string;
  subline: string;
  problems: string[];
  solutions: Array<{ problem: string; outcome: string }>;
  metaDescription: string;
}

export interface Translations {
  // Site-wide
  site: {
    name: string;
    tagline: string;
    description: string;
  };
  // Navigation
  nav: {
    solutions: string;
    allSolutions: string;
    services: string;
    references: string;
    about: string;
    contact: string;
    cta: string;
  };
  // Home page
  home: {
    heroLabel: string;
    heroTitle: string[];   // lines
    heroSub: string;
    ctaPrimary: string;
    ctaSecondary: string;
    statsLabel1: string;
    statsValue1: string;
    statsLabel2: string;
    statsValue2: string;
    statsLabel3: string;
    statsValue3: string;
    trustLabel: string;
    trustDesc: string;
    whyLabel: string;
    whyTitle: string;
    pains: Array<{ title: string; desc: string; stat: string }>;
    sectorsLabel: string;
    sectorsTitle: string;
    sectorsSub: string;
    sectorsMissing: string;
    sectorsMissingCta: string;
    processLabel: string;
    processTitle: string;
    processSub: string;
    steps: Array<{ number: string; title: string; desc: string; duration: string }>;
    referencesLabel: string;
    referencesTitle: string;
    referencesAll: string;
  };
  // CTA Banner
  ctaBanner: {
    label: string;
    title: string;
    subtitle: string;
    cta: string;
  };
  // Solutions hub
  solutionsHub: {
    label: string;
    title: string;
    subtitle: string;
    inspect: string;
    noSectorTitle: string;
    noSectorSub: string;
    noSectorCta: string;
  };
  // Sector page
  sectorPage: {
    label: string;       // "{name} Otomasyonu"
    ctaDemo: string;     // "Bu Sektör İçin Demo Al"
    problemsLabel: string;
    problemsTitle: string;
    solutionLabel: string;
    solutionTitle: string;
    solutionSub: string;
    techLabel: string;
    techTitle: string;
    techSub: string;
    referencesLabel: string;
    referencesTitle: string;
    noCaseText: string;
    noCaseCta: string;
    ctaSuffix: string;
    ctaSubtitle: string;
    ctaBtn: string;
    problemCol: string;
    outcomeCol: string;
    problemBadge: string;
    outcomeBadge: string;
  };
  // Services page
  services: {
    metaTitle: string;
    metaDesc: string;
    heroLabel: string;
    heroTitle: string;
    heroSub: string;
    categories: Array<{
      title: string;
      desc: string;
      useCases: string[];
      duration: string;
      sectors: string[];
    }>;
  };
  // References page
  references: {
    metaTitle: string;
    metaDesc: string;
    heroLabel: string;
    heroTitle: string;
    heroSub: string;
    statsBar: string;
    readMore: string;
    emptyCta: string;
  };
  // About page
  about: {
    metaTitle: string;
    metaDesc: string;
    heroLabel: string;
    heroTitle: string;
    heroSub: string;
    missionLabel: string;
    missionTitle: string;
    missionText: string;
    valuesLabel: string;
    values: Array<{ title: string; desc: string }>;
  };
  // Contact page
  contact: {
    metaTitle: string;
    metaDesc: string;
    heroLabel: string;
    heroTitle: string;
    heroSub: string;
    formName: string;
    formCompany: string;
    formSector: string;
    formSize: string;
    formProcess: string;
    formProcessPlaceholder: string;
    formPhone: string;
    formSubmit: string;
    formSuccess: string;
    sizes: string[];
    responseNote: string;
  };
  // Footer
  footer: {
    solutionsCol: string;
    companyCol: string;
    contactCol: string;
    tagline: string;
    blog: string;
    kvkk: string;
    privacy: string;
    terms: string;
    rights: string;
  };
  // Sectors list
  sectors: SectorData[];
}
