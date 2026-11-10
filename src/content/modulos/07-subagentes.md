---
numero: 7
titulo: "Subagentes"
semana: 7
objetivo: "Crear subagentes especializados (revisor, pruebas) y delegarles tareas en VisitasAPI."
premium: true
fuentes:
  - titulo: "Subagentes"
    url: "https://code.claude.com/docs/en/sub-agents"
---

## Conceptos clave

Un subagente es un asistente especializado con su propio contexto, instrucciones y herramientas permitidas. Se define en un archivo Markdown dentro de `.claude/agents/`. Sirve para delegar tareas acotadas (revisar código, escribir pruebas) sin llenar la conversación principal.

> El material extra de este módulo (subagentes adicionales listos para usar) forma parte del Kit Premium. El contenido base de abajo es completo y gratuito.

## Laboratorio

1. Crea `.claude/agents/revisor.md` con una descripción clara y solo herramientas de lectura.
2. Crea `.claude/agents/pruebas.md` enfocado en xUnit.
3. Pide: "Usa el revisor para revisar el último cambio" y compara su opinión con tu propio diff.

## Reto

Haz que el revisor siga una lista de 5 puntos propios (nombres, capas, manejo de errores...) y pruébalo con código que los incumpla.

## Preguntas de repaso

- ¿Qué ventaja da que un subagente tenga su propio contexto?
- ¿Por qué limitar las herramientas de un revisor?
- ¿Cuándo no vale la pena crear un subagente?
