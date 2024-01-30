#!/usr/bin/node
const request = require('request');

// Get the movie ID from the command line argument
const movieID = process.argv[2];

// Check if the movie ID is provided
if (!movieID) {
  console.error('Usage: ./3-starwars_title.js <movie-ID>');
  process.exit(1);
}

// Construct the URL with the provided movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

// Make a GET request to the Star Wars API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error requesting Star Wars API:', error);
  } else {
    // Parse the JSON response
    const movieData = JSON.parse(body);

    // Check if the movie data contains a title
    if (movieData.title) {
      console.log(movieData.title);
    } else {
      console.error('Title not found for the given movie ID');
    }
  }
});
