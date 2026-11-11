---
numero: 5
titulo: "Modos de operación, permisos y seguridad"
semana: 5
objetivo: "Decidir cuánta autonomía darle a Claude en cada situación y proteger VisitasAPI con reglas que no dependan de lo que Claude decida."
ogImage: "/og/05-permisos-seguridad.png"
fuentes:
  - titulo: "Choose a permission mode"
    url: "https://code.claude.com/docs/en/permission-modes"
  - titulo: "Configure permissions"
    url: "https://code.claude.com/docs/en/permissions"
  - titulo: "Security"
    url: "https://code.claude.com/docs/en/security"
  - titulo: "Sandboxing"
    url: "https://code.claude.com/docs/en/sandboxing"
---

## Los seis modos de permisos

| Modo (valor) | Qué hace sin preguntarte | Úsalo para |
| --- | --- | --- |
| Manual (`default`) | Solo lecturas | Código sensible o que no conoces |
| Aceptar ediciones (`acceptEdits`) | Lecturas, edición de archivos y comandos como `mkdir` o `mv` dentro del proyecto | Iterar y revisar después con `git diff` |
| Plan (`plan`) | Lee y explora, pero no edita tu código | Analizar antes de cambiar |
| Auto (`auto`) | Casi todo; un modelo clasificador revisa cada acción y bloquea las riesgosas | Tareas largas sin interrupciones |
| No preguntar (`dontAsk`) | Solo lo preaprobado; lo demás se rechaza | Scripts y CI |
| Omitir permisos (`bypassPermissions`) | Todo | Solo contenedores o máquinas virtuales aisladas |

Desde la versión 2.1.283, **Auto es el modo inicial** en la terminal y en VS Code. En la terminal cambias de modo con `Shift+Tab` (Auto → Manual → Aceptar ediciones → Plan) o al iniciar con `claude --permission-mode plan`.

## Qué bloquea el modo Auto por defecto

El clasificador confía en tu carpeta de trabajo y en los remotos de Git configurados al iniciar. Bloquea, entre otras cosas: descargar y ejecutar código (`curl | bash`), enviar datos sensibles a sitios externos, despliegues y migraciones en producción, `git push --force`, `git reset --hard` y borrar archivos que ya existían. Si le dices en la conversación "no hagas push", lo respeta, pero esa frase puede perderse al compactar. Para una garantía real usa una regla `deny`.

## Reglas de permisos

Las reglas viven en `settings.json` y las hace cumplir Claude Code, no el modelo. Se evalúan en este orden: **deny → ask → allow**. La primera coincidencia gana, y un `deny` en cualquier nivel no se puede anular con un `allow`.

```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "permissions": {
    "allow": [
      "Bash(dotnet build *)",
      "Bash(dotnet test *)",
      "Bash(git commit *)"
    ],
    "ask": [
      "Bash(git push *)",
      "Bash(dotnet ef database update *)"
    ],
    "deny": [
      "Read(./.env)",
      "Read(**/appsettings.Production.json)",
      "Edit(src/Infrastructure/Migrations/**)"
    ]
  }
}
```

| Sintaxis | Qué cubre |
| --- | --- |
| `Bash(dotnet test *)` | Cualquier comando que empiece con `dotnet test`. El `*` va después del subcomando |
| `Read(./.env)` | Leer ese archivo; también bloquea editarlo |
| `Edit(src/**)` | Editar cualquier archivo bajo `src/` |
| `WebFetch(domain:learn.microsoft.com)` | Descargar páginas de ese dominio |
| `mcp__github__*` | Todas las herramientas del servidor MCP `github` |

**Cuidado:** una regla de Bash compara el texto del comando. `Bash(git push *)` en `deny` no detiene `git -C . push`. Para un límite real del sistema operativo existe el sandbox (`/sandbox`), disponible en macOS, Linux y WSL2 (no en Windows nativo).

## Dónde van las configuraciones (de mayor a menor prioridad)

| Archivo | Alcance | ¿Se sube a Git? |
| --- | --- | --- |
| Configuración administrada (TI) | Toda la organización; nadie la puede anular | No aplica |
| `.claude/settings.local.json` | Solo tú, en este repositorio | No |
| `.claude/settings.json` | Todo el equipo, en este repositorio | Sí |
| `~/.claude/settings.json` | Tú, en todos tus proyectos | No |

Cuando eliges "Sí, y no volver a preguntar", Claude guarda la regla en `.claude/settings.local.json`. Con `/permissions` ves todas las reglas y de qué archivo viene cada una.

## Buenas prácticas de seguridad

- Usa Manual al abrir código de terceros y acepta el diálogo de confianza solo en carpetas que conoces.
- Nunca guardes secretos en CLAUDE.md. Bloquéalos con reglas `Read` en `deny`.
- Los checkpoints no deshacen cambios en bases de datos ni APIs: protege esos comandos con `ask` o `deny`.
- Reserva `bypassPermissions` para contenedores sin acceso a internet.

## Laboratorio (martes y miércoles)

**Parte A · Modos (martes)**

1. Haz commit de todo lo pendiente para poder comparar después.
2. En modo **Manual** pide: "agrega un endpoint GET /salud que devuelva OK". Anota cuántas veces te pidió permiso.
3. Deshaz con `Esc` `Esc` y repite en **Aceptar ediciones**, luego en **Plan** y por último en **Auto**.
   *Comprueba:* tienes una tabla con modo, preguntas recibidas y si llegó a editar.
4. Haz un cambio a mano en `Sede.cs` sin hacer commit. En modo Auto pide: "deja el repositorio exactamente como estaba en el último commit".
   *Observa:* si Claude intenta `git reset --hard` o `git checkout -- .`, el clasificador lo bloquea porque descartaría trabajo sin guardar que no pediste borrar explícitamente. Anota qué alternativa propone Claude.

**Parte B · Reglas (miércoles)**

5. Crea `.claude/settings.json` con el ejemplo de arriba. Gracias a `$schema`, VS Code te autocompleta las claves.
6. Crea un `.env` falso con `CLAVE=prueba` (agrégalo a `.gitignore`) y pide a Claude que lo lea.
   *Comprueba:* la regla lo bloquea.
7. Pide "aplica la migración a la base de datos".
   *Comprueba:* te pregunta antes de ejecutar `dotnet ef database update`.
8. Pide "corrige un error en la migración inicial editando el archivo".
   *Comprueba:* la regla `Edit` sobre `Migrations/**` lo impide, aunque estés en modo Auto. Este es el cierre del reto del Módulo 4.
9. Abre `/permissions`, revisa las pestañas Allow, Ask y Deny y la de denegaciones recientes.
10. Pide `dotnet build` y elige "Sí, y no volver a preguntar".
    *Comprueba:* aparece una regla nueva en `.claude/settings.local.json`.

## Reto (jueves)

Diseña la política de permisos de VisitasAPI para un compañero que recién llega: qué va en `settings.json` del equipo y qué en tu `settings.local.json`. Justifica cada regla en el mensaje del commit.

## Preguntas de control (sábado)

1. ¿En qué orden se evalúan deny, ask y allow, y qué pasa si un deny y un allow coinciden?
2. ¿Por qué escribir "no hagas push" en CLAUDE.md no es una garantía?
3. ¿Qué diferencia hay entre `acceptEdits` y `auto`?
4. ¿En qué entorno es aceptable usar `bypassPermissions`?
