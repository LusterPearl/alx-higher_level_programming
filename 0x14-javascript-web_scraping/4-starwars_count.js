#!/usr/bin/node
const request = require('request');

// Get the API url from the command line argument
const apiUrl = process.argv[2];

// Check if API is provided
if (!apiUrl) {
	console.error('Usage: ./4-starwars_count.js https://swapi-api.alx-tools.com/api/films/');
	process.exit(1);
}

// Character ID for Wedge Antilles
const wedgeAntillesId = 18;

// Make a request to the Star Wars API
request(apiUrl, (error, response, body) => {
	if (error) {
		console.error('Error:', error);
		process.exit(1);
	}

	// Parse the JSON response
	const films = JSON.parse(body).results;

	// Filter films where Wedge Antilles is present
	const filmsWithWedge = films.filter(film =>
		film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`)
  );

	// Print the number of films where Wedge Antilles is present
	console.log(filmsWithWedge.length);
});
