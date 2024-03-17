// Fixed Navbar
$(window).scroll(function () {
    if ($(window).width() < 992) {
        if ($(this).scrollTop() > 55) {
            $('.fixed-top').addClass('shadow');
        } else {
            $('.fixed-top').removeClass('shadow');
        }
    } else {
        if ($(this).scrollTop() > 55) {
            $('.fixed-top').addClass('shadow').css('top', -55);
        } else {
            $('.fixed-top').removeClass('shadow').css('top', 0);
        }
    }
});

// Fixed Navbar
$(window).scroll(function () {
    if ($(window).width() < 992) {
        if ($(this).scrollTop() > 55) {
            $('.cadastro-fixed-top').addClass('shadow');
        } else {
            $('.cadastro-fixed-top').removeClass('shadow');
        }
    } else {
        if ($(this).scrollTop() > 0) {
            $('.cadastro-fixed-top').addClass('shadow');
        } else {
            $('.cadastro-fixed-top').removeClass('shadow');
        }
    }
});


//Filtro
