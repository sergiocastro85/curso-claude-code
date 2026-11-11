# Temario · Claude Code desde cero

Proyecto práctico: **VisitasAPI** (.NET 8, Clean Architecture). Ritmo: L-V 40 min, sábado 20, domingo 15 (aprox. 245 min por semana).
Regla de oro de todo el curso: **predecir, revisar el diff, explicar**.
Versión del contenido: reemplazo del 2026-11-09 (10 módulos, uno por semana). Ya no existe el módulo 00-como-usar ni los módulos antiguos. Ningún módulo es premium.

| Slug | Semana | Título | Objetivo (al terminar podrás...) |
| --- | --- | --- | --- |
| 01-introduccion | 1 | Introducción a Claude Code | Instalar Claude Code, entender cómo trabaja por dentro y crear el esqueleto de VisitasAPI. |
| 02-vscode-cursor | 2 | Claude Code con VS Code y Cursor | Trabajar con Claude dentro del editor, revisar sus cambios en diffs visuales y saber cuándo usar la extensión y cuándo la terminal. |
| 03-prompting | 3 | Prompting profesional para Claude Code | Escribir prompts que Claude pueda verificar solo, separar la exploración de la implementación y cuidar la ventana de contexto. |
| 04-memoria | 4 | Memoria persistente con Claude Code | Lograr que Claude recuerde las reglas de VisitasAPI entre sesiones sin que tengas que repetirlas. |
| 05-permisos-seguridad | 5 | Modos de operación, permisos y seguridad | Decidir cuánta autonomía darle a Claude en cada situación y proteger VisitasAPI con reglas que no dependan de lo que Claude decida. |
| 06-mcp | 6 | MCP (Model Context Protocol) con Claude Code | Conectar Claude a herramientas externas (documentación oficial de .NET, GitHub y una base de datos) para que deje de depender de lo que tú le pegues en el chat. |
| 07-hooks | 7 | Hooks y automatización basada en eventos | Convertir las reglas que deben cumplirse siempre en comandos que se ejecutan solos, sin depender de que Claude se acuerde. |
| 08-subagentes | 8 | Subagentes y equipos de IA con Claude Code | Delegar tareas a especialistas con su propio contexto y herramientas, y saber cuándo escalar a trabajo en paralelo. |
| 09-skills-plugins | 9 | Skills y plugins en Claude Code | Empaquetar tus procedimientos repetidos como skills y compartir todo lo que construiste (skills, subagentes, hooks y MCP) como un plugin. |
| 10-proyecto-final | 10 | Proyecto final | Agregar a VisitasAPI un módulo de reportes mensuales de visitas por comuna usando todo lo aprendido y demostrando que entiendes cada pieza. |

Notas:
- Fuente de verdad: frontmatter de src/content/modulos. Si cambia allí, actualizar esta tabla.
- Estructura real de los módulos 01 a 09: conceptos, Laboratorio (martes y miércoles), Reto (jueves) y Preguntas de control (sábado). El módulo 10 usa: El encargo, Plan de la semana (lunes a domingo), Criterios de terminado y Y después.
- Cada módulo tiene 1 a 4 fuentes oficiales enlazadas (módulo 02 solo una) y su propia imagen OG en public/og/.
- Ningún módulo lleva `premium: true`. El Kit Premium (plugin, subagentes/skills extra, repositorio comentado) se vende aparte y no condiciona el contenido base.
- Cambio de orden frente a la v1: antes pruebas/depuración, CLAUDE.md y flujo de trabajo eran módulos propios; ahora la memoria es el 04, hooks el 07, subagentes el 08 y skills+plugins el 09. No hay un módulo dedicado a pruebas xUnit.
- Los slugs no deben cambiar una vez publicados (las URLs se comparten en redes). Los slugs antiguos (00-como-usar, 02-claude-md, etc.) ya no existen: si alguno se compartió, hace falta redirección.
- Estado de verificación: contraste con documentación oficial hecho (docs/verificacion-contenido.md); laboratorios sin ejecutar de punta a punta.
