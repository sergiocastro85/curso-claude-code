// Sin @ts-check: @tailwindcss/vite trae su propia versión de Vite y sus tipos chocan con los de Astro
// (solo afecta al tipado; en ejecución funciona igual).
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';

// PENDIENTE: cambiar `site` por el dominio real antes de publicar.
// Se usa para URLs canónicas, Open Graph y sitemap.
export default defineConfig({
  site: 'https://curso-claude-code.pages.dev',
  integrations: [sitemap({ filter: (page) => !page.includes('/gracias') })],
  vite: {
    plugins: [tailwindcss()],
  },
});
