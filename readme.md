# Conversor de Unidades con Python y Flask

Una aplicación web simple desarrollada en Python utilizando el microframework Flask para realizar conversiones básicas de unidades de longitud y temperatura.

## 🚀 Funcionalidades

- Conversión de Kilómetros a Millas y viceversa.
- Conversión de grados Celsius a Fahrenheit y viceversa.
- Manejo de errores para entradas no numéricas.

## 📁 Estructura del Proyecto

```text
UnitConverterPython/
│
├── templates/
│   └── index.html         # Interfaz web con formulario
├── app.py                 # Servidor y rutas Flask
├── logica_conversor.py    # Funciones y lógica de conversión
├── requirements.txt       # Dependencias del proyecto
└── README.md              # Documentación
```

## 🛠️ Instalación y Uso

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/aluminetor/UnitConverterPython.git
   cd UnitConverterPython
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar la aplicación:**
   ```bash
   python app.py
   ```

4. **Abrir en el navegador:**
   Visita `http://127.0.0.1:5000/` en tu navegador web.