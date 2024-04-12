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

$('input[type=radio][name=tipoPessoa]').change(function () {
    if (this.value === 'pessoaFisica') {
        $('#camposPessoaFisica').show();
        $('#camposONG').hide();
        $('#camposPessoaJuridica').hide();
    }
    else if (this.value === 'ong') {
        $('#camposPessoaFisica').hide();
        $('#camposONG').show();
        $('#camposPessoaJuridica').hide();
    }
    else if (this.value === 'pessoaJuridica') {
        $('#camposPessoaFisica').hide();
        $('#camposONG').hide();
        $('#camposPessoaJuridica').show();
    }
});

//Filtro
