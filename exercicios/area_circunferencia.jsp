<!DOCTYPE html="pt-br">
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<title> Cálculo da área da Circulo</title>
	</head>
	<body>
        <%
            double dblRaio, pi = 3.14151692, dblArea = 0;

            if(request.getParameter("fldRaio") != null)
                dblRaio = Double.parseDouble(request.getParameter("fldRaio"));
			else
				dblRaio = 0;
            dblArea = pi*dblRaio*dblRaio;
        %>	

        <h2>Valor da area do circulo: <%= dblArea %></h2>
	</body>
</html>