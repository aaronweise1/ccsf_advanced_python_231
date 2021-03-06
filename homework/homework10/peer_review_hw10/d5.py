#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
import http.server
'''
Assignment: Write an HTTP service that chooses an available high port number 
and serves a single copy of a memorable text to the first request that comes
'''

#create a class server class with do Get
class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write('Hello World from hhtp server on port 8118!\n'.encode()) #the text

if __name__ == '__main__':
    server = ('localhost', 8118)  #create server
    httpd = http.server.HTTPServer(server, Handler)
    #give some info
    print("Serving on port 8118.\nTo kill server:Ctrl+C")
    print("To see the server response logon into a second SSHSecure Shell client.")
    print("then type:'curl http://localhost:8118'")
    print("verify that the server received the get & responded successfully(200) ")
    print("once done kill the server in the 1st SSHSecure Shell client:Ctrl+C")
    #start the server
    httpd.serve_forever()
