#!/usr/bin/python3
"""
must use the package requests
You are not allow to import packages other than requests
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')

    print(x_request_id)
