#!/usr/bin/python3
"""
    displayin header content
"""
import requests
import sys


if __name__ == '__main__':
    res = requests.get(sys.argv[1])
    print(res.headers['X-Request-Id'])
