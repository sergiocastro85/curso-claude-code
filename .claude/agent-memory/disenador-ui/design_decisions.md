---
name: design-decisions
description: Decisiones de diseño del sitio (paleta, tipografía, tema) y su motivo
metadata:
  type: project
---

- Oscuro por defecto, claro vía prefers-color-scheme y [data-theme]. Acento único cobre: #ff8a3d (oscuro) / #b34a00 (claro). **Why:** identidad "terminal editorial", distinta de Anthropic; ambos pasan AA.
- Fuentes del sistema (mono + sans), sin web fonts. **Why:** meta Lighthouse >= 95 y LCP < 2 s en móvil.
- Tailwind v4 con `@theme inline` que referencia variables CSS (`--color-*: initial` deja solo colores de la marca). **Why:** que el cambio de tema solo toque las variables.
- Favicon: `>_` en acento sobre fondo cálido. **Why:** marca propia, sin referencias a Anthropic.
- Valores completos en docs/design-system.md y src/styles/global.css.
