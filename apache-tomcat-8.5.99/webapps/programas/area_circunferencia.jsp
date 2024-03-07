<!DOCTYPE html="pt-br">
<html lang="pt-br">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<title> Cálculo da área da Circulo</title>
        <style>
            body {
                background-image: linear-gradient(to bottom, red, orange);
                align-items: center;
                display: flex;              
            }

            h2 {
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                border: 1px solid blue;
                padding: 3rem;
                border-radius: 100%;
                width: 100px;
            }
        </style>
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