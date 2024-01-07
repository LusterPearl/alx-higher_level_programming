#!/usr/bin/python3
"""
a Python script that takes in a letter and sends a POST
"""
import requests
import sys


if __name__ == "__main_":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    payload = {'q': letter}
    response = requests.post(url, data=payload)

    try:
        result = response.json()
        if result:
            print("[{}] {}".format(result['id'], result['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid Json")
