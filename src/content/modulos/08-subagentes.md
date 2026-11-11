---
numero: 8
titulo: "Subagentes y equipos de IA con Claude Code"
semana: 8
objetivo: "Delegar tareas a especialistas con su propio contexto y herramientas, y saber cuándo escalar a trabajo en paralelo."
ogImage: "/og/08-subagentes.png"
fuentes:
  - titulo: "Create custom subagents"
    url: "https://code.claude.com/docs/en/sub-agents"
  - titulo: "Run agents in parallel"
    url: "https://code.claude.com/docs/en/agents"
  - titulo: "Agent teams"
    url: "https://code.claude.com/docs/en/agent-teams"
  - titulo: "Worktrees"
    url: "https://code.claude.com/docs/en/worktrees"
---

## Qué es un subagente

Un subagente es un asistente especializado que trabaja en **su propia ventana de contexto**, con su propio prompt de sistema, herramientas y permisos. Hace la tarea lateral (buscar, leer logs, revisar código) y te devuelve solo un resumen. Así tu conversación principal no se llena de resultados que no volverás a leer.

Piensa en una reunión: en vez de que todos lean juntos 40 archivos, mandas a alguien a leerlos y que vuelva con tres conclusiones.

## Subagentes incluidos

| Subagente | Herramientas | Para qué lo usa Claude |
| --- | --- | --- |
| Explore | Solo lectura | Buscar y entender código sin cambiarlo (rápido, medio o muy exhaustivo) |
| Plan | Solo lectura | Investigar durante el modo Plan |
| general-purpose | Todas las disponibles | Tareas de varios pasos que exploran y modifican |

Explore y Plan arrancan sin tu CLAUDE.md para ser rápidos. Si una regla debe llegarles, repítela en tu prompt.

## Qué recibe un subagente al iniciar

- Su propio prompt de sistema (el cuerpo de su archivo `.md`).
- El mensaje de delegación que escribe Claude con la tarea.
- Tus archivos CLAUDE.md (salvo Explore, Plan o si su definición dice `omitClaudeMd: true`).
- Las skills que precargue con el campo `skills`.

**No recibe** tu historial de conversación ni los archivos que ya leíste. Por eso la descripción de la tarea debe ser autosuficiente. La excepción es una bifurcación (`/subtask`), que sí hereda toda la conversación.

## Crear tu propio subagente

Es un archivo Markdown con encabezado YAML. Solo `name` y `description` son obligatorios; Claude usa la `description` para decidir cuándo delegar.

| Ubicación | Alcance |
| --- | --- |
| `.claude/agents/` | Este proyecto; se sube a Git |
| `~/.claude/agents/` | Todos tus proyectos |
| `--agents '{...}'` | Solo esta sesión |
| Plugin | Donde el plugin esté activo |

Ejemplo para VisitasAPI (`.claude/agents/revisor-dotnet.md`):

```markdown
---
name: revisor-dotnet
description: Revisa cambios en C# contra Clean Architecture y seguridad. Úsalo después de modificar código.
tools: Read, Grep, Glob, Bash
model: sonnet
memory: project
---
Eres un revisor senior de .NET. Cuando te invoquen:
1. Ejecuta git diff para ver los cambios recientes.
2. Verifica que Domain no dependa de Infrastructure ni de EF Core.
3. Busca inyección SQL, secretos en código y validación faltante.
4. Revisa que cada endpoint nuevo tenga pruebas.
Organiza tus hallazgos en Crítico, Advertencia y Sugerencia,
con archivo, línea y cómo corregirlo. No edites archivos.
Antes de empezar, consulta tu memoria; al terminar, guarda los patrones recurrentes.
```

## Campos más útiles

| Campo | Qué hace |
| --- | --- |
| `tools` / `disallowedTools` | Lista blanca o negra de herramientas. Sin `Edit` ni `Write`, el subagente no puede modificar archivos |
| `model` | `sonnet`, `opus`, `haiku`, `fable`, un ID completo o `inherit` (el de la conversación) |
| `permissionMode` | Modo de permisos propio (se ignora si la sesión está en Auto, Aceptar ediciones u Omitir permisos) |
| `memory` | Memoria persistente: `user`, `project` o `local` |
| `skills` | Skills que se precargan al iniciar |
| `mcpServers` | Servidores MCP solo para este subagente |
| `hooks` | Hooks que solo corren mientras el subagente trabaja |
| `isolation: worktree` | Trabaja en una copia aislada del repositorio (git worktree) |
| `maxTurns` | Límite de turnos antes de detenerse |
| `effort` | Nivel de esfuerzo de razonamiento para este subagente |

## Cómo invocarlos

- **Automático:** Claude delega según la `description`. Frases como "úsalo después de…" o "use proactively" ayudan.
- **Por nombre:** "Usa el subagente revisor-dotnet para revisar mis cambios" (Claude decide si delegar).
- **Mencionándolo:** escribe `@` y elige el subagente; así garantizas que corra ese.
- **Toda la sesión:** `claude --agent revisor-dotnet`.
- **Bifurcación:** `/subtask <tarea>` crea un subagente que hereda toda la conversación y trabaja en segundo plano.

Por defecto los subagentes corren **en segundo plano**: tú sigues trabajando y el resultado llega cuando terminan. Con `/tasks` ves los que están corriendo y puedes detenerlos. Si un subagente en segundo plano necesita un permiso, la pregunta aparece en tu sesión principal con su nombre.

## Patrones de trabajo

| Patrón | Prompt de ejemplo | Para qué |
| --- | --- | --- |
| Aislar salida pesada | "Usa un subagente para ejecutar todas las pruebas y reportar solo las que fallan con su error" | Que el log no llene tu contexto |
| Investigación en paralelo | "Investiga en paralelo con subagentes separados cómo se manejan errores en Api, Application e Infrastructure" | Varias búsquedas independientes |
| Cadena | "Usa revisor-dotnet para encontrar problemas y luego escritor-pruebas para cubrirlos" | Flujos de varios pasos |
| Escritor / revisor | Una sesión implementa; un subagente con contexto limpio revisa el diff | El revisor no está sesgado por lo que acaba de escribir |

## Cuándo usar subagente y cuándo no

| Usa la conversación principal si… | Usa un subagente si… |
| --- | --- |
| Necesitas ir y venir varias veces | La tarea produce mucha salida que no necesitas ver |
| Las fases comparten mucho contexto | Quieres limitar herramientas o permisos |
| Es un cambio rápido y puntual | El trabajo es independiente y basta un resumen |

Cada subagente consume tokens propios y cuenta para los límites de tu plan. Varios en paralelo multiplican el consumo; `/usage` muestra cuánto gasta cada uno.

## Más allá: trabajo en paralelo

| Opción | Qué es | Estado |
| --- | --- | --- |
| Subagentes | Trabajadores dentro de una sesión | Estable |
| Worktrees (`claude --worktree`) | Cada sesión en su propia copia de Git para no pisarse | Estable |
| Agent view (`claude agents`) | Una pantalla para lanzar y vigilar sesiones en segundo plano | Vista previa |
| Agent teams | Un líder coordina varias sesiones con lista de tareas compartida y mensajes entre ellas | Experimental, desactivado por defecto |
| Dynamic workflows | Un script que orquesta muchos subagentes y cruza sus resultados | Para auditorías o migraciones grandes |

Para este curso basta con dominar subagentes y worktrees. Los equipos de agentes son para cuando ya manejes bien lo anterior.

## Laboratorio (martes y miércoles)

**Parte A · Delegar y medir (martes)**

1. Abre una sesión nueva y ejecuta `/context`. Anota el uso.
2. Pide: "Usa un subagente para investigar cómo se manejan los errores en toda la solución y dame solo un resumen de máximo 10 líneas".
   *Comprueba:* ves la delegación en la transcripción (Explore o general-purpose) y el resumen llega sin los archivos completos.
3. Ejecuta `/context` otra vez y compara con el paso 1.
4. Repite la misma pregunta en otra sesión **sin** subagente y compara cuánto creció el contexto.
   *Comprueba:* puedes decir con números cuánto contexto ahorró el subagente.
5. Crea `.claude/agents/revisor-dotnet.md` con el ejemplo de arriba.
6. Introduce a propósito `using Microsoft.EntityFrameworkCore;` en una clase de Domain y pide: `@revisor-dotnet revisa mis cambios`.
   *Comprueba:* lo reporta como Crítico con archivo y línea.

**Parte B · Restringir y encadenar (miércoles)**

7. Crea `.claude/agents/escritor-pruebas.md` con `tools: Read, Grep, Glob, Edit, Write, Bash` y un hook de frontmatter que bloquee ediciones fuera de la carpeta de pruebas:
   ```markdown
   ---
   name: escritor-pruebas
   description: Escribe pruebas xUnit que reproducen problemas reportados. Solo edita la carpeta tests.
   tools: Read, Grep, Glob, Edit, Write, Bash
   hooks:
     PreToolUse:
       - matcher: "Edit|Write"
         hooks:
           - type: command
             command: powershell
             args: ["-NoProfile", "-ExecutionPolicy", "Bypass", "-File", "${CLAUDE_PROJECT_DIR}/.claude/hooks/solo-tests.ps1"]
   ---
   Escribe pruebas xUnit con FluentAssertions. Cada prueba debe fallar antes de la corrección.
   ```
8. Crea `.claude/hooks/solo-tests.ps1` (basado en `proteger.ps1` del Módulo 7) que salga con código 2 si la ruta no contiene `/tests/`. Pruébalo a mano. Acepta el diálogo de confianza de la carpeta: sin él, los hooks del frontmatter no se ejecutan.
9. Pide a `@escritor-pruebas` que "también corrija el código de producción".
   *Comprueba:* el hook impide que toque archivos fuera de `tests/`.
10. Ejecuta `/tasks` mientras un subagente trabaja y detén uno.
11. Usa `/subtask redacta el README de VisitasAPI con lo que hemos hecho` y sigue trabajando mientras termina.
    *Comprueba:* el resultado llega como mensaje cuando termina y el README menciona cosas de esta conversación (porque la bifurcación la heredó).

## Reto (jueves)

Encadena subagentes: "Usa revisor-dotnet para encontrar problemas en VisitaService y luego escritor-pruebas para cubrir cada problema con una prueba que falle". Después arregla tú mismo, sin Claude, al menos una de esas pruebas y explica en el commit por qué fallaba.

## Preguntas de control (sábado)

1. ¿Qué problema de contexto resuelve un subagente?
2. ¿Qué recibe y qué no recibe un subagente al iniciar?
3. ¿Por qué un revisor no debería tener `Edit` ni `Write`?
4. ¿Qué diferencia hay entre un subagente normal y una bifurcación con `/subtask`?
5. ¿Qué costo tiene lanzar muchos subagentes en paralelo?
