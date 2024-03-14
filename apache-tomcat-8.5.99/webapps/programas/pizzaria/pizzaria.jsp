'<!DOCTYPE html="pt-br">
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="Content-Type" content="text/html">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pizzaria AlexandreDev</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <%
        String strnome = request.getParameter("nome");
        int intprecounidade, intquantidade, inttotal;
        intprecounidade = Integer.parseInt(request.getParameter("unidade"));
        intquantidade = Integer.parseInt(request.getParameter("qtde"));
        inttotal = intprecounidade * intquantidade;
    %>
    <div class="resp centralizar">
        <h2 class="centralizar">Valor total da compra: R$<%= inttotal %>.</h2>
        <h2 class="centralizar">Obrigado pela preferência <%= strnome %></h2>
    </div>
</body>
</html>