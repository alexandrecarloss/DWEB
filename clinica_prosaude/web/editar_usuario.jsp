<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@page import="java.sql.ResultSet"%>
<%@page import="model.C_Usuarios"%>
<jsp:useBean id="conexao" scope="page" class="banco_dados.ConexaoBancoDados"/>
<jsp:useBean id="usuario" scope="page" class="banco_dados.Usuarios"/>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title>SGC - Versão 1.0</title>
        <link href="clinica_medica.css" rel="stylesheet" type="text/css" />
    </head>
    <body class="FundoPagina">
        <%
            ResultSet rsRegistro;
            boolean blnConectado;
                        
            C_Usuarios Usuario = new C_Usuarios();
            int intCodigoUsuario = Integer.parseInt(request.getParameter("codigo_usuario"));
            blnConectado = false;
            
            if (conexao.abrirConexao()) 
            {
                usuario.configurarConexao(conexao.obterConexao());
                
                rsRegistro = usuario.lerRegistro(intCodigoUsuario);
                
                Usuario.setIdUsuario(rsRegistro.getString("Identificacao_Usuario"));
                Usuario.setSenhaAcesso(rsRegistro.getString("Senha_Acesso"));
                Usuario.setCadastroFuncionario(rsRegistro.getString("Cadastro_Funcionario"));
                Usuario.setCadastroUsuario(rsRegistro.getString("Cadastro_Usuario"));
                Usuario.setCadastroPaciente(rsRegistro.getString("Cadastro_Paciente"));
                Usuario.setCadastroEspecialidade(rsRegistro.getString("Cadastro_Especialidade"));
                Usuario.setCadastroMedico(rsRegistro.getString("Cadastro_Medico"));
                Usuario.setCadastroConvenio(rsRegistro.getString("Cadastro_Convenio"));
                Usuario.setAgendamentoConsulta(rsRegistro.getString("Agendamento_Consulta"));
                Usuario.setCancelamentoConsulta(rsRegistro.getString("Cancelamento_Consulta"));
                Usuario.setModuloAdministrativo(rsRegistro.getString("Modulo_Administrativo"));
                Usuario.setModuloAgendamento(rsRegistro.getString("Modulo_Agendamento"));
                Usuario.setModuloAtendimento(rsRegistro.getString("Modulo_Atendimento"));
                Usuario.setCodigoUsuario(intCodigoUsuario);

                conexao.fecharConexao();
                
                blnConectado = true;
            }
            else
                out.println("<p>Falha na conexão com o banco de dados!</p>");
        %>
                
        <% if (blnConectado) {%>
        <p class="TituloAplicacao">SGC - Sistema de Gestão de Clínicas 1.0</p>
        <p class="TituloPagina">Cadastro de Funcionários - Edição</p>

        <form name="formEditaUsuario" method="post" action="atualizarUsuario" target="_parent">
              <p>Nome do usuário: <input type="text" name="txtNomeUsuario" size="20" maxlength="20" value="<%=Usuario.getIdUsuario()%>"/></p>
              
              <% if(Usuario.getModuloAdministrativo().equals("S")) { %>
              <p><input name="chkAdministrativo" type="checkbox" value="ModuloAdministrativo" checked="checked" />Módulo administrativo</p>
              <%
                }
                else
                {
              %>
              <p><input name="chkAdministrativo" type="checkbox" value="ModuloAdministrativo" />Módulo administrativo</p>
              <% } %>

              <% if(Usuario.getCadastroFuncionario().equals("S")) { %>
              <p>&nbsp;&nbsp;&nbsp;&nbsp;<input name="chkFuncionario" type="checkbox" value="Funcionario" checked="checked"/>Cadastro de funcionários</p>
              <%
                }
                else
                {
              %>
              <p>&nbsp;&nbsp;&nbsp;&nbsp;<input name="chkFuncionario" type="checkbox" value="Funcionario" />Cadastro de funcionários</p>
              <% } %>

              <% if(Usuario.getCadastroUsuario().equals("S")) { %>
              <p>&nbsp;&nbsp;&nbsp;&nbsp;<input name="chkUsuario" type="checkbox" value="Usuario" checked="checked"/>Cadastro de usuários</p>
              <%
                }
                else
                {
              %>
              <p>&nbsp;&nbsp;&nbsp;&nbsp;<input name="chkUsuario" type="checkbox" value="Usuario" />Cadastro de usuários</p>
              <% } %>

              <% if(Usuario.getCadastroEspecialidade().equals("S")) { %>
              <p>&nbsp;&nbsp;&nbsp;&nbsp;<input name="chkEspecialidade" type="checkbox" value="Especialidade" checked="checked"/>Cadastro de especialidades</p>
              <%
                }
                else
                {
              %>
              <p>&nbsp;&nbsp;&nbsp;&nbsp;<input name="chkEspecialidade" type="checkbox" value="Especialidade" />Cadastro de especialidades</p>
              <% } %>

              <% if(Usuario.getCadastroMedico().equals("S")) { %>
              <p>&nbsp;&nbsp;&nbsp;&nbsp;<input name="chkMedico" type="checkbox" value="Medico" checked="checked"/>Cadastro de médicos</p>
              <%
                }
                else
                {
              %>
              <p>&nbsp;&nbsp;&nbsp;&nbsp;<input name="chkMedico" type="checkbox" value="Medico" />Cadastro de médicos</p>
              <% } %>

              <% if(Usuario.getCadastroConvenio().equals("S")) { %>
              <p>&nbsp;&nbsp;&nbsp;&nbsp;<input name="chkConvenio" type="checkbox" value="Convenio" checked="checked"/>Cadastro de convênios</p>
              <%
                }
                else
                {
              %>
              <p>&nbsp;&nbsp;&nbsp;&nbsp;<input name="chkConvenio" type="checkbox" value="Convenio" />Cadastro de convênios</p>
              <% } %>

              <% if(Usuario.getModuloAgendamento().equals("S")) { %>
              <p><input name="chkAgendamento" type="checkbox" value="ModuloAgendamento" checked="checked"/>Módulo de agendamento</p>
              <%
                }
                else
                {
              %>
              <p><input name="chkAgendamento" type="checkbox" value="ModuloAgendamento" />Módulo de agendamento</p>
              <% } %>

              <% if(Usuario.getCadastroPaciente().equals("S")) { %>
              <p>&nbsp;&nbsp;&nbsp;&nbsp;<input name="chkPaciente" type="checkbox" value="Paciente" checked="checked"/>Cadastro de pacientes</p>
              <%
                }
                else
                {
              %>
              <p>&nbsp;&nbsp;&nbsp;&nbsp;<input name="chkPaciente" type="checkbox" value="Paciente" />Cadastro de pacientes</p>
              <% } %>
              
              <% if(Usuario.getAgendamentoConsulta().equals("S")) { %>
              <p>&nbsp;&nbsp;&nbsp;&nbsp;<input name="chkAgendarConsulta" type="checkbox" value="AgendarConsulta" checked="checked"/>Agendamento de consulta</p>
              <%
                }
                else
                {
              %>
              <p>&nbsp;&nbsp;&nbsp;&nbsp;<input name="chkAgendarConsulta" type="checkbox" value="AgendarConsulta" />Agendamento de consulta</p>
              <% } %>

              <% if(Usuario.getCancelamentoConsulta().equals("S")) { %>
              <p>&nbsp;&nbsp;&nbsp;&nbsp;<input name="chkCancelarConsulta" type="checkbox" value="CancelarConsulta" checked="checked"/>Cancelamento de consulta</p>
              <%
                }
                else
                {
              %>
              <p>&nbsp;&nbsp;&nbsp;&nbsp;<input name="chkCancelarConsulta" type="checkbox" value="CancelarConsulta" />Cancelamento de consulta</p>
              <% } %>
              
              <% if(Usuario.getModuloAtendimento().equals("S")) { %>
              <p><input name="chkAtendimento" type="checkbox" value="ModuloAtendimento" checked="checked"/>Módulo de atendimento médico</p>
              <%
                }
                else
                {
              %>
              <p><input name="chkAtendimento" type="checkbox" value="ModuloAtendimento" />Módulo de atendimento médico</p>
              <% } %>
              
              <p>
                  <input type="hidden" name="codigo_usuario" value="<%=intCodigoUsuario%>">
                  <input type="hidden" name="senha_acesso" value="<%=Usuario.getSenhaAcesso()%>">
              </p>
              <br>
              <p><input type="submit" name="btnAtualizar" value="Atualizar" />
                  <span class="LinkVoltar"><a href="javascript:history.back()">[Voltar]</a></span>
              </p>
        </form>
        
        <p class="RodapePagina">Copyright(c) 2015 - Editora Érica Ltda.</p>
        <%}%>
    </body>
</html>
