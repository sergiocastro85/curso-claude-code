---
numero: 4
titulo: "Pruebas y depuración con IA"
semana: 4
objetivo: "Generar y revisar pruebas xUnit y depurar errores explicando la causa, no solo aplicando el arreglo."
fuentes:
  - titulo: "Flujos de trabajo comunes"
    url: "https://code.claude.com/docs/en/common-workflows"
  - titulo: "Solución de problemas"
    url: "https://code.claude.com/docs/en/troubleshooting"
---

## Conceptos clave

Una prueba generada por IA solo vale si entiendes qué comprueba. Una prueba que siempre pasa no protege nada. Para depurar, pide la **causa raíz** y una forma de reproducir el error, no solo "arréglalo".

## Laboratorio

1. Pide pruebas xUnit para el caso de uso `RegistrarVisita` (caso feliz, datos inválidos, repositorio que falla).
2. Antes de ejecutarlas, predice cuáles pasarán:

```bash
dotnet test
```

3. Rompe a propósito una regla del dominio y comprueba que alguna prueba falle.
4. Provoca un error real y pide a Claude que explique la causa antes de proponer el arreglo.

## Reto

Escribe tú una prueba a mano y pide a Claude que la critique. Anota qué casos olvidaste.

## Preguntas de repaso

- ¿Por qué una prueba que nunca falla es peligrosa?
- ¿Qué diferencia hay entre arreglar el síntoma y la causa?
- ¿Cómo reproduces un error antes de corregirlo?
