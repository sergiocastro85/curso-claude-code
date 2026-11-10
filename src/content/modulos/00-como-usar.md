---
numero: 0
titulo: "Cómo usar este curso"
semana: 0
objetivo: "Entender el ritmo, la regla de oro y preparar tu entorno (Windows, .NET 8, Git, cuenta de Claude)."
duracionMinutos: 60
fuentes:
  - titulo: "Claude Code: visión general"
    url: "https://code.claude.com/docs/en/overview"
  - titulo: "Configuración e instalación"
    url: "https://code.claude.com/docs/en/setup"
---

## Conceptos clave

El curso dura 10 semanas. De lunes a viernes dedicas 40 minutos, el sábado 20 y el domingo 15: unos 245 minutos por semana. Es mejor constancia corta que maratones.

La **regla de oro** se repite en todos los módulos:

1. **Predecir:** antes de pedirle algo a Claude, escribe qué esperas que haga.
2. **Revisar el diff:** lee cada cambio antes de aceptarlo.
3. **Explicar:** si no puedes explicarlo con tus palabras, no entra a tu proyecto.

El proyecto que construirás es **VisitasAPI**, una API en .NET 8 con Clean Architecture.

## Laboratorio

1. Instala el SDK de .NET 8 y comprueba la versión:

```bash
dotnet --version
git --version
```

2. Crea una carpeta de trabajo y un repositorio vacío:

```bash
mkdir VisitasAPI
cd VisitasAPI
git init
```

3. Prepara una cuenta que te permita usar Claude Code (revisa las condiciones vigentes en el sitio oficial).
4. Crea un archivo `bitacora.md` donde anotarás tus predicciones cada día.

## Reto

Escribe en tu bitácora, en tres frases, qué quieres poder hacer al terminar las 10 semanas.

## Preguntas de repaso

- ¿Cuáles son los tres pasos de la regla de oro?
- ¿Por qué conviene revisar el diff antes de aceptar un cambio?
- ¿Qué versión de .NET usaremos?
