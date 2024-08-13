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

    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });

    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
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

    // Alterna campos com base na seleção de tipo de cadastro
    document.querySelectorAll('input[name="tipoCadastro"]').forEach((input) => {
        input.addEventListener('change', function () {
            const tipo = this.value;
            const camposProduto = document.getElementById('camposProduto');
            const camposServico = document.getElementById('camposServico');
            if (tipo === 'produto') {
                camposProduto.style.display = 'block';
                camposServico.style.display = 'none';
            } else {
                camposProduto.style.display = 'none';
                camposServico.style.display = 'block';
            }
        });
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

// Função para uncheck os outros métodos de pagamento
function uncheckOthers(selectedId) {
    const checkboxes = document.querySelectorAll('input[name="PaymentMethod"]');
    const cardInfo = document.getElementById('card-info');
    let showCardInfo = false;

    checkboxes.forEach(checkbox => {
        if (checkbox.id !== selectedId) {
            checkbox.checked = false;
        }
    });

    if (selectedId === 'Card-1' || selectedId === 'Card-0') {
        showCardInfo = true;
    }

    cardInfo.style.display = showCardInfo ? 'block' : 'none';
}

document.addEventListener('DOMContentLoaded', function() {
    // Função para exibir o modal de confirmação
    window.showConfirmModal = function() {
        const isPaymentMethodSelected = document.querySelector('input[name="PaymentMethod"]:checked');
        const isAddressFormVisible = document.getElementById('address-form').style.display === 'block';
        let isAddressValid = true;
        let errorMessage = '';

        // Verifica se o método de pagamento foi selecionado
        if (!isPaymentMethodSelected) {
            errorMessage += 'Por favor, selecione um método de pagamento.<br>';
        }

        // Se o formulário de endereço está visível, valida os campos
        if (isAddressFormVisible) {
            const requiredFields = document.querySelectorAll('#address-form input[required]');
            requiredFields.forEach(field => {
                if (!field.value) {
                    isAddressValid = false;
                }
            });
            if (!isAddressValid) {
                errorMessage += 'Por favor, preencha todos os campos do endereço.<br>';
            }
        }

        if (errorMessage) {
            const errorContainer = document.getElementById('error-message');
            errorContainer.innerHTML = errorMessage;
            errorContainer.style.display = 'block';
        } else {
            const confirmModal = new bootstrap.Modal(document.getElementById('confirmModal'));
            confirmModal.show();
        }
    };

    
    window.confirmOrder = function() {
        document.getElementById('orderForm').submit();
    };
    
    window.hideConfirmModal = function() {
        const confirmModal = bootstrap.Modal.getInstance(document.getElementById('confirmModal'));
        confirmModal.hide();
    };

    window.toggleAddressForm = function() {
        const addressForm = document.getElementById('address-form');
        if (addressForm.style.display === 'none') {
            addressForm.style.display = 'block';
        } else {
            addressForm.style.display = 'none';
        }
    };
    
    window.uncheckOthers = function(checkboxId) {
        const checkboxes = document.querySelectorAll('input[name="PaymentMethod"]');
        checkboxes.forEach(checkbox => {
            if (checkbox.id !== checkboxId) {
                checkbox.checked = false;
            }
        });
    };




    // Código para as estrelas de avaliação
    const stars = document.querySelectorAll('.rating .star');
    const ratingValueInput = document.getElementById('ratingValue');

    stars.forEach(star => {
        star.addEventListener('click', function() {
            const value = this.getAttribute('data-value');
            ratingValueInput.value = value;
            updateStars(value);
        });

        star.addEventListener('mouseover', function() {
            const value = this.getAttribute('data-value');
            updateStars(value);
        });

        star.addEventListener('mouseout', function() {
            const selectedValue = ratingValueInput.value;
            updateStars(selectedValue);
        });
    });

    function updateStars(value) {
        stars.forEach(star => {
            if (star.getAttribute('data-value') <= value) {
                star.classList.add('selected');
            } else {
                star.classList.remove('selected');
            }
        });
    }
});