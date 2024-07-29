package servlets;

import banco_dados.ConexaoBancoDados;
import banco_dados.Usuarios;
import java.io.IOException;
import java.io.PrintWriter;
import java.sql.ResultSet;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 *
 * @author Emmerson
 */
public class PesquisarUsuario extends HttpServlet {
     
    @Override
     protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        ResultSet rsRegistro;
        PrintWriter out;
        String strUsuario;
        int intCodigoUsuario;
        
        strUsuario = request.getParameter("txtUsuario");
        
        response.setContentType("text/html;charset=UTF-8");
        out = response.getWriter();
        
        out.println("<!DOCTYPE html>");
        out.println("<html>");
        out.println("<head>");
        out.println("<meta http-equiv='Content-Type' content='text/html; charset=utf-8' />");
        out.println("<title>SGC - Versão 1.0</title>");
        out.println("<link href='clinica_medica.css' rel='stylesheet' type='text/css' />");
        out.println("</head>");
        out.println("<body class='FundoPagina'>");
        out.println("<p class='TituloAplicacao'>SGC - Sistema de Gestão de Clínicas 1.0 </p>");
        out.println("<p class='TituloPagina'>Cadastro de Usuários </p>");
        
        try{
            ConexaoBancoDados conexao = new ConexaoBancoDados();
            Usuarios usuario = new Usuarios();
            
            if(conexao.abrirConexao()){
                usuario.configurarConexao(conexao.obterConexao());
                
                intCodigoUsuario = usuario.localizarRegistro(strUsuario.toUpperCase());
                
                if(intCodigoUsuario != 0){
                    rsRegistro = usuario.lerRegistro(intCodigoUsuario);
                    
                    out.println("<h2>Identificação do uduário:"+rsRegistro.getString("Identificacao_Usuario")+"<br>");
                    out.println("<br><br>");
                    out.println("<a href='editar_usuario.jsp?codigo_usuario="+intCodigoUsuario+"'>[Editar]</a> <a href='excluir_usuario.jsp?codigo_usuario="+intCodigoUsuario+"'>[Excluir]</a>");
                    out.println("<span class='LinkVoltar'><a href='javascript:history.back()'>[Voltar]</a></span>");
                }else{
                    out.println("<h2>Usuário não encontrando!</h2>");
                    out.println("<br><br><br>");
                    out.println("<p class='LinkVoltar'><a href='javascript:history.back()'>[Voltar]</a></p>");                    
                }
                conexao.fecharConexao();
            }else
                out.println("<h2>Não foi possível estabelecer conexão com o banco de dados!</h2>");
        
        }catch(Exception erro){
            erro.printStackTrace();
            out.println("<h2>Erro do sistema:processo de cadastro do usuário!</h2>");
        }
        out.println("<p class='RodapePagina'>Copyright(c) 2024 - Editora IFAM.</p>");
        out.println("</body>");
        out.println("</html>");
    }

}
