$(document).ready(function() {

//informatiile pentru click event pentru butonul Search
    $("#search").click(function() {
        //trimite un get request catre Google API
        var searchReq = $.get("/sendRequest/" + $("#query").val());
        searchReq.done(function(data) {
            //afisare rezultate in link dupa ce requestul este complet
            $("#url").attr("href", data.result);
        });
    });

});