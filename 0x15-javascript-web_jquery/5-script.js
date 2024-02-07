// Wait for the document to be fully loaded
$(document).ready(function () {
  // When the DIV#add_item element is clicked
  $('#add_item').click(function () {
    // Create a new <li> element
    const newItem = $('<li></li>').text('Item');
    // Append the new <li> element to the UL.my_list
    $('.my_list').append(newItem);
  });
});
