#!/usr/bin/node
const request = require('request');

// Get the URL from the command line arguments
const url = process.argv[2];

// Check if a URL is provided
if (!url) {
  console.error('Usage: /2-statuscode.js https://alx-intranet.hbtn.io');
  process.exit(1);
}

// Make a Get request to the specified URL
request.get(url, (error, response) => {
  if (error) {
    // Print an error message if there is an error is an error
    console.error(error);
  } else {
    // Print the status code
    console.log('code:', response.statusCode);
  }
});
