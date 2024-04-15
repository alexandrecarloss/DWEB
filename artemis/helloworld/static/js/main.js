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

const exampleModal = document.getElementById('exampleModal');

if (exampleModal) {
  // Adicionando evento de exibição do modal
  exampleModal.addEventListener('show.bs.modal', event => {
    // Botão que acionou o modal
    const button = event.relatedTarget;
    // Extrair informações dos atributos data-bs-*
    const recipient = button.getAttribute('data-bs-whatever');
    // Atualizar o conteúdo do modal
    const modalTitle = exampleModal.querySelector('.modal-title');
    const modalBodyInput = exampleModal.querySelector('.modal-body input');
    
    modalBodyInput.value = recipient;
  });

  // Adicionando evento de clique ao botão "Send message"
  const sendButton = exampleModal.querySelector('.btn-primary');
  sendButton.addEventListener('click', () => {
    // Obter valores do destinatário e da mensagem
    const recipient = document.getElementById('recipient-name').value;
    const message = document.getElementById('message-text').value;
    // Construir o link para o WhatsApp
    const whatsappLink = `https://wa.me/55${recipient}?text=${encodeURIComponent(message)}`;
    // Abrir o link em uma nova guia
    window.open(whatsappLink, '_blank');
  });
}

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

  // Ativar botões de opções pagina usuario
  $(document).ready(function(){
    $('.list-group-item').click(function(){
        $('.list-group-item').removeClass('active');
        $(this).addClass('active');
        
        // Esconder todos os conteúdos
        $('.conteudo').hide();
        
        // Mostrar o conteúdo correspondente ao botão clicado
        var target = $(this).data('target');
        $('#' + target).show();
        
        return false;
    });
    
    // Exibir o conteúdo "Pets Cadastrados" por padrão
    $('#pets').show();
});




