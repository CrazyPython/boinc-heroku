#!/usr/bin/python
# coding=utf-8
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import urllib, os

PORT_NUMBER = int(os.environ['PORT'])
BONICOKU_URL = 'https://boincoku.herokuapp.com/'

class Handler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(301)
        self.send_header("Location", BONICOKU_URL)
        self.end_headers()

    def do_GET(self):
        return self.do_HEAD()



try:
    server = HTTPServer(('', PORT_NUMBER), Handler)
    print('Started httpserver on port ' + str(PORT_NUMBER))
    server.serve_forever()
except KeyboardInterrupt:
    server.socket.close()
