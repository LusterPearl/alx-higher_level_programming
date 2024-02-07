// Wait for the document to be fully loaded
jQuery(document).ready(function () {
  // When the Div red_header ellement is clicked
  jQuery('#red_header').click(function () {
    // Select the <header> element and change its text color to red
    jQuery('header').css('color', '#FF0000');
  });
});
