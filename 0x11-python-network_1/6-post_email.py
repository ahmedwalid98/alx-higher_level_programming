#!/usr/bin/python3
"""
    send post request by requests
"""
import requests
import sys


if __name__ == '__main__':
    payload = {"email": sys.argv[2]}
    res = requests.post(sys.argv[1], data=payload)
    print(res.text)
