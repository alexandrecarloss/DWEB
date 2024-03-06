<!DOCTYPE html>
<%@ page import = "java.util.Date" %>
<%@ page import = "java.test.SimpleDateFormat" %>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="Content-Type" content="text/html">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Exemplo de uso do elemento sintático de JSP</title>
</head>
<body>
  <%! intContAcesso = 0; %>
  <%java.util.Date dataAtual = new Java.util.Date();
    String strData = new SimpleDateFormat("dd/MM/yyyy").format(dataAtual);
    %>
    <h2>Data atual: <%= strData %></h2><br>
    <%
    out.println("<h2> Contagem de atualizações da página </h2><br>");
    intContAcesso++;
    %>
    <h2>Numero de vezes que você acessou/atualizou a página: <%= intContAcesso %></h2>
</body>
</html>
