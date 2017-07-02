# https://codeburst.io/python-friday-challenge-1-a7b5ff3df31f
# Set up a plain HTTP server and handle a POST request

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

'''
To test the program:
(1) Run challenge1.py to run the server
(2) Run challenge1_client.py to run the Client -- it posts a message (name of file to run) to port 8000
After that you will see the output on server if communication is successful. Client will print 200 if requesst is successfully sent.
'''


# --------------------------------------------------------------------------------------------------------

# Another way to do it
''' Server.py
import subprocess
from bottle import run, post, request, response, get, route


@route('/<path>', method='POST')
def process(path):
    return subprocess.check_output(['python', path + '.py'], shell=True)


def run_server():
    run(host='localhost', port=8080, debug=True)

if __name__ == '__main__':
    run_server

'''