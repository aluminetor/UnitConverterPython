# AGENTS.md — Conversor de Unidades

Aplicación web didáctica para convertir unidades de medida (distancia, temperatura). Proyecto de aprendizaje para dominar conceptos básicos de Python y desarrollo backend con Flask. El código debe mantenerse simple, legible y comprensible para un estudiante de programación.

## Stack y estructura

- Python 3.10+ y Flask (sin bases de datos, ORMs ni librerías adicionales).
- `app.py`: Controlador Flask, manejo de peticiones (`GET`, `POST`) y paso de datos a la vista.
- `logica_conversor.py`: Lógica pura de conversión usando funciones y `match/case`.
- `templates/index.html`: Interfaz del usuario en HTML con Jinja2 y CSS embebido.
- `requirements.txt`: Dependencias mínimas (`Flask`).

## Convenciones

- Textos de la interfaz y mensajes en español.
- Código limpio, legible y modular: mantener separada la lógica matemática (`logica_conversor.py`) de las rutas web (`app.py`).
- Los valores de los `<option>` en `index.html` deben coincidir exactamente con los casos del `match` en `logica_conversor.py`.
- Uso estricto de bloques `try / except` para capturar errores de casting (`ValueError`) y no tumbar el servidor.

## Reglas de conversión (fácil equivocarse)

- Toda entrada de formulario llega como `string`; siempre validar y convertir a `float` antes de operar.
- Redondear siempre los resultados numéricos a 2 decimales con `round(valor, 2)`.
- El caso por defecto (`case _:`) en `match` debe retornar un mensaje descriptivo de opción inválida en lugar de romper la ejecución.
- Fórmulas de temperatura:
  - Celsius a Fahrenheit: `(C * 9/5) + 32`
  - Fahrenheit a Celsius: `(F - 32) / 1.8`

## Forma de trabajar

- Haz solo lo que se pide: no agregues librerías externas ni reestructures la arquitectura sin instrucción explícita.
- Cambios pequeños y enfocados; no reescribas lo que ya funciona.
- Si agregas una nueva conversión:
  1. Añade el `<option>` en `templates/index.html`.
  2. Añade el `case` correspondiente en `logica_conversor.py`.
- Al terminar, resume qué has cambiado y cualquier detalle relevante a verificar.

## Memoria
- Al empezar, lee `MEMORY.md` para conocer el estado del proyecto y las decisiones tomadas.
- Al terminar una tarea, actualízalo: estado actual, decisiones importantes (con su porqué) y errores a evitar.
- Mantenlo breve (máximo ~50 líneas): resume o elimina lo que ya no aporte.
- Si algo se convierte en una regla permanente, propón moverlo a `AGENTS.md` en lugar de dejarlo en la memoria.
- No guardes nunca datos sensibles (claves, tokens, datos personales).


## Límites

- ✅ Siempre: mantener la separación de responsabilidades (backend vs lógica pura), validar datos numéricos con `try/except`.
- ⚠️ Pregunta antes: crear archivos nuevos, agregar rutas adicionales en Flask o modificar la estructura de carpetas.
- 🚫 Nunca: instalar dependencias pesadas (Django, SQLAlchemy, etc.), usar JavaScript complejo innecesario o cambiar Flask por otro framework.
- ✅ Siempre: actualizar `MEMORY.md` al terminar cada tarea. 

## Verificación

- Probar el servidor en consola: `python app.py`.
- Abrir `http://127.0.0.1:5000/` en el navegador y verificar:
  - Envío de número válido y retorno correcto redondeado a 2 decimales.
  - Envío de campos vacíos o texto no numérico: debe mostrar el mensaje de validación sin lanzar error 500 en terminal.