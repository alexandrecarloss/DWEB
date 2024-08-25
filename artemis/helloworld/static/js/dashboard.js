// Função para gerar cores aleatórias para o dashboard
function gera_cor(qtd=1){
    var bg_color = []
    var border_color = []
    for(let i = 0; i < qtd; i++){
        let r = Math.random() * 255;
        let g = Math.random() * 255;
        let b = Math.random() * 255;
        bg_color.push(`rgba(${r}, ${g}, ${b}, ${0.2})`)
        border_color.push(`rgba(${r}, ${g}, ${b}, ${1})`)
    }    
    return [bg_color, border_color];   
}

// Função para renderizar o gráfico do dashboard de faturamento do petshop total vendido mes/ano
function renderiza_petshop_relatorio_faturamento_venda(url){
    // Fazer fetch para receber os dados do backend
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        // Receber canva do html que vai renderizar o dashboard
        const ctx = document.getElementById('petshop_relatorio_faturamento_venda').getContext('2d');
        // Gerar cores aleatórias para o dashboard
        var cores_faturamento_mensal_produto = gera_cor(qtd=12)
        // Atribuir dados do chart
        const myChart = new Chart(ctx, {
            //Tipo de dashboard
            type: 'bar',
            data: {
                // nomes de meses que estão no label de data
                labels: data.labels,
                datasets: [{
                    //Nome do dado
                    label: 'faturamento produto R$',
                    // dados equivalentes aos meses
                    data: data.data,
                    backgroundColor: cores_faturamento_mensal_produto[0],
                    borderColor: cores_faturamento_mensal_produto[1],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    })
}


// Função para renderizar o gráfico do dashboard de quantidade do petshop total vendido mes/ano
function renderiza_petshop_relatorio_quantidade_venda(url){
    // Fazer fetch para receber os dados do backend
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        // Receber canva do html que vai renderizar o dashboard
        const ctx = document.getElementById('petshop_relatorio_quantidade_venda').getContext('2d');
        // Gerar cores aleatórias para o dashboard
        var cores_quantidade_mensal_produto = gera_cor(qtd=12)
        // Atribuir dados do chart
        const myChart = new Chart(ctx, {
            //Tipo de dashboard
            type: 'bar',
            data: {
                // nomes de meses que estão no label de data
                labels: data.labels,
                datasets: [{
                    //Nome do dado
                    label: 'quantidade produto',
                    // dados equivalentes aos meses
                    data: data.data,
                    backgroundColor: cores_quantidade_mensal_produto[0],
                    borderColor: cores_quantidade_mensal_produto[1],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    })
}


// Função para renderizar o gráfico do dashboard de quantidade vendida por categoria
function renderiza_petshop_relatorio_produto_categoria(url){
    // Fazer fetch para receber os dados do backend
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        // Receber canva do html que vai renderizar o dashboard
        const ctx = document.getElementById('petshop_relatorio_produto_categoria').getContext('2d');
        // Gerar cores aleatórias para o dashboard
        var cores_produtos_categoria = gera_cor(qtd=12)
        // Atribuir dados do chart
        const myChart = new Chart(ctx, {
            //Tipo de dashboard
            type: 'doughnut',
            data: {
                // nomes de meses que estão no label de data
                labels: data.labels,
                datasets: [{
                    //Nome do dado
                    label: 'quantidade',
                    // dados equivalentes aos meses
                    data: data.data,
                    backgroundColor: cores_produtos_categoria[0],
                    borderColor: cores_produtos_categoria[1],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    })
}

// Função para renderizar o gráfico do dashboard de faturamento do petshop total vendido mes/ano
function renderiza_petshop_relatorio_faturamento_servico(url){
    // Fazer fetch para receber os dados do backend
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        // Receber canva do html que vai renderizar o dashboard
        const ctx = document.getElementById('petshop_relatorio_faturamento_servico').getContext('2d');
        // Gerar cores aleatórias para o dashboard
        var cores_faturamento_mensal_servico = gera_cor(qtd=12)
        // Atribuir dados do chart
        const myChart = new Chart(ctx, {
            //Tipo de dashboard
            type: 'bar',
            data: {
                // nomes de meses que estão no label de data
                labels: data.labels,
                datasets: [{
                    //Nome do dado
                    label: 'faturamento serviço R$',
                    // dados equivalentes aos meses
                    data: data.data,
                    backgroundColor: cores_faturamento_mensal_servico[0],
                    borderColor: cores_faturamento_mensal_servico[1],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    })
}


// Função para renderizar o gráfico do dashboard de quantidade do petshop total vendido mes/ano
function renderiza_petshop_relatorio_quantidade_servico(url){
    // Fazer fetch para receber os dados do backend
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        // Receber canva do html que vai renderizar o dashboard
        const ctx = document.getElementById('petshop_relatorio_quantidade_servico').getContext('2d');
        // Gerar cores aleatórias para o dashboard
        var cores_quantidade_mensal_servico = gera_cor(qtd=12)
        // Atribuir dados do chart
        const myChart = new Chart(ctx, {
            //Tipo de dashboard
            type: 'bar',
            data: {
                // nomes de meses que estão no label de data
                labels: data.labels,
                datasets: [{
                    //Nome do dado
                    label: 'quantidade serviço',
                    // dados equivalentes aos meses
                    data: data.data,
                    backgroundColor: cores_quantidade_mensal_servico[0],
                    borderColor: cores_quantidade_mensal_servico[1],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    })
}

// Função para renderizar o gráfico do dashboard de quantidade vendida por categoria
function renderiza_petshop_relatorio_produto_categoria_faturamento(url){
    // Fazer fetch para receber os dados do backend
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        // Receber canva do html que vai renderizar o dashboard
        const ctx = document.getElementById('petshop_relatorio_produto_categoria_faturamento').getContext('2d');
        // Gerar cores aleatórias para o dashboard
        var cores_produtos_categoria_faturamento = gera_cor(qtd=12)
        // Atribuir dados do chart
        const myChart = new Chart(ctx, {
            //Tipo de dashboard
            type: 'doughnut',
            data: {
                // nomes de meses que estão no label de data
                labels: data.labels,
                datasets: [{
                    //Nome do dado
                    label: 'faturamento R$',
                    // dados equivalentes aos meses
                    data: data.data,
                    backgroundColor: cores_produtos_categoria_faturamento[0],
                    borderColor: cores_produtos_categoria_faturamento[1],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    })
}


function renderiza_receita_mes(url) {  
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('receita_mes').innerHTML = data.total
    })

}

////////////////////////////// Usuário ///////////////////////////////////////

// Função para renderizar o gráfico do dashboard de gastos com produtos mes/ano
function renderiza_usuario_relatorio_gastos_produtos(url){
    // Fazer fetch para receber os dados do backend
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        // Receber canva do html que vai renderizar o dashboard
        const ctx = document.getElementById('usuario_relatorio_gastos_produtos').getContext('2d');
        // Gerar cores aleatórias para o dashboard
        var cores_gastos_produtos_mensal = gera_cor(qtd=12)
        // Atribuir dados do chart
        const myChart = new Chart(ctx, {
            //Tipo de dashboard
            type: 'bar',
            data: {
                // nomes de meses que estão no label de data
                labels: data.labels,
                datasets: [{
                    //Nome do dado
                    label: 'gastos com produtos R$',
                    // dados equivalentes aos meses
                    data: data.data,
                    backgroundColor: cores_gastos_produtos_mensal[0],
                    borderColor: cores_gastos_produtos_mensal[1],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    })
}


// Função para renderizar o gráfico do dashboard de gastos com servicos mes/ano
function renderiza_usuario_relatorio_gastos_servicos(url){
    // Fazer fetch para receber os dados do backend
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        // Receber canva do html que vai renderizar o dashboard
        const ctx = document.getElementById('usuario_relatorio_gastos_servicos').getContext('2d');
        // Gerar cores aleatórias para o dashboard
        var cores_gastos_servicos_mensal = gera_cor(qtd=12)
        // Atribuir dados do chart
        const myChart = new Chart(ctx, {
            //Tipo de dashboard
            type: 'bar',
            data: {
                // nomes de meses que estão no label de data
                labels: data.labels,
                datasets: [{
                    //Nome do dado
                    label: 'gastos com serviços R$',
                    // dados equivalentes aos meses
                    data: data.data,
                    backgroundColor: cores_gastos_servicos_mensal[0],
                    borderColor: cores_gastos_servicos_mensal[1],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    })
}

// Função para renderizar o gráfico do dashboard de quantidade comprada por categoria
function renderiza_usuario_relatorio_produto_categoria(url){
    // Fazer fetch para receber os dados do backend
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        // Receber canva do html que vai renderizar o dashboard
        const ctx = document.getElementById('usuario_relatorio_produto_categoria').getContext('2d');
        // Gerar cores aleatórias para o dashboard
        var cores_quantidade_produto_categoria = gera_cor(qtd=12)
        // Atribuir dados do chart
        const myChart = new Chart(ctx, {
            //Tipo de dashboard
            type: 'doughnut',
            data: {
                // nomes de meses que estão no label de data
                labels: data.labels,
                datasets: [{
                    //Nome do dado
                    label: 'quantidade',
                    // dados equivalentes aos meses
                    data: data.data,
                    backgroundColor: cores_quantidade_produto_categoria[0],
                    borderColor: cores_quantidade_produto_categoria[1],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    })
}


// Função para renderizar o gráfico do dashboard de quantidade comprada por categoria
function renderiza_usuario_relatorio_produto_categoria_gastos(url){
    // Fazer fetch para receber os dados do backend
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        // Receber canva do html que vai renderizar o dashboard
        const ctx = document.getElementById('usuario_relatorio_produto_categoria_gastos').getContext('2d');
        // Gerar cores aleatórias para o dashboard
        var cores_gastos_produto_categoria = gera_cor(qtd=12)
        // Atribuir dados do chart
        const myChart = new Chart(ctx, {
            //Tipo de dashboard
            type: 'doughnut',
            data: {
                // nomes de meses que estão no label de data
                labels: data.labels,
                datasets: [{
                    //Nome do dado
                    label: 'gasto R$',
                    // dados equivalentes aos meses
                    data: data.data,
                    backgroundColor: cores_gastos_produto_categoria[0],
                    borderColor: cores_gastos_produto_categoria[1],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    })
}


// Função para renderizar o gráfico do dashboard de quantidade de pets adotados
function renderiza_ong_relatorio_adocoes_concluidas(url){
    // Fazer fetch para receber os dados do backend
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        // Receber canva do html que vai renderizar o dashboard
        const ctx = document.getElementById('ong_relatorio_adocoes_concluidas').getContext('2d');
        // Gerar cores aleatórias para o dashboard
        var cores_quantidade_mensal_adocao = gera_cor(qtd=12)
        // Atribuir dados do chart
        const myChart = new Chart(ctx, {
            //Tipo de dashboard
            type: 'bar',
            data: {
                // nomes de meses que estão no label de data
                labels: data.labels,
                datasets: [{
                    //Nome do dado
                    label: 'Qtde adoção',
                    // dados equivalentes aos meses
                    data: data.data,
                    backgroundColor: cores_quantidade_mensal_adocao[0],
                    borderColor: cores_quantidade_mensal_adocao[1],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    })
}



// Função para renderizar o gráfico do dashboard de quantidade de pets adotados por tipo
function renderiza_ong_relatorio_adocoes_concluidas_tipo(url){
    // Fazer fetch para receber os dados do backend
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        // Receber canva do html que vai renderizar o dashboard
        const ctx = document.getElementById('ong_relatorio_adocoes_concluidas_tipo').getContext('2d');
        // Gerar cores aleatórias para o dashboard
        var cores_quantidade_mensal_adocao_tipo = gera_cor(qtd=12)
        // Atribuir dados do chart
        const myChart = new Chart(ctx, {
            //Tipo de dashboard
            type: 'doughnut',
            data: {
                // nomes de meses que estão no label de data
                labels: data.labels,
                datasets: [{
                    //Nome do dado
                    label: 'Qtde adoção tipo',
                    // dados equivalentes aos meses
                    data: data.data,
                    backgroundColor: cores_quantidade_mensal_adocao_tipo[0],
                    borderColor: cores_quantidade_mensal_adocao_tipo[1],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    })
}



function renderiza_total_adocoes(url) {  
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('total_adocoes').innerHTML = data.total
    })
}

function renderiza_total_produtos_vendidos(url) {  
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('total_produtos_vendidos').innerHTML = data.total
    })
}


function renderiza_total_servicos_concluidos(url) {  
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('total_servicos_concluidos').innerHTML = data.total
    })
}


function renderiza_total_petshops(url) {  
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('total_petshops').innerHTML = data.total
    })
}


function renderiza_total_ongs(url) {  
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('total_ongs').innerHTML = data.total
    })
}