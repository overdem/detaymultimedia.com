// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import vercel from '@astrojs/vercel/serverless';

export default defineConfig({
  output: 'server',
  adapter: vercel({
    functionPerRoute: true
  }),
  site: 'https://detaymultimedia.com',
  integrations: [sitemap()],
});
