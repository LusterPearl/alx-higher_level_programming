#!/bin/bash
# This script takes a URL, sends a request

curl -sI "$1" | grep -i Content-Length | awk '{print $2}' | tr -d '\r\n'
