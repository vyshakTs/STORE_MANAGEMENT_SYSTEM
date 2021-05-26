/// <reference path="jquery.min.js" />
var i = 1;
var j = 1;
var chekcd = 0;
var optid = 0;
var featureid = 0;
var select_options;
$(document).ready(function () {
    $('#product_table').dataTable({
        "paging": true,
        "ordering": true,
        "info": false
    });
});
$('#product_table thead tr th input').click(function () {
    if (chekcd == 0) {
        $('#product_table tbody input').prop('checked', true);
        $('.tableholder .item-operatn').show();
        chekcd = 1;
    }
    else if (chekcd == 1) {
        $('#product_table tbody input').prop('checked', false);
        $('.tableholder .item-operatn').hide();
        chekcd = 0;
    }
});
//select check box
$('#product_table tbody tr input').change(function() {
    if ($('#product_table tbody tr input').is(':checked'))
        $('.tableholder .item-operatn').show();
    else
        $('.tableholder .item-operatn').hide();
});

$('#add_option').click(function ()
{
    optid++;
    select_options = $('#option\\[0\\]\\.optionname').html();
    //select_options = $('#option[0].optionname').attr('name');
    $("<div class=\"option_container\" id=\"option" + optid + "\"><div class=\"form-group\"><label class=\"col-lg-2 control-label\">Option Name</label><div class=\"col-lg-3\"><select class=\"form-control\" name=\"option[" + optid + "].optionname\">"+select_options+"</select></div><label class=\"col-lg-2 control-label\">option value</label><div class=\"col-lg-3\"><input type=\"text\" class=\"form-control\" placeholder=\"\" name=\"option[" + optid + "].optionvalue\" /></div></div><div class=\"form-group\"><label class=\"col-lg-2 control-label\">Price</label><div class=\"col-lg-3\"><input type=\"text\" class=\"form-control\" placeholder=\"\" name=\"option[" + optid + "].price\" /></div><label class=\"col-lg-2 control-label\">Stock</label><div class=\"col-lg-3\"><input type=\"text\" class=\"form-control\" placeholder=\"\" name=\"option[" + optid + "].stock\" /></div><div class=\"col-lg-2\"><button class=\"btn-danger btn deleteopt\"><span class=\"fa-trash-o fa\"></span></button></div></div><div class=\"segemnt\"></div></div>")
        .insertBefore($(this).parent('div').parent('.form-group')).prop("id", "option" + i)
        .on("click", ".deleteopt", function () {
            $(this).parent('div').parent('.form-group').parent('.option_container').remove();
            //optid--; problm detected
    });;
})
//deletefeature
$('#add_feature').click(function () {
    featureid++;
    $("<div class=\"option_container\"><div class=\"form-group\"><label class=\"col-lg-2 control-label\">Feature Name</label><div class=\"col-lg-3\"><input type=\"text\" class=\"form-control\" placeholder=\"\" name=\"feature[" + featureid + "].name\" /></div><label class=\"col-lg-2 control-label\">Feature Value</label><div class=\"col-lg-3\"><input type=\"text\" class=\"form-control\" placeholder=\"\" name=\"feature[" + featureid + "].value\" /></div><div class=\"col-lg-2\"><button class=\"btn-danger btn deletefeature\"><span class=\"fa-trash-o fa\"></span></button></div></div><div class=\"segemnt\"></div></div>")
        .insertBefore($(this).parent('div').parent('.form-group')).prop("id", "feature" + j).on("click", ".deletefeature", function () {
        $(this).parent('div').parent('.form-group').parent('.option_container').remove();
    });;
});
$('.shiping_rate').hide();
$('.shiping_togg').click(function () {
    $('.shiping_rate').toggle();
});