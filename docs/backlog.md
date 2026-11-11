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
| HU-04 | Landing: sobre el autor, gratis vs premium, FAQ, CTA final | Must | 3 | En desarrollo (Parcial) |
| HU-05 | Formulario de correo con autorización Ley 1581 | Must | 3 | En desarrollo (Parcial) |
| HU-06 | Página /privacidad | Must | 2 | En desarrollo (Parcial) |
| HU-07 | Página /gracias | Must | 1 | Aprobada |
| HU-08 | Colección de módulos y esquema | Must | 2 | Aprobada |
| HU-09 | Página /curso (índice) | Must | 2 | En desarrollo (Rechazada 2026-11-10: dice "11 módulos") |
| HU-10 | Página /curso/[slug] (plantilla de módulo) | Must | 3 | Aprobada |
| HU-11 | Contenido de módulos 01 a 05 | Must | 3 | En validación |
| HU-12 | Contenido de módulos 06 a 10 | Must | 3 | En validación |
| HU-13 | Imágenes Open Graph | Should | 2 | En validación |
| HU-14 | Página /recursos | Should | 2 | Aprobada |
| HU-15 | Página /sobre-mi | Should | 1 | En desarrollo (Parcial) |
| HU-16 | Página /premium | Should | 2 | En desarrollo (Parcial) |
| HU-17 | Analítica sin cookies y UTM | Could | 1 | En desarrollo (Parcial) |

Cambio de contenido 2026-11-09: el curso pasó a 10 módulos (01-introduccion a 10-proyecto-final), sin 00-como-usar y sin módulos premium. HU-08, 09, 10, 11, 12, 13, 07 y 16 actualizadas el 2026-11-10.

Validación del 2026-11-05 (revisión estática de src/, public/, astro.config.mjs y dist/) y re-validación del 2026-11-10: ver docs/validacion.md. "Aprobada" = Aceptada; "En desarrollo (Parcial)" = faltan criterios.

Nota de coherencia: ARQUITECTURA.md sección 3 usa `/curso/modulo-N`, pero el encargo y la estructura de contenido usan slugs `00-como-usar`, `01-...`, `10-proyecto-final`. **Decisión:** se usan los slugs de archivo vigentes (ver docs/temario.md; ya no existe 00-como-usar). Actualizar ARQUITECTURA.md queda pendiente del autor (el PO no edita ese archivo sin aprobación).

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

## HU-04 · Landing: sobre el autor, gratis vs premium, FAQ, CTA final
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
Prioridad: Must · 3 sesiones · En desarrollo (Parcial, 2026-11-05). Falta: servicio de email elegido y conectado (PUBLIC_FORM_ACTION vacío: hoy el correo no se guarda en ningún sitio), redirección a /gracias desde el servicio, manejo de error del servicio, enlace de baja. `novalidate` ya corregido (2026-11-10: SubscribeForm.astro ya no lo usa).

## HU-06 · Página /privacidad
Como suscriptor quiero conocer cómo se tratan mis datos para ejercer mis derechos.
- Dado /privacidad, Entonces incluye: responsable (nombre y correo de contacto), datos recolectados (correo), finalidad, derechos del titular (conocer, actualizar, rectificar, suprimir, revocar), procedimiento para ejercerlos, proveedor de email como encargado, vigencia y fecha de actualización.
- Dado el texto, Entonces cita la Ley 1581 de 2012 y el Decreto 1377 de 2013.
- Dado la página, Entonces es accesible desde el pie y desde el formulario.
- Nota: el texto es una plantilla de buena fe; se recomienda revisión de un abogado antes del lanzamiento.
Prioridad: Must · 2 sesiones · En desarrollo (Parcial, 2026-11-05). Correo de contacto ya definido en .env (2026-11-10; el PO no puede leer .env, verificar que se muestre en /privacidad). Falta: vigencia, fecha de actualización, proveedor de email nombrado como encargado.

## HU-07 · Página /gracias
Como suscriptor quiero confirmación y un siguiente paso.
- Dado /gracias, Entonces confirma la suscripción, indica revisar el correo (y spam) y ofrece enlace a /curso/01-introduccion.
- Dado /gracias, Entonces incluye `noindex`.
Prioridad: Must · 1 sesión · Aprobada (2026-11-05; ojo: el texto "Te enviamos la bienvenida" solo es veraz cuando HU-05 envíe correos)

## HU-08 · Colección de módulos y esquema
Como autor quiero escribir módulos en Markdown validado para migrarlos fácil.
- Dado `src/content/config.ts`, Entonces el esquema define numero, titulo, semana, objetivo, duracionMinutos, premium, fuentes, ogImage.
- Dado `src/content/modulos`, Entonces existen 10 archivos (01-introduccion a 10-proyecto-final, sin 00-como-usar), con título y objetivo de docs/temario.md y ninguno con `premium: true`.
- Dado un frontmatter inválido, Cuando se ejecuta `npx astro check` o build, Entonces falla con error claro.
Prioridad: Must · 2 sesiones · Aprobada (2026-11-05; el fallo por frontmatter inválido se deduce del esquema zod, no se probó)

## HU-09 · Página /curso (índice)
Como estudiante quiero ver todo el curso de un vistazo.
- Dado /curso, Entonces lista los 10 módulos ordenados, con semana, título, objetivo y duración.
- Dado un módulo, Cuando se pulsa, Entonces abre su página.
- Dado /curso, Entonces muestra una barra o lista de 10 semanas; si guarda progreso, usa almacenamiento local con JavaScript justificado, si no, queda fuera de alcance.
Prioridad: Must · 2 sesiones · Aprobada (2026-11-05; sin progreso guardado = fuera de alcance. Observación: las 10 barras salen todas rellenas, no representan progreso)

## HU-10 · Página /curso/[slug]
Como estudiante quiero leer cada módulo con navegación clara.
- Dado cada uno de los 10 slugs, Entonces la ruta se genera estáticamente y no hay 404.
- Dado un módulo, Entonces muestra título, semana, objetivo, duración, contenido y lista de fuentes con enlaces.
- Dado un módulo, Entonces tiene enlaces "Anterior" y "Siguiente" (omitidos en los extremos).
- Dado un módulo, Entonces su SeoHead usa título y objetivo propios y `ogImage` si existe.
- Dado un módulo con `premium: true` (hoy ninguno), Entonces solo se muestra el material extra marcado y nunca se oculta el contenido base; con `premium: false` no aparece nota ni etiqueta premium.
- Dado un código en bloque, Entonces es legible en móvil (scroll horizontal, sin desbordar la página).
Prioridad: Must · 3 sesiones · Aprobada (2026-11-05)

## HU-11 · Contenido de módulos 01 a 05
Como estudiante quiero el contenido real de las primeras semanas (01-introduccion, 02-vscode-cursor, 03-prompting, 04-memoria, 05-permisos-seguridad).
- Dado cada módulo, Entonces incluye secciones: conceptos clave, laboratorio, reto, preguntas de repaso.
- Dado cada módulo, Entonces tiene al menos 1 fuente oficial enlazada y el texto es redacción propia (no copia de la documentación).
- Dado un laboratorio, Entonces es ejecutable en unos 245 min de trabajo semanal y avanza VisitasAPI.
- Dado el texto, Entonces no afirma afiliación con Anthropic.
Prioridad: Must · 3 sesiones · En validación (re-validada 2026-11-10 con el contenido nuevo). Estructura, fuentes y neutralidad cumplen y hay verificación técnica contra la documentación oficial (docs/verificacion-contenido.md). Pendiente: nadie ha ejecutado los laboratorios de punta a punta en Windows 11 con .NET 8; 02-vscode-cursor tiene una sola fuente.

## HU-12 · Contenido de módulos 06 a 10
Como estudiante quiero el contenido de las semanas restantes y el proyecto final (06-mcp, 07-hooks, 08-subagentes, 09-skills-plugins, 10-proyecto-final).
- Mismos criterios que HU-11 para los módulos 06 a 09 (el 10 sigue la estructura "encargo, plan, criterios de terminado").
- Dado 10-proyecto-final, Entonces incluye criterios de terminado verificables (endpoint con pruebas, CSV, hook de migraciones, revisión del subagente, README propio) y publicación del repositorio en GitHub.
Prioridad: Must · 3 sesiones (dividir por módulos si excede) · En validación (re-validada 2026-11-10). Pendiente: laboratorios sin ejecutar (prioridad 07-hooks en PowerShell y 06-mcp con token de GitHub y DBHub); 10-proyecto-final no menciona publicar en GitHub, que la landing promete.

## HU-13 · Imágenes Open Graph
Como autor quiero vistas previas atractivas en LinkedIn y Facebook.
- Dado la landing y cada módulo, Entonces existe imagen 1200x630 px < 300 KB en public/og/ (default/og-default y los 10 PNG por slug) con texto legible en celular, y el `ogImage` de cada módulo apunta a su PNG.
- Dado las imágenes, Entonces no usan logos ni identidad de Anthropic.
- Dado cada URL, Cuando se prueba en LinkedIn Post Inspector y el Depurador de Facebook, Entonces muestra título, descripción e imagen correctos.
Prioridad: Should · 2 sesiones · En validación (2026-11-10). Existen default.png, og-default.png y los 10 PNG (01-introduccion a 10-proyecto-final) y cada frontmatter apunta a su archivo. Falta: confirmar 1200x630 y peso < 300 KB (el PO no puede medirlo), revisar visualmente legibilidad, y probar en LinkedIn/Facebook (requiere URL pública). Nota: hay default.svg, default.png y og-default.png; confirmar con el desarrollador cuál usa SeoHead y borrar los sobrantes.

## HU-14 · Página /recursos
Como estudiante quiero plantillas gratuitas descargables.
- Dado /recursos, Entonces ofrece plantillas gratuitas (CLAUDE.md, settings.json, ejemplo de agente) visibles o descargables.
- Dado un recurso, Entonces indica qué es y cómo usarlo, y cita la licencia (sugerida CC BY-NC 4.0, a confirmar por el autor).
- Dado que el PDF del curso requiere correo, Entonces se ofrece mediante SubscribeForm con autorización.
Prioridad: Should · 2 sesiones · Aprobada (2026-11-05; el PDF aún no existe y su entrega depende de HU-05). Revisar al actualizar: las plantillas (CLAUDE.md, settings.json, subagente) deben coincidir con los módulos 04, 05 y 08 nuevos.

## HU-15 · Página /sobre-mi
Como visitante quiero conocer al autor (Sergio Andrés Castro Cano) para confiar en el curso.
- Dado /sobre-mi, Entonces cuenta la historia y motivación, enlaza a LinkedIn y a /privacidad para contacto de datos, sin afirmaciones no verificables.
- Dado la página, Entonces incluye CTA "Empieza gratis".
Prioridad: Should · 1 sesión · En desarrollo (Parcial, 2026-11-05). LinkedIn real configurado (2026-11-10). Pendiente: confirmar con el autor que autoriza publicar su nombre, cargo y experiencia.

## HU-16 · Página /premium
Como estudiante quiero conocer el Kit Premium y comprarlo o pedir aviso.
- Dado /premium, Entonces describe contenido del kit, qué sigue gratis (los 10 módulos completos; ningún módulo es premium), y no promete resultados laborales.
- Dado el "certificado de finalización" listado en el kit, Entonces se aclara cómo se emite (manual, por el autor) o se quita, porque el certificado automatizado está fuera de alcance.
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
