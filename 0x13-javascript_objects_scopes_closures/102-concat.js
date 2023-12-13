#!/usr/bin/node

const fs = require('fs');

const [, , fileA, fileB, fileC] = process.argv;

const contentA = fs.readFileSync(fileA, 'utf-8');

const contentB = fs.readFileSync(fileB, 'utf-8');

const concatenatedContent = `${contentA}${contentB}`;

fs.writeFileSync(fileC, concatenatedContent);

console.log('Files concatenated successfully!');
