// Wait for the document to be fully loaded
$(document).ready(function () {
  // Make an AJAX GET request to fetch translation data
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    // Display the translation of "hello" in the HTML tag DIV#hello
    $('#hello').text(data.hello);
  });
});
