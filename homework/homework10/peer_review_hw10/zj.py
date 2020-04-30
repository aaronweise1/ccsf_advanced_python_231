#!/usr/bin/env python3

import http.server

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        message = '\nPython is an experiment in how much freedom programmers need. - Guido van Rossum\n'
        self.send_response ( 200 )
        self.send_header ( 'Content-Type', 'text/plain' )
        self.end_headers ()
        self.wfile.write(bytes(message, 'utf8'))
        return

if __name__ == '__main__':
    try:
        print('starting server on port 8118...')
        server = ('', 8118)
        httpd = http.server.HTTPServer( server, Handler )
        httpd.serve_forever()

    except KeyboardInterrupt:
        print(' received, shutting down the web server')
        try:
            if connection:
                connection.close()
        except: pass

