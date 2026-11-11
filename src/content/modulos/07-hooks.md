---
numero: 7
titulo: "Hooks y automatización basada en eventos"
semana: 7
objetivo: "Convertir las reglas que deben cumplirse siempre en comandos que se ejecutan solos, sin depender de que Claude se acuerde."
ogImage: "/og/07-hooks.png"
fuentes:
  - titulo: "Automate actions with hooks"
    url: "https://code.claude.com/docs/en/hooks-guide"
  - titulo: "Hooks reference"
    url: "https://code.claude.com/docs/en/hooks"
---

## Por qué hooks

CLAUDE.md es una sugerencia; un hook es una garantía. Un hook es un comando que Claude Code ejecuta automáticamente en un momento fijo del trabajo: antes de usar una herramienta, después de editar un archivo o al terminar de responder. Si la regla es "siempre, sin excepción", va en un hook.

| Mecanismo | ¿Quién decide si se cumple? | Úsalo para |
| --- | --- | --- |
| CLAUDE.md | El modelo (puede olvidarlo) | Convenciones y contexto |
| Regla de permisos | Claude Code, comparando texto | Permitir, preguntar o bloquear herramientas |
| Hook | Tu script, con lógica propia | Validaciones con condiciones, formateo, avisos, pruebas obligatorias |

## Eventos más usados

| Evento | Cuándo se dispara | Uso típico |
| --- | --- | --- |
| `PreToolUse` | Antes de ejecutar una herramienta; puede bloquearla | Proteger archivos, validar comandos |
| `PostToolUse` | Después de que una herramienta termina bien | Formatear el archivo editado |
| `UserPromptSubmit` | Al enviar un prompt, antes de que Claude lo procese | Agregar contexto (rama actual, fecha) |
| `Stop` | Cuando Claude termina de responder | Exigir que las pruebas pasen |
| `SessionStart` | Al iniciar o retomar sesión, también tras compactar | Reinyectar contexto importante |
| `Notification` | Cuando Claude necesita tu atención | Aviso en el escritorio |
| `SessionEnd` | Al cerrar la sesión | Limpieza |

Hay más de 30 eventos; la lista completa está en la referencia de hooks.

## Cómo funciona un hook

1. **Entrada:** Claude Code le pasa al hook un JSON por la entrada estándar con `session_id`, `cwd`, `hook_event_name`, `tool_name` y `tool_input` (por ejemplo, `tool_input.file_path` o `tool_input.command`).
2. **Filtro:** el `matcher` decide para qué herramientas corre: `"Edit|Write"` solo tras editar archivos. El campo `if` filtra más fino con sintaxis de permisos, por ejemplo `"Bash(git *)"`, y solo funciona en eventos de herramientas.
3. **Salida por código:** `0` = sin objeción (el flujo normal de permisos sigue); `2` = bloquear, y el texto que escribas en stderr le llega a Claude como explicación. Cualquier otro código es un error que no bloquea.
4. **Salida por JSON:** para más control, sal con `0` e imprime un JSON, por ejemplo `{"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny", "permissionDecisionReason": "..."}}`. Usa código 2 **o** JSON, no ambos.
5. **Varios hooks del mismo evento** corren en paralelo. Si uno niega y otro permite, gana la decisión más restrictiva.

**Tipos de hook:** `command` (comando, el más común), `http` (envía el evento a una URL), `prompt` (un modelo decide sí o no), `agent` (un subagente verifica con herramientas; experimental) y `mcp_tool`.

## Hooks en Windows: lo que debes saber

En Windows, un hook escrito como texto (forma *shell*) se ejecuta con **Git Bash** si lo tienes instalado, o con **PowerShell** si no. Como `$CLAUDE_PROJECT_DIR` se escribe distinto en cada shell, usa la **forma exec**: el campo `args` hace que el comando se ejecute sin shell, cada elemento es un argumento y Claude Code reemplaza `${CLAUDE_PROJECT_DIR}` por la ruta del proyecto. Además, PowerShell bloquea scripts `.ps1` por defecto, así que pasa `-ExecutionPolicy Bypass`.

```json
{
  "type": "command",
  "command": "powershell",
  "args": ["-NoProfile", "-ExecutionPolicy", "Bypass", "-File", "${CLAUDE_PROJECT_DIR}/.claude/hooks/proteger.ps1"]
}
```

Dentro de un script de PowerShell, la variable de entorno se lee como `$env:CLAUDE_PROJECT_DIR`. Usa barras `/` en las rutas de `args`.

## Hooks para VisitasAPI

**Script 1: proteger migraciones y secretos** (`.claude/hooks/proteger.ps1`)

```powershell
$datos = [Console]::In.ReadToEnd() | ConvertFrom-Json
$ruta = "$($datos.tool_input.file_path)" -replace '\\', '/'
$protegidos = @('/Migrations/', 'appsettings.Production.json', '/.env')
foreach ($p in $protegidos) {
  if ($ruta -like "*$p*") {
    [Console]::Error.WriteLine("Bloqueado: $ruta coincide con '$p'. Usa 'dotnet ef migrations add' para cambiar el esquema.")
    exit 2
  }
}
exit 0
```

**Script 2: formatear el archivo editado** (`.claude/hooks/formatear.ps1`)

```powershell
$datos = [Console]::In.ReadToEnd() | ConvertFrom-Json
$ruta = "$($datos.tool_input.file_path)"
if ($ruta -like '*.cs') {
  Push-Location $env:CLAUDE_PROJECT_DIR
  $relativa = Resolve-Path -Relative $ruta
  dotnet format whitespace --folder --include $relativa | Out-Null
  Pop-Location
}
exit 0
```

**Registro en `.claude/settings.json`**

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [{
          "type": "command",
          "command": "powershell",
          "args": ["-NoProfile", "-ExecutionPolicy", "Bypass", "-File", "${CLAUDE_PROJECT_DIR}/.claude/hooks/proteger.ps1"]
        }]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [{
          "type": "command",
          "command": "powershell",
          "args": ["-NoProfile", "-ExecutionPolicy", "Bypass", "-File", "${CLAUDE_PROJECT_DIR}/.claude/hooks/formatear.ps1"]
        }]
      }
    ],
    "Stop": [
      {
        "hooks": [{
          "type": "agent",
          "prompt": "Ejecuta dotnet test en la raíz del proyecto. Si alguna prueba falla, responde ok:false indicando cuáles fallaron. $ARGUMENTS",
          "timeout": 180
        }]
      }
    ]
  }
}
```

## Límites que debes conocer

- Un `PreToolUse` que niega bloquea incluso en modo `bypassPermissions`. Pero un hook que dice `allow` no salta las reglas `deny`.
- `PostToolUse` no puede deshacer lo que ya pasó.
- Claude también puede modificar archivos con comandos de shell (Bash o PowerShell); un matcher `Edit|Write` no los ve. Para cobertura total agrega `Bash|PowerShell` al matcher o revisa `git status --porcelain` en un hook `Stop`.
- Si un hook falla o se demora, por defecto la acción sigue. Para que un fallo bloquee, agrega `"onFailure": "block"` (versión 2.1.295 o superior).
- Un `Stop` que bloquea muchas veces seguidas se anula tras 8 intentos; revisa el campo `stop_hook_active` para no crear ciclos.
- Los hooks ejecutan comandos con tus permisos: revisa cualquier hook que venga en un repositorio ajeno antes de confiar en la carpeta.

## Diagnóstico

| Síntoma | Qué revisar |
| --- | --- |
| El hook nunca corre | `/hooks`: ¿aparece bajo el evento correcto? ¿El matcher coincide exactamente (distingue mayúsculas)? |
| "hook error" en la transcripción | Prueba el script a mano con un JSON de ejemplo y revisa `$LASTEXITCODE` |
| No sé qué hizo el hook | `Ctrl+O` abre la transcripción; `claude --debug-file ruta.log` registra entrada, salida y código |
| El JSON del hook no tiene efecto | Algo más escribe en stdout antes del JSON, o un campo está en el nivel equivocado |

## Laboratorio (martes y miércoles)

**Parte A · Bloquear (martes)**

1. Crea la carpeta `.claude/hooks/` y el script `proteger.ps1`.
2. Pruébalo a mano, sin Claude:
   ```powershell
   '{"tool_input":{"file_path":"src/Infrastructure/Migrations/x.cs"}}' | powershell -NoProfile -ExecutionPolicy Bypass -File .claude/hooks/proteger.ps1; $LASTEXITCODE
   '{"tool_input":{"file_path":"src/Domain/Sede.cs"}}' | powershell -NoProfile -ExecutionPolicy Bypass -File .claude/hooks/proteger.ps1; $LASTEXITCODE
   ```
   *Comprueba:* el primero imprime "Bloqueado…" y devuelve 2; el segundo devuelve 0.
3. Registra el hook `PreToolUse` en `.claude/settings.json`.
4. En Claude, ejecuta `/hooks`.
   *Comprueba:* el hook aparece bajo **PreToolUse**.
5. Pide: "corrige el nombre de una columna editando la migración inicial".
   *Comprueba:* Claude recibe el mensaje de bloqueo y cambia de enfoque (propone `dotnet ef migrations add`).
6. Abre `Ctrl+O` y ubica el resultado del hook en la transcripción.

**Parte B · Formatear y exigir pruebas (miércoles)**

7. Crea `formatear.ps1` y regístralo en `PostToolUse`.
8. Pide un cambio pequeño en `Sede.cs` y desordena tú la indentación antes de aceptar.
   *Comprueba:* después de la edición, el archivo queda bien indentado.
9. Inicia con `claude --debug-file hooks.log`, repite el paso 8 y abre `hooks.log`.
   *Comprueba:* encuentras la ejecución del hook y su código de salida.
10. Agrega el hook `Stop` de tipo `agent`.
11. Rompe una prueba a propósito y pide una tarea pequeña que no tenga relación con ella.
    *Comprueba:* Claude no termina hasta que la prueba vuelve a pasar.

## Reto (jueves)

Crea un hook `UserPromptSubmit` que agregue al contexto la rama actual y la cantidad de archivos modificados (usa `git branch --show-current` y `git status --porcelain`). El script debe imprimir un JSON con `hookSpecificOutput.additionalContext`. Pruébalo a mano antes de registrarlo y luego pregúntale a Claude "¿en qué rama estoy?" sin que pueda usar herramientas.

Después escribe con tus palabras, en máximo cinco líneas, qué diferencia hay entre tu hook `Stop` y escribir "ejecuta las pruebas" en CLAUDE.md.

## Preguntas de control (sábado)

1. ¿Qué significa salir con código 2 en un hook `PreToolUse`?
2. ¿Por qué un hook es más confiable que una instrucción en CLAUDE.md?
3. ¿Qué evento usarías para formatear y cuál para bloquear?
4. ¿Por qué en Windows conviene la forma exec (`args`) con `-ExecutionPolicy Bypass`?
5. ¿Qué cambios de archivos no ve un matcher `Edit|Write` y cómo los cubres?
