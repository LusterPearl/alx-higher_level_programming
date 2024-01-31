#!/usr/bin/node
const request = require('request');
const fs = require('fs');

// Check if the correct of command-line
if (process.argv.length !== 4) {
  console.error('Usage: ./5-request_store.js <URL> <file_path>');
  process.exit(1);
}
// Get the file and string to write from the command
const url = process.argv[2];
const filePath = process.argv[3];

// Make a request to the specifed URL
request(url, (error, response, body) => {
  if (error) {
    console.error(error.message);
  } else if (response.statusCode === 200) {
    // Write the body content to the specified file path
    fs.writeFileSync(filePath, body, 'utf-8');
  } else {
    console.error(`Failed to retrieve content. Status code: ${response.statusCode}`);
  }
});
