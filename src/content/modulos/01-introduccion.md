---
numero: 1
titulo: "Introducción a Claude Code"
semana: 1
objetivo: "Instalar Claude Code, entender cómo trabaja por dentro y crear el esqueleto de VisitasAPI."
ogImage: "/og/01-introduccion.png"
fuentes:
  - titulo: "Overview"
    url: "https://code.claude.com/docs/en/overview"
  - titulo: "How Claude Code works"
    url: "https://code.claude.com/docs/en/how-claude-code-works"
  - titulo: "Quickstart"
    url: "https://code.claude.com/docs/en/quickstart"
---

## Conceptos clave

- **Qué es:** una herramienta de programación agéntica. Lee tu código, edita archivos, ejecuta comandos y se integra con tus herramientas. Funciona en la terminal, en VS Code, en JetBrains, en la app de escritorio y en la web, y todas comparten el mismo motor.
- **El ciclo agéntico:** Claude trabaja en tres fases que se repiten: reunir contexto, actuar y verificar. Puedes interrumpirlo en cualquier momento.
- **Modelo + herramientas:** el modelo razona y las herramientas actúan (archivos, búsqueda, ejecución de comandos, web e inteligencia de código). Cambias de modelo con `/model`.
- **Ventana de contexto:** guarda la conversación, los archivos leídos, CLAUDE.md y las skills cargadas. Cuando se llena, Claude la compacta (la resume) y puede perder instrucciones dadas al principio. Las reglas permanentes van en CLAUDE.md (Módulo 4).
- **Sesiones:** cada sesión empieza con el contexto limpio. Se guardan en `~/.claude/projects/` y se retoman con `claude --continue` o `claude --resume`.
- **Checkpoints:** antes de editar un archivo, Claude guarda una copia. `Esc` dos veces (o `/rewind`) deshace cambios en archivos, pero no cambios en bases de datos, APIs externas ni los hechos con comandos de shell.

## Comandos esenciales

| Comando o tecla | Para qué sirve |
| --- | --- |
| `claude` | Inicia una sesión interactiva en la carpeta actual |
| `claude -p "pregunta"` | Ejecuta una sola consulta y termina (modo no interactivo) |
| `claude --continue` | Retoma la última conversación |
| `claude --resume` | Elige una conversación anterior de una lista |
| `/init` | Genera un CLAUDE.md inicial para el proyecto |
| `/context` | Muestra qué ocupa la ventana de contexto |
| `/compact` | Resume la conversación para liberar espacio |
| `/clear` | Empieza de cero en la misma sesión |
| `/model` | Cambia de modelo |
| `/doctor` | Revisa la instalación y la configuración |
| `Esc` | Detiene a Claude en el acto |
| `Esc` `Esc` | Abre el menú para volver a un checkpoint |

## Laboratorio (martes y miércoles)

**Parte A · Instalación (martes)**

1. En PowerShell ejecuta `irm https://claude.ai/install.ps1 | iex`. Cierra la ventana, abre una nueva y ejecuta `claude --version`.
   *Comprueba:* aparece un número de versión. Si dice que `claude` no se reconoce, la carpeta de instalación no está en el PATH; sigue la guía de solución de problemas de instalación.
2. Instala [Git for Windows](https://git-scm.com/downloads/win) si no lo tienes. Con él, Claude puede usar Bash; sin él, usa PowerShell.
   *Comprueba:* `git --version` responde.
3. Verifica .NET con `dotnet --list-sdks`.
   *Comprueba:* aparece una versión 8.x.
4. Crea la solución a mano, sin IA:
   ```powershell
   mkdir VisitasAPI; cd VisitasAPI
   dotnet new sln -n VisitasAPI
   dotnet new classlib -n Domain -o src/Domain
   dotnet new classlib -n Application -o src/Application
   dotnet new classlib -n Infrastructure -o src/Infrastructure
   dotnet new webapi -n Api -o src/Api --use-controllers
   dotnet sln add (Get-ChildItem -Recurse -Filter *.csproj).FullName
   dotnet add src/Application/Application.csproj reference src/Domain/Domain.csproj
   dotnet add src/Infrastructure/Infrastructure.csproj reference src/Application/Application.csproj
   dotnet add src/Api/Api.csproj reference src/Application/Application.csproj src/Infrastructure/Infrastructure.csproj
   dotnet new gitignore
   git init; git add .; git commit -m "Estructura inicial"
   ```
   *Comprueba:* `dotnet build` termina sin errores.

**Parte B · Primera sesión (miércoles)**

5. Dentro de la carpeta ejecuta `claude` e inicia sesión cuando te lo pida.
6. Pregunta sin pedir cambios: "Explícame la estructura de esta solución y cómo se relacionan los proyectos".
   *Comprueba:* en la salida ves qué herramientas usó para reunir contexto (lectura de archivos, búsqueda). Anótalas.
7. Pulsa `Shift+Tab` hasta ver **manual mode** en la barra inferior. Así cada cambio te pedirá aprobación.
8. Pide: "Agrega la entidad Sede en Domain con Id, Nombre, Comuna y Dirección". Antes de aprobar, escribe en un papel qué archivo crees que va a crear.
   *Comprueba:* tu predicción coincide con el archivo propuesto. Si no, pregúntale por qué eligió esa ubicación.
9. Pulsa `Esc` `Esc`, elige el mensaje anterior y restaura el código.
   *Comprueba:* `git status` ya no muestra el archivo nuevo.
10. Vuelve a pedirlo con otra redacción y acéptalo. Ejecuta `/context` y anota qué ocupa más espacio. Cierra con `/exit` y vuelve con `claude --continue`.
    *Comprueba:* Claude recuerda que acabas de crear `Sede`.

## Reto (jueves)

Pide a Claude que agregue las entidades `Supervisor`, `Visita` y `Hallazgo` con sus relaciones (una visita pertenece a una sede y a un supervisor; una visita tiene varios hallazgos). Luego, sin Claude, dibuja en papel el diagrama de relaciones y compáralo con lo que generó. Corrige con un nuevo prompt cualquier diferencia que no te convenza y haz commit.

## Preguntas de control (sábado)

1. ¿Cuáles son las tres fases del ciclo agéntico y en cuál lee archivos Claude?
2. ¿Qué diferencia hay entre `claude --continue` y empezar una sesión nueva?
3. ¿Por qué un checkpoint no te protege si Claude borra datos de una base de datos?
4. ¿Qué pasa con las instrucciones que diste al principio cuando la conversación se compacta?
