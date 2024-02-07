// Wait for the document to be fully loaded
$(document).ready(function () {
  // Make an AJAX GET request to fetch character data
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    // Update the text content of the <div id"charactet">
    $('#character').text(data.name);
  });
});
