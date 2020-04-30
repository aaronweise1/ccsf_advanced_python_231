import http.server

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(('Hey there! You are currently in path '+self.path).encode())

if __name__ == '__main__':
    server = ('', 8118)
    httpd = http.server.HTTPServer(server, Handler)
    httpd.serve_forever()
