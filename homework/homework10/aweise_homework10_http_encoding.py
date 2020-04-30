"""
Write an HTTP service that chooses an available high port 
number and serves a single copy of a memorable text to the 
first request that comes in. Because of firewall rules, 
requests to services running on hills have to come from 
within the college network.
"""

import http.server 
import socket 

message = """
Do you like green eggs and ham?

I do not like them, Sam-I-am.
I do not like green eggs and ham!

Would you like them here or there?

I would not like them here or there.
I would not like them anywhere.

I do so like green eggs and ham!
Thank you! Thank you,
Sam-I-am!
"""

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())


def getOpenPort(high_port, low_port):
    for port_num in range(high_port, low_port, -1):
        if checkPort(port_num):
            print('Port', port_num, 'is open')
            return port_num
    print('No open ports found')
    return None
        

def checkPort(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server = 'localhost'
    try:
        s.connect((server,port))
        return True
    except:
        return False 





if __name__ == '__main__':
    port_num = getOpenPort(high_port=10000, low_port=100)
    print("\nTo test the web server's first response,\ntype the following in a new terminal window:")
    print("curl http://hills.ccsf.edu:" + str(port_num) + "\n\n")
    server = ('', port_num)
    httpd = http.server.HTTPServer(server, Handler)
    # Assignment requires only the "first request that comes in" to generate a response
    httpd.handle_request()

