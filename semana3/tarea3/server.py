from http.server import HTTPServer, BaseHTTPRequestHandler
import json

estudiantes = [
    {
        "id": 1,
        "nombre": "Pedrito",
        "apellido": "García",
        "carrera": "Ingeniería de Sistemas",
    },
]

class RESTRequestHandler(BaseHTTPRequestHandler):
    def response_handler(self, status, data):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))
    
    def read_data(self):
        content_length = int(self.headers["Content-Length"])
        data = self.rfile.read(content_length)
        data = json.loads(data.decode("utf-8"))
        return data
    
    def do_GET(self):
        #Ruta para obtener todos los estudiantes
        if self.path == "/estudiantes":
            self.response_handler(200, estudiantes)
        #Ruta para obtener todas las carreras
        elif self.path.startswith("/estudiantes/carreras"):
            carreras = set(estudiante["carrera"] for estudiante in estudiantes)
            self.response_handler(200, list(carreras))
        #Ruta para obtener estudiantes de la carrera de Economía
        elif self.path.startswith("/estudiantes/carrera/Economia"):
            estudiantes_economia = [estudiante for estudiante in estudiantes if estudiante["carrera"] == "Economía"]
            self.response_handler(200, estudiantes_economia)
        else:
            #Manejo de rutas no existentes
            self.response_handler(404, {"Error": "Ruta no existente"})

    def do_POST(self):
        #Ruta para agregar nuevos estudiantes
        if self.path == "/estudiantes":
            data = self.read_data()
            data["id"] = len(estudiantes) + 1
            estudiantes.append(data)
            self.response_handler(201, estudiantes)
        else:
            #Manejo de rutas no existentes
            self.response_handler(404, {"Error": "Ruta no existente"})

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
