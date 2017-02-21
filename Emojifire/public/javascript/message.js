$(document).ready(function() {
    $('form[name=emojify]').submit(function(event) {
        event.preventDefault();
    });

    $('input[name=message]').keyup(function(event) {
        event.preventDefault();
        if (event.keyCode == 13 || event.keyCode == 32) {    
            $.ajax({
                type: 'POST',
                url: '/parse',
                data: {
                    message: $('input[name=message]').val()
                },
                success: function(data) {
                    $('#messages').html(twemoji.parse(data));
                }
            });
        }
    });

    $('input[name=message]').on('input', function(event) {
        event.preventDefault();
        if ($('input[name=message]').val().length == 0) {
            $("#messages").html("<h class='text-center'>What do you want to emojify?</h>");
        }
    });
});
