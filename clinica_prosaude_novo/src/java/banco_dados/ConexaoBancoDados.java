/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package banco_dados;

/**
 *
 * @author Aluno
 */

import java.sql.Connection;
import java.sql.DriverManager;

/**
 *
 * @author emmerson
 */
public class ConexaoBancoDados {
    Connection conBanco;
    
    public boolean abrirConexao(){
        String url = "jdbc:mysql://localhost/clinica_medica?user=root&password=root&TimeZone=true&serverTimezone=UTC&autoReconnect=true&useSSL=false";
                
        try{
            Class.forName("com.mysql.cj.jdbc.Driver");
            conBanco = DriverManager.getConnection(url);
            
            return true;
        }catch(Exception erro){
            erro.printStackTrace();
            return false;
        }
    }
    
    public boolean fecharConexao(){
        try{
            conBanco.close();
            
            return true;
        }catch(Exception erro){
            erro.printStackTrace();
            return false;
        }
    }
    
    public Connection obterConexao(){
        return conBanco;
    }
}
