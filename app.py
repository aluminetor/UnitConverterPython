from flask import Flask, render_template, request

from logica_conversor import convertir

# Inicializamos la aplicación Flask
app = Flask(__name__)

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
        except ValueError:
            resultado = "Por favor ingresa un número válido."

        # Convertimos a float para que tu función pueda operar matemáticamente
        valor_float = float(valor_str)

        # Invocamos tu función de logica_conversor.py
        resultado = convertir(valor_float, tipo)

    # Renderizamos el archivo HTML pasándole la variable resultado
    return render_template('index.html', resultado=resultado)

# Bloque estándar para arrancar el servidor en modo desarrollo
if __name__ == '__main__':
    app.run(debug=True)