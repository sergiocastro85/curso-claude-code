---
numero: 1
titulo: "Introducción a Claude Code"
semana: 1
objetivo: "Instalar Claude Code, entender cómo trabaja y crear el esqueleto de VisitasAPI."
fuentes:
  - titulo: "Visión general"
    url: "https://code.claude.com/docs/en/overview"
  - titulo: "Inicio rápido"
    url: "https://code.claude.com/docs/en/quickstart"
  - titulo: "Configuración e instalación"
    url: "https://code.claude.com/docs/en/setup"
---

## Conceptos clave

Claude Code es un asistente que trabaja en tu terminal y dentro de tu proyecto: lee archivos, propone cambios y ejecuta comandos con tu permiso. No es un chat aparte: ve tu código real.

Funciona en un ciclo: tú describes una tarea, Claude explora, propone cambios y tú los apruebas o rechazas. Tú sigues siendo quien decide.

## Laboratorio

1. Instala Claude Code siguiendo la guía oficial de instalación para tu sistema.
2. Entra a la carpeta de VisitasAPI e inicia una sesión:

```bash
cd VisitasAPI
claude
```

3. Pide un esqueleto de solución con cuatro proyectos (Domain, Application, Infrastructure, Api). **Antes**, anota qué comandos esperas que ejecute.
4. Revisa cada comando y cada archivo creado antes de aprobarlo.
5. Compila para confirmar que todo funciona:

```bash
dotnet build
```

## Reto

Pídele a Claude que te explique la estructura que creó, y comprueba si coincide con lo que predijiste. Anota las diferencias.

## Preguntas de repaso

- ¿Qué diferencia hay entre Claude Code y un chat en el navegador?
- ¿Qué hace cada una de las cuatro capas de Clean Architecture?
- ¿Qué pasa si rechazas un comando que Claude propone?
