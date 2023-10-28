import http.server
import socketserver

PORT = 8000
FILE_TO_SERVE = 'poli.html'

class SinglePageHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = FILE_TO_SERVE
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

with socketserver.TCPServer(("", PORT), SinglePageHandler) as httpd:
    print(f"Serving {FILE_TO_SERVE} at port {PORT}")
    httpd.serve_forever()
