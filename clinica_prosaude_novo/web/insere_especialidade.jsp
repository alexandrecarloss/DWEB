<%-- 
    Document   : insere_especialidade
    Created on : 26/03/2024, 15:09:02
    Author     : emmsr
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<jsp:useBean id="conexao" scope="page" class="banco_dados.ConexaoBancoDados" />
<jsp:useBean id="especialidade" scope="page" class="banco_dados.Especialidades" />
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Conexão com Banco de Dados</title>
    </head>
    <body>
        <h1>Conexão com banco de dados</h1>
        
        <%
            if(conexao.abrirConexao()){
                especialidade.configurarConexao(conexao.obterConexao());
                
                if(especialidade.inserirRegistros("Clinica Geral"))
                    out.println("<h2>Especialidade 'Clinica Geral' cadastrada com sucesso</h2>");
                else
                    out.println("<h3>Erro ao tentar cadastrar especialidade</h3>");
                
                conexao.fecharConexao();
            }else
                out.println("<p>Falha na conexao com o banco de dados</p>");
        %>
    </body>
</html>

