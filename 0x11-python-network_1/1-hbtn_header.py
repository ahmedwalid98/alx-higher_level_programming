#!/usr/bin/python3
import urllib.request
import sys
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of
"""


if __name__ == '__main__':
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        print(response.getheader('X-Request-Id'))
