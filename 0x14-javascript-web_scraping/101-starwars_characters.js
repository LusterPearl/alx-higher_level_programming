#!/usr/bin/node
const request = require('request');

// Check if the correct number of command-line arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./101-starwars_characters.js <Movie_ID>');
  process.exit(1);
}

const movieId = process.argv[2];

// Star Wars API URL
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error.message);
  } else if (response.statusCode === 200) {
    // Parse the JSON response
    const movieData = JSON.parse(body);

    // Extract character URLs in the order specified by the 'characters' list
    const characterUrls = movieData.characters;

    // Fetch details for each character and print their names
    characterUrls.forEach((characterUrl) => {
      request(characterUrl, (characterError, characterResponse, characterBody) => {
        if (characterError) {
          console.error('Error fetching character:', characterError.message);
        } else if (characterResponse.statusCode === 200) {
          const characterData = JSON.parse(characterBody);
          console.log(characterData.name);
        } else {
          console.error(`Failed to retrieve character data. Status code: ${characterResponse.statusCode}`);
        }
      });
    });
  } else {
    console.error(`Failed to retrieve movie data. Status code: ${response.statusCode}`);
  }
});
