'<!DOCTYPE html="pt-br">
<html lang="pt-br">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<title> Cálculo da área de um Retângulo</title>
        <link rel="stylesheet" href="styleresp.css">
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