$(document).ready(function() {
    $('form[name=emojify]').submit(function(event) {
        event.preventDefault();

        $.ajax({
            type: 'POST',
            url: '/parse',
            data: {
                message: $('input[name=message]').val()
            },
            success: function(data) {
                $('#messages').html(data);
            }
        });
    });
});