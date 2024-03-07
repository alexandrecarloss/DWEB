<!DOCTYPE html="pt-br">
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<title> Cálculo da área do Triângulo</title>
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
                padding: 3rem;
                width: 200px;
                border-bottom: 1px solid blue;
            }

            h2:before {
                content: "";
                position: absolute;
                top: -50%;
                left: 10%;
                width: 1px;
                height: 300px;
                background-color: blue;
                transform: rotate(45deg);           
            }

            h2:after {
                content: "";
                position: absolute;
                bottom: -50%;
                right: 10%;
                width: 1px;
                height: 300px;
                background-color: blue;
                transform: rotate(-45deg);           
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
               intArea = (intLargura*intAltura)/2;
        %>	

        <h2>Valor da area do triangulo: <%= intArea %></h2>
	</body>
</html>