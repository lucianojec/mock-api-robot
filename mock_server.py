from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class MockServerRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/teste":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"mensagem": "Mock funcionando"}
            self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        if self.path == "/api/postar":
            self.send_response(201)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"status": "criado"}
            self.wfile.write(json.dumps(response).encode())

def run():
    server_address = ('', 8888)
    httpd = HTTPServer(server_address, MockServerRequestHandler)
    print("Servidor mock rodando na porta 8888...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
