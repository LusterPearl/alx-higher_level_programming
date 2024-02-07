$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/';

    $.ajax({
      type: 'GET',
      url: apiUrl + '?lang=' + languageCode,
      success: function (response) {
        $('#hello').text(response.hello);
      },
      error: function () {
        $('#hello').text('Error: Failed to fetch translation.');
      }
    });
  });
});
