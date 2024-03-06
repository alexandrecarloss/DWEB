<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="Content-Type" content="text/html">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cálculo de área de um trapézio</title>
</head>
<body>
  <% int intBaseMaior, intBaseMenor, intAltura, intArea;
  intBaseMenor = Integer.parseInt(request.getParameter("base_menor"));
  intBaseMaior = Integer.parseInt(request.getParameter("base_maior"));
  altura = Integer.parseInt(request.getParameter("altura"));
  intArea = ((intBaseMenor + intBaseMaior) * intAltura) /2;
  %>
  <h2>Valor da área do trapézio: <%= intArea %>/h2>
</body>
</html>
