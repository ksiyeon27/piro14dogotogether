$('.search_toggleBtn').on('click', function () {
   if ($("#menu_wrap").hasClass("active")) {
        $('#menu_wrap').removeClass('active');
        $('.search_toggleBtn').css({
            "left":"0.5rem"
        });
    } else{
        $('#menu_wrap').addClass('active');
        $('.search_toggleBtn').css({
            "left":"19.5rem"
        });
    }

});

