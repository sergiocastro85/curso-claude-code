# Validación HU-01 a HU-17

Método: revisión estática de src/, public/ y docs/. El PO no tiene shell: **no se ejecutó `npm run build` ni `npx astro check`**, no se midió peso de imágenes ni Lighthouse, y no se probaron vistas previas en LinkedIn/Facebook. El PO tampoco puede leer .env. Lo no comprobable se declara así.

## Re-validación 2026-11-10 (contenido nuevo: 10 módulos)

Contexto: el contenido se reemplazó el 2026-11-09. Hay 10 módulos (01-introduccion a 10-proyecto-final), sin 00-como-usar, ninguno premium, cada uno con `ogImage` propio. Corregido desde el 2026-11-05: `novalidate` fuera de SubscribeForm.astro; correo de contacto definido en .env.

| HU | Veredicto | Evidencia | Qué falla o falta |
| --- | --- | --- | --- |
| HU-08 | Aceptada | 10 archivos en src/content/modulos con título y objetivo iguales a docs/temario.md; esquema en config.ts; ningún `premium: true` | Nada. |
| HU-09 | Rechazada | src/pages/curso/index.astro:11 | La descripción dice "Los 11 módulos del curso gratuito". Debe decir 10. La lista se genera de la colección, así que solo falla el texto. |
| HU-10 | Aceptada | getStaticPaths desde la colección; ModuleLayout con nota premium condicionada a `premium` (ninguno la activa); ogImage pasado a BaseLayout | Reserva: build no ejecutado, confirmar que no queden rutas a slugs viejos. |
| HU-11 | Parcial | Módulos 01 a 05: conceptos, Laboratorio, Reto, Preguntas de control; fuentes oficiales (02 con una sola); contraste técnico en docs/verificacion-contenido.md | Laboratorios sin ejecutar (ver abajo). 02-vscode-cursor con una sola fuente: aceptable, pero conviene una segunda. |
| HU-12 | Parcial | Módulos 06 a 09 con estructura completa y 1 a 4 fuentes; 10-proyecto-final con encargo, plan semanal y tabla de criterios de terminado | Laboratorios sin ejecutar. 10-proyecto-final no incluye publicar en GitHub, que la landing promete; sus criterios no exigen "pruebas pasando" como línea propia (solo en el hook Stop y en "Pruebas con datos conocidos"). |
| HU-13 | Parcial | public/og/ contiene 01-introduccion.png a 10-proyecto-final.png, default.png, default.svg y og-default.png; cada módulo referencia su PNG; site.ts usa og-default.png | Existencia de los 10 PNG + og-default: cumplida. Falta medir 1200x630 y < 300 KB, revisar legibilidad en celular y probar en LinkedIn/Facebook (URL pública). default.png y default.svg parecen sobrantes. |
| HU-03 | Aceptada | Tarjetas desde la colección; 10 módulos | Ver contradicción 3 (enlace/etiqueta Premium inexistente, sin efecto). |
| HU-07 | Aceptada | src/pages/gracias.astro:26 apunta a /curso/01-introduccion/ (correcto, ya no al 00) | Observación: "Te enviamos la bienvenida" no es veraz mientras HU-05 no envíe correos. |
| HU-14 | Aceptada | recursos.astro | Verificar que las plantillas coincidan con los módulos 04, 05 y 08 nuevos. |
| HU-16 | Parcial | premium.astro, PricingTable.astro | Lista "certificado de finalización" mientras el certificado automatizado está fuera de alcance; sin plataforma de pago ni compra de prueba. Los 10 módulos son gratis (no hay extra premium en módulos): coherente. |
| HU-05 | Parcial (mejora) | `novalidate` retirado: sin JS el navegador exige correo y casilla | Sin servicio de email conectado ni manejo de error del servicio ni enlace de baja. Verificar PUBLIC_FORM_ACTION en .env. |
| HU-06 | Parcial (mejora) | Correo de contacto leído de PUBLIC_CONTACT_EMAIL (ya en .env) | privacidad.astro:31 aún dice "servicio de email (por definir)"; faltan vigencia, fecha de actualización y revisión legal. |

Sin cambios respecto al 2026-11-05: HU-01, HU-02 Aceptadas; HU-04, HU-15, HU-17 Parciales (LinkedIn y token de analítica; el PO no puede confirmar el contenido de .env).

Resultado: Aceptadas HU-01, 02, 03, 07, 08, 10, 14; Rechazada HU-09 (texto "11 módulos"); Parciales HU-04, 05, 06, 11, 12, 13, 15, 16, 17.

## Laboratorios sin ejecutar (pendiente)

Según docs/verificacion-contenido.md, nadie ha seguido los laboratorios de punta a punta en Windows 11 con .NET 8 ni marcado cada "Comprueba". Hasta hacerlo, HU-11 y HU-12 no pasan a Aprobada.
- Prioridad 1: 07-hooks (hooks en PowerShell, `-ExecutionPolicy Bypass`, `dotnet format whitespace --folder --include`).
- Prioridad 2: 06-mcp (token de GitHub, DBHub de solo lectura, regla `mcp__github__*`).
- Resto: 01 (`dotnet new webapi --use-controllers`, `.FullName`), 05 (bloqueo de `git reset --hard` observado), 08 (hook en frontmatter del subagente, confianza de la carpeta), 02, 03, 04, 09 y 10.
- Acción: asignar a una persona (el autor) y registrar fecha y resultado por módulo en este archivo.

## Contradicciones entre copy/landing y el temario nuevo (para el desarrollador, en src/)

1. src/pages/curso/index.astro:11: "Los 11 módulos" debe decir "Los 10 módulos".
2. src/pages/index.astro:66-67: "con Clean Architecture, pruebas y ... Al final tendrás el repositorio en tu GitHub". 10-proyecto-final no tiene paso de publicar en GitHub. Usar el copy de docs/copy-landing.md (sección 5) actualizado, o pedir al autor añadir el paso al módulo 10.
3. src/pages/index.astro:104: "con el PDF del curso" cuando el PDF no existe; usar el texto actualizado de la sección 10.
4. src/components/PricingTable.astro:11 y src/pages/premium.astro:13: "Certificado de finalización" (certificado automatizado = Won't). Aclarar que lo emite el autor o quitarlo.
5. src/components/ModuleCard.astro:27 y ModuleLayout.astro:25-28: la etiqueta/nota Premium ya no se muestra (ningún módulo es premium). Sin efecto; dejar o retirar a criterio del desarrollador.
6. src/pages/index.astro: el filtro `semana >= 1` ya es innecesario (no existe módulo 00); inofensivo.
7. src/pages/privacidad.astro:31: "servicio de email (por definir)" y falta vigencia/fecha.
8. Imágenes sobrantes en public/og/: default.png y default.svg (SeoHead usa og-default.png).
9. Temario: no existe ya un módulo de pruebas/depuración con xUnit; el copy habla de "pruebas" y la regla de oro "predecir, revisar, explicar" aparece solo en unos pocos módulos. Decisión del autor: reforzarla en los módulos o suavizar el copy.
10. Si se compartió algún enlace con slugs antiguos (00-como-usar, 02-claude-md, etc.), hace falta redirección en Cloudflare Pages (`_redirects`).

## Hallazgos transversales
- Sin logos de Anthropic; el nombre solo aparece en el descargo, el FAQ y la imagen OG (la OG por módulo no se revisó visualmente).
- ARQUITECTURA.md sigue diciendo `/curso/modulo-N`; el sitio usa los slugs de archivo.

## Pendientes priorizados

Bloqueantes de lanzamiento (Must)
1. HU-05: elegir y conectar el servicio de email (verificar y citar límites vigentes del plan gratuito), manejo de error, enlace de baja. Decisión del autor pendiente.
2. HU-06: texto del proveedor de email, vigencia, fecha de actualización; revisión legal.
3. PUBLIC_LINKEDIN_URL y dominio real en `site` (cierra HU-04 y HU-15).
4. Ejecutar `npm run build` y `npx astro check` y registrar el resultado.
5. Corregir las contradicciones 1 a 4 de arriba.

Calidad del producto (Must)
6. Ejecutar los laboratorios (sección anterior) y cerrar HU-11 y HU-12.

Después (Should/Could)
7. HU-13: medir peso y tamaño de los 11 PNG; probar en LinkedIn y Facebook con URL pública.
8. HU-16: decidir plataforma de pago tras verificar comisiones vigentes; mantener "Próximamente" hasta tener lista de correos y kit probado.
9. HU-17: token de Cloudflare Web Analytics y prueba de UTM tras desplegar.
10. Lighthouse (meta >= 95) y JavaScript de la landing tras el primer despliegue de vista previa.
11. Barra de 10 semanas en /curso: decorativa o quitarla.
