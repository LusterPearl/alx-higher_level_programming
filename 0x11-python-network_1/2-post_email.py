#!/usr/bin/python3
"""
sends a POST request to the passed URL with the
email as a parameter,
and displays the body of the response
"""
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(url, data=data) as response:
        content = response.read().decode('utf-8')
        print(content)
