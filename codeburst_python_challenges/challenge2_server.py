# https://codeburst.io/python-friday-challenge-2-6f6808f43273
# Simulating live data stream

"""
import http.server
import subprocess


PORT = 8000
HTTPServer = http.server.HTTPServer


class RequestHandler(http.server.BaseHTTPRequestHandler):
    ''' A class to handle requests to server '''

    # Set request headers
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    # Set POST request handling
    def do_POST(self):
        ''' Handle POST requests '''
        self._set_headers()
        filename = self.path.replace('/', '')
        if self.path == '/challenge1_message':
            return subprocess.run(['python', filename + '.py'], shell=True)
        else:
            print(filename, 'Route not found')
            print('Route:', self.path)


def run(server_class=HTTPServer, handler_class=RequestHandler, port=PORT):
    ''' Creating and running a server '''
    server_address = ('', port)     # (host, port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == '__main__':
    run()

# --------------------------------------------------------------------------------------------------------

"""

import subprocess
from bottle import run, post, request, response, get, route
import json


@route('/', method='POST')
def process():
    # return subprocess.check_output(['python', path + '.py'], shell=True)
    print(request.json)


def run_server():
    run(host='localhost', port=8000, debug=True)

if __name__ == '__main__':
    run_server()

'''
To test the program:
(1) Run challenge2_server.py to run the server
(2) Run challenge2.py to run the Client -- it send the json with humidity data to port 8000
After that you will see the output on server if communication is successful. Client will print 200 if requesst is successfully sent.
'''
