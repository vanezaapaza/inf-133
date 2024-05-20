# Importa la clase Flask del paquete flask
from flask import Flask, request, jsonify

# Crea una instancia de la clase Flask y la asigna a la variable 'app'.
# '__name__' es un parámetro especial que representa el nombre del módulo actual.
# Flask lo utiliza para determinar la ruta de las plantillas y archivos estáticos.
app = Flask(__name__)


# Este decorador asociará la función 'hello_world()' con la ruta raíz ('/') de la aplicación.
# Esto significa que cuando alguien acceda a la ruta raíz en el navegador, Flask ejecutará esta función.
@app.route("/")
def hello_world():
    return "¡Hola, mundo!"

# Ruta para saludar utilizando el método GET.
@app.route("/saludar", methods=["GET"])
def saludar():
    # Obtener el nombre de los argumentos de la URL.
    nombre = request.args.get("nombre")
    # Si el nombre no está presente, se devuelve un mensaje de error.
    if not nombre:
        return (
            jsonify({"error": "Se requiere un nombre en los parámetros de la URL."}),
            400,
        )
    # Retorna un saludo personalizado utilizando el nombre recibido como parámetro.
    return jsonify({"mensaje": f"¡Hola, {nombre}!"})


@app.route("/Sumar", methods=["GET"])
def sumar():
    # Obtener el nombre de los argumentos de la URL.
    numero1 = int(request.args.get("num1"))
    numero2 = int(request.args.get("num2"))
    sumar = numero1 + numero2

    # Si el nombre no está presente, se devuelve un mensaje de error.
    if not sumar:
        return (
            jsonify({"error": "Se requiere un nombre en los parámetros de la URL."}),
            400,
        )
    # Retorna un saludo personalizado utilizando el nombre recibido como parámetro.
    return jsonify({"mensaje": f"la suma es, {sumar}"})

@app.route("/Palindromo", methods=["GET"])
def palindromo():
    cadena = request.args.get("cadena")
    # Verificar si la cadena es un palíndromo
    if cadena == cadena[::-1]:
        mensaje = f'La cadena "{cadena}" es un palíndromo.'
    else:
        mensaje = f'La cadena "{cadena}" no es un palíndromo.'
    
    # Retorna el resultado
    return jsonify({"mensaje": mensaje})


@app.route("/vocal", methods=["GET"])
def vocal():
    cadena = request.args.get("cadena")
    vocal = request.args.get("vocal")
    
    cantidad = cadena.count(vocal)
    if not vocal:
        return (
            jsonify({"error": "Se requiere un nombre en los parámetros de la URL."}),
            400,
        )

    # Retorna el resultado
    return jsonify({"mensaje": cantidad})

# Esta condición verifica si este script se está ejecutando directamente.
# Si es así, Flask iniciará un servidor web local en el puerto predeterminado (5000).
if __name__ == "__main__":
    app.run()