#!/usr/bin/python3
"""
takes all https alx-intranet status and tabulates response
"""
import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urlopen(url) as response:
        page = response.read()
        headers = response.info()
        print("Body response:")
        print(f"    - type: {type(body)}")
        print(f"    - content: {body}")
        print(f"    - utf8 content: {utf8_content}")
