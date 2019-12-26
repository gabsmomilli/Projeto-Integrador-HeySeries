$(function() {
    $("#btnSearch").click(function() {
        $("#tableSeries").children("tbody").html('');
        $.getJSON("http://localhost:5000/search/title/" + $("#text").val(), function(data) {
            var html = "";
            $.each(data, function(i, item) {
                html += "<tr><td>" + item.title + "</td><td>" + item.notes + "</td><td>" + item.genre + "</td><td>" + item.year + "</td></tr>";
            });
            $("#tableSeries").children("tbody").html(html);
        });
    });
     $("#btnSearch").click(function() {
        $("#tableSeries").children("tbody").html('');
        console.log($("#rdbGenre").is(":checked"));
        if($("#rdbGenre").is(":checked")) {
            $.getJSON("http://localhost:5000/search/genre/" + $("#text").val(), function(data) {
                var html = "";
                $.each(data, function(i, item) {
                    html += "<tr><td>" + item.title + "</td><td>" + item.notes + "</td><td>" + item.genre + "</td><td>" + item.year + "</td></tr>";
                });
                $("#tableSeries").children("tbody").html(html);
            });
        } else if($("#rdbTitle").is(":checked")) {
            $.getJSON("http://localhost:5000/search/title/" + $("#text").val(), function(data) {
                var html = "";
                $.each(data, function(i, item) {
                    html += "<tr><td>" + item.title + "</td><td>" + item.notes + "</td><td>" + item.genre + "</td><td>" + item.year + "</td></tr>";
                });
                $("#tableSeries").children("tbody").html(html);
            });
        } else if($("#rdbYear").is(":checked")) {
            $.getJSON("http://localhost:5000/search/year/" + $("#text").val(), function(data) {
                var html = "";
                $.each(data, function(i, item) {
                    html += "<tr><td>" + item.title + "</td><td>" + item.notes + "</td><td>" + item.genre + "</td><td>" + item.year + "</td></tr>";
                });
                $("#tableSeries").children("tbody").html(html);
            });
        }


    });
});