#!/usr/bin/python3
"""
    serach by word
"""
import sys
import requests


if __name__ == '__main__':
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    paylode = {'q': letter}
    res = requests.post('http://0.0.0.0:5000/search_user', data=paylode)
    try:
        response = res.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
