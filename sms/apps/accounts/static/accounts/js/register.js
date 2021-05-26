/// <reference path="jquery.min.js" /
var maxtab = 3;
//code in the block must removed 
$(document).ready(function () {
    $('#gotostore').click(function () {
            window.location.replace("account");
    });
});
//end thsi section
$(document).ready(
function () {
    $("html").niceScroll({
        cursorcolor: "#8ccf38",
        cursorwidth: 8,
        zindex: 99,
        cursorminheight: 10,
        background: "#ccc",
        //cursorborder: "2px solid #8ccf38"
    });
}, 1000);

$(document).ready(function () {
    var form = $("#register");

    form.validate({
        rules: {
            store_name: "required",
            email: {
                required: true,
                email: true
            },
            password: {
                required: true,
                minlength: 5
            },
            fullname: "required",
            zipcode: {
                required: true,
                number: true,
            }
        },
        messages: {
            store_name: "Your store Name Can't be Empty",
            email: "Please enter a valid email address",
            password: {
                required: "Please provide a password",
                minlength: "Your password must be at least 5 characters long"
            },
        }
    });
    $('#stage1_next').click(function () {
        if (form.valid()) {
            $('.stepby-tab ul .tab1').parent()
            $('.stepby-tab ul .tab1').removeClass("current-step");
            $('.stepby-tab ul .tab2').addClass("current-step");
            $('.tab-container .tab1').hide();
            $('.tab-container .tab2').show();
            $('.stepby-tab .tab1 ').click(function () {
                if (form.valid()) {
                    $('.stepby-tab ul .tab2').removeClass("current-step");
                    $('.stepby-tab ul .tab1').addClass("current-step");
                    $('.stepby-tab ul .tab3').removeClass("current-step");
                    $('.tab-container .tab1').show();
                    $('.tab-container .tab2').hide();
                    $('.tab-container .tab3').hide();
                }
            });
            $('.stepby-tab .tab2 ').click(function () {
                if (form.valid()) {
                    $('.stepby-tab ul .tab1').removeClass("current-step");
                    $('.stepby-tab ul .tab2').addClass("current-step");
                    $('.stepby-tab ul .tab3').removeClass("current-step");
                    $('.tab-container .tab1').hide();
                    $('.tab-container .tab2').show();
                    $('.tab-container .tab3').hide();
                }
            });
        }
        else {

        }
    });
    $('#goback').click(function () {
            $('.tab-container .tab2').hide();
            $('.tab-container .tab1').show();
            $('.stepby-tab ul .tab2').removeClass("current-step");
            $('.stepby-tab ul .tab1').addClass("current-step");
    });
    $('#Submit2').click(function () {
        if (form.valid()) {
            $('.tab-container .tab2').hide();
            $('.tab-container .tab3').show();
            $('.stepby-tab ul .tab2').removeClass("current-step");
            $('.stepby-tab ul .tab3').addClass("current-step");
            $('.stepby-tab .tab3 ').click(function () {
                $('.stepby-tab ul .tab1').removeClass("current-step");
                $('.stepby-tab ul .tab2').removeClass("current-step");
                $('.stepby-tab ul .tab3').addClass("current-step");
                $('.tab-container .tab1').hide();
                $('.tab-container .tab2').hide();
                $('.tab-container .tab3').show();
            });
        }
        else { }
        });
});