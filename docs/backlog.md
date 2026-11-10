# Backlog · Sitio "Claude Code desde cero"

Estimación en sesiones de 40 min (máx. 3 por historia). Estados: Pendiente, En diseño, En desarrollo, En validación, Aprobada.
Prioridad del roadmap: landing, captura de correo, módulos, premium.
Criterios transversales (aplican a todas): `npm run build` y `npx astro check` sin errores; colores solo por tokens; contenido en español; sin logos de Anthropic; móvil primero.

## Resumen

| ID | Título | MoSCoW | Ses. | Estado |
| --- | --- | --- | --- | --- |
| HU-01 | Base del sitio: layout, SeoHead y pie con descargo | Must | 3 | Aprobada |
| HU-02 | Landing: hero, problema, método | Must | 2 | Aprobada |
| HU-03 | Landing: temario, proyecto real, para quién es | Must | 2 | Aprobada |
| HU-04 | Landing: sobre Kevin, gratis vs premium, FAQ, CTA final | Must | 3 | En desarrollo (Parcial) |
| HU-05 | Formulario de correo con autorización Ley 1581 | Must | 3 | En desarrollo (Parcial) |
| HU-06 | Página /privacidad | Must | 2 | En desarrollo (Parcial) |
| HU-07 | Página /gracias | Must | 1 | Aprobada |
| HU-08 | Colección de módulos y esquema | Must | 2 | Aprobada |
| HU-09 | Página /curso (índice) | Must | 2 | Aprobada |
| HU-10 | Página /curso/[slug] (plantilla de módulo) | Must | 3 | Aprobada |
| HU-11 | Contenido de módulos 00 a 04 | Must | 3 | En desarrollo (Parcial) |
| HU-12 | Contenido de módulos 05 a 10 | Must | 3 | En desarrollo (Parcial) |
| HU-13 | Imágenes Open Graph | Should | 2 | En desarrollo (Parcial) |
| HU-14 | Página /recursos | Should | 2 | Aprobada |
| HU-15 | Página /sobre-mi | Should | 1 | En desarrollo (Parcial) |
| HU-16 | Página /premium | Should | 2 | En desarrollo (Parcial) |
| HU-17 | Analítica sin cookies y UTM | Could | 1 | En desarrollo (Parcial) |

Validación del 2026-11-05 (revisión estática de src/, public/, astro.config.mjs y dist/): ver docs/validacion.md. "Aprobada" = Aceptada; "En desarrollo (Parcial)" = faltan criterios.

Nota de coherencia: ARQUITECTURA.md sección 3 usa `/curso/modulo-N`, pero el encargo y la estructura de contenido usan slugs `00-como-usar`, `01-...`, `10-proyecto-final`. **Decisión:** se usan los slugs de archivo (ver docs/temario.md). Actualizar ARQUITECTURA.md queda pendiente del autor (el PO no edita ese archivo sin aprobación).

---

## HU-01 · Base del sitio: layout, SeoHead y pie con descargo
Como visitante quiero ver páginas con vista previa correcta al compartirlas y un pie claro de no afiliación para confiar en que el curso es independiente.
- Dado cualquier página, Cuando se inspecciona el HTML, Entonces contiene `<title>`, meta description, canonical, `og:title`, `og:description`, `og:image` (URL absoluta), `og:url`, `og:type`, `twitter:card=summary_large_image`.
- Dado que una página no define imagen, Cuando se renderiza, Entonces usa una imagen OG por defecto.
- Dado cualquier página, Cuando se llega al pie, Entonces aparece el texto exacto: "Curso independiente. No está afiliado, patrocinado ni avalado por Anthropic. Claude y Claude Code son marcas de Anthropic."
- Dado el pie, Entonces hay enlaces a /privacidad, /recursos, /sobre-mi.
- Dado todo el sitio, Entonces no hay logo ni identidad visual de Anthropic o Claude.
- Dado la navegación, Cuando se usa solo teclado, Entonces todos los enlaces son alcanzables y con foco visible.
Prioridad: Must · 3 sesiones · Aprobada (2026-11-05; reserva: build/astro check no ejecutados por el PO)

## HU-02 · Landing: hero, problema, método
Como visitante que llega de LinkedIn o Facebook quiero entender en 3 segundos qué ofrece el curso para decidir si empiezo.
- Dado la ruta `/`, Cuando carga, Entonces el hero muestra el titular y subtítulo de docs/copy-landing.md, un CTA "Empieza gratis" y un CTA "Ver temario".
- Dado el CTA "Empieza gratis", Cuando se pulsa, Entonces lleva al formulario de la sección 10 (ancla).
- Dado "Ver temario", Cuando se pulsa, Entonces desplaza a la sección de temario.
- Dado las secciones Problema y Método, Entonces el texto coincide con copy-landing.md y el método nombra "predecir, revisar, explicar" y el ritmo L-V 40 min, sábado 20, domingo 15.
- Dado `prefers-reduced-motion`, Entonces no hay animación de escritura.
Prioridad: Must · 2 sesiones · Aprobada (2026-11-05)

## HU-03 · Landing: temario, proyecto real, para quién es
Como visitante quiero ver el contenido concreto y si el curso es para mi nivel.
- Dado la sección Temario, Entonces hay 10 tarjetas (semanas 1 a 10) con número, título y objetivo, generadas desde la colección de módulos (no escritas a mano).
- Dado una tarjeta, Cuando se pulsa, Entonces lleva a `/curso/[slug]` correcto.
- Dado la sección Proyecto real, Entonces menciona VisitasAPI, .NET 8 y Clean Architecture.
- Dado la sección Para quién es, Entonces lista quién sí, quién no y requisitos mínimos.
Prioridad: Must · 2 sesiones · Aprobada (2026-11-05)

## HU-04 · Landing: sobre Kevin, gratis vs premium, FAQ, CTA final
Como visitante quiero resolver mis dudas y ver qué es gratis y qué es de pago.
- Dado la sección Gratis vs. Premium, Entonces la tabla coincide con ARQUITECTURA.md sección 7 y aclara que el curso completo es gratis.
- Dado que el Kit aún no se vende, Entonces no se muestra precio inventado; se muestra "Próximamente". Si se muestra precio, incluye valor final y moneda.
- Dado la FAQ, Entonces hay 6 preguntas de copy-landing.md, incluida "¿Es oficial de Anthropic?" con respuesta "No".
- Dado la FAQ, Cuando se usa teclado, Entonces cada pregunta se abre y cierra (sin JavaScript de cliente si es posible, p. ej. `<details>`).
- Dado la sección 10, Entonces contiene el formulario (HU-05) y un enlace a LinkedIn que abre en pestaña nueva con `rel="noopener noreferrer"`.
- Dado la landing completa, Entonces tiene las 10 secciones en el orden de ARQUITECTURA.md sección 4 y JavaScript total < 30 KB.
Prioridad: Must · 3 sesiones · En desarrollo (Parcial, 2026-11-05). Falta: enlace a LinkedIn real (hoy cae a https://www.linkedin.com/ por falta de PUBLIC_LINKEDIN_URL) y formulario funcional (HU-05).

## HU-05 · Formulario de correo con autorización Ley 1581
Como visitante quiero suscribirme dando mi autorización expresa para recibir el curso por correo.
- Dado el formulario, Entonces tiene campo correo (tipo email, obligatorio, con etiqueta visible) y casilla de autorización **sin marcar por defecto**.
- Dado que la casilla no está marcada, Cuando se envía, Entonces no se envía el dato y se muestra "Para continuar debes aceptar la autorización de datos."
- Dado el texto de la casilla, Entonces enlaza a /privacidad e identifica finalidad (enviar el curso y comunicaciones relacionadas).
- Dado un correo válido y casilla marcada, Cuando se envía, Entonces se registra en el servicio de email elegido y se redirige a /gracias.
- Dado un correo inválido o error del servicio, Entonces se muestra un mensaje claro sin perder lo escrito.
- Dado cada correo enviado, Entonces incluye enlace de baja (configuración del servicio de email).
- Dado el formulario, Entonces se reutiliza el mismo componente `SubscribeForm` en landing y otras páginas.
- Decisión pendiente (a confirmar con el autor): servicio de email (MailerLite, Brevo o Buttondown). Verificar límites del plan gratuito vigentes antes de elegir y citar la fuente aquí.
Prioridad: Must · 3 sesiones · En desarrollo (Parcial, 2026-11-05). Falta: servicio de email elegido y conectado (PUBLIC_FORM_ACTION vacío: hoy el correo no se guarda en ningún sitio), redirección a /gracias desde el servicio, manejo de error del servicio, enlace de baja; corregir `novalidate` (sin JS el formulario envía sin autorización).

## HU-06 · Página /privacidad
Como suscriptor quiero conocer cómo se tratan mis datos para ejercer mis derechos.
- Dado /privacidad, Entonces incluye: responsable (nombre y correo de contacto), datos recolectados (correo), finalidad, derechos del titular (conocer, actualizar, rectificar, suprimir, revocar), procedimiento para ejercerlos, proveedor de email como encargado, vigencia y fecha de actualización.
- Dado el texto, Entonces cita la Ley 1581 de 2012 y el Decreto 1377 de 2013.
- Dado la página, Entonces es accesible desde el pie y desde el formulario.
- Nota: el texto es una plantilla de buena fe; se recomienda revisión de un abogado antes del lanzamiento.
Prioridad: Must · 2 sesiones · En desarrollo (Parcial, 2026-11-05). Falta: correo de contacto real (PUBLIC_CONTACT_EMAIL), vigencia, fecha de actualización, proveedor de email nombrado como encargado.

## HU-07 · Página /gracias
Como suscriptor quiero confirmación y un siguiente paso.
- Dado /gracias, Entonces confirma la suscripción, indica revisar el correo (y spam) y ofrece enlace a /curso/00-como-usar.
- Dado /gracias, Entonces incluye `noindex`.
Prioridad: Must · 1 sesión · Aprobada (2026-11-05; ojo: el texto "Te enviamos la bienvenida" solo es veraz cuando HU-05 envíe correos)

## HU-08 · Colección de módulos y esquema
Como autor quiero escribir módulos en Markdown validado para migrarlos fácil.
- Dado `src/content/config.ts`, Entonces el esquema define numero, titulo, semana, objetivo, duracionMinutos, premium, fuentes, ogImage.
- Dado `src/content/modulos`, Entonces existen 11 archivos: 00-como-usar, 01 a 09 y 10-proyecto-final, con título y objetivo de docs/temario.md.
- Dado un frontmatter inválido, Cuando se ejecuta `npx astro check` o build, Entonces falla con error claro.
Prioridad: Must · 2 sesiones · Aprobada (2026-11-05; el fallo por frontmatter inválido se deduce del esquema zod, no se probó)

## HU-09 · Página /curso (índice)
Como estudiante quiero ver todo el curso de un vistazo.
- Dado /curso, Entonces lista los 11 módulos ordenados, con semana, título, objetivo y duración.
- Dado un módulo, Cuando se pulsa, Entonces abre su página.
- Dado /curso, Entonces muestra una barra o lista de 10 semanas; si guarda progreso, usa almacenamiento local con JavaScript justificado, si no, queda fuera de alcance.
Prioridad: Must · 2 sesiones · Aprobada (2026-11-05; sin progreso guardado = fuera de alcance. Observación: las 10 barras salen todas rellenas, no representan progreso)

## HU-10 · Página /curso/[slug]
Como estudiante quiero leer cada módulo con navegación clara.
- Dado cada uno de los 11 slugs, Entonces la ruta se genera estáticamente y no hay 404.
- Dado un módulo, Entonces muestra título, semana, objetivo, duración, contenido y lista de fuentes con enlaces.
- Dado un módulo, Entonces tiene enlaces "Anterior" y "Siguiente" (omitidos en los extremos).
- Dado un módulo, Entonces su SeoHead usa título y objetivo propios y `ogImage` si existe.
- Dado un módulo con `premium: true`, Entonces solo se muestra el material extra marcado y nunca se oculta el contenido base.
- Dado un código en bloque, Entonces es legible en móvil (scroll horizontal, sin desbordar la página).
Prioridad: Must · 3 sesiones · Aprobada (2026-11-05)

## HU-11 · Contenido de módulos 00 a 04
Como estudiante quiero el contenido real de las primeras semanas.
- Dado cada módulo, Entonces incluye secciones: conceptos clave, laboratorio, reto, preguntas de repaso.
- Dado cada módulo, Entonces tiene al menos 1 fuente oficial enlazada y el texto es redacción propia (no copia de la documentación).
- Dado un laboratorio, Entonces es ejecutable en unos 245 min de trabajo semanal y avanza VisitasAPI.
- Dado el texto, Entonces no afirma afiliación con Anthropic.
Prioridad: Must · 3 sesiones · En desarrollo (Parcial, 2026-11-05). Estructura, fuentes y neutralidad cumplen; falta profundidad: laboratorios de 3 a 5 pasos que no se pueden comprobar contra ~245 min semanales, y 00/02 apenas avanzan VisitasAPI.

## HU-12 · Contenido de módulos 05 a 10
Como estudiante quiero el contenido de las semanas restantes y el proyecto final.
- Mismos criterios que HU-11 para los módulos 05 a 10.
- Dado 10-proyecto-final, Entonces incluye lista de entrega verificable (repositorio, pruebas pasando, README, configuración de Claude Code).
Prioridad: Must · 3 sesiones (dividir por módulos si excede) · En desarrollo (Parcial, 2026-11-05). Lista de entrega de 10-proyecto-final cumple; falta profundidad de laboratorios (06-mcp, 07, 08 muy breves; 06 con una sola fuente) y comprobación de exactitud técnica contra la documentación oficial.

## HU-13 · Imágenes Open Graph
Como autor quiero vistas previas atractivas en LinkedIn y Facebook.
- Dado la landing y cada módulo, Entonces existe imagen 1200x630 px < 300 KB en public/og/ con texto legible en celular.
- Dado las imágenes, Entonces no usan logos ni identidad de Anthropic.
- Dado cada URL, Cuando se prueba en LinkedIn Post Inspector y el Depurador de Facebook, Entonces muestra título, descripción e imagen correctos.
Prioridad: Should · 2 sesiones · En desarrollo (Parcial, 2026-11-05). Solo existe public/og/default.png (landing y módulos comparten la misma); faltan imágenes por módulo, medir peso < 300 KB y probar en LinkedIn/Facebook (requiere URL pública).

## HU-14 · Página /recursos
Como estudiante quiero plantillas gratuitas descargables.
- Dado /recursos, Entonces ofrece plantillas gratuitas (CLAUDE.md, settings.json, ejemplo de agente) visibles o descargables.
- Dado un recurso, Entonces indica qué es y cómo usarlo, y cita la licencia (sugerida CC BY-NC 4.0, a confirmar por el autor).
- Dado que el PDF del curso requiere correo, Entonces se ofrece mediante SubscribeForm con autorización.
Prioridad: Should · 2 sesiones · Aprobada (2026-11-05; el PDF aún no existe y su entrega depende de HU-05)

## HU-15 · Página /sobre-mi
Como visitante quiero conocer a Kevin para confiar en el curso.
- Dado /sobre-mi, Entonces cuenta la historia y motivación, enlaza a LinkedIn y a /privacidad para contacto de datos, sin afirmaciones no verificables.
- Dado la página, Entonces incluye CTA "Empieza gratis".
Prioridad: Should · 1 sesión · En desarrollo (Parcial, 2026-11-05). Falta: URL real de LinkedIn (hoy genérica).

## HU-16 · Página /premium
Como estudiante quiero conocer el Kit Premium y comprarlo o pedir aviso.
- Dado /premium, Entonces describe contenido del kit, qué sigue gratis, y no promete resultados laborales.
- Dado que hay precio, Entonces se muestra valor final y moneda; si no, un formulario de "avísame" con autorización (HU-05).
- Dado el botón de compra, Entonces apunta a la plataforma externa elegida y se prueba con una compra de prueba.
- Decisión pendiente: plataforma (Hotmart, Lemon Squeezy, Gumroad). Buscar comisiones vigentes y citar fuente aquí antes de decidir. Recomendación preliminar: no abrir ventas hasta tener lista de correos y el kit probado; riesgo: bajo potencial de ingresos si la audiencia inicial es pequeña, tratar el kit como validación de demanda.
Prioridad: Should · 2 sesiones · En desarrollo (Parcial, 2026-11-05). Modo "avísame" cumple en la UI pero depende de HU-05; botón de compra y compra de prueba no verificables (plataforma sin decidir).

## HU-17 · Analítica sin cookies y UTM
Como autor quiero saber qué red trae suscriptores.
- Dado el sitio, Entonces usa Cloudflare Web Analytics (sin cookies) sin banner de cookies adicional.
- Dado un enlace con parámetros utm_*, Entonces la visita queda atribuida en la analítica.
- Dado la landing, Entonces el script no la lleva sobre 30 KB de JavaScript.
Prioridad: Could · 1 sesión · En desarrollo (Parcial, 2026-11-05). Código listo (script condicionado a PUBLIC_CF_ANALYTICS_TOKEN) pero sin token ni despliegue: atribución UTM no comprobable.

## Fuera de alcance de la v1 (Won't)
- Mentorías y taller para equipos con reserva en el sitio (se gestionan por contacto directo).
- Cuentas de usuario, login y pagos propios.
- Certificado automatizado.
