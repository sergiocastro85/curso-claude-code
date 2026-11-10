---
numero: 5
titulo: "Permisos, settings y seguridad"
semana: 5
objetivo: "Configurar settings.json y permisos, y evitar exponer secretos o ejecutar comandos peligrosos."
fuentes:
  - titulo: "Configuración (settings)"
    url: "https://code.claude.com/docs/en/settings"
  - titulo: "Permisos"
    url: "https://code.claude.com/docs/en/permissions"
  - titulo: "Seguridad"
    url: "https://code.claude.com/docs/en/security"
---

## Conceptos clave

Claude Code pide permiso antes de acciones sensibles. Puedes dejar reglas en `.claude/settings.json`: qué se permite sin preguntar (`allow`), qué siempre pregunta (`ask`) y qué se prohíbe (`deny`).

Regla práctica: permite comandos de lectura y compilación, pregunta en todo lo que publique o instale, y prohíbe leer archivos con secretos como `.env`.

## Laboratorio

1. Crea `.claude/settings.json` en VisitasAPI con este punto de partida:

```json
{
  "permissions": {
    "allow": ["Bash(dotnet build *)", "Bash(dotnet test *)"],
    "ask": ["Bash(git push *)"],
    "deny": ["Read(./.env)"]
  }
}
```

2. Crea un `.env` de prueba con un valor falso y pide a Claude que lo lea. Comprueba que se bloquea.
3. Revisa que `.gitignore` excluya `.env` y `appsettings.*.json` con secretos.

## Reto

Escribe una lista de 5 comandos que NUNCA aprobarías sin leer y por qué.

## Preguntas de repaso

- ¿Qué diferencia hay entre `allow`, `ask` y `deny`?
- ¿Dónde guardas una clave de API en lugar de escribirla en el código?
- ¿Por qué `git push` conviene dejarlo en `ask`?
