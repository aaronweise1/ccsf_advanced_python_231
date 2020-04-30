# Write an HTTP service that chooses an available high port number and serves a
# single copy of a memorable text to the first request that comes in. Because 
# of firewall rules, requests to services running on hills have to come from 
# within the college network

import http.server
import socket
import threading
import http.client


class Handler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write('Hello!'.encode())

    def do_POST(self):
        return self.do_GET()

    def do_HEAD(self):
        return self.do_GET()


def get_available_port():
    with socket.socket() as s:
        s.bind(('',0))
        return s.getsockname()[1]

def start_server(port):
    with http.server.HTTPServer(('localhost', port), Handler) as httpd:
        # if no client requests are made, exit program after timeout (seconds)
        # httpd.timeout = 10
        httpd.handle_request()
        # for testing with browser, server needs to serve two requests
        # httpd.handle_request()

def make_request(port):
    conn = http.client.HTTPConnection('localhost:' + str(port))
    conn.request('GET', '')
    resp = conn.getresponse()
    return resp.read().decode()


port = get_available_port()
# start server in its own thread
threading.Thread(target=start_server, args=(port,)).start()
print('server started on port:', str(port), flush=True)
text = make_request(port)
print('client request returned:', text, flush=True)



    
