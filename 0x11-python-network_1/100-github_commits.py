#!/usr/bin/python3
"""
Please list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line
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
