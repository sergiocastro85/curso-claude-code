# Arquitectura · Landing y sitio del curso "Claude Code desde cero"

> Documento de arquitectura para publicar el curso de 10 semanas como sitio web gratuito, compartible en LinkedIn y Facebook, con un modelo de monetización freemium.
> Autor: Kevin Castro Gómez · Versión 1.0 · 18 de octubre de 2026

---

## 1. Decisión en una línea

**Astro + Tailwind CSS, publicado gratis en Cloudflare Pages**, con el contenido del curso en archivos Markdown dentro del repositorio, captura de correos con un servicio de email gratuito y venta del "Kit Premium" mediante una plataforma de pagos externa.

---

## 2. Por qué Astro

| Criterio | Astro | Next.js | Docusaurus / Starlight solo |
| --- | --- | --- | --- |
| Velocidad de la landing | Excelente: HTML estático, cero JavaScript por defecto | Buena, pero envía más JS | Buena |
| Contenido en Markdown | Nativo (Content Collections con validación) | Requiere configuración (MDX) | Nativo |
| Landing con diseño libre | Total | Total | Limitado al tema de documentación |
| Hosting gratis | Cualquier hosting estático | Mejor en Vercel | Cualquier hosting estático |
| Curva de aprendizaje | Baja (HTML + componentes `.astro`) | Media (React, App Router) | Baja |
| SEO y vista previa en redes | Muy bueno (HTML listo para los rastreadores) | Muy bueno | Bueno |

**Conclusión:** Astro da lo mejor de los dos mundos: una landing llamativa y totalmente personalizada, más páginas de módulos generadas desde Markdown. Si más adelante quieres un área de documentación tipo manual, se agrega **Starlight** (el tema de documentación oficial de Astro) en `/curso` sin cambiar de framework.

### Hosting gratuito

| Opción | Ventajas | Cuándo elegirla |
| --- | --- | --- |
| **Cloudflare Pages** (recomendada) | Ancho de banda generoso, CDN global, analítica sin cookies, despliegue automático desde GitHub | Opción por defecto |
| GitHub Pages | Todo en GitHub, cero cuentas extra | Si quieres lo más simple |
| Netlify / Vercel | Formularios y funciones serverless | Si necesitas lógica de servidor |

> Revisa los límites actuales del plan gratuito de cada proveedor antes de publicar: cambian con el tiempo.

---

## 3. Mapa del sitio

```text
/                       Landing page (embudo principal)
/curso                  Índice del curso: 10 semanas, progreso
/curso/modulo-1 … 9     Una página por módulo (teoría, laboratorio, reto, preguntas)
/curso/proyecto-final   Semana 10
/recursos               Plantillas gratuitas: CLAUDE.md, settings.json, agentes
/premium                Página de venta del Kit Premium
/sobre-mi               Autor: historia, por qué creó el curso
/gracias                Confirmación tras suscribirse o comprar
/privacidad             Política de tratamiento de datos (obligatoria)
```

---

## 4. Landing page: estructura y copy

La landing es un embudo: cada sección empuja a la siguiente y todas llevan al mismo CTA principal (**"Empieza gratis"** → suscripción por correo → acceso al curso).

| # | Sección | Objetivo | Contenido propuesto |
| --- | --- | --- | --- |
| 1 | **Hero** | Captar en 3 segundos | Titular: *"Domina Claude Code en 10 semanas, con 40 minutos al día"*. Subtítulo: *"El curso práctico en español para programar con IA sin dejar de pensar como desarrollador."* CTA primario + CTA secundario "Ver temario" |
| 2 | **Problema** | Identificación | "Usas la IA pero no entiendes lo que genera", "Copias y pegas sin poder defender tu código" |
| 3 | **Método** | Diferenciación | La *regla de oro*: predecir, revisar el diff, explicar. Ritmo L–V 40 min, sábado 20, domingo 15 |
| 4 | **Temario** | Valor concreto | 9 tarjetas de módulos + proyecto final, cada una con un resultado tangible |
| 5 | **Proyecto real** | Prueba | VisitasAPI en .NET 8 con Clean Architecture: lo que tendrás en tu GitHub al final |
| 6 | **Para quién es** | Filtro | Estudiantes, técnicos y desarrolladores junior en LATAM; requisitos mínimos |
| 7 | **Sobre el autor** | Confianza | Sergio Andrés Castro Cano, ingeniero de sistemas con más de 5 años en desarrollo y soporte de soluciones |
| 8 | **Gratis vs. Premium** | Monetización | Tabla comparativa (ver sección 7) |
| 9 | **FAQ** | Objeciones | ¿Necesito pagar Claude? ¿Sirve en Windows? ¿Cuánto tiempo? ¿Es oficial de Anthropic? (No) |
| 10 | **CTA final** | Conversión | Formulario de correo + botón a LinkedIn |

### Lineamientos visuales (los desarrolla el agente de diseño)

- **Estética:** "terminal editorial": fondo oscuro cálido, tipografía monoespaciada para títulos de módulos, acentos de un solo color vibrante (ej. naranja cobre o verde terminal).
- **Elementos llamativos:** animación de "escritura" en el hero simulando una sesión de terminal; tarjetas de módulo con número grande; barra de progreso de 10 semanas.
- **Accesibilidad:** contraste AA, navegación con teclado, `prefers-reduced-motion` para desactivar animaciones.
- **Modo claro y oscuro** con tokens de color en variables CSS.
- **Móvil primero:** la mayoría del tráfico desde LinkedIn y Facebook llega desde el celular.

> **Marca:** no uses el logo ni la identidad visual de Anthropic o Claude. El curso es independiente; diseña una marca propia.

---

## 5. Estructura del repositorio

```text
curso-claude-code/
├── .claude/
│   ├── agents/
│   │   ├── po-curso.md              Product Owner
│   │   ├── disenador-ui.md          Diseño UI/UX
│   │   └── desarrollador-astro.md   Desarrollo
│   └── settings.json                Permisos del proyecto
├── CLAUDE.md                        Reglas del proyecto para Claude Code
├── docs/
│   ├── ARQUITECTURA.md              Este documento
│   ├── backlog.md                   Historias de usuario (lo mantiene el PO)
│   └── design-system.md             Tokens y componentes (lo mantiene diseño)
├── public/
│   ├── og/                          Imágenes 1200×630 para redes
│   └── favicon.svg
├── src/
│   ├── content/
│   │   ├── config.ts                Esquemas de las colecciones
│   │   └── modulos/
│   │       ├── 00-como-usar.md
│   │       ├── 01-introduccion.md
│   │       ├── …
│   │       └── 10-proyecto-final.md
│   ├── components/
│   │   ├── Hero.astro
│   │   ├── TerminalTyping.astro
│   │   ├── ModuleCard.astro
│   │   ├── PricingTable.astro
│   │   ├── Faq.astro
│   │   ├── SubscribeForm.astro
│   │   └── SeoHead.astro            Meta tags y Open Graph
│   ├── layouts/
│   │   ├── BaseLayout.astro
│   │   └── ModuleLayout.astro
│   ├── pages/
│   │   ├── index.astro
│   │   ├── curso/index.astro
│   │   ├── curso/[slug].astro
│   │   ├── recursos.astro
│   │   ├── premium.astro
│   │   ├── sobre-mi.astro
│   │   ├── gracias.astro
│   │   └── privacidad.astro
│   └── styles/global.css            Tokens de diseño
├── astro.config.mjs
└── package.json
```

### Esquema de contenido (Content Collections)

Cada módulo es un `.md` con frontmatter validado. Así el contenido del documento del curso se migra copiando cada sección a su archivo.

```ts
// src/content/config.ts
import { defineCollection, z } from 'astro:content';

const modulos = defineCollection({
  type: 'content',
  schema: z.object({
    numero: z.number(),
    titulo: z.string(),
    semana: z.number(),
    objetivo: z.string(),
    duracionMinutos: z.number().default(245),
    premium: z.boolean().default(false),   // material extra solo para el kit
    fuentes: z.array(z.object({ titulo: z.string(), url: z.string().url() })),
    ogImage: z.string().optional(),
  }),
});

export const collections = { modulos };
```

```markdown
---
numero: 1
titulo: "Introducción a Claude Code"
semana: 1
objetivo: "Instalar Claude Code, entender cómo trabaja y crear el esqueleto de VisitasAPI."
fuentes:
  - titulo: "Overview"
    url: "https://code.claude.com/docs/en/overview"
---

## Conceptos clave
…
```

### Flujo de datos

```text
Markdown (src/content/modulos)
        │  build (astro build)
        ▼
HTML estático + CSS mínimo ──► Cloudflare Pages (CDN)
        │                              │
        │                              ├──► Visitante desde LinkedIn / Facebook
        │                              │
Formulario de correo ──────────► Servicio de email (lista + secuencia de bienvenida)
Botón "Comprar Kit" ───────────► Plataforma de pago externa ──► Entrega del ZIP / acceso
Analítica sin cookies ─────────► Cloudflare Web Analytics
```

No hay base de datos ni servidor propio: **costo de infraestructura $0**.

---

## 6. Compartir en LinkedIn y Facebook

### 6.1 Vista previa perfecta (Open Graph)

Cada página genera sus etiquetas desde `SeoHead.astro`:

```html
<meta property="og:title" content="Módulo 6 · MCP con Claude Code" />
<meta property="og:description" content="Conecta Claude a la documentación de .NET, GitHub y tu base de datos." />
<meta property="og:image" content="https://tudominio.dev/og/modulo-6.png" />
<meta property="og:url" content="https://tudominio.dev/curso/modulo-6" />
<meta property="og:type" content="article" />
<meta name="twitter:card" content="summary_large_image" />
```

- Imagen **1200 × 630 px**, texto grande y legible en el celular, una por módulo.
- Antes de publicar, valida la vista previa con **LinkedIn Post Inspector** y el **Depurador de contenido compartido de Facebook** (también fuerzan a refrescar la caché).
- Agrega parámetros UTM a cada enlace para saber qué red trae más suscriptores: `?utm_source=linkedin&utm_medium=post&utm_campaign=modulo-6`.

### 6.2 Plan de publicación (12 semanas)

| Semana | LinkedIn | Facebook (grupos de programación LATAM) |
| --- | --- | --- |
| 0 | Anuncio: "Voy a publicar gratis un curso de Claude Code en español" + enlace a la landing | Mismo anuncio en 2–3 grupos donde se permita |
| 1–9 | Un **carrusel PDF** por módulo (6–8 diapositivas: problema, concepto, ejemplo, enlace) | Resumen corto + imagen del módulo |
| 10 | Caso real: "Así quedó VisitasAPI" con capturas y repositorio | Video corto mostrando el flujo |
| 11 | Lanzamiento del Kit Premium con precio de lanzamiento | Oferta en grupos donde se permita promoción |

> El carrusel en PDF suele tener más alcance que un enlace externo en LinkedIn. Pon el enlace en el primer comentario si notas que tus publicaciones con enlace llegan a menos personas.

---

## 7. Monetización (modelo freemium)

El curso **completo es gratis**: genera confianza, audiencia y posicionamiento profesional. El dinero llega de productos complementarios.

| Producto | Formato | Precio sugerido (validar) | Herramienta |
| --- | --- | --- | --- |
| **Curso base** | Web abierta | Gratis (a cambio del correo para el PDF descargable) | Servicio de email con plan gratuito (MailerLite, Brevo o Buttondown) |
| **Kit Premium** | ZIP: plugin `visitas-toolkit`, plantillas de CLAUDE.md y `settings.json`, 5 subagentes y 5 skills extra, repositorio final con historial de commits, certificado de finalización | USD 9–19 (lanzamiento) | Hotmart, Lemon Squeezy o Gumroad |
| **Mentoría 1:1** | Videollamada de 45 min para revisar tu configuración o proyecto | USD 15–30 | Cal.com o Calendly + enlace de pago (Mercado Pago, Wompi) |
| **Taller para equipos** | 2 sesiones en vivo para empresas o universidades | A convenir | Facturación directa |
| **Apoyo voluntario** | Botón "Invítame un café" | Libre | Ko-fi o Buy Me a Coffee |

### Tabla para la landing: Gratis vs. Premium

| | Gratis | Kit Premium |
| --- | --- | --- |
| 10 semanas de contenido | ✔ | ✔ |
| Laboratorios y retos | ✔ | ✔ |
| PDF descargable del curso | ✔ (con correo) | ✔ |
| Plugin `visitas-toolkit` listo para instalar | | ✔ |
| Subagentes y skills adicionales | | ✔ |
| Repositorio final comentado | | ✔ |
| Certificado de finalización | | ✔ |

### Consideraciones de pago desde Colombia

- **Hotmart** es muy usada en LATAM para infoproductos y acepta medios locales.
- **Lemon Squeezy** y **Gumroad** actúan como vendedor registrado (manejan impuestos internacionales) y cobran en dólares.
- **Mercado Pago** y **Wompi** sirven para enlaces de pago en pesos colombianos (mentorías).
- Revisa las comisiones vigentes y tus obligaciones tributarias (RUT, facturación electrónica ante la DIAN si superas los topes) antes del lanzamiento.

### Embudo de email (automatizado)

1. **Día 0:** bienvenida + PDF del curso + enlace al Módulo 1.
2. **Días 7, 14, 21…:** un correo por semana con el módulo siguiente y un tip práctico.
3. **Semana 10:** felicitación + oferta del Kit Premium con descuento por 72 horas.
4. **Semana 12:** invitación a mentoría.

---

## 8. Legal y ética (Colombia)

- **Descargo visible en el pie de página:** *"Curso independiente. No está afiliado, patrocinado ni avalado por Anthropic. Claude y Claude Code son marcas de Anthropic."*
- **Contenido original:** explica con tus palabras y enlaza la documentación oficial; no copies textos completos de la documentación.
- **Habeas Data (Ley 1581 de 2012):** si recoges correos necesitas una política de tratamiento de datos publicada (`/privacidad`), una casilla de autorización en el formulario y un mecanismo para darse de baja.
- **Licencia del contenido gratuito:** sugerida CC BY-NC 4.0 (pueden compartirlo citándote, sin uso comercial).
- **Precios en la landing:** muestra el valor final y la moneda.

---

## 9. Calidad y rendimiento

| Métrica | Meta |
| --- | --- |
| Lighthouse Performance (móvil) | ≥ 95 |
| Lighthouse Accessibility | ≥ 95 |
| Largest Contentful Paint | < 2,0 s |
| JavaScript en la landing | < 30 KB |
| Peso de la imagen OG | < 300 KB |

Pruebas: `astro check` (tipos y esquemas), Lighthouse CI en cada pull request y revisión manual en el celular.

---

## 10. Despliegue

1. Crear el proyecto: `npm create astro@latest curso-claude-code` y agregar Tailwind con `npx astro add tailwind`.
2. Subir el repositorio a GitHub.
3. En Cloudflare Pages: conectar el repositorio, comando de build `npm run build`, carpeta de salida `dist`.
4. Cada `git push` a `main` publica automáticamente; cada pull request genera una URL de vista previa.
5. (Opcional) Dominio propio `.dev` o `.co` apuntando a Cloudflare.

---

## 11. Equipo de agentes (Claude Code)

Los tres subagentes viven en `.claude/agents/` y trabajan en cadena. Tú eres quien aprueba en cada paso.

```text
   Tú (idea)
     │
     ▼
  po-curso ──────────► docs/backlog.md   (historias + criterios de aceptación)
     │
     ▼
  disenador-ui ──────► docs/design-system.md + estilos y maquetas de secciones
     │
     ▼
  desarrollador-astro ► código, build, pruebas, pull request
     │
     ▼
  po-curso ──────────► valida contra los criterios de aceptación
```

| Agente | Responsabilidad | Puede editar | No puede |
| --- | --- | --- | --- |
| `po-curso` | Visión, backlog, priorización, copy, monetización, validación final | `docs/` | Tocar código |
| `disenador-ui` | Sistema de diseño, componentes visuales, accesibilidad, imágenes OG | `docs/design-system.md`, `src/styles/`, `src/components/` (solo marcado y estilos) | Lógica, configuración, despliegue |
| `desarrollador-astro` | Implementación, contenido, SEO técnico, rendimiento, build | Todo el proyecto salvo `docs/backlog.md` | Hacer `push` o desplegar sin tu aprobación |

**Cómo usarlos:**

```text
@po-curso escribe las historias de usuario de la landing con criterios de aceptación
@disenador-ui diseña el Hero y la sección de temario según el backlog
@desarrollador-astro implementa la historia HU-01 y ejecuta el build
@po-curso valida HU-01 contra sus criterios de aceptación
```

---

## 12. CLAUDE.md sugerido para el repositorio

```markdown
# Curso Claude Code · sitio web
Astro + Tailwind, sitio estático publicado en Cloudflare Pages.

## Comandos
- Desarrollo: `npm run dev`
- Build: `npm run build` (debe terminar sin errores antes de cada commit)
- Verificación: `npx astro check`

## Reglas
- Contenido en español, tono cercano y directo.
- Los módulos viven en src/content/modulos y siguen el esquema de src/content/config.ts.
- Nada de JavaScript en el cliente salvo en componentes con `client:*` justificados.
- Colores solo mediante los tokens de src/styles/global.css.
- Nunca usar logos ni identidad visual de Anthropic.
- IMPORTANTE: no hacer git push ni desplegar sin aprobación explícita.
```

---

## 13. Plan de trabajo (adaptado a 40 min/día)

| Sprint | Duración | Entregable |
| --- | --- | --- |
| 1 | 1 semana | Backlog del PO, marca y sistema de diseño |
| 2 | 1 semana | Landing completa publicada en una URL de vista previa |
| 3 | 1 semana | Páginas de los 10 módulos migradas desde el documento del curso |
| 4 | 1 semana | Formulario de correo, `/privacidad`, imágenes OG, analítica |
| 5 | 1 semana | Página `/premium` y Kit Premium empaquetado |
| 6 | Continuo | Publicaciones semanales en LinkedIn y Facebook |

---

## 14. Checklist de lanzamiento

- [ ] Lighthouse ≥ 95 en móvil
- [ ] Vista previa correcta en LinkedIn Post Inspector y en el depurador de Facebook
- [ ] Formulario de correo con autorización de datos funcionando
- [ ] Política de privacidad publicada
- [ ] Descargo de no afiliación en el pie de página
- [ ] Enlaces con UTM listos
- [ ] Primer carrusel de LinkedIn preparado
- [ ] Kit Premium probado con una compra de prueba
