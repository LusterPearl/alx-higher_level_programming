#!/usr/bin/node
const request = require('request');

// Check if the correct number of command-line arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./starwars_count.js <api_url>');
  process.exit(1);
}

// Retrieve the API URL from the command-line arguments
const apiUrl = process.argv[2];
const characterId = 18; // Character ID for Wedge Antilles

// Make a request to the Star Wars API
request(apiUrl, (error, response, body) => {
  // Check for request error
  if (error) {
    console.error('Error:', error.message);
  } else if (response.statusCode === 200) { // Check if the request was successful
    // Parse the JSON response
    const filmsData = JSON.parse(body);

    // Count the number of films where Wedge Antilles is present
    const count = filmsData.results.reduce((acc, film) => {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
        return acc + 1;
      }
      return acc;
    }, 0);

    // Print the count
    console.log(count);
  } else {
    // Print an error message if the request was not successful
    console.error(`Failed to retrieve data. Status code: ${response.statusCode}`);
  }
});
