---
name: validacion-2026-11-05
description: Resultado de la primera validación HU-01..HU-17 y causas raíz de los pendientes
metadata:
  type: project
---

- 8 Aceptadas (HU-01,02,03,07,08,09,10,14), 9 Parciales, 0 Rechazadas. Detalle en docs/validacion.md.
- Causa raíz de casi todos los Parciales: no hay .env (sin servicio de email, LinkedIn, contacto, analítica ni compra). **Why:** decisiones del autor pendientes. **How to apply:** al revalidar, comprobar primero si existen esas variables.
- Hallazgo de cumplimiento: `novalidate` en SubscribeForm.astro permite envío sin autorización cuando no hay JS. Revalidar HU-05 sobre esto.
- El PO no tiene shell: no puede correr build ni Lighthouse; declarar siempre esa reserva y no aprobar lo no comprobable.
- Estados usados en backlog: Aceptada = Aprobada; Parcial = "En desarrollo (Parcial)".
