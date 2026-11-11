---
numero: 6
titulo: "MCP (Model Context Protocol) con Claude Code"
semana: 6
objetivo: "Conectar Claude a herramientas externas (documentación oficial de .NET, GitHub y una base de datos) para que deje de depender de lo que tú le pegues en el chat."
ogImage: "/og/06-mcp.png"
fuentes:
  - titulo: "Connect Claude Code to tools via MCP"
    url: "https://code.claude.com/docs/en/mcp"
  - titulo: "MCP quickstart"
    url: "https://code.claude.com/docs/en/mcp-quickstart"
  - titulo: "Microsoft Learn MCP Server"
    url: "https://learn.microsoft.com/training/support/mcp"
  - titulo: "DBHub"
    url: "https://github.com/bytebase/dbhub"
---

## Qué es MCP y cuándo lo necesitas

MCP es un estándar abierto para conectar herramientas de IA con datos y servicios. Un **servidor MCP** expone herramientas (por ejemplo, "buscar en la documentación", "crear un issue" o "consultar la base de datos") y Claude Code las usa como si fueran propias.

La señal para conectar uno es simple: **te descubres copiando datos de otra herramienta al chat**. Si pegas fragmentos de documentación, descripciones de issues o resultados de consultas SQL, ese sistema debería estar conectado.

| Sin MCP | Con MCP |
| --- | --- |
| Pegas la documentación de ASP.NET Core en el chat | Claude busca en Microsoft Learn la versión vigente |
| Copias el texto de un issue | Claude lee el issue y lo cierra al terminar |
| Ejecutas una consulta y pegas el resultado | Claude consulta la base de datos de solo lectura |

## Lo que un servidor MCP puede ofrecer

- **Herramientas:** acciones que Claude invoca. Aparecen con nombres como `mcp__github__create_issue`.
- **Recursos:** datos que mencionas con `@servidor:protocolo://ruta`, como un archivo.
- **Prompts:** comandos predefinidos que el servidor publica.

## Tres formas de conectar un servidor

| Tipo | Cuándo | Comando |
| --- | --- | --- |
| HTTP remoto (recomendado) | Servicios en la nube | `claude mcp add --transport http <nombre> <url>` |
| stdio local | Programas que corren en tu máquina | `claude mcp add <nombre> -- <comando> [args]` |
| JSON | Tienes la configuración de otro cliente | `claude mcp add-json <nombre> '<json>'` |

El transporte SSE está obsoleto: usa HTTP. En stdio, el `--` separa las opciones de Claude del comando del servidor; todo lo que va después se pasa tal cual. Si la documentación de un servidor está escrita para otro cliente (Claude Desktop, Cursor), busca la URL, el comando de arranque o el bloque `mcpServers` y conviértelo con alguno de estos tres comandos.

## Alcances

| Alcance | Bandera | Dónde se guarda | ¿Se comparte? |
| --- | --- | --- | --- |
| Local (por defecto) | `--scope local` | `~/.claude.json`, solo para este proyecto | No |
| Proyecto | `--scope project` | `.mcp.json` en la raíz | Sí, por Git |
| Usuario | `--scope user` | `~/.claude.json`, para todos tus proyectos | No |

Si el mismo servidor aparece en varios alcances, gana local, luego proyecto y luego usuario. Los campos no se mezclan: se usa la definición completa del alcance ganador. Claude Code pide aprobación antes de usar servidores de un `.mcp.json` que llegó en un repositorio; para reiniciar esas decisiones existe `claude mcp reset-project-choices`.

## `.mcp.json` para VisitasAPI

```json
{
  "mcpServers": {
    "microsoft-learn": {
      "type": "http",
      "url": "https://learn.microsoft.com/api/mcp"
    },
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": { "Authorization": "Bearer ${GITHUB_PAT}" }
    }
  }
}
```

- `${GITHUB_PAT}` se toma de tu variable de entorno, así el token nunca queda en el repositorio. También existe `${VAR:-valor_por_defecto}`.
- Una entrada con `url` necesita siempre `"type"`; sin él, Claude Code la trata como stdio y la rechaza.
- El servidor de Microsoft Learn es gratuito, no requiere autenticación y busca en la documentación oficial de .NET y Azure.

## Gestión y diagnóstico

| Comando | Para qué |
| --- | --- |
| `claude mcp list` | Lista servidores y su estado: Connected, Needs authentication, Failed to connect, Pending approval |
| `claude mcp get <nombre>` | Detalle del servidor y, si falla, el código HTTP y el error |
| `claude mcp remove <nombre>` | Elimina un servidor |
| `/mcp` | Dentro de la sesión: estado, número de herramientas, autenticación OAuth, activar o desactivar por proyecto |
| `/mcp reconnect all` | Reintenta todos los servidores caídos |
| `claude mcp login <nombre>` | Inicia sesión OAuth desde la terminal |

| Síntoma | Causa probable | Qué hacer |
| --- | --- | --- |
| `Failed to connect` con 401 | Token inválido o vencido | Revisa la variable de entorno y vuelve a crear el token |
| `Needs authentication` | El servidor usa OAuth | `/mcp` → autenticar, o `claude mcp login` |
| `Pending approval` | Servidor de `.mcp.json` sin aprobar | Abre `claude` y apruébalo |
| La variable `${VAR}` no se expande | No está definida en la terminal donde abriste Claude | Defínela y reinicia la sesión |
| El servidor no aparece en VS Code | VS Code no heredó tus variables de entorno | Abre VS Code desde la terminal con `code .` |

## Contexto, límites y seguridad

- **Búsqueda de herramientas:** por defecto Claude solo carga los nombres de las herramientas MCP y trae la definición completa cuando la necesita. Puedes conectar varios servidores sin llenar el contexto.
- **Límite de salida:** aviso a partir de 10.000 tokens y máximo de 25.000 por defecto (`MAX_MCP_OUTPUT_TOKENS` lo cambia). Las respuestas más grandes se guardan en un archivo y Claude lo lee cuando lo necesita.
- **Llamadas largas:** una llamada MCP que pasa de dos minutos se mueve a segundo plano; la ves en `/tasks`.
- **Confía antes de conectar.** Un servidor que trae contenido externo puede incluir instrucciones maliciosas (inyección de prompts). Usa servidores oficiales o revisados.
- **Base de datos:** conéctala siempre con un usuario de solo lectura.
- **Permisos:** las herramientas MCP se controlan con reglas como `mcp__github__*` (Módulo 5). Por ejemplo, `"ask": ["mcp__github__*"]` hace que Claude te pregunte antes de cualquier acción en GitHub.

## Laboratorio (martes y miércoles)

**Parte A · Documentación oficial (martes)**

1. Agrega Microsoft Learn: `claude mcp add --transport http microsoft-learn https://learn.microsoft.com/api/mcp`.
2. Ejecuta `claude mcp list`.
   *Comprueba:* `microsoft-learn` aparece como **Connected**.
3. Abre `claude` y ejecuta `/mcp`. Entra al servidor y mira cuántas herramientas expone y cómo se llaman.
4. Pregunta: "Usando Microsoft Learn, ¿cuál es la forma recomendada de devolver ProblemDetails en ASP.NET Core 8? Cita la página".
   *Comprueba:* la respuesta trae enlaces a learn.microsoft.com. Abre uno y confirma que dice lo mismo.
5. Pide: "Compara esa recomendación con cómo lo hace hoy `SedesController` y propón cambios. No edites todavía".
6. Ejecuta `/context` y busca cuánto ocupan las herramientas MCP.
   *Comprueba:* ocupan poco, porque solo se cargaron los nombres.

**Parte B · GitHub (miércoles)**

7. Sube VisitasAPI a un repositorio privado en GitHub.
8. Crea un token de grano fino en GitHub (Settings → Developer settings → Fine-grained tokens) con acceso **solo** a ese repositorio y permisos de lectura y escritura en Issues.
9. En PowerShell, guarda el token como variable de usuario: `[Environment]::SetEnvironmentVariable("GITHUB_PAT", "tu_token", "User")`. Cierra y vuelve a abrir la terminal.
   *Comprueba:* `$env:GITHUB_PAT` muestra el token.
10. Crea el `.mcp.json` de arriba en la raíz (o usa `claude mcp add --scope project`). Abre `claude` y aprueba el servidor del proyecto.
    *Comprueba:* `claude mcp get github` dice **Connected**. Si dice 401, revisa el paso 9.
11. Pide: "Crea un issue en el repositorio para agregar paginación a GET /visitas, con criterios de aceptación".
    *Comprueba:* el issue aparece en GitHub.
12. Agrega a `.claude/settings.json` la regla `"ask": ["mcp__github__*"]`, abre una sesión nueva y pide "agrega un comentario al issue que acabas de crear".
    *Comprueba:* Claude te pide permiso antes de usar la herramienta de GitHub, aunque estés en modo Auto.

## Reto (jueves)

Conecta una base de datos de solo lectura con [DBHub](https://github.com/bytebase/dbhub) como servidor stdio:

1. Crea una copia de tu base de desarrollo (por ejemplo, `visitas-lectura.db` si usas SQLite) y llénala con 20 visitas de prueba.
2. Revisa en el README de DBHub el formato de `--dsn` para tu motor y su opción de solo lectura. En SQL Server, conéctate además con un usuario que solo tenga permiso de lectura.
3. Agrégalo con `claude mcp add --transport stdio db -- npx -y @bytebase/dbhub --dsn "<tu-dsn>"` más la opción de solo lectura que encontraste.
4. Pregunta: "¿Cuántas visitas por comuna hay registradas?".
5. Escribe tú la consulta SQL a mano, ejecútala y compara el resultado con el de Claude.
6. Pide "borra las visitas de la comuna 10" y confirma que la escritura falla. Si no falla, tu conexión no es de solo lectura: corrígela antes de seguir.

## Preguntas de control (sábado)

1. ¿Cuál es la señal de que deberías conectar un servidor MCP?
2. ¿Qué diferencia hay entre un servidor HTTP y uno stdio?
3. ¿Por qué el token de GitHub va como `${GITHUB_PAT}` y no escrito en `.mcp.json`?
4. ¿Qué alcance usarías para un servidor que todo el equipo debe tener?
5. ¿Qué riesgo tiene conectar un servidor MCP desconocido y cómo lo reduces?
