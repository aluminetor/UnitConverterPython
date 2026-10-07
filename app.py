from flask import Flask, render_template, request

from logica_conversor import convertir

# Inicializamos la aplicación Flask
app = Flask(__name__)

# Historial en memoria de últimas 5 conversiones exitosas.
# Lista de strings, la más reciente va primero. Se borra al reiniciar.
historial = []

# Etiquetas cortas para mostrar el historial (ej: "10 km ➔ 6.21 millas")
ETIQUETAS = {
    "km_a_millas": ("km", "millas"),
    "millas_a_km": ("millas", "km"),
    "c_a_f": ("°C", "°F"),
    "f_a_c": ("°F", "°C"),
}

# Definimos la ruta principal ('/') aceptando métodos GET (cuando visitas la página)
# y POST (cuando envías el formulario con el botón)
@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None

    # Verificamos si el usuario envió el formulario
    if request.method == 'POST':
        # request.form recibe los valores a través del atributo 'name' de cada input del HTML
        # Ojo: todo lo que viene de un formulario web llega como string (texto)
        valor_str = request.form.get('valor')
        tipo = request.form.get('tipo_conversion')
        
        # Intentamos la conversión de forma segura
        try:
            valor_float = float(valor_str)
            resultado = convertir(valor_float, tipo)
            # Solo guardamos conversiones exitosas (resultado numérico)
            if isinstance(resultado, (int, float)):
                origen, destino = ETIQUETAS.get(tipo, ("", ""))
                texto = f"{valor_float} {origen} ➔ {resultado} {destino}"
                historial.insert(0, texto)
                historial[:] = historial[:5]
        except ValueError:
            resultado = "Por favor ingresa un número válido."

    # Renderizamos el archivo HTML pasándole resultado e historial
    return render_template('index.html', resultado=resultado, historial=historial)

# Bloque estándar para arrancar el servidor en modo desarrollo
if __name__ == '__main__':
    app.run(debug=True)