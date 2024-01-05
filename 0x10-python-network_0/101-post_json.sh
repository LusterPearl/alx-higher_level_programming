#!/bin/bash
# This script sends a JSON POST request to the specified URL with the contents of a file and displays the body of the response
URL=$1
FILE=$2
if [ -f "$FILE" ]; then
    curl -sX POST -H "Content-Type: application/json" -d @"$FILE" "$URL"
else
    echo "File not found: $FILE"
fi
