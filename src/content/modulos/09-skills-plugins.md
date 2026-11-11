---
numero: 9
titulo: "Skills y plugins en Claude Code"
semana: 9
objetivo: "Empaquetar tus procedimientos repetidos como skills y compartir todo lo que construiste (skills, subagentes, hooks y MCP) como un plugin."
ogImage: "/og/09-skills-plugins.png"
fuentes:
  - titulo: "Extend Claude with skills"
    url: "https://code.claude.com/docs/en/skills"
  - titulo: "Plugins overview"
    url: "https://code.claude.com/docs/en/plugins/overview"
  - titulo: "Create a plugin"
    url: "https://code.claude.com/docs/en/plugins/create"
  - titulo: "Plugin security and trust"
    url: "https://code.claude.com/docs/en/plugins/security"
---

## Qué es una skill

Una skill es un archivo `SKILL.md` con instrucciones que Claude carga cuando son relevantes o cuando escribes `/nombre-skill`. Créala cuando te descubras pegando las mismas instrucciones una y otra vez, o cuando una parte de CLAUDE.md dejó de ser un dato y se volvió un procedimiento.

**Ventaja clave:** al inicio solo se carga la descripción; el contenido completo entra al contexto cuando se usa. Los antiguos comandos de `.claude/commands/` ahora son skills y siguen funcionando.

## ¿CLAUDE.md, skill, subagente, hook o MCP?

| Necesitas… | Usa |
| --- | --- |
| Datos que aplican en cada sesión (comandos, convenciones) | CLAUDE.md |
| Un procedimiento o conocimiento que se usa a veces | Skill |
| Una tarea aislada que devuelve un resumen | Subagente |
| Algo que debe pasar siempre, sin excepción | Hook |
| Conectarte a un sistema externo | MCP |
| Compartir varios de los anteriores como una unidad | Plugin |

## Dónde viven las skills

| Ubicación | Ruta | Alcance |
| --- | --- | --- |
| Personal | `~/.claude/skills/<nombre>/SKILL.md` | Todos tus proyectos |
| Proyecto | `.claude/skills/<nombre>/SKILL.md` | Este repositorio; se sube a Git |
| Plugin | `<plugin>/skills/<nombre>/SKILL.md` | Donde esté activo, como `/plugin:skill` |
| Cuenta de claude.ai | Skills activadas en tu cuenta | Se sincronizan si inicias sesión con claude.ai |

Las skills de tu cuenta de claude.ai se descargan en `~/.claude/skills/synced/`. Cámbialas en claude.ai, no en esa carpeta: la próxima sincronización sobrescribe los cambios locales.

## Campos clave del encabezado

| Campo | Para qué |
| --- | --- |
| `description` | Cuándo usarla. Pon primero el caso de uso principal (máximo 1.536 caracteres junto con `when_to_use`) |
| `disable-model-invocation: true` | Solo tú la invocas. Para acciones con efectos: desplegar, hacer commit |
| `user-invocable: false` | Solo Claude la usa. Para conocimiento de fondo |
| `allowed-tools` | Herramientas que puede usar sin pedir permiso durante ese turno |
| `arguments` / `$ARGUMENTS` / `$0` | Recibir parámetros: `/nueva-entidad Hallazgo` |
| `context: fork` + `agent` | Ejecutarla en un subagente aislado |
| `paths` | Activarla solo al trabajar con ciertos archivos |
| `` !`comando` `` | Insertar la salida de un comando antes de que Claude lea la skill |

Algunas skills incluidas: `/code-review`, `/verify`, `/run`, `/batch`, `/debug`, `/loop`, `/doctor` y `/skill-doctor` (muestra qué skills no usas y cuánto contexto ocupan).

## Skill para VisitasAPI

`.claude/skills/nueva-entidad/SKILL.md`:

```markdown
---
name: nueva-entidad
description: Crea una entidad completa en VisitasAPI siguiendo Clean Architecture. Úsala cuando el usuario pida agregar una entidad o un CRUD nuevo.
arguments: [entidad]
allowed-tools: Bash(dotnet build *) Bash(dotnet test *)
---
## Estado actual
!`git status --short`

## Tarea
Crea la entidad $entidad siguiendo exactamente el patrón de Sede:
1. Entidad en Domain, sin dependencias externas.
2. DTOs y servicio en Application.
3. Configuración EF Core y repositorio en Infrastructure.
4. Controlador en Api con códigos HTTP y ProblemDetails.
5. Pruebas xUnit del servicio.
6. Ejecuta dotnet build y dotnet test; corrige hasta que pasen.
No crees la migración: dime el comando para que la ejecute yo.
```

Se invoca con `/nueva-entidad Hallazgo`. Mantén el `SKILL.md` por debajo de 500 líneas y mueve el material extenso a archivos de apoyo en la misma carpeta (por ejemplo, `ejemplos.md`), enlazándolos desde `SKILL.md` para que Claude sepa cuándo leerlos.

## Plugins

Un plugin es una carpeta que empaqueta skills, subagentes, hooks y servidores MCP para instalarlos como una sola unidad.

```text
visitas-toolkit/
├── .claude-plugin/plugin.json   ← nombre, versión, descripción
├── skills/nueva-entidad/SKILL.md
├── agents/revisor-dotnet.md
├── hooks/hooks.json
└── .mcp.json
```

| Acción | Comando |
| --- | --- |
| Explorar e instalar plugins | `/plugin` (pestaña Discover) |
| Agregar un marketplace | `/plugin marketplace add <usuario/repo>` |
| Instalar del marketplace oficial | `/plugin install <plugin>@claude-plugins-official` |
| Probar tu plugin sin publicarlo | `claude --plugin-dir ./visitas-toolkit` |
| Recargar tras cambios | `/reload-plugins` |
| Desactivar sin desinstalar | `claude plugin disable <plugin>` |

Al instalar eliges alcance: usuario (todos tus proyectos), proyecto (todo el equipo, vía `.claude/settings.json`) o local (solo tú en este repositorio).

En un plugin, las rutas de los hooks y servidores usan `${CLAUDE_PLUGIN_ROOT}` (la carpeta del plugin) en vez de `${CLAUDE_PROJECT_DIR}`. Los subagentes de un plugin ignoran los campos `hooks`, `mcpServers` y `permissionMode` por seguridad: pon esos hooks en `hooks/hooks.json` del plugin.

**Seguridad y costo:** un plugin ejecuta código con tus permisos; revísalo antes de instalarlo. Además, cada plugin activo agrega sus descripciones al contexto en cada turno, aunque no lo uses.

Como trabajas en C#, revisa en `/plugin` los plugins de inteligencia de código (LSP): le permiten a Claude ver errores de compilación justo después de editar.

## Laboratorio (martes y miércoles)

**Parte A · Skills (martes)**

1. Crea `.claude/skills/nueva-entidad/SKILL.md` con el ejemplo de arriba.
2. Escribe `/` en Claude y busca `nueva-entidad` en el menú.
   *Comprueba:* aparece con su descripción y la pista del argumento.
3. Ejecuta `/nueva-entidad Comuna`.
   *Comprueba:* revisa el diff contra los seis pasos de la skill. ¿Cumplió todos? ¿Te dio el comando de migración en vez de crearla?
4. En una sesión nueva pide, sin nombrar la skill: "agrega la entidad Programa con Id y Nombre".
   *Comprueba:* Claude usa la skill por su cuenta. Si no lo hace, mejora la `description` y repite.
5. Crea una skill personal en `~/.claude/skills/resumen-cambios/SKILL.md` que inserte `` !`git diff HEAD` `` y pida resumir los cambios y señalar riesgos. Agrégale `disable-model-invocation: true`.
   *Comprueba:* solo corre cuando tú escribes `/resumen-cambios`.
6. Ejecuta `/skill-doctor` y desactiva lo que no uses.

**Parte B · Plugins (miércoles)**

7. Ejecuta `/plugin`, revisa el marketplace oficial e instala un plugin útil para ti con alcance **local**.
   *Comprueba:* en la pestaña de instalados aparece con su alcance; anota su costo de contexto.
8. Crea la carpeta `visitas-toolkit` fuera del proyecto con `.claude-plugin/plugin.json`:
   ```json
   {
     "name": "visitas-toolkit",
     "version": "0.1.0",
     "description": "Skills, subagentes y hooks para proyectos .NET con Clean Architecture"
   }
   ```
9. Copia ahí la skill `nueva-entidad` (en `skills/`) y el subagente `revisor-dotnet` (en `agents/`).
10. En una carpeta vacía ejecuta `claude --plugin-dir ../visitas-toolkit` y escribe `/`.
    *Comprueba:* aparece `/visitas-toolkit:nueva-entidad`.

## Reto (jueves)

Completa el plugin `visitas-toolkit` con los hooks del Módulo 7 en `hooks/hooks.json` (con rutas `${CLAUDE_PLUGIN_ROOT}/scripts/...`) y el `.mcp.json` del Módulo 6. Pruébalo en un proyecto .NET nuevo creado desde cero y anota qué tuviste que ajustar para que funcione fuera de VisitasAPI.

## Preguntas de control (sábado)

1. ¿Por qué una skill cuesta menos contexto que poner lo mismo en CLAUDE.md?
2. ¿Cuándo usarías `disable-model-invocation: true`?
3. ¿Qué hace `` !`comando` `` en una skill?
4. ¿Cuándo vale la pena un plugin en vez de skills sueltas?
