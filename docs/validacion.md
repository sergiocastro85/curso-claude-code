# Validación HU-01 a HU-17 · 2026-11-05

Método: revisión estática de src/, public/, astro.config.mjs y del HTML ya generado en dist/. El PO no tiene shell: **no se ejecutó `npm run build` ni `npx astro check`**, y no se sabe si dist/ corresponde al último código. Tampoco se midió Lighthouse, peso de imágenes ni vistas previas en LinkedIn/Facebook. Lo no comprobable se declara así y no se da por aprobado.

## Resumen

| HU | Veredicto | Evidencia | Qué falta |
| --- | --- | --- | --- |
| HU-01 | Aceptada | src/components/SeoHead.astro, src/layouts/BaseLayout.astro, src/site.ts (descargo exacto), dist/curso/06-mcp/index.html (og:image absoluta, og:url, twitter:card), skip-link y :focus-visible en global.css | Reserva: ejecutar build y astro check. El pie añade "licencia por confirmar" (resolver con el autor). |
| HU-02 | Aceptada | src/components/Hero.astro, src/pages/index.astro, TerminalTyping.astro (CSS puro, reduced-motion) | Nada. |
| HU-03 | Aceptada | src/pages/index.astro (10 tarjetas desde getCollection, filtro semana >= 1), ModuleCard.astro | Nada. |
| HU-04 | Parcial | index.astro (10 secciones en orden), PricingTable.astro ("Próximamente"), Faq.astro (6 `details`, "No" en oficial) | Enlace a LinkedIn real: sin PUBLIC_LINKEDIN_URL cae a https://www.linkedin.com/. Formulario no funcional (HU-05). JS < 30 KB: solo hay un script en línea pequeño, sin medir. |
| HU-05 | Parcial | SubscribeForm.astro: correo con etiqueta, casilla sin marcar y obligatoria, texto con finalidad y enlace a /privacidad, mensaje exacto, componente reutilizado en landing, /recursos y /premium | Sin servicio de email (PUBLIC_FORM_ACTION vacío): hoy el correo no se registra en ninguna parte y se redirige a /gracias igual. Sin manejo de error del servicio ni enlace de baja. `novalidate` anula la validación nativa: sin JS se envía sin autorización (el comentario del código dice lo contrario). |
| HU-06 | Parcial | src/pages/privacidad.astro (responsable, dato, finalidad, derechos, procedimiento, Ley 1581 y Decreto 1377, enlazada desde pie y formulario) | Correo de contacto real (hoy "[por definir antes de publicar]"), vigencia, fecha de actualización, proveedor de email como encargado ("por definir"). Revisión legal. |
| HU-07 | Aceptada | src/pages/gracias.astro; `noindex` presente en dist/gracias/index.html; excluida del sitemap | El mensaje "Te enviamos la bienvenida" es falso mientras HU-05 no envíe correos. |
| HU-08 | Aceptada | src/content/config.ts (esquema completo), 11 archivos en src/content/modulos con título y objetivo iguales a docs/temario.md | El fallo ante frontmatter inválido se deduce del esquema zod; no se probó. |
| HU-09 | Aceptada | src/pages/curso/index.astro (11 módulos ordenados, semana, objetivo, duración, enlaces; lista de 10 semanas) | Observación: las 10 barras salen todas llenas y no son progreso; sin guardado, fuera de alcance. |
| HU-10 | Aceptada | src/pages/curso/[slug].astro (getStaticPaths), ModuleLayout.astro (metadatos, fuentes, Anterior/Siguiente, ogImage, nota premium sin ocultar contenido), `pre{overflow-x:auto}` en global.css, 11 HTML en dist/curso/ | Nada. |
| HU-11 | Parcial | Módulos 00 a 04: las 4 secciones, 2 a 3 fuentes oficiales cada uno, sin afirmar afiliación | Laboratorios cortos (3 a 5 pasos): no se puede afirmar que llenen ~245 min semanales; 00 y 02 casi no avanzan VisitasAPI. Exactitud técnica sin verificar contra la documentación. |
| HU-12 | Parcial | Módulos 05 a 10: secciones y fuentes presentes; 10-proyecto-final tiene "Lista de entrega" (repo, build/test, README, CLAUDE.md y settings.json) | Mismo problema de profundidad; 06-mcp, 07 y 08 son muy breves y 06 tiene una sola fuente. |
| HU-13 | Parcial | public/og/default.png (legible, sin logos de Anthropic; menciona el descargo) | Solo hay imagen por defecto: ninguna por módulo. Peso y 1200x630 no medidos. Sin prueba en LinkedIn/Facebook (necesita URL pública). |
| HU-14 | Aceptada | src/pages/recursos.astro (CLAUDE.md, settings.json, subagente visibles con uso y licencia "por confirmar"; SubscribeForm para el PDF) | El PDF no existe; su entrega depende de HU-05. |
| HU-15 | Parcial | src/pages/sobre-mi.astro (historia, privacidad, CTA "Empieza gratis") | URL real de LinkedIn. |
| HU-16 | Parcial | src/pages/premium.astro (contenido del kit, qué sigue gratis, sin promesas laborales, "Próximamente" con formulario "avísame") | El "avísame" depende de HU-05. Botón de compra y compra de prueba no verificables (plataforma sin decidir). |
| HU-17 | Parcial | BaseLayout.astro carga el script de Cloudflare solo con PUBLIC_CF_ANALYTICS_TOKEN | Sin token ni despliegue no se puede comprobar analítica ni atribución UTM. |

Resultado: 8 Aceptadas, 9 Parciales, 0 Rechazadas. Aceptadas: HU-01, 02, 03, 07, 08, 09, 10, 14. Sin cambios de estado a "Aprobada" para las Parciales.

## Hallazgos transversales
- Ningún color fuera de tokens en src/ (los hexadecimales solo están en global.css). Sin logos de Anthropic; el nombre solo aparece en el descargo, el FAQ y la imagen OG.
- Sin archivo .env: LinkedIn, contacto, servicio de email, analítica y compra están vacíos. Es el origen de casi todos los Parciales.
- ARQUITECTURA.md sigue diciendo `/curso/modulo-N`; el sitio usa los slugs de archivo (decisión ya registrada).

## Pendientes priorizados

Bloqueantes de lanzamiento (Must)
1. HU-05: elegir y conectar el servicio de email (verificar y citar límites vigentes del plan gratuito), manejo de error, enlace de baja. Decisión del autor pendiente.
2. HU-05: quitar `novalidate` o forzar la autorización sin JS (fallo de cumplimiento de la Ley 1581). Mientras no haya servicio, /gracias y la copy no deben prometer un correo que no se envía.
3. HU-06: definir correo de contacto, vigencia, fecha de actualización y nombre del proveedor; revisión legal.
4. Configurar PUBLIC_LINKEDIN_URL (cierra HU-04 y HU-15) y reemplazar `site` por el dominio real.
5. Ejecutar `npm run build` y `npx astro check` y registrar el resultado (cierra la reserva de HU-01).

Calidad del producto (Must)
6. HU-11 y HU-12: ampliar laboratorios para que cuadren con ~245 min semanales y avancen VisitasAPI; verificar exactitud técnica y fuentes (06-mcp con una sola fuente). Dividir por módulos, máximo 3 sesiones por historia.

Después (Should/Could)
7. HU-13: imágenes OG por módulo; medir peso; probar en LinkedIn Post Inspector y Depurador de Facebook al tener URL pública.
8. HU-16: decidir plataforma de pago tras verificar comisiones vigentes; hacer compra de prueba. Mantener "Próximamente" hasta tener lista de correos y kit probado.
9. HU-17: crear token de Cloudflare Web Analytics y comprobar atribución UTM tras desplegar.
10. Medir Lighthouse (meta >= 95) y JavaScript de la landing tras el primer despliegue de vista previa.
11. Barra de 10 semanas en /curso: dejarla decorativa o quitarla (hoy parece progreso al 100 %).
