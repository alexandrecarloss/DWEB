package banco_dados;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import model.C_Usuarios;

public class Usuarios {
    private Connection conBanco;
    private PreparedStatement psComando;
    private ResultSet rsRegistros;

    public void configurarConexao(Connection conBanco){
        this.conBanco = conBanco;
    }

    public boolean inserirRegistro(C_Usuarios usuario){
        String strComandoSQL = "INSERT INTO Usuarios(Identificacao_Usuario, Senha_Acesso, Cadastro_Funcionario, Cadastro_Usuario, Cadastro_Paciente, Cadastro_Especialidade," +
                "Cadastro_medico, Cadastro_Convenio, Agendamento_Consulta, Cancelamento_Consulta, Modulo_Administrativo, Modulo_Agendamento, Modulo_Atendimento)" +
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";

        try{
            psComando = conBanco.prepareStatement(strComandoSQL);
            psComando.setString(1, usuario.getIdUsuario());
            psComando.setString(2, usuario.getSenhaAcesso());
            psComando.setString(3, usuario.getCadastroFuncionario());
            psComando.setString(4, usuario.getCadastroUsuario());
            psComando.setString(5, usuario.getCadastroPaciente());
            psComando.setString(6, usuario.getCadastroEspecialidade());
            psComando.setString(7, usuario.getCadastroMedico());
            psComando.setString(8, usuario.getCadastroConvenio());
            psComando.setString(9, usuario.getAgendamentoConsulta());
            psComando.setString(10, usuario.getCancelamentoConsulta());
            psComando.setString(11, usuario.getModuloAdministrativo());
            psComando.setString(12, usuario.getModuloAgendamento());
            psComando.setString(13, usuario.getModuloAtendimento());
            psComando.executeUpdate();
            return true;
        } catch(SQLException erro){
           erro.printStackTrace();
           return false;
        }
    }

    public int localizarRegistro(String strUsuario){
        int intCodigoUsuario = 0;
        String strComandoSQL = "SELECT Registro_Usuario FROM usuarios WHERE Identificacao_Usuario = ?";

        try{
            psComando = conBanco.prepareStatement(strComandoSQL);
            psComando.setString(1, strUsuario);
            rsRegistros = psComando.executeQuery();
            if (rsRegistros.next()) {
                intCodigoUsuario = rsRegistros.getInt("Registro_Usuario");
            }
        } catch(SQLException erro){
            erro.printStackTrace();
        }
        return intCodigoUsuario;
    }

    public ResultSet lerRegistro(int intCodigoUsuario){
        String strComandoSQL = "SELECT * FROM usuarios WHERE Registro_Usuario = ?";
        
        try{
            psComando = conBanco.prepareStatement(strComandoSQL);
            psComando.setInt(1, intCodigoUsuario);
            rsRegistros = psComando.executeQuery();
            if (rsRegistros.next()) {
                return rsRegistros;
            }
        } catch(SQLException erro){
            erro.printStackTrace();
        }
        return null;
    }

    public boolean alterarRegistro(C_Usuarios usuario){
        String strComandoSQL = "UPDATE usuarios SET Identificacao_Usuario = ?, Senha_Acesso = ?, Cadastro_Funcionario = ?, Cadastro_Usuario = ?, Cadastro_Paciente = ?, Cadastro_Especialidade = ?, Cadastro_Medico = ?, Cadastro_Convenio = ?, Agendamento_Consulta = ?, Cancelamento_Consulta = ?, Modulo_Administrativo = ?, Modulo_Agendamento = ?, Modulo_Atendimento = ? WHERE Registro_Usuario = ?";

        try{
            psComando = conBanco.prepareStatement(strComandoSQL);
            psComando.setString(1, usuario.getIdUsuario());
            psComando.setString(2, usuario.getSenhaAcesso());
            psComando.setString(3, usuario.getCadastroFuncionario());
            psComando.setString(4, usuario.getCadastroUsuario());
            psComando.setString(5, usuario.getCadastroPaciente());
            psComando.setString(6, usuario.getCadastroEspecialidade());
            psComando.setString(7, usuario.getCadastroMedico());
            psComando.setString(8, usuario.getCadastroConvenio());
            psComando.setString(9, usuario.getAgendamentoConsulta());
            psComando.setString(10, usuario.getCancelamentoConsulta());
            psComando.setString(11, usuario.getModuloAdministrativo());
            psComando.setString(12, usuario.getModuloAgendamento());
            psComando.setString(13, usuario.getModuloAtendimento());
            psComando.setInt(14, usuario.getCodigoUsuario());
            psComando.executeUpdate();
            return true;
        } catch(SQLException erro){
            erro.printStackTrace();
            return false;
        }
    }

    public boolean excluirRegistro(int intCodigoUsuario){
        String strComandoSQL = "DELETE FROM usuarios WHERE Registro_Usuario = ?";
        
        try{
            psComando = conBanco.prepareStatement(strComandoSQL);
            psComando.setInt(1, intCodigoUsuario);
            psComando.executeUpdate();
            return true;
        } catch(SQLException erro){
            erro.printStackTrace();
            return false;
        }
    }
}
