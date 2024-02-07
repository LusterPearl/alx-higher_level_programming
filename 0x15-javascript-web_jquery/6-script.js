// Wait for the document to be fully loaded
$(document).ready(function () {
  // When the DIV#updated_header element is clicked
  $('#update_header').click(function () {
    // Update the text content
    $('header').text('New Header!!!');
  });
});
