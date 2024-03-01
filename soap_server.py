from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

# Define la función del servicio SUMAR DOS NUMEROS
def SumaDosNumeros(num1, num2):
    return ("La suma de {} y {} es {}".format(num1, num2, num1 + num2))

# Define la función del servicio SUMAR DOS NUMEROS
def CadenaPalindromo(cadena):
    VerifCaden = ""''.join(c.lower() for c in cadena if c.isalnum())#devuelve true si el caracter es alfanumerico
    return VerifCaden == VerifCaden[::-1]#sirve para invertir una cadena
    

# Creamos la ruta del servidor SOAP
dispatcher = SoapDispatcher(
    "ejemplo-soap-server",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)

# Registramos el servicio para sumar dos numeros
dispatcher.register_function(
    "SumaDosNumeros",
    SumaDosNumeros,
    returns={"result": str},
    args={"num1": int, "num2": int},
)

## Registramos el servicio para saber si una cadena es palindromo
dispatcher.register_function(
    "CadenaPalindromo",
    CadenaPalindromo,
    returns={"result": bool},
    args={"cadena": str},
)

# Iniciamos el servidor HTTP
server = HTTPServer(("0.0.0.0", 8000), SOAPHandler)
server.dispatcher = dispatcher
print("Servidor SOAP iniciado en http://localhost:8000/")
server.serve_forever()