$(document).ready(function() {
    $("input[name=message]").keypress(function(e) {
        if (e.keyCode == 13) {
            e.preventDefault();
        }

        $.get("/welcome/pyscript", function(data) {
            $("#messages").html(data);
        });
    });
});