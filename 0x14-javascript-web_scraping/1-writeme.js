#!/usr/bin/node
const fs = require('fs');

// Function to write content to a file
function writeToFile (filePath, content) {
  try {
    // Synchronously write the content to the file using utf-8 encoding
    fs.writeFileSync(filePath, content, 'utf-8');
  } catch (error) {
    // Handle errors if any occur during file writing
    console.error(error);
  }
}

// Check if the correct number of command-line arguments is provided
if (process.argv.length !== 4) {
  console.error('Usage: ./1-writeme.js <file_path> <content>');
  process.exit(1);
}

// Retrieve file path and content from command-line arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Call the writeToFile function to perform the file writing operation
writeToFile(filePath, content);
