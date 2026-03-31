import type { Lang } from './types';
import { tr } from './tr';
import { en } from './en';

export const languages: Record<Lang, string> = {
  tr: 'Türkçe',
  en: 'English',
};

export const defaultLang: Lang = 'tr';

export const translations = { tr, en };

export function getLangFromURL(url: URL): Lang {
  const [, lang] = url.pathname.split('/');
  if (lang in translations) return lang as Lang;
  return defaultLang;
}

export function t(lang: Lang) {
  return translations[lang] ?? translations[defaultLang];
}

/** Mevcut sayfanın karşı dil versiyonunun URL'ini döndürür */
export function getAlternateLangURL(currentPath: string, targetLang: Lang): string {
  const segments = currentPath.split('/').filter(Boolean);
  if (segments.length === 0) return `/${targetLang}`;

  const [currentLang, ...rest] = segments;
  if (currentLang === 'tr' || currentLang === 'en') {
    return `/${targetLang}${rest.length ? '/' + rest.join('/') : ''}`;
  }
  return `/${targetLang}/${segments.join('/')}`;
}

export type { Lang };
