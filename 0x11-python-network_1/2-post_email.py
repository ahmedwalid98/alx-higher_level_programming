#!/usr/bin/python3
"""
    post request
"""
import urllib.request
import urllib.parse
import sys


if __name__ == '__main__':
    body = {
        'email': sys.argv[2]
    }
    data = urllib.parse.urlencode(body).encode("ascii")
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
