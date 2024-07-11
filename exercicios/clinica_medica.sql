-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema clinica_medica
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema clinica_medica
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `clinica_medica` DEFAULT CHARACTER SET utf8 ;
USE `clinica_medica` ;

-- -----------------------------------------------------
-- Table `clinica_medica`.`funcionarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_medica`.`funcionarios` (
  `codigo_funcionario` INT NOT NULL,
  `nome_completo` VARCHAR(50) NULL,
  `numero_rg` VARCHAR(12) NULL,
  `orgao_emissor` VARCHAR(6) NULL,
  `numero_cpf` VARCHAR(14) NULL,
  `endereco` VARCHAR(50) NULL,
  `numero` VARCHAR(15) NULL,
  `complemento` VARCHAR(30) NULL,
  `bairro` VARCHAR(40) NULL,
  `cidade` VARCHAR(40) NULL,
  `estado` VARCHAR(2) NULL,
  `telefone` VARCHAR(20) NULL,
  `celular` VARCHAR(20) NULL,
  `numero_ctps` VARCHAR(20) NULL,
  `numero_pis` VARCHAR(20) NULL,
  `data_nascimento` DATE NULL,
  PRIMARY KEY (`codigo_funcionario`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `clinica_medica`.`especialidades`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_medica`.`especialidades` (
  `codigo_especialidade` INT NOT NULL,
  `descricao_especialidade` VARCHAR(45) NULL,
  PRIMARY KEY (`codigo_especialidade`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `clinica_medica`.`medicos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_medica`.`medicos` (
  `codigo_medico` INT NOT NULL,
  `nome_medico` VARCHAR(50) NULL,
  `crm` VARCHAR(20) NULL,
  `codigo_especialidade` INT NOT NULL,
  PRIMARY KEY (`codigo_medico`),
  INDEX `fk_medicos_especialidades_idx` (`codigo_especialidade` ASC) VISIBLE,
  CONSTRAINT `fk_medicos_especialidades`
    FOREIGN KEY (`codigo_especialidade`)
    REFERENCES `clinica_medica`.`especialidades` (`codigo_especialidade`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `clinica_medica`.`convenios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_medica`.`convenios` (
  `codigo_convenio` INT NOT NULL,
  `empresa_convenio` VARCHAR(45) NULL,
  `cnpj` VARCHAR(18) NULL,
  `telefone` VARCHAR(20) NULL,
  PRIMARY KEY (`codigo_convenio`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `clinica_medica`.`pacientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_medica`.`pacientes` (
  `codigo_paciente` INT NOT NULL,
  `nome` VARCHAR(50) NULL,
  `numero_rg` VARCHAR(12) NULL,
  `orgao_emissor` VARCHAR(6) NULL,
  `numero_cpf` VARCHAR(14) NULL,
  `endereco` VARCHAR(50) NULL,
  `numero` VARCHAR(50) NULL,
  `complemento` VARCHAR(30) NULL,
  `bairro` VARCHAR(40) NULL,
  `cidade` VARCHAR(40) NULL,
  `estado` VARCHAR(2) NULL,
  `telefone` VARCHAR(20) NULL,
  `celular` VARCHAR(20) NULL,
  `data_nascmento` DATE NULL,
  `sexo` VARCHAR(1) NULL,
  `tem_convenio` VARCHAR(1) NULL,
  `senha_acesso` VARCHAR(10) NULL,
  `codigo_convenio` INT NOT NULL,
  PRIMARY KEY (`codigo_paciente`),
  INDEX `fk_pacientes_convenios1_idx` (`codigo_convenio` ASC) VISIBLE,
  CONSTRAINT `fk_pacientes_convenios1`
    FOREIGN KEY (`codigo_convenio`)
    REFERENCES `clinica_medica`.`convenios` (`codigo_convenio`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `clinica_medica`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_medica`.`usuarios` (
  `registro_usuario` INT NOT NULL,
  `identificacao_usuario` VARCHAR(20) NULL,
  `senha_acesso` VARCHAR(10) NULL,
  `cadastro_funcionario` VARCHAR(1) NULL,
  `cadastro_usuario` VARCHAR(1) NULL,
  `cadastro_paciente` VARCHAR(1) NULL,
  `cadastro_especialidade` VARCHAR(1) NULL,
  `cadastro_medico` VARCHAR(1) NULL,
  `cadastro_convenio` VARCHAR(1) NULL,
  `agendamento_consulta` VARCHAR(1) NULL,
  `cancelamento_consulta` VARCHAR(1) NULL,
  `modulo_administrativo` VARCHAR(1) NULL,
  `modulo_agendamento` VARCHAR(1) NULL,
  `modulo_atendimento` VARCHAR(1) NULL,
  PRIMARY KEY (`registro_usuario`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `clinica_medica`.`agenda_consulta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_medica`.`agenda_consulta` (
  `registro_agenda` INT NOT NULL,
  `data` DATE NULL,
  `hora` VARCHAR(5) NULL,
  `retorno` VARCHAR(1) NULL,
  `cancelado` VARCHAR(1) NULL,
  `motivo_cancelamento` TEXT NULL,
  `registro_usuario` INT NOT NULL,
  `codigo_medico` INT NOT NULL,
  `codigo_paciente` INT NOT NULL,
  PRIMARY KEY (`registro_agenda`),
  INDEX `fk_agenda_consulta_usuarios1_idx` (`registro_usuario` ASC) VISIBLE,
  INDEX `fk_agenda_consulta_medicos1_idx` (`codigo_medico` ASC) VISIBLE,
  INDEX `fk_agenda_consulta_pacientes1_idx` (`codigo_paciente` ASC) VISIBLE,
  CONSTRAINT `fk_agenda_consulta_usuarios1`
    FOREIGN KEY (`registro_usuario`)
    REFERENCES `clinica_medica`.`usuarios` (`registro_usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_agenda_consulta_medicos1`
    FOREIGN KEY (`codigo_medico`)
    REFERENCES `clinica_medica`.`medicos` (`codigo_medico`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_agenda_consulta_pacientes1`
    FOREIGN KEY (`codigo_paciente`)
    REFERENCES `clinica_medica`.`pacientes` (`codigo_paciente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `clinica_medica`.`prontuario_paciente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_medica`.`prontuario_paciente` (
  `registro` INT NOT NULL,
  `historico` TEXT NULL,
  `receituario` TEXT NULL,
  `exames` TEXT NULL,
  `registro_agenda` INT NOT NULL,
  PRIMARY KEY (`registro`),
  INDEX `fk_prontuario_paciente_agenda_consulta1_idx` (`registro_agenda` ASC) VISIBLE,
  CONSTRAINT `fk_prontuario_paciente_agenda_consulta1`
    FOREIGN KEY (`registro_agenda`)
    REFERENCES `clinica_medica`.`agenda_consulta` (`registro_agenda`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
