#!/usr/bin/node

const arg = process.argv[2];
const numofoccurences = parseInt(arg, 10);

if (isNaN(numofoccurences)) {
  console.log('Missing number of occurrences');
} else {
  let counter = 0;
  while (counter < numofoccurences) {
    console.log('C is fun');
    counter++;
  }
}
