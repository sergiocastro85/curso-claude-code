---
numero: 3
titulo: "Prompting profesional para Claude Code"
semana: 3
objetivo: "Escribir prompts que Claude pueda verificar solo, separar la exploración de la implementación y cuidar la ventana de contexto."
ogImage: "/og/03-prompting.png"
fuentes:
  - titulo: "Best practices"
    url: "https://code.claude.com/docs/en/best-practices"
  - titulo: "Common workflows"
    url: "https://code.claude.com/docs/en/common-workflows"
  - titulo: "Prompt library"
    url: "https://code.claude.com/docs/en/prompt-library"
---

## La restricción que lo explica todo

La ventana de contexto se llena rápido y el rendimiento baja a medida que se llena. Casi todas las buenas prácticas salen de ahí: dar contexto preciso, limpiar entre tareas y delegar la investigación.

## Los cinco principios

1. **Dale una forma de verificar su trabajo.** Pruebas, un build, un linter o una captura de pantalla. Sin una verificación que pueda ejecutar, tú eres el único control de calidad. Pide evidencia: la salida de las pruebas, no un "ya quedó".
2. **Explorar → planear → implementar → commit.** Usa el modo Plan para que lea y proponga sin tocar archivos. Si puedes describir el cambio en una sola frase, sáltate el plan.
3. **Sé específico:** qué archivo, qué escenario, qué restricción y qué patrón existente seguir.
4. **Dale contenido rico:** `@archivos`, capturas de pantalla, URLs de documentación o datos por tubería (`Get-Content error.log | claude -p "explica este error"`).
5. **Corrige temprano.** Si ya lo corregiste dos veces en lo mismo, ejecuta `/clear` y empieza con un prompt mejor que incluya lo aprendido.

## Antes y después, con VisitasAPI

| Estrategia | Prompt vago | Prompt profesional |
| --- | --- | --- |
| Criterio de verificación | "Valida las fechas de las visitas" | "En `CrearVisitaValidator` rechaza visitas con fecha futura o anteriores a 2026-01-01. Escribe pruebas xUnit para hoy (válida), mañana (inválida) y 2025-12-31 (inválida). Ejecuta `dotnet test` y corrige hasta que pasen." |
| Acotar la tarea | "Agrega pruebas" | "Escribe pruebas para `VisitaService.Registrar` cubriendo el caso en que la sede no existe. Sin mocks de EF Core: usa SQLite en memoria." |
| Seguir un patrón | "Crea el controlador de supervisores" | "Mira cómo está hecho `@SedesController.cs` y sigue ese patrón (DTOs, códigos HTTP, validación) para crear `SupervisoresController`." |
| Describir el síntoma | "Arregla el bug" | "`GET /visitas?comuna=10` devuelve visitas de otras comunas. Revisa el filtro en `VisitaRepository`. Primero escribe una prueba que reproduzca el error y luego corrígelo." |
| Causa raíz | "El build falla" | "El build falla con este error: [pegar]. Corrige la causa raíz, no lo silencies, y confirma que `dotnet build` termina sin errores." |

## Patrón de entrevista para funcionalidades grandes

```text
Quiero agregar un módulo de reportes mensuales de visitas a VisitasAPI.
Entrevístame en detalle con la herramienta AskUserQuestion sobre implementación,
casos límite y compromisos. No preguntes lo obvio. Cuando terminemos,
escribe la especificación completa en SPEC.md.
```

Después abre una sesión nueva para implementar la especificación con el contexto limpio.

## Errores comunes

| Error | Solución |
| --- | --- |
| Sesión "cajón de sastre": mezclar tareas sin relación | `/clear` entre tareas |
| Corregir una y otra vez lo mismo | Después de dos intentos, `/clear` y un prompt mejor |
| Confiar sin verificar | Siempre pruebas, build o capturas |
| Investigación sin límites que llena el contexto | Acotar la pregunta o usar un subagente |
| Preguntas sueltas que ensucian la conversación | `/btw pregunta` responde sin agregarlo al historial |

## Laboratorio (martes y miércoles)

**Parte A · Explorar y planear (martes)**

1. Crea una rama: `git switch -c hallazgos-prompt-pro`.
2. Pulsa `Shift+Tab` hasta ver **plan mode**. Pide: "Lee el proyecto y explícame cómo debería implementar el registro de hallazgos de una visita. No escribas código".
   *Comprueba:* Claude no modifica ningún archivo (`git status` limpio).
3. Pide el plan. Pulsa `Ctrl+G` para abrirlo en tu editor y agrega una restricción tuya (por ejemplo, "un hallazgo tiene severidad Baja, Media o Alta").
4. Aprueba el plan eligiendo la opción de aprobar ediciones manualmente.
5. Implementa `POST /visitas/{id}/hallazgos` con un prompt que tenga los tres elementos: archivo de referencia, criterio de verificación y restricción.
   *Comprueba:* Claude te muestra la salida de `dotnet test` en verde.
6. Haz commit. Ejecuta `/rename hallazgos-pro`.

**Parte B · Comparar contra un prompt vago (miércoles)**

7. Vuelve a `main` y crea otra rama: `git switch main; git switch -c hallazgos-vago`. Ejecuta `/clear`.
8. Pide solo: "agrega hallazgos a las visitas".
9. Compara ambas ramas con `git diff hallazgos-pro hallazgos-vago --stat` y llena esta tabla en tus notas: archivos tocados, pruebas creadas, correcciones que tuviste que pedir, minutos invertidos.
   *Comprueba:* puedes explicar con un ejemplo concreto qué hizo distinto cada prompt.
10. Usa `/btw ¿qué diferencia hay entre 400 y 422 en ASP.NET Core?` y confirma con `/context` que la respuesta no se agregó a la conversación.

## Reto (jueves)

Usa el patrón de entrevista para diseñar el módulo de reportes y guarda `SPEC.md`. No implementes nada todavía: revísalo tú y agrega al final una sección "Fuera de alcance" escrita por ti, con al menos tres puntos.

## Preguntas de control (sábado)

1. ¿Por qué dar un criterio de verificación cambia cómo termina Claude una tarea?
2. ¿Cuándo conviene saltarse el modo Plan?
3. ¿Qué haces si ya corregiste a Claude dos veces en lo mismo?
4. ¿Para qué sirve `/btw`?
