import requests

#Consultando a un servidor RESTful
url = "http://localhost:8000/"
#POST agrega un nuevo estudiante por la ruta /estudiantes
ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica",
}

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)

#POST agrega un nuevo estudiante por la ruta /estudiantes
nuevo_estudiante = {
    "nombre": "Pedrito",
    "apellido": "Lopez",
    "carrera": "Ingeniería",
}

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)

#Nuevas funcionalidades
#Obtener todas las carreras
ruta_carreras = url + "estudiantes/carreras"
carreras_response = requests.request(method="GET", url=ruta_carreras)
print(carreras_response.text)

#Obtener estudiantes de la carrera de Economía
ruta_estudiantes_economia = url + "estudiantes/carrera/Economia"
estudiantes_economia_response = requests.request(method="GET", url=ruta_estudiantes_economia)
print(estudiantes_economia_response.text)

#Agregar 2 estudiantes de Economía
nuevo_estudiante_economia_1 = {
    "nombre": "Económico",
    "apellido": "Estudiante1",
    "carrera": "Economía",
}

post_response_economia_1 = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante_economia_1)
print(post_response_economia_1.text)

nuevo_estudiante_economia_2 = {
    "nombre": "Económico",
    "apellido": "Estudiante2",
    "carrera": "Economía",
}

post_response_economia_2 = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante_economia_2)
print(post_response_economia_2.text)
