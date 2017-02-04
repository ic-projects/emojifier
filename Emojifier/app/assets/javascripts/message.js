$(document).ready(function() {
    $("input[name=message]").keypress(function(e) {
        if (e.keyCode == 13) {
            e.preventDefault();

            $.ajax({
                type: 'GET',
                url: "welcome/pysave",
                dataType: "json",
                data: {
                    item: {
                        input: $("input[name=message]").val()
                    }
                },
                success: function (data) {
                    // Adds row with data.item.input and data.item.output
                }
            });
        } else {

            $.get("/welcome/pyscript", function (data) {
                $("#messages").html(data);
            });

            $.ajax({
                type:"GET",
                url:"welcome/pyscript",
                dataType: "json",
                data: {
                    item: {
                        input: $("input[name=message]").val()
                    }
                },
                success: function (data) {
                    alert(11)
                }
            })
        }
    });
});