---
numero: 2
titulo: "Claude Code con VS Code y Cursor"
semana: 2
objetivo: "Trabajar con Claude dentro del editor, revisar sus cambios en diffs visuales y saber cuándo usar la extensión y cuándo la terminal."
ogImage: "/og/02-vscode-cursor.png"
fuentes:
  - titulo: "Use Claude Code in VS Code"
    url: "https://code.claude.com/docs/en/vs-code"
---

## Conceptos clave

- **La extensión es la forma recomendada** de usar Claude Code en VS Code. Requiere VS Code 1.94 o superior. En Cursor se instala la misma extensión (`anthropic.claude-code`), y también funciona en otros editores derivados de VS Code.
- **El ícono Spark** abre el panel. Aparece arriba a la derecha del editor cuando hay un archivo abierto, en la barra lateral y en la barra de estado como "✻ Claude Code".
- **Contexto desde el editor:** Claude ve automáticamente el texto seleccionado y el archivo abierto. Con `@archivo` o `@carpeta/` le das archivos concretos, y con `@terminal:nombre` le pasas la salida de una terminal.
- **Revisión de cambios:** en modo Manual ves un diff lado a lado y puedes aceptar o rechazar cada cambio por separado. Si editas la propuesta antes de aceptarla, Claude se entera.
- **Extensión y CLI comparten** la configuración (`~/.claude/settings.json`) y el historial. La extensión trae su propia copia del CLI, pero para escribir `claude` en la terminal necesitas el CLI instalado aparte (Módulo 1).
- **Solo en el CLI:** todos los comandos, el atajo `!` para correr comandos de shell y el autocompletado con Tab. Si necesitas algo de eso, abre la terminal integrada y ejecuta `claude`. Desde una terminal externa, `/ide` la conecta con VS Code.

## Atajos en Windows

| Atajo | Acción |
| --- | --- |
| `Ctrl+Esc` | Alternar el foco entre el editor y Claude |
| `Ctrl+Shift+Esc` | Abrir una conversación nueva en una pestaña |
| `Alt+K` | Insertar una referencia `@archivo#líneas` de lo seleccionado |
| `Shift+Enter` | Nueva línea sin enviar |
| `Ctrl+Alt+F` | Vista enfocada: oculta las llamadas a herramientas |
| `Ctrl+Shift+T` | Reabrir la última sesión cerrada |

## Laboratorio (martes y miércoles)

**Parte A · Extensión y revisión de cambios (martes)**

1. Abre Extensiones (`Ctrl+Shift+X`), busca "Claude Code" e instálala. Si usas Cursor, haz lo mismo allí.
   *Comprueba:* aparece "✻ Claude Code" en la barra de estado.
2. Abre la carpeta de VisitasAPI y el archivo `Sede.cs`. Haz clic en el ícono Spark e inicia sesión.
3. En el indicador de modo (debajo del cuadro de texto) elige **Manual**.
4. Selecciona la clase `Sede`, pulsa `Alt+K` y pide: "Agrega validaciones para que Nombre no esté vacío ni supere 120 caracteres".
   *Comprueba:* el mensaje incluye una referencia tipo `@Sede.cs#3-12`.
5. En el diff, acepta un cambio con **Accept this change** y rechaza otro con **Reject this change**.
   *Comprueba:* el archivo final solo contiene el cambio aceptado.
6. Escribe `/plan crear el DbContext con EF Core y la migración inicial`. El plan se abre como documento: agrega un comentario en una línea (por ejemplo, "usa SQLite en desarrollo") y apruébalo.
   *Comprueba:* la implementación respeta tu comentario.

**Parte B · Historial, checkpoints y CLI (miércoles)**

7. Pasa el mouse sobre un mensaje anterior y elige **Rewind code to here**.
   *Comprueba:* `git diff` muestra que el código volvió a ese punto y la conversación sigue completa.
8. Abre la terminal integrada (`` Ctrl+` ``) y ejecuta `claude --resume`. Elige la misma conversación.
   *Comprueba:* desde el CLI, Claude recuerda lo que hicieron en la extensión.
9. En la terminal ejecuta `dotnet build` y luego, en el panel, pregunta: "Revisa la salida de @terminal:pwsh y explícame cada advertencia" (usa el nombre real de tu terminal).
10. Abre **Session history**, renombra la sesión como `modulo-2` y archiva una conversación vieja.

## Reto (jueves)

Trabaja con dos conversaciones en paralelo (`Ctrl+Shift+Esc`): en una pide el `SedesController` con CRUD completo; en la otra, pruebas unitarias para la entidad `Visita`. Luego compila con `dotnet build` y resuelve tú mismo el primer error que aparezca antes de pedir ayuda. Anota cuánto tardaste y qué aprendiste del error.

## Preguntas de control (sábado)

1. ¿Qué tres cosas no puedes hacer desde la extensión y sí desde el CLI?
2. ¿Dónde se guarda la configuración que comparten la extensión y el CLI?
3. ¿Qué diferencia hay entre "Rewind code to here" y "Fork conversation from here"?
4. ¿Por qué la documentación recomienda el modo Manual al abrir código que no conoces?
