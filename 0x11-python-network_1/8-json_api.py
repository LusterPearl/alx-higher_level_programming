#!/usr/bin/python3
"""
a Python script that takes in a letter and sends a POST
"""
import requests
import sys


if __name__ == "__main_":
    url = "http://0.0.0.0:5000/search_user"
    letter = argv[1] if len(argv) == 2 else ""

    payload = {'q': letter}
    req = requests.post(url, data=payload)

    try:
        val = req.json()
        if val:
            print("[{}] {}".format(val.get('id'), val.get('name')))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid Json")
