/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package banco_dados;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import model.C_Medicos;

/**
 *
 * @author Aluno
 */
public class Medicos {

    private Connection conBanco;
    private PreparedStatement psComando;
    private ResultSet rsRegistros;

    public void configurarConexao(Connection conBanco){
        this.conBanco = conBanco;
    }   

    public boolean inserirRegistro(C_Medicos medico){
        String strComandoSQL;
        try{
            strComandoSQL = "INSERT INTO medicos(nome_medico, CRM, codigo_especialidade) "+
                    "VALUES('"+medico.getNomeMedico()+"',"+"'"+
                    medico.getCRM()+"',"+
                    medico.getCodigoEspecialidade()+")";
            
            psComando = conBanco.prepareStatement(strComandoSQL);
            psComando.executeUpdate();
            
            return true;
        }catch(Exception erro){
            erro.printStackTrace();
            return false;
        }
    }

    public int localizarRegistro(String strMedico){
        int intCodigoMedico = 0;
        String strComandoSQL;
        try{
            strComandoSQL = "SELECT codigo_medico FROM medicos WHERE nome_medico ='"+strMedico+"'";
            
            psComando = conBanco.prepareStatement(strComandoSQL);
            rsRegistros = psComando.executeQuery();
            if (rsRegistros.next()) {
                intCodigoMedico = rsRegistros.getInt("codigo_medico");
            }
        }catch(Exception erro){
            erro.printStackTrace();
        }
        
        return intCodigoMedico;
    }

    public ResultSet lerRegistro(int intCodigoMedico){
        String strComandoSQL;
        try{
            strComandoSQL = "SELECT * FROM medicos WHERE codigo_medico = "+intCodigoMedico;

            psComando = conBanco.prepareStatement(strComandoSQL);
            rsRegistros = psComando.executeQuery();
            rsRegistros.next();
            
            return rsRegistros;
        }catch(Exception erro){
            erro.printStackTrace();
            return null;
        }
    }

    public boolean alterarRegistro(C_Medicos medico){
        
        String strComandoSQL;try{
            strComandoSQL = "UPDATE medicos SET nome_medico='"+
                    medico.getNomeMedico()+"',"+"codigo_especialidade="+
                    medico.getCodigoEspecialidade()+","+"CRM='"+
                    medico.getCRM()+"' WHERE codigo_medico ="+
                    medico.getCodigoMedico(); 
            
            psComando = conBanco.prepareStatement(strComandoSQL);
            psComando.executeUpdate();
            
            return true;
        }catch(Exception erro){
            erro.printStackTrace();
            return false;
        }
    }

    public boolean excluirRegistro(int intCodigoMedico){
        
        String strComandoSQL;
        
        try{
            strComandoSQL = "DELETE FROM medicos WHERE codigo_Medico ="+intCodigoMedico;
            
            psComando = conBanco.prepareStatement(strComandoSQL);
            psComando.executeUpdate();
            
            return true;
            
        }catch(Exception erro){
            erro.printStackTrace();
            return false;
        }
    }
}
