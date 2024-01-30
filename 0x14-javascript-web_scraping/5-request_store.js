#!/usr/bin/node
const fs = require('fs');
const request = require('request');

// Get the URL and file path from the command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Check if both URL and file path are provided
if (!url || !filePath) {
  console.error('Usage: ./5-request_store.js https://jsonplaceholder.typicode.com/todos <file_path>');
  process.exit(1);
}

// Make a request to te specified URL
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  // Write the body response to the specified file path
  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      console.error('Error writing to file:', err);
      process.exit(1);
    }

    console.log(`Body response stored in ${filePath}`);
  });
});
