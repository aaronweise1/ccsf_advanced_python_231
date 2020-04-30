#!/usr/local/bin/python3
# Course   : CS 231 
# Homework : 10
# Due date  :  April 13, 2020
# Filename: hw10.py

"""
 Write an HTTP service that chooses an available high port number and serves a single copy of a memorable text to the first request that comes in. Because of firewall rules, requests to services running on hills have to come from within the college network 
"""

# run the program as normal with python3 in terimal
# you will see (server-side) outputs:
# Server is starting...
# Server is running on port [the available port goes here]
# ctrl-c to quit server

# some methods of checking the content of the url:
# open second terminal window
# 1
# type 'curl http://localhost:port' and ENTER, where port is the 
# available port, which displayed in server-side outputs 
# 2
# urllib.request: the code is at the bottom, copy and paste it to use

# the content of the url, the output should be: 
# Hello CS 231 class!
# Hope you're staying safe!
# Your server is running now...

 

import http.server
import socket
 
class request_Handler(http.server.BaseHTTPRequestHandler):
      
    def do_GET(self):
        self.send_response (200)
        self.send_header ('Content-Type', 'text/plain')
        self.end_headers ()
        # Send message to the client aka serves a single copy of a memorable text 
        message = "\tHello CS 231 class!\n \tHope you're staying safe!\n \tYour server is running now..."
        self.wfile.write(message.encode())
        return

# find an available port for server        
def find_free_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 0))
    addr, port = s.getsockname()
    s.close()
    return port

def run(free_port):
    try:
        print('Server is starting...')
        # Server settings
        server_address = ('', free_port)
        httpd = http.server.HTTPServer(server_address, request_Handler)
        print('Server is running on port', free_port)
        # To quit server press ctrl-c 
        print('ctrl-c to quit server')
        httpd.serve_forever()
        # httpd.handle_request()
    except KeyboardInterrupt:
        print("The server is shut down.")
        # httpd.server_close()
  
    

if __name__ == '__main__':
    free_port = find_free_port()
    # print(str(free_port))
    run(free_port)

########################################################

# urllib.request method:
# import urllib.request
# # save the answer to a variable
# available_port = input("What is port number the server is running on?")

# with urllib.request.urlopen('http://localhost:'+ available_port) as response:
#    html = response.read().decode()
#    print(html)