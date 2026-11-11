---
numero: 10
titulo: "Proyecto final"
semana: 10
objetivo: "Agregar a VisitasAPI un módulo de reportes mensuales de visitas por comuna usando todo lo aprendido y demostrando que entiendes cada pieza."
ogImage: "/og/10-proyecto-final.png"
fuentes:
  - titulo: "Best practices"
    url: "https://code.claude.com/docs/en/best-practices"
  - titulo: "What's new"
    url: "https://code.claude.com/docs/en/whats-new/index"
---

## El encargo

Construye `GET /reportes/visitas?anio=2026&mes=10`, que devuelva por comuna: número de visitas, número de hallazgos por severidad y supervisor con más visitas. Debe poder exportarse a CSV.

## Plan de la semana

- [ ] **Lunes:** sesión en modo Plan con el patrón de entrevista; guarda `SPEC.md` y escribe tú la sección "Fuera de alcance" (Módulos 3 y 5).
- [ ] **Martes:** sesión limpia; crea la entidad base con `/nueva-entidad Reporte` y consulta Microsoft Learn por MCP para la mejor forma de exportar a CSV en ASP.NET Core (Módulos 6 y 9).
- [ ] **Miércoles:** implementa la consulta y las pruebas. Los hooks protegen las migraciones y formatean; el hook `Stop` exige pruebas en verde (Módulo 7).
- [ ] **Jueves:** `@revisor-dotnet` revisa el diff con contexto limpio; corrige solo lo crítico (Módulo 8).
- [ ] **Viernes:** actualiza CLAUDE.md con lo que aprendiste y ejecuta `/doctor prompt-audit` (Módulo 4).
- [ ] **Sábado:** escribe un README donde expliques, sin ayuda, qué hace cada archivo de `.claude/` y por qué existe.
- [ ] **Domingo:** explica en voz alta durante 5 minutos el flujo completo, como si lo sustentaras ante un compañero.

## Criterios de terminado

| Criterio | Cómo lo compruebas |
| --- | --- |
| El endpoint devuelve los datos correctos | Pruebas con datos conocidos y una consulta SQL escrita por ti que da lo mismo |
| El CSV abre bien en Excel | Lo abres y las tildes se ven correctas |
| Ninguna migración se editó a mano | El hook nunca se desactivó y `git log` lo muestra |
| El revisor no deja hallazgos críticos | Salida del subagente en el pull request |
| Entiendes cada cambio | Puedes explicar cualquier línea que alguien señale al azar |

**Criterio de éxito del curso:** puedes borrar la carpeta `.claude/`, reconstruirla de memoria en 40 minutos y explicar cada línea.

## Y después

Claude Code cambia cada semana. Antes de retomar cualquier módulo, revisa la página oficial de novedades y comprueba que los comandos sigan igual.
