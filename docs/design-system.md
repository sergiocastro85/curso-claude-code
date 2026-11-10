# Sistema de diseño · "terminal editorial"

Marca propia, independiente. Sin logo, colores ni identidad de Anthropic o Claude. Fuente de verdad de los valores: `src/styles/global.css`.

## Principios
- Móvil primero (diseñar a 375 px, ampliar después).
- Un solo acento (cobre/naranja). Nada de degradados ni iconos decorativos.
- Títulos de módulo y etiquetas en mono; cuerpo en sans del sistema (cero fuentes web: rendimiento).
- Solo tokens; prohibidos colores sueltos en componentes.

## Color
| Token | Oscuro (defecto) | Claro | Uso |
| --- | --- | --- | --- |
| `--bg` | #1a1613 | #faf5ee | Fondo |
| `--surface` / `--surface-2` | #241e19 / #2e2721 | #f1e9de / #e8ddcf | Tarjetas, bloques |
| `--border` | #4a3f36 | #b9a995 | Bordes (3:1 mín. en controles) |
| `--text` | #f3ebe1 | #1f1a16 | Texto |
| `--text-muted` | #bfb2a3 | #5a4f44 | Texto secundario |
| `--accent` | #ff8a3d | #b34a00 | CTA, enlaces, números |
| `--accent-hover` | #ffa466 | #8f3b00 | Hover |
| `--on-accent` | #1a1613 | #ffffff | Texto sobre acento |
| `--focus` | #ffd0a8 | #7a2f00 | Anillo de foco |
| `--success` / `--danger` | #8fd694 / #ff8f84 | #1d6b2a / #a3261b | Mensajes de formulario |
| `--code-bg` | #120f0d | #2a231d | Bloques de código |

Contraste calculado (WCAG): texto/fondo y muted/fondo >= 7:1 en oscuro; acento sobre fondo ~7,7:1 en oscuro y ~5:1 en claro; `--on-accent` sobre `--accent` ~7,7:1 oscuro y ~5,4:1 claro. Todo AA. Verificar de nuevo si se cambia un valor.

Modo: oscuro por defecto; claro automático con `prefers-color-scheme: light`; se fuerza con `<html data-theme="light|dark">`. En Tailwind: `bg-bg`, `bg-surface`, `text-muted`, `bg-accent text-on-accent`, `border-border`, `bg-code`.

## Tipografía
- `--font-mono` (ui-monospace, Cascadia Code, Menlo, Consolas): h1-h3 de módulos, números, etiquetas, terminal. Clase `.font-title` / `font-mono`.
- `--font-sans` (system-ui): cuerpo y UI.
- Escala: xs 13, sm 15, base 17, lg 20, xl 26, 2xl fluido (30-52), display fluido (64-112) para el número de módulo. Interlineado cuerpo 1,65; títulos 1,15. Medida máx. `--measure` 65ch.

## Espaciado, radios, sombras
- Espaciado base 4 px: `--space-1..24` (4, 8, 12, 16, 24, 32, 48, 64, 96). Contenedor `--container` 68rem (`.container`, margen 1rem en móvil).
- Radios: sm 4, md 8 (botones, inputs), lg 14 (tarjetas). Sombras `--shadow-sm/md`, solo en tarjetas elevadas; en oscuro se prefiere borde.

## Componentes y estados (lo implementa el desarrollador)
- **Botón primario:** `bg-accent text-on-accent`, mono, mín. 48 px de alto; hover `--accent-hover`; foco anillo `--focus`; deshabilitado opacidad .5. **Secundario:** borde `--border`, texto `--text`.
- **Hero:** titular en mono con cursor `.cursor`; bloque terminal (`pre`, `--code-bg`) con líneas que se "escriben" (CSS, sin JS); con reduced-motion se muestra el texto completo estático. Microcopy bajo los CTA.
- **ModuleCard:** número enorme (`--text-display`, mono, `--accent`), título mono, objetivo en muted, semana como etiqueta. Toda la tarjeta es un enlace; hover: borde `--accent`; foco visible. Estado premium: etiqueta de texto "Premium" (no solo color).
- **Barra de 10 semanas:** 10 segmentos (`--surface-2`, activos `--accent`), con texto "Semana N de 10" para lectores de pantalla.
- **PricingTable:** tabla semántica `<table>` con `<th scope>`; marcas con texto ("Incluido"/"No incluido") además del símbolo. Precio solo con valor y moneda; si no hay, "Próximamente".
- **Faq:** `<details>/<summary>`, marcador propio, foco visible, sin JS.
- **SubscribeForm:** etiqueta visible sobre el campo, casilla de autorización sin marcar con enlace a /privacidad, error en `--danger` con texto e `aria-live`, éxito en `--success`. Borde de input `--border` (3:1).
- **Código:** `pre` con scroll horizontal, sin desbordar la página.

## Accesibilidad
- Contraste AA en ambos modos; foco `:focus-visible` global de 3 px.
- Enlace de salto `.skip-link`; objetivos táctiles >= 44 px.
- `prefers-reduced-motion`: se anulan animaciones, cursor parpadeante y scroll suave.
- Nunca transmitir información solo con color. Imágenes con `alt`; decorativas con `alt=""`.

## Marca
Favicon propio: `public/favicon.svg` (prompt de terminal `>_` en acento sobre fondo cálido). Descargo de no afiliación obligatorio en el pie.

## Pendiente de diseño
Componentes `.astro`, imágenes OG (1200x630, < 300 KB, `public/og/`) y revisión de accesibilidad real con Lighthouse.
