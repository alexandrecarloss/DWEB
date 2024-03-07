<!DOCTYPE html="pt-br">
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<title> Cálculo da área de um Retângulo</title>
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
                width: 200px;
            }
        </style>
	</head>
	<body>
        <%
            int intLargura, intAltura, intArea = 0;

            if(request.getParameter("fldAltura") != null)
                intAltura =  Integer.parseInt(request.getParameter("fldAltura"));
            else
                intAltura = 0;
            
            if(request.getParameter("fldLargura") != null)
                intLargura =  Integer.parseInt(request.getParameter("fldLargura"));
            else
                intLargura = 0;
            
            if((intAltura != 0)&&(intLargura != 0))
               intArea = (intLargura*intAltura);
        %>	

        <h2>Valor da area do retangulo: <%= intArea %></h2>
	</body>
</html>