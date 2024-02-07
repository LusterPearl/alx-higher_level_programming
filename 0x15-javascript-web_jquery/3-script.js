// Wait for the document to be fully loaded
jQuery(document).ready(function () {
  // When the DIV#red_header element is clicked
  jQuery('#red_header').click(function () {
    // Add the 'red' class to the <header> element
    jQuery('header').addClass('red');
  });
});
