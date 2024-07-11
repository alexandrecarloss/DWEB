/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author user
 */
import java.sql.Connection;
import java.sql.DriverManager;

public class Conexao {
    private static final String url = "jdbc:mysql://localhost:3306/exemplobd";
    private static final String user = "root";
    private static final String password = "root";
    
    private static Connection conn;
    
    public static Connection getConexao() {
        if (conn == null) {
            conn = DriverManager.getConnection(url, user, password);
        }
    }
    
}
