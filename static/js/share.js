$(document).ready(function(){
    let temp = $("<input>");
    let url = $(location).attr('href');
    $('#share-btn').click(function() {
        $("body").append(temp);
        temp.val(url).select();
        document.execCommand("copy");
        temp.remove();
        $('#share-btn').text("URL copied!");
    })

    $("#toggle").hover(
        function() {
            $('#favorite').stop().animate({"opacity": "0"}, "slow");
        },
        function() {
            $('#favorite').stop().animate({"opacity": "1"}, "slow");
        });

})
