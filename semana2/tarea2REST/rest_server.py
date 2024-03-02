from http.server import HTTPServer, BaseHTTPRequestHandler
import json

estudiantes = [
    {
        "id": 1,
        "nombre": "Pedrito",
        "apellido": "García",
        "carrera": "Ingeniería de Sistemas",
    },
    {
        "id": 2,
        "nombre": "Pablo",
        "apellido": "Alvarez",
        "carrera": "Ingeniería de Redes",
    },
]

class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/lista_estudiantes":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
        elif self.path == "/buscar_nombre":
            # Filtrar estudiantes cuyos nombres comienzan con "P"
            #startswith analiza si la cadena empieza con el caracter requerido
            estudiantes_con_P = [estudiante for estudiante in estudiantes if estudiante["nombre"].startswith("P")]
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes_con_P).encode("utf-8"))
        elif self.path == "/contar_carreras":
            # Nueva ruta para contar la cantidad de estudiantes por carrera
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            # Crear un diccionario para contar estudiantes por carrera
            carreras_count = {}
            for estudiante in estudiantes:
                carrera = estudiante.get("carrera", "Desconocida")
                carreras_count[carrera] = carreras_count.get(carrera, 0) + 1
            self.wfile.write(json.dumps(carreras_count).encode("utf-8"))
        elif self.path == "/total_estudiantes":
            # cantidad total de estudiantes
            total_estudiantes = len(estudiantes)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"total_estudiantes": total_estudiantes}).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))
        
    def do_POST(self):
        if self.path == "/agrega_estudiante":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data.decode("utf-8"))
            post_data["id"] = len(estudiantes) + 1
            estudiantes.append(post_data)
            self.send_response(201)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))
    
def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()
        
if __name__ == "__main__":
    run_server()