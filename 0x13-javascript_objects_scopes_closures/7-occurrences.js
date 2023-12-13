#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
// Use reduce to count the occurrences of searchElement in the list
  return list.reduce((count, element) => (element === searchElement) ? count + 1 : count, 0);
};
