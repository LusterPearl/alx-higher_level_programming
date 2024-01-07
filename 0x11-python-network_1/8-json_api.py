#!/usr/bin/python3
"""
a Python script that takes in a letter and sends a POST
"""
import requests
import sys


if __name__ == "__main_":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': letter}

    response = requests.post(url, data=payload)

    try:
        json_data - response.json()

        if json_data:
            print(f"[{json_data['id']}] {json_data['name']}")
        else:
            print("No result")

    except ValueError:
        print("Not a valid Json")
