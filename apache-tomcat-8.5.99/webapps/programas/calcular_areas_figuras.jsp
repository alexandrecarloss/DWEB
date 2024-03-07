'<!DOCTYPE html="pt-br">
<html lang="pt-br">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <meta charset="ISO-8859-1">
		<title> Cálculo de Áreas</title>
        <link rel="stylesheet" href="style.css">
	</head>
	<body>
       <%
            int intFiguraGeometrica;
            String strTituloFormulario, strFormulario;

            if(request.getParameter("TipoFigura") !=  null)
                intFiguraGeometrica = Integer.parseInt(request.getParameter("TipoFigura"));
            else 
                intFiguraGeometrica = 0;

            if(intFiguraGeometrica == 1){
                strTituloFormulario = "Calculo da area de um Retangulo";
                strFormulario = "<form name='formCalculoAreasFiguras' method='get' action='area_retangulo.jsp'>";
            }else if(intFiguraGeometrica == 2){
                strTituloFormulario = "Calculo da area de uma Circunferencia";
                strFormulario = "<form name='formCalculoAreasFiguras' method='get' action='area_circunferencia.jsp'>";
            }else if(intFiguraGeometrica == 3){
                strTituloFormulario = "Calculo da area de um Triangulo";
                strFormulario = "<form name='formCalculoAreasFiguras' method='get' action='area_triangulo.jsp'>";
            } else if(intFiguraGeometrica == 4){
                strTituloFormulario = "Calculo da area de uma Trapézio";
                strFormulario = "<form name='formCalculoAreasFiguras' method='get' action='area_trapezio.jsp'>";
            }   else{
                strTituloFormulario ="**Erro**";
                strFormulario = "<form name='formCalculoAreasFiguras'>" ;
            }
            out.println(strFormulario);
       %>
       <h2 style="text-align: center;"> <%= strTituloFormulario  %></h2>
        
       <%
            if((intFiguraGeometrica == 1)||(intFiguraGeometrica == 3)){
                out.println("<p> Digite o valor da altura:");
                out.println("<input name='fldAltura' type='text' size='8' maxlength='8'/>");
                out.println("</p>");

                out.println("<p> Digite o valor da largura:");
                out.println("<input name='fldLargura' type='text' size='8' maxlength='8'/>");
                out.println("</p>");
            }else if(intFiguraGeometrica == 2){
                out.println("<p> Digite o valor o raio da circunferencia:");
                out.println("<input name='fldRaio' type='text' size='8' maxlength='8'/>");
                out.println("</p>");
            }else if(intFiguraGeometrica == 4){
                
                out.println("<p>Digite o valor da base menor:");
                out.println("<input name='base_menor' size='10' maxlength='10'>");
                out.println("</p>");
                out.println("<p>Digite o valor da base maior:");
                out.println("<input name='base_maior' size='10' maxlength='10'></p>");
                out.println("<p>Digite o valor da altura:");
                out.println("<input name='altura' size='10' maxlength='10'></p>");
            }else{
                out.println("<h2>Deve ser especificado o tipo de figura</h2>");
            }
       %>
       <p>
            <input type="submit" name="btnCalcular" value="Calcular"/>
       </p>    
    </body>
</html>