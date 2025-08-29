import http.server
import socketserver

PORT = 8000

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/large-payload':
            payload_size_in_bytes = 40 * 1024 * 1024  # 40 MB
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(payload_size_in_bytes))
            self.end_headers()
            self.wfile.write(b'a' * payload_size_in_bytes)
        else:
            self.send_error(404)

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Server serving at port {PORT}")
    httpd.serve_forever()
