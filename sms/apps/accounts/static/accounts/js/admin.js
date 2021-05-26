/// <reference path="jquery.min.js" />
$(document).ready(
function () {
    $("html").niceScroll({
        cursorcolor: "#8ccf38",
        cursorwidth: 8,
        zindex: 99,
        cursorminheight: 10,
        background: "#343434",
        //cursorborder: "2px solid #8ccf38"
    });
}, 1000);

$(document).ready(function () {
});

$('#menu_togg').click(function () {
    //$('#sidebar').toggleClass('sidebar_deactive');
    $('#sidebar').toggle();
    $('.wrapper').toggleClass('wraper_margin');
});