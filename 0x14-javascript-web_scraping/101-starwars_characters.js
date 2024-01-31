#!/usr/bin/node
const request = require('request');

// Check if the correct number of command-line arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./101-starwars_characters.js <movie_id>');
  process.exit(1);
}

// Get the Movie ID from the command line argument
const movieId = process.argv[2];

// Construct the Star Wars API URL for the specified movie
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    // Handle error if there is an issue with the request
    console.error(error.message);
  } else if (response.statusCode === 200) {
    // Parse the JSON response to get movie details
    const movie = JSON.parse(body);

    // Extract character URLs from the movie details
    const characterUrls = movie.characters;

    // Recursive function to fetch and print character details
    function fetchCharacter (index) {
      // Check if there are more characters to fetch
      if (index < characterUrls.length) {
        const characterUrl = characterUrls[index];

        // Make a request to the character URL
        request(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            // Handle error if there is an issue with the character request
            console.error(charError.message);
          } else if (charResponse.statusCode === 200) {
            // Parse the JSON response to get character details
            const character = JSON.parse(charBody);

            // Print the name of the character
            console.log(character.name);

            // Fetch the next character in the list
            fetchCharacter(index + 1);
          } else {
            // Handle error if there is an issue with the character request
            console.error(`Failed to retrieve character data. Status code: ${charResponse.statusCode}`);
          }
        });
      }
    }

    // Start fetching characters from the beginning of the list
    fetchCharacter(0);
  } else {
    // Handle error if there is an issue with the movie request
    console.error(`Failed to retrieve movie data. Status code: ${response.statusCode}`);
  }
});
