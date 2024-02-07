// Wait for the ocument to be fully loaded
$(document).ready(function () {
  // Make an AJX GET request to fetch movie data
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    // Loop through the results array
    data.results.forEach(function (movie) {
      // Append a new list item with the movie title to the UL#list_movies element
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});
