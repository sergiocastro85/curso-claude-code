// Datos globales del sitio. Los valores sensibles o que cambian vienen de variables de entorno
// (ver .env.example). Nada de claves en el código.
const env = import.meta.env;

export const SITE = {
  nombre: 'Claude Code desde cero',
  descripcion:
    'Aprende a programar con IA en 40 minutos al día. Proyecto real VisitasAPI en .NET 8. Gratis y en español.',
  autor: 'Kevin Castro Gómez',
  ogDefault: '/og/default.png',
  linkedin: (env.PUBLIC_LINKEDIN_URL as string | undefined) || 'https://www.linkedin.com/',
  contacto: (env.PUBLIC_CONTACT_EMAIL as string | undefined) || '',
  // Endpoint del servicio de email (MailerLite, Brevo o Buttondown). Vacío = modo sin servicio.
  formAction: (env.PUBLIC_FORM_ACTION as string | undefined) || '',
  // Token de Cloudflare Web Analytics (sin cookies). Vacío = no se carga analítica.
  analyticsToken: (env.PUBLIC_CF_ANALYTICS_TOKEN as string | undefined) || '',
  // Enlace de compra del Kit Premium. Vacío = "Próximamente".
  premiumBuyUrl: (env.PUBLIC_PREMIUM_BUY_URL as string | undefined) || '',
  descargo:
    'Curso independiente. No está afiliado, patrocinado ni avalado por Anthropic. Claude y Claude Code son marcas de Anthropic.',
};
