<!DOCTYPE html="pt-br">
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<title> Cálculo da área de um trapézio</title>
	</head>
	<body>
        <%
            int intBaseMenor, intBaseMaior, intAltura, intArea;
            intBaseMenor = Integer.parseInt(request.getParameter("base_menor"));
            intBaseMaior = Integer.parseInt(request.getParameter("base_maior"));
            intAltura = Integer.parseInt(request.getParameter("altura"));
            intArea = ((intBaseMenor + intBaseMaior)*intAltura)/2;
        %>	

        <h2>Valor da area do trapezio: <%= intArea %></h2>
	</body>
</html>