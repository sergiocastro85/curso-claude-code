---
numero: 3
titulo: "Explorar, planificar, codificar"
semana: 3
objetivo: "Usar modo plan y revisar diffs para construir la primera funcionalidad (registro de visitas) sin perder el control."
fuentes:
  - titulo: "Flujos de trabajo comunes"
    url: "https://code.claude.com/docs/en/common-workflows"
  - titulo: "Buenas prácticas"
    url: "https://code.claude.com/docs/en/best-practices"
---

## Conceptos clave

Un flujo sano tiene tres fases: **explorar** (leer el código sin cambiar nada), **planificar** (acordar los pasos) y **codificar** (aplicar cambios pequeños). El modo plan de Claude Code permite las dos primeras sin modificar archivos.

Cambios pequeños significan diffs pequeños, y un diff pequeño sí se puede revisar de verdad.

## Laboratorio

1. Activa el modo plan y pide: "Planifica el registro de visitas (POST /visitas) con caso de uso, repositorio y endpoint".
2. Lee el plan. Corrige lo que no te convenza antes de aprobar.
3. Sal del modo plan y pide implementar solo el primer paso. Revisa el diff.
4. Haz un commit por paso con un mensaje claro:

```bash
git add .
git commit -m "feat: caso de uso RegistrarVisita"
```

## Reto

Implementa el endpoint completo en tres commits y explica en tu bitácora cada cambio con tus palabras.

## Preguntas de repaso

- ¿Qué ventaja tiene planificar antes de codificar?
- ¿Por qué conviene un commit por paso?
- ¿Qué haces si el diff incluye algo que no entiendes?
