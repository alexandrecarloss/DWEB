/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package model;

/**
 *
 * @author Aluno
 */
public class C_Medicos {
    
    private String  nomeMedico,
                    CRM;
    
    private int     codigoMedico,
                    codigoEspecialidade;

    public C_Medicos() {
        this.nomeMedico = "";
        this.CRM = "";
    }

    public C_Medicos(String nomeMedico, String CRM, int codigoMedico, int codigoEspecialidade) {
        this.nomeMedico = nomeMedico;
        this.CRM = CRM;
        this.codigoMedico = codigoMedico;
        this.codigoEspecialidade = codigoEspecialidade;
    }

    public String getNomeMedico() {
        return nomeMedico;
    }

    public void setNomeMedico(String nomeMedico) {
        this.nomeMedico = nomeMedico;
    }

    public String getCRM() {
        return CRM;
    }

    public void setCRM(String CRM) {
        this.CRM = CRM;
    }

    public int getCodigoMedico() {
        return codigoMedico;
    }

    public void setCodigoMedico(int codigoMedico) {
        this.codigoMedico = codigoMedico;
    }

    public int getCodigoEspecialidade() {
        return codigoEspecialidade;
    }

    public void setCodigoEspecialidade(int codigoEspecialidade) {
        this.codigoEspecialidade = codigoEspecialidade;
    }
    
    
    
}
