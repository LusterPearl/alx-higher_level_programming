// Wait for the document to be fully loaded
jQuery(document).ready(function () {
// When the DIV#toggle_header element is clicked
  jQuery('#toggle_header').click(function () {
    // Toggle the class f the <header> element read and green
    jQuery('header').toggleClass('red green');
  });
});
