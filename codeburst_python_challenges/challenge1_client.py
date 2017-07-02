# https://codeburst.io/python-friday-challenge-1-a7b5ff3df31f
# Set up a plain HTTP server and handle a POST request

import requests

PORT = 8000

req = requests.post('http://localhost:8000/challenge1_message')
print(req.status_code)
