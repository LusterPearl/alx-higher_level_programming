#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"

    auth = (username, token)

    response = requests.get(url, auth=auth)

    try:
        json_data = response.json()

        if 'id' in json_data:
            print(json_data['id'])
        else:
            print("None")

    except ValueError:
        print("None")
