package banco_dados;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class TesteConexao {
    public static void main(String[] args) {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection conexao = DriverManager.getConnection("jdbc:mysql://localhost:3306/clinica_medica", "root", "root");
            if (conexao != null) {
                System.out.println("Conexão estabelecida com sucesso!");
                conexao.close();
            } else {
                System.out.println("Falha na conexão!");
            }
        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        }
    }
}