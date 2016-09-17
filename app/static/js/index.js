/**
 * Created by cwh on 16-9-17.
 */
$(document).ready(function() {
    $('#nav_about').click(function (e) {
        $('#content-frame').attr('src', 'about');
    });
    $('#nav_invite').click(function (e) {
        $('#content-frame').attr('src', 'class/os');
    });
    $("#content-frame").load(function(){
        var content_height = $(this).contents().find("body").height();
        $(this).height(content_height);
    });
    var nav_show = false;
    $("#nav_menu").click(function(e) {
        if(nav_show){
            $(".button-collapse").sideNav('hide');
            nav_show = false;
        } else {
            $(".button-collapse").sideNav('show');
            nav_show = true;
        }
    });
});