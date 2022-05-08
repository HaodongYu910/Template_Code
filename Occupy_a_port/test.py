#!/usr/bin/env python3
'''    Testing program for socket
      Author: Jimmy
      we can use this to handle a port and response some info
'''
import http.server
import socketserver
import http

port = 80
class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(http.HTTPStatus.INTERNAL_SERVER_ERROR)
        self.end_headers()
        
        mystring = "500 Internal Server Error! nicaicai\n"
        self.data = bytes(mystring, 'utf-8')
        self.wfile.write(self.data)

with socketserver.TCPServer(("", port), Handler) as httpd:
    httpd.serve_forever()

