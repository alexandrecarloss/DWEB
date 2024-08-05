// Espera o documento estar pronto antes de executar o código
$(document).ready(function () {
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
  
    // Fixed Navbar for Cadastro page
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
  
    // Modal Example
    const exampleModal = document.getElementById('exampleModal');
    if (exampleModal) {
      // Evento de exibição do modal
      exampleModal.addEventListener('show.bs.modal', event => {
        const button = event.relatedTarget;
        const recipient = button.getAttribute('data-bs-whatever');
        const modalTitle = exampleModal.querySelector('.modal-title');
        const modalBodyInput = exampleModal.querySelector('.modal-body input');
        modalBodyInput.value = recipient;
      });
  
      // Evento de clique no botão "Send message"
      const sendButton = exampleModal.querySelector('.btn-primary');
      sendButton.addEventListener('click', () => {
        const recipient = document.getElementById('recipient-name').value;
        const message = document.getElementById('message-text').value;
        const whatsappLink = `https://wa.me/55${recipient}?text=${encodeURIComponent(message)}`;
        window.open(whatsappLink, '_blank');
      });
    }
  
    // Alterna campos com base na seleção de tipo de pessoa
    $('input[type=radio][name=tipoPessoa]').change(function () {
      if (this.value === 'pessoaFisica') {
        $('#camposPessoaFisica').show();
        $('#camposONG').hide();
        $('#camposPessoaJuridica').hide();
      } else if (this.value === 'ong') {
        $('#camposPessoaFisica').hide();
        $('#camposONG').show();
        $('#camposPessoaJuridica').hide();
      } else if (this.value === 'pessoaJuridica') {
        $('#camposPessoaFisica').hide();
        $('#camposONG').hide();
        $('#camposPessoaJuridica').show();
      }
    });
  
    // Alterna campos com base na seleção de tipo de cadastro
    $('input[type=radio][name=tipoCadastro]').change(function () {
      if (this.value === 'produto') {
        $('#camposProduto').show();
        $('#camposServico').hide();
      } else if (this.value === 'servico') {
        $('#camposProduto').hide();
        $('#camposServico').show();
      }
    });
  
    // Ativa os botões de opções na página do usuário
    $('.list-group-item').click(function () {
      $('.list-group-item').removeClass('active');
      $(this).addClass('active');
  
      $('.conteudo').hide();
      
      var target = $(this).data('target');
      
      $('#' + target).show();
      return false;
    });
  
    // Incrementa ou decrementa o valor no campo de quantidade
    $('.btn-minus').click(function () {
      const $quantityInput = $(this).closest('.quantity').find('.quantity-input');
      let currentValue = parseInt($quantityInput.val());
      if (currentValue > 1) {
        $quantityInput.val(currentValue - 1);
      }
    });
  
    $('.btn-plus').click(function () {
      const $quantityInput = $(this).closest('.quantity').find('.quantity-input');
      let currentValue = parseInt($quantityInput.val());
      $quantityInput.val(currentValue + 1);
    });
  });
  
  // Função para toggle o formulário de endereço
  function toggleAddressForm() {
    const addressForm = document.getElementById('address-form');
    const savedAddress = document.getElementById('saved-address');
    const isChecked = document.getElementById('Address-1').checked;
  
    if (isChecked) {
      addressForm.style.display = 'block';
      savedAddress.style.display = 'none';

    } else {
        addressForm.style.display = 'none';
        savedAddress.style.display = 'block';
      }
    }
    
    // Função para toggle o formulário de pagamento
    function togglePaymentForm() {
      const paymentForm = document.getElementById('payment-form');
      const savedPayment = document.getElementById('saved-payment');
      const isChecked = document.getElementById('Payment-1').checked;
    
      if (isChecked) {
        paymentForm.style.display = 'block';
        savedPayment.style.display = 'none';
      } else {
        paymentForm.style.display = 'none';
        savedPayment.style.display = 'block';
      }
    }
    
    // Função para toggle o formulário de entrega
    function toggleDeliveryForm() {
      const deliveryForm = document.getElementById('delivery-form');
      const savedDelivery = document.getElementById('saved-delivery');
      const isChecked = document.getElementById('Delivery-1').checked;
    
      if (isChecked) {
        deliveryForm.style.display = 'block';
        savedDelivery.style.display = 'none';
      } else {
        deliveryForm.style.display = 'none';
        savedDelivery.style.display = 'block';
      }
    }
