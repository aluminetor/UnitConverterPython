# MEMORY.md — Conversor de Unidades

Memoria del proyecto entre sesiones. Máximo ~50 líneas: resume o elimina lo que ya no aporte.

## Estado actual
- v1 funcional: conversión bidireccional de longitud (Km/Millas) y temperatura (Celsius/Fahrenheit).
- Historial en memoria: últimas 5 conversiones exitosas en `app.py` (`historial`, más reciente primero), renderizado en `index.html`.
- Arquitectura limpia: frontend Jinja2 (`templates/index.html`), servidor Flask (`app.py`) y lógica matemática desacoplada (`logica_conversor.py`).
- Manejo de excepciones con `try/except` para atrapar entradas no numéricas (`ValueError`).
- Repositorio Git inicializado y vinculado a GitHub.

## Decisiones (y por qué)
- Uso de `match/case`: código más limpio y legible que múltiples `if/elif` anidados.
- Separación de responsabilidades: `logica_conversor.py` es una función pura que no sabe de web ni de Flask, facilitando pruebas y mantenimiento.
- Redondeo a 2 decimales con `round()`: evita números infinitos periódicos en conversiones como Fahrenheit/Celsius.
- Flask sin base de datos: mantiene el proyecto ligero y pedagógico para enfocarse en la lógica base de Python.
- Historial como lista de strings en `app.py` (no en `logica_conversor.py`): respeta separación de responsabilidades; solo se guarda si `convertir()` retorna numérico; `insert(0)` + corte `[:5]`.

## Aprendizajes y errores a evitar
- Los formularios HTML envían texto (`str`); siempre hacer casting a `float` antes de operar.
- Los valores del `<select>` en HTML deben coincidir exactamente (claves en minúscula) con los casos del `match`.
- No guardar errores ni "Opcion invalida" en el historial (filtrar con `isinstance` numérico); no duplicar lógica fuera del `try/except` (causaba 500).

## Próximos pasos
- Añadir nuevas categorías de conversión (ej. masa: Kg a Libras, volumen: Litros a Galones).
- Mejorar el diseño visual con CSS responsivo o estilos modernos.