# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 23:02:45 2020   @author: Mary Liu
Write an HTTP service that chooses an available high port number and 
serves a single copy of a memorable text to the first request that 
comes in. Because of firewall rules, requests to services running 
on hills have to come from within the college network
"""
import http.server
import socketserver
import os

class Handler(http.server.SimpleHTTPRequestHandler):
	def do_GET(self):
		os.chdir("/var/tmp")	
		if self.path == '/var/tmp':
			self.path = 'index.html'
		return http.server.SimpleHTTPRequestHandler.do_GET(self)
    
if __name__ == '__main__':
    PORT = 8123
    handler_object = Handler
    with socketserver.TCPServer(("", PORT), handler_object) as server:
        server.handle_request()
