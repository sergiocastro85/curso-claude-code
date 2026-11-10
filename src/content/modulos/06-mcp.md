---
numero: 6
titulo: "MCP: conectar herramientas"
semana: 6
objetivo: "Conectar Claude a documentación de .NET, GitHub y una base de datos mediante MCP."
fuentes:
  - titulo: "Conectar Claude Code con MCP"
    url: "https://code.claude.com/docs/en/mcp"
---

## Conceptos clave

MCP (Model Context Protocol) es un estándar abierto para que Claude use herramientas externas: documentación, GitHub, bases de datos. Cada servidor MCP agrega capacidades, pero también agrega riesgo: instala solo servidores de fuentes en las que confíes y dales el mínimo acceso.

## Laboratorio

1. Revisa en la guía oficial cómo agregar un servidor MCP con el comando `claude mcp add`.
2. Conecta un servidor de documentación y pregunta algo sobre .NET 8 que verifiques tú después.
3. Conecta GitHub con permisos mínimos y pide listar los issues de un repositorio de prueba.
4. Si usas una base de datos, conéctala en modo solo lectura y con datos de prueba.

## Reto

Haz una tabla con cada servidor MCP que conectaste: qué permite, qué riesgo tiene y cómo lo limitaste.

## Preguntas de repaso

- ¿Qué problema resuelve MCP?
- ¿Por qué una base de datos debería conectarse en solo lectura?
- ¿Qué verificas antes de instalar un servidor MCP de terceros?
