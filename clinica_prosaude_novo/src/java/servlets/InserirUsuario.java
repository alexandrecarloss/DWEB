package servlets;

import banco_dados.ConexaoBancoDados;
import banco_dados.Usuarios;
import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import model.C_Usuarios;

public class InserirUsuario extends HttpServlet {  

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String strIDUsuario, strSenha, strAdministrativo, strFuncionario, strUsuario, strEspecialidade, strMedico, strConvenio, strAgendamento,
                strPaciente, strAgendarConsulta, strCancelarConsulta, strAtendimento;
        PrintWriter out;

        strIDUsuario = request.getParameter("txtUsuario");
        strSenha = request.getParameter("txtSenha");

        strAdministrativo = request.getParameter("chkAdministrativo") != null ? "S" : "N";
        strFuncionario = request.getParameter("chkFuncionario") != null ? "S" : "N";
        strUsuario = request.getParameter("chkUsuario") != null ? "S" : "N";
        strEspecialidade = request.getParameter("chkEspecialidade") != null ? "S" : "N";
        strMedico = request.getParameter("chkMedico") != null ? "S" : "N";
        strConvenio = request.getParameter("chkConvenio") != null ? "S" : "N";
        strAgendamento = request.getParameter("chkAgendamento") != null ? "S" : "N";
        strPaciente = request.getParameter("chkPaciente") != null ? "S" : "N";
        strAgendarConsulta = request.getParameter("chkAgendarConsulta") != null ? "S" : "N";
        strCancelarConsulta = request.getParameter("chkCancelarConsulta") != null ? "S" : "N";
        strAtendimento = request.getParameter("chkAtendimento") != null ? "S" : "N";

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

        try {
            ConexaoBancoDados conexao = new ConexaoBancoDados();
            Usuarios usuario = new Usuarios();

            C_Usuarios Usuario = new C_Usuarios(strIDUsuario.toUpperCase(),
                    strSenha.toUpperCase(),
                    strAdministrativo,
                    strFuncionario,
                    strUsuario,
                    strEspecialidade,
                    strMedico,
                    strConvenio,
                    strAgendamento,
                    strPaciente,
                    strAgendarConsulta,
                    strCancelarConsulta,
                    strAtendimento,
                    0);

            if (conexao.abrirConexao()) {
                usuario.configurarConexao(conexao.obterConexao());

                if (usuario.inserirRegistro(Usuario)) {
                    out.println("<h2>Usuário cadastrado com sucesso!</h2>");
                    out.println("<br><br><br><br>");
                    out.println("<a href='menu_usuarios.html'>Voltar</a>");
                } else {
                    out.println("<h2>Não foi possível cadastrar o usuário!</h2>");
                }

                conexao.fecharConexao();
            } else {
                out.println("<h2>Não foi possível estabelecer conexão com o banco de dados!</h2>");
            }

        } catch (Exception erro) {
            erro.printStackTrace();
            out.println("<h2>Erro do sistema: processo de cadastro de usuário!</h2>");
        }
        out.println("<p class='RodapePagina'> Copyright(c) 2024 - Editora IFAM.</p>");
        out.println("</body>");
        out.println("</html>");
    }        
}
