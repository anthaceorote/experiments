# https://codeburst.io/python-friday-challenge-2-6f6808f43273
# Simulating live data stream

import random
import threading
import requests
import json
import sys

humidity_data = []


def humidity_stream():
    ''' Generate constant decimal values between 0.0 and 99.99 '''
    return random.uniform(0.0, 99.99)


def get_humidity():
    ''' Posts humidity value at interval between 0.1 to 1 seconds '''
    global humidity_data
    humidity_data.append(round(humidity_stream(), 2))
    # print(humidity_data)
    threading.Timer(random.random(), get_humidity).start()


def send_humidity():
    ''' Send humidity list every 10 measurements via HTTP Post '''
    global humidity_data
    if len(humidity_data) % 10 == 0 and len(humidity_data) > 0:
        req = requests.post('http://localhost:8000/', json={'humidity_data': humidity_data[-10:]})
        print(req.status_code)
        # print(humidity_data[-10:])

if __name__ == '__main__':
    get_humidity()
    while len(humidity_data) <= 100:
        send_humidity()
