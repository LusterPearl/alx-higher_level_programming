#!/usr/bin/node

const dict = require('./101-data').dict;

const sortedDict = Object.entries(dict).reduce((result, [userId, occurrences]) => {
  if (!result[occurrences]) {
    result[occurrences] = [];
  }
  result[occurrences].push(userId);
  return result;
}, {});

console.log(sortedDict);
