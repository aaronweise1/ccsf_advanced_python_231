# CS231
# Assignment# 10
# Write an HTTP service that chooses an available high port number and
# serves a single copy of a memorable text to the first request that comes in.

import http.server

message = 'There is no such a thing as ignorance, but only degrees of wisdom.'
PORT_NUMBER = 65347

# Create a class handles any incoming request from the browser
class myHandler(http.server.BaseHTTPRequestHandler):

    #Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write(message.encode())

# create a server that run forever
if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print('Started httpserver on port', PORT_NUMBER,'use <Ctrl-C> to stop\n'
    'send the request from browser using URL http://localhost:65347 or http://hills.ccsf.edu:65347\n'
    'to send a request from the command line try $ curl http://hills.ccsf.edu:65347\n'
    'while server is running.')

    server.serve_forever()


'''
# create a server that doesn’t run forever
def run_while_true(server_class=http.server.HTTPServer,
                   handler_class=myHandler):
    server_address = ('', PORT_NUMBER)
    httpd = server_class(server_address, handler_class)
    print('Started Http Server on port', PORT_NUMBER)
    while True:
        try:
            httpd.handle_request()
            print('Http Server stopped.')
            return
        except:
            pass

run_while_true()
'''



# To send the request from browser http://localhost:65347 if server running in PC
# Or  http://hills.ccsf.edu:65347



# See process run by user
# ps -u userid

