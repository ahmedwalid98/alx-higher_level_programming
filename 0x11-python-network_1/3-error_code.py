#!/usr/bin/python3
"""
    handle errors
"""
import urllib.request
import urllib.error
import sys


if __name__ == '__main__':
    try:
        req = urllib.request.Request(sys.argv[1])
        with urllib.request.urlopen(req) as res:
            print(res.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.status))
