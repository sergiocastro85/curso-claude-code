---
numero: 9
titulo: "Hooks y automatización"
semana: 9
objetivo: "Automatizar validaciones (formato, build, pruebas) con hooks y entender cómo se empaqueta un plugin."
premium: true
fuentes:
  - titulo: "Guía de hooks"
    url: "https://code.claude.com/docs/en/hooks-guide"
  - titulo: "Referencia de hooks"
    url: "https://code.claude.com/docs/en/hooks"
  - titulo: "Plugins"
    url: "https://code.claude.com/docs/en/plugins"
---

## Conceptos clave

Un **hook** es un comando que se ejecuta automáticamente en momentos concretos (por ejemplo, después de editar un archivo). A diferencia de pedirle algo a Claude, el hook corre siempre: es una garantía, no una sugerencia.

Un **plugin** agrupa skills, agentes, comandos y hooks para compartirlos o instalarlos juntos.

> El plugin `visitas-toolkit` listo para instalar forma parte del Kit Premium.

## Laboratorio

1. Define un hook que ejecute `dotnet format` después de que Claude edite archivos `.cs`.
2. Añade otro que ejecute `dotnet build` y muestre el error si falla.
3. Rompe el formato a propósito y comprueba que el hook lo corrige.
4. Lee en la guía de plugins qué archivos necesitarías para empaquetar tu configuración.

## Reto

Diseña (sin implementar) un plugin con tu skill, tu comando y tu hook. Dibuja su estructura de carpetas.

## Preguntas de repaso

- ¿Por qué un hook es más fiable que pedirle a Claude "recuerda formatear"?
- ¿Qué riesgo tiene un hook que ejecuta comandos automáticamente?
- ¿Qué incluye un plugin?
