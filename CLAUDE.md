# Curso Claude Code · sitio web
Astro + Tailwind, sitio estático publicado en Cloudflare Pages. Arquitectura completa en @docs/ARQUITECTURA.md.

## Comandos
- Desarrollo: `npm run dev`
- Build: `npm run build` (debe terminar sin errores antes de cada commit)
- Verificación: `npx astro check`

## Equipo de agentes
- `po-curso`: backlog, copy, monetización y validación (solo escribe en docs/).
- `disenador-ui`: sistema de diseño, estilos, componentes visuales, imágenes OG.
- `desarrollador-astro`: implementación, contenido, SEO, rendimiento.
Flujo: PO → diseño → desarrollo → PO valida.

## Reglas
- Contenido en español, tono cercano y directo.
- Los módulos viven en src/content/modulos y siguen el esquema de src/content/config.ts.
- Nada de JavaScript en el cliente salvo componentes con `client:*` justificados.
- Colores solo mediante los tokens de src/styles/global.css.
- Nunca usar logos ni identidad visual de Anthropic; el pie de página lleva el descargo de no afiliación.
- Formularios con autorización de datos (Ley 1581 de 2012).
- IMPORTANTE: no hacer git push ni desplegar sin aprobación explícita.
