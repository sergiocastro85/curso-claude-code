# Claude Code desde cero · sitio web

Sitio estático (Astro + Tailwind) del curso gratuito de 10 semanas "Claude Code desde cero", en español.
Se publica en Cloudflare Pages. Arquitectura completa en [docs/ARQUITECTURA.md](docs/ARQUITECTURA.md).

> Curso independiente. No está afiliado, patrocinado ni avalado por Anthropic.

## Requisitos
Node.js 22 (ver `.nvmrc`).

## Comandos
| Comando | Qué hace |
| --- | --- |
| `npm ci` | Instala dependencias |
| `npm run dev` | Servidor local |
| `npm run build` | Genera `dist/` (debe pasar antes de cada commit) |
| `npx astro check` | Verifica tipos y esquemas |

## Configuración
Copia `.env.example` a `.env` y completa las variables. `.env` nunca se sube al repositorio.
En Cloudflare Pages las mismas variables se configuran en el panel del proyecto.

## Estructura
- `src/content/modulos/`: los módulos del curso en Markdown (esquema en `src/content/config.ts`).
- `src/pages`, `src/components`, `src/layouts`: rutas y piezas del sitio.
- `src/styles/global.css`: tokens de diseño.
- `docs/`: backlog, sistema de diseño y validación.
- `.claude/`: agentes (`po-curso`, `disenador-ui`, `desarrollador-astro`) y permisos de Claude Code.

## Flujo de trabajo
Rama por historia (`feat/hu-05-formulario`) → pull request → CI verde → merge a `main`.
Cada push a `main` despliega en Cloudflare Pages, por eso `main` se protege y se revisa por PR.
