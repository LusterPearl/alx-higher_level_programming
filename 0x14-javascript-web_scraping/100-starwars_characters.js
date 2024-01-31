#!/usr/bin/node
const request = require('request');

// Check if the correct number of command-line arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./100-starwars_characters.js <Movie_ID>');
  process.exit(1);
}

// Retrieve the Movie ID from the command-line argument
const movieId = process.argv[2];

// API endpoint for Star Wars movie details
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a request to the Star Wars API for the movie details
request(apiUrl, (error, response, body) => {
  // Check for request error
  if (error) {
    console.error('Error:', error.message);
    process.exit(1);
  }

  // Parse the JSON response
  const movieData = JSON.parse(body);

  // Display the characters from the movie
  movieData.characters.forEach(characterUrl => {
    // Make a request to get character details
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error:', charError.message);
        process.exit(1);
      }

      // Parse the character JSON response
      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});
