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

// Função para renderizar o gráfico do dashboard de faturamento do patshop total vendido mes/ano
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
        var cores_faturamento_mensal = gera_cor(qtd=12)
        // Atribuir dados do chart
        const myChart = new Chart(ctx, {
            //Tipo de dashboard
            type: 'bar',
            data: {
                // nomes de meses que estão no label de data
                labels: data.labels,
                datasets: [{
                    //Nome do dado
                    label: 'faturamento',
                    // dados equivalentes aos meses
                    data: data.data,
                    backgroundColor: cores_faturamento_mensal[0],
                    borderColor: cores_faturamento_mensal[1],
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
        var cores_faturamento_mensal = gera_cor(qtd=12)
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
                    backgroundColor: cores_faturamento_mensal[0],
                    borderColor: cores_faturamento_mensal[1],
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
        var cores_faturamento_mensal = gera_cor(qtd=12)
        // Atribuir dados do chart
        const myChart = new Chart(ctx, {
            //Tipo de dashboard
            type: 'bar',
            data: {
                // nomes de meses que estão no label de data
                labels: data.labels,
                datasets: [{
                    //Nome do dado
                    label: 'gastos com produtos',
                    // dados equivalentes aos meses
                    data: data.data,
                    backgroundColor: cores_faturamento_mensal[0],
                    borderColor: cores_faturamento_mensal[1],
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
        var cores_faturamento_mensal = gera_cor(qtd=12)
        // Atribuir dados do chart
        const myChart = new Chart(ctx, {
            //Tipo de dashboard
            type: 'bar',
            data: {
                // nomes de meses que estão no label de data
                labels: data.labels,
                datasets: [{
                    //Nome do dado
                    label: 'gastos com serviços',
                    // dados equivalentes aos meses
                    data: data.data,
                    backgroundColor: cores_faturamento_mensal[0],
                    borderColor: cores_faturamento_mensal[1],
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
        var cores_faturamento_mensal = gera_cor(qtd=12)
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
                    backgroundColor: cores_faturamento_mensal[0],
                    borderColor: cores_faturamento_mensal[1],
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