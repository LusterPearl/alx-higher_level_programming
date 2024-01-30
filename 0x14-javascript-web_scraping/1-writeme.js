#!/usr/bin/node
const fs = require('fs');

// Get the file and string to write from the command
const filePath = process.argv[2];
const contentToWrite = process.argv[3];

// Check if both file path and content are provided
if (!filePath || !contentToWrite) {
  console.error('Usage: ./1-writeme.js my_file.txt "Python is cool"');
  process.exit(1);
}

// Write the string to the file in utf-8
fs.writeFile(filePath, contentToWrite, 'utf-8', (err) => {
  if (err) {
    // Print the error object if an error ocured during writing
    console.error(`Error writing to ${filePath}: ${err.message}`);
    console.error(err);
  } else {
    console.log(`Content has been written to ${filePath}`);
  }
});
