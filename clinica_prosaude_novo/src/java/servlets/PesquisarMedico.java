package servlets;

import banco_dados.ConexaoBancoDados;
import banco_dados.Medicos;
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
public class PesquisarMedico extends HttpServlet {
     
    @Override
     protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        ResultSet rsRegistro;
        PrintWriter out;
        String strMedico;
        int intCodigoMedico;
        
        strMedico = request.getParameter("txtMedico");
        
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
        out.println("<p class='TituloPagina'>Cadastro de Médicos </p>");
        
        try{
            ConexaoBancoDados conexao = new ConexaoBancoDados();
            Medicos medico = new Medicos();
            
            if(conexao.abrirConexao()){
                medico.configurarConexao(conexao.obterConexao());
                
                intCodigoMedico = medico.localizarRegistro(strMedico.toUpperCase());
                
                if(intCodigoMedico != 0){
                    rsRegistro = medico.lerRegistro(intCodigoMedico);
                    
                    out.println("<h2>Nome do Médico:"+rsRegistro.getString("nome_medico")+"<br>");
                    out.println("<br><br>");
                    out.println("<a href='editar_medico.jsp?codigo_medico="+intCodigoMedico+"'>[Editar]</a> <a href='excluir_medico.jsp?codigo_medico="+intCodigoMedico+"'>[Excluir]</a>");
                    out.println("<span class='LinkVoltar'><a href='javascript:history.back()'>[Voltar]</a></span>");
                }else{
                    out.println("<h2>Codigo do Médico:"+intCodigoMedico+"<br>");
                    out.println("<h2>Médico não encontrando!</h2>");
                    out.println("<br><br><br>");
                    out.println("<p class='LinkVoltar'><a href='javascript:history.back()'>[Voltar]</a></p>");                    
                }
                conexao.fecharConexao();
            }else
                out.println("<h2>Não foi possível estabelecer conexão com o banco de dados!</h2>");
        
        }catch(Exception erro){
            erro.printStackTrace();
            out.println("<h2>Erro do sistema:processo de cadastro do medico!</h2>");
        }
        out.println("<p class='RodapePagina'>Copyright(c) 2024 - Editora IFAM.</p>");
        out.println("</body>");
        out.println("</html>");
    }

}
