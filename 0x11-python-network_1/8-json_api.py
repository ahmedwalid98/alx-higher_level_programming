#!/usr/bin/python3
"""
    serach by word
"""
import sys
import requests


if __name__ == '__main__':
    paylode = {'q': sys.argv[2] if sys.argv[2] else ""}
    res = requests.post('http://0.0.0.0:5000/search_user', data=paylode)
    try:
        response = res.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
