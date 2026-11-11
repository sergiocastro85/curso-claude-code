# Verificación técnica del contenido

Revisión del 9 de noviembre de 2026 contra la documentación oficial de Claude Code (code.claude.com/docs) y las novedades publicadas hasta v2.1.316 (31 de octubre de 2026). No se encontraron cambios oficiales que invaliden el temario.

## Errores corregidos

| Módulo | Problema | Corrección |
| --- | --- | --- |
| 07 | El hook usaba `$CLAUDE_PROJECT_DIR` en forma *shell*. En Windows sin Git Bash los hooks corren en PowerShell, donde esa variable no existe, así que la ruta quedaba vacía. | Forma exec (`command` + `args`), donde Claude Code sustituye `${CLAUDE_PROJECT_DIR}` sin depender del shell. |
| 07 | `powershell -File script.ps1` falla con la política de ejecución por defecto de Windows (scripts bloqueados). | Se agregó `-ExecutionPolicy Bypass` al comando del hook. |
| 07 | `dotnet format --include` con ruta absoluta y sin solución explícita podía no encontrar el archivo y era lento. | `dotnet format whitespace --folder --include` con ruta relativa a la raíz del proyecto. |
| 01 | `dotnet new webapi` en .NET 8 crea Minimal APIs, pero el curso usa controladores (`SedesController`). | Se agregó `--use-controllers`. |
| 01 | `dotnet sln add (Get-ChildItem …)` en Windows PowerShell 5.1 puede pasar solo el nombre del archivo. | Se usa `.FullName`. |
| 01 | `dotnet add … reference` con carpetas en vez de `.csproj`. | Rutas completas a cada `.csproj`; se agregó `dotnet new gitignore`. |
| 05 | El paso "pide `git reset --hard`" podía no bloquearse: si el usuario nombra la acción explícitamente, el clasificador puede tomarlo como aprobación. | El laboratorio ahora deja que Claude elija la acción y observa el bloqueo. |
| 06 | Regla de ejemplo `mcp__github__delete_*` dependía de nombres de herramientas no verificados. | `"ask": ["mcp__github__*"]`, que cubre todo el servidor. |
| 06 | El reto con DBHub afirmaba que la base sería de solo lectura sin indicar cómo. | Se pide configurar la opción de solo lectura (o un usuario sin escritura) y comprobar que la escritura falla. |
| 08 | "Edición solo en la carpeta de pruebas" no explicaba cómo, y las reglas de permisos son de toda la sesión. | Hook en el frontmatter del subagente, con el aviso de que requiere aceptar la confianza de la carpeta. |

## Afirmaciones contrastadas (sin cambios)

- Instalación en Windows (`irm https://claude.ai/install.ps1 | iex`), Git for Windows opcional.
- Auto como modo inicial desde v2.1.283; ciclo de `Shift+Tab`; orden deny → ask → allow; `Read` deny también bloquea Edit y Write; sandbox en macOS, Linux y WSL2.
- Ubicaciones de CLAUDE.md, límite de 200 líneas / 25 KB de `MEMORY.md`, `/doctor prompt-audit`, `.claude/rules/` con `paths`.
- Requisito de VS Code 1.94, atajos de Windows, `@terminal:nombre`, `/plan`, rewind por mensaje.
- Comandos MCP, alcances y precedencia, límites de salida (10.000 / 25.000 tokens), endpoint de Microsoft Learn MCP.
- Eventos y códigos de salida de hooks, tope de 8 bloqueos en `Stop`, `onFailure: "block"` desde v2.1.295.
- Campos de subagentes, ejecución en segundo plano por defecto, `/subtask`, agent teams experimentales.
- Campos de skills, `$ARGUMENTS` y `arguments`, `/skill-doctor`, estructura y comandos de plugins.

## Pendiente de verificar en una máquina real

Nadie ha ejecutado aún los laboratorios de principio a fin. Antes de publicar cada módulo, alguien debe seguir sus pasos en Windows 11 con .NET 8 y marcar cada *Comprueba*. Prioridad: Módulo 7 (hooks en PowerShell) y Módulo 6 (token de GitHub y DBHub).
