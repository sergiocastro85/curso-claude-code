---
numero: 4
titulo: "Memoria persistente con Claude Code"
semana: 4
objetivo: "Lograr que Claude recuerde las reglas de VisitasAPI entre sesiones sin que tengas que repetirlas."
ogImage: "/og/04-memoria.png"
fuentes:
  - titulo: "How Claude remembers your project"
    url: "https://code.claude.com/docs/en/memory"
  - titulo: "Explore the .claude directory"
    url: "https://code.claude.com/docs/en/claude-directory"
---

## Dos sistemas de memoria

| | CLAUDE.md | Memoria automática |
| --- | --- | --- |
| Quién la escribe | Tú | Claude |
| Qué contiene | Instrucciones y reglas | Aprendizajes: tus preferencias, correcciones y decisiones del proyecto |
| Dónde vive | En el repositorio o en `~/.claude/` | `~/.claude/projects/<proyecto>/memory/` (solo en tu máquina) |
| Cuánto se carga | Completo, en cada sesión | Las primeras 200 líneas o 25 KB de `MEMORY.md` |

Ambos son **contexto, no reglas obligatorias**. Si algo debe cumplirse siempre, sin excepción, se convierte en un hook (Módulo 7) o en una regla de permisos (Módulo 5).

## Dónde va cada CLAUDE.md

| Alcance | Ubicación | Para qué |
| --- | --- | --- |
| Usuario | `~/.claude/CLAUDE.md` | Tus preferencias en todos los proyectos |
| Proyecto | `./CLAUDE.md` o `./.claude/CLAUDE.md` | Reglas del equipo; se sube a Git |
| Local | `./CLAUDE.local.md` | Tus notas de este proyecto; va en `.gitignore` |
| Subcarpeta | `src/Api/CLAUDE.md` | Se carga cuando Claude trabaja en esa carpeta |
| Organización | `C:\Program Files\ClaudeCode\CLAUDE.md` en Windows | Políticas que define TI |

Los archivos no se reemplazan: se concatenan. Lo más cercano a tu carpeta de trabajo se lee al final. Si tu repositorio ya tiene un `AGENTS.md` para otras herramientas, Claude lo lee cuando no hay CLAUDE.md.

## Cómo escribir un buen CLAUDE.md

- **Menos de 200 líneas.** Un archivo largo hace que Claude ignore reglas.
- **Instrucciones verificables:** "Ejecuta `dotnet test` antes de cada commit" en vez de "prueba tus cambios".
- **Para cada línea pregúntate:** ¿si la borro, Claude se equivocaría? Si no, bórrala.
- **Incluye:** comandos que Claude no puede adivinar, reglas de estilo distintas a las comunes, decisiones de arquitectura, trampas del entorno.
- **No incluyas:** lo que Claude deduce leyendo el código, tutoriales largos ni descripciones archivo por archivo.
- **Importa otros archivos** con `@ruta/archivo.md`, y usa `.claude/rules/` para reglas que solo aplican a ciertas rutas.

## Ejemplo para VisitasAPI

```markdown
# VisitasAPI
Web API .NET 8 con Clean Architecture: Domain → Application → Infrastructure → Api.

## Comandos
- Compilar: `dotnet build`
- Pruebas: `dotnet test` (una sola prueba: `dotnet test --filter "FullyQualifiedName~Nombre"`)
- Migraciones: `dotnet ef migrations add <Nombre> -p src/Infrastructure -s src/Api`

## Reglas
- Domain no referencia ningún otro proyecto ni paquetes de EF Core.
- Los controladores solo llaman servicios de Application, nunca repositorios.
- Nombres de clases y métodos en español; sufijos técnicos en inglés (Service, Repository, Dto).
- IMPORTANTE: nunca edites archivos dentro de `Migrations/` a mano.

## Al compactar
Conserva siempre la lista de archivos modificados y los comandos de prueba.
```

## Reglas por ruta con `.claude/rules/`

Un archivo `.claude/rules/controladores.md` con este encabezado solo se carga cuando Claude toca un controlador:

```markdown
---
paths:
  - "src/Api/Controllers/**/*.cs"
---
- Todo endpoint devuelve ProblemDetails en errores.
- Documenta cada acción con atributos ProducesResponseType.
```

## Comandos de memoria

| Comando | Para qué |
| --- | --- |
| `/init` | Genera un CLAUDE.md inicial analizando el proyecto |
| `/memory` | Abre y edita los CLAUDE.md; activa o desactiva la memoria automática |
| `/context` | Confirma qué archivos de memoria se cargaron |
| `/doctor prompt-audit` | Revisa tus instrucciones en busca de contradicciones o reglas obsoletas |
| "Recuerda que…" | Claude lo guarda en la memoria automática |
| "Agrega esto a CLAUDE.md" | Claude lo escribe en el archivo de instrucciones |

## Laboratorio (martes y miércoles)

**Parte A · CLAUDE.md (martes)**

1. Ejecuta `/init` en VisitasAPI y lee el CLAUDE.md que genera.
2. Marca con `~~tachado~~` todo lo que Claude podría deducir leyendo el código. Cuenta cuántas líneas sobreviven.
3. Reescríbelo tú usando el ejemplo de arriba como guía. Debe quedar en menos de 60 líneas.
4. Haz commit del CLAUDE.md.
5. Abre una sesión nueva y ejecuta `/context`.
   *Comprueba:* tu CLAUDE.md aparece en **Memory files**.

**Parte B · Reglas por ruta, local y memoria automática (miércoles)**

6. Crea `.claude/rules/controladores.md` con la regla por ruta.
7. Pide: "Agrega un endpoint GET /sedes/{id}/visitas". 
   *Comprueba:* el controlador devuelve ProblemDetails y tiene `ProducesResponseType`, aunque no lo pediste.
8. Crea `CLAUDE.local.md` con tu cadena de conexión de desarrollo y agrégalo a `.gitignore`.
   *Comprueba:* `git status` no lo muestra como archivo por subir.
9. Dile a Claude: "Recuerda que prefiero pruebas con xUnit y FluentAssertions". Luego abre `/memory` → carpeta de memoria automática.
   *Comprueba:* encuentras el archivo con tu preferencia y puedes editarlo.
10. Ejecuta `/doctor prompt-audit` y aplica solo las sugerencias que puedas justificar.

## Reto (jueves)

Rompe una regla a propósito: pide "agrega el campo Observaciones a Visita y actualiza la migración editando el archivo". Observa si Claude respeta la regla de no editar migraciones. Si no la respeta, mejora la redacción de la regla y vuelve a probar en una sesión limpia. Anota la conclusión: ¿bastó con CLAUDE.md o hace falta algo más fuerte? (lo resolverás en los Módulos 5 y 7).

## Preguntas de control (sábado)

1. ¿Qué diferencia hay entre CLAUDE.md y la memoria automática?
2. ¿Por qué `CLAUDE.local.md` va en `.gitignore`?
3. ¿Cuándo usarías `.claude/rules/` en vez de escribir en CLAUDE.md?
4. Si una regla se debe cumplir siempre, ¿basta con escribirla en CLAUDE.md?
