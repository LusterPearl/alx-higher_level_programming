$(document).ready(function () {
  function fetchTranslation () {
    const languageCode = $('#language_code').val();
    const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/';

    $.ajax({
      type: 'GET',
      url: apiUrl + '?lang=' + languageCode,
      success: function (response) {
        $('#hello').text(reponse.hello);
      },
      error: function () {
        $('#hello').text('Error: Filed to tetch transalation.');
      }
    });
  }

  $('#btn_translate').click(fetchTranslation);

  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      fetchTranslation();
    }
  });
});
