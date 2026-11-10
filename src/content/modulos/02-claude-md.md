---
numero: 2
titulo: "CLAUDE.md y contexto"
semana: 2
objetivo: "Escribir un CLAUDE.md útil y manejar el contexto para que Claude siga las reglas de tu proyecto."
fuentes:
  - titulo: "Memoria y CLAUDE.md"
    url: "https://code.claude.com/docs/en/memory"
  - titulo: "Buenas prácticas"
    url: "https://code.claude.com/docs/en/best-practices"
---

## Conceptos clave

`CLAUDE.md` es un archivo en la raíz del proyecto que Claude lee al empezar cada sesión. Sirve para dejar por escrito lo que un compañero nuevo necesitaría saber: comandos, convenciones y reglas.

Un buen `CLAUDE.md` es corto y concreto. Si es larguísimo, las reglas importantes se pierden. Además, el contexto de una conversación es limitado: sesiones largas y desordenadas empeoran los resultados.

## Laboratorio

1. Crea `CLAUDE.md` en VisitasAPI con estas secciones: comandos (`dotnet build`, `dotnet test`), arquitectura (qué va en cada capa) y reglas (nombres en español para el dominio, sin lógica en los controladores).
2. Inicia una sesión nueva y pide una entidad `Visita`. Comprueba si respeta tus reglas.
3. Quita una regla, repite el pedido y compara el resultado.

## Reto

Reduce tu `CLAUDE.md` a menos de 40 líneas sin perder ninguna regla que haya cambiado el resultado.

## Preguntas de repaso

- ¿Cuándo lee Claude el archivo `CLAUDE.md`?
- ¿Por qué es mala idea escribir un `CLAUDE.md` enorme?
- ¿Qué cosas NO deberían ir ahí (por ejemplo, secretos)?
