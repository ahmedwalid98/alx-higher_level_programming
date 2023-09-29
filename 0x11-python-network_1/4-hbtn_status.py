#!/usr/bin/python3
"""
    fetch url using requests
"""
import requests


if __name__ == '__main__':
    body = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response')
    print('\t- type: {}'.format(type(body.text)))
    print('\t- content: {}'.format(body.text))
