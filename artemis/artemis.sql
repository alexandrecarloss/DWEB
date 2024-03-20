-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`pet_tipo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`pet_tipo` (
  `pttid` INT NOT NULL AUTO_INCREMENT,
  `pttnome` VARCHAR(60) NOT NULL,
  UNIQUE INDEX `pttid_UNIQUE` (`pttid` ASC) VISIBLE,
  PRIMARY KEY (`pttid`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`pessoa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`pessoa` (
  `pesid` INT NOT NULL AUTO_INCREMENT,
  `pescpf` CHAR(11) NOT NULL,
  `pesdtnascto` DATE NOT NULL,
  `pessexo` CHAR(1) NOT NULL,
  `pescidade` VARCHAR(65) NOT NULL,
  `pesbairro` VARCHAR(65) NOT NULL,
  `pesrua` VARCHAR(65) NOT NULL,
  `pesemail` VARCHAR(65) NOT NULL,
  `pesnumero` SMALLINT NOT NULL,
  `pestelefone` VARCHAR(15) NOT NULL,
  `venda_venid` INT NULL,
  PRIMARY KEY (`pesid`),
  UNIQUE INDEX `pesid_UNIQUE` (`pesid` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`pet_porte`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`pet_porte` (
  `ptpid` INT NOT NULL AUTO_INCREMENT,
  `ptpnome` VARCHAR(65) NOT NULL,
  `ptpdescricao` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`ptpid`),
  UNIQUE INDEX `ptpid_UNIQUE` (`ptpid` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`pet`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`pet` (
  `petid` INT NOT NULL AUTO_INCREMENT,
  `petnome` VARCHAR(65) NOT NULL,
  `petsexo` CHAR(1) NOT NULL,
  `petcastrado` ENUM('Castrado', 'Não Castrado', 'Não sei') NOT NULL,
  `petdtnascto` DATE NOT NULL,
  `petpeso` FLOAT NOT NULL,
  `ong_ongid` INT NULL,
  `pet_tipo_pttid` INT NOT NULL,
  `pessoa_pesid` INT NULL,
  `pet_porte_ptpid` INT NOT NULL,
  PRIMARY KEY (`petid`),
  UNIQUE INDEX `petid_UNIQUE` (`petid` ASC) VISIBLE,
  INDEX `fk_pet_pet_tipo1_idx` (`pet_tipo_pttid` ASC) VISIBLE,
  INDEX `fk_pet_pessoa1_idx` (`pessoa_pesid` ASC) VISIBLE,
  INDEX `fk_pet_pet_porte1_idx` (`pet_porte_ptpid` ASC) VISIBLE,
  CONSTRAINT `fk_pet_pet_tipo1`
    FOREIGN KEY (`pet_tipo_pttid`)
    REFERENCES `mydb`.`pet_tipo` (`pttid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_pet_pessoa1`
    FOREIGN KEY (`pessoa_pesid`)
    REFERENCES `mydb`.`pessoa` (`pesid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_pet_pet_porte1`
    FOREIGN KEY (`pet_porte_ptpid`)
    REFERENCES `mydb`.`pet_porte` (`ptpid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`pet_raca`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`pet_raca` (
  `ptrid` INT NOT NULL AUTO_INCREMENT,
  `ptrnome` VARCHAR(65) NULL,
  `pet_tipo_pttid` INT NOT NULL,
  PRIMARY KEY (`ptrid`),
  UNIQUE INDEX `racaid_UNIQUE` (`ptrid` ASC) VISIBLE,
  INDEX `fk_pet_raca_pet_tipo1_idx` (`pet_tipo_pttid` ASC) VISIBLE,
  CONSTRAINT `fk_pet_raca_pet_tipo1`
    FOREIGN KEY (`pet_tipo_pttid`)
    REFERENCES `mydb`.`pet_tipo` (`pttid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`ong`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`ong` (
  `ongid` INT NOT NULL AUTO_INCREMENT,
  `ongnome` VARCHAR(65) NOT NULL,
  `ongcidade` VARCHAR(70) NULL,
  `ongbairro` VARCHAR(70) NOT NULL,
  `ongrua` VARCHAR(70) NOT NULL,
  `ongnum` SMALLINT NOT NULL,
  `ongtelefone` VARCHAR(15) NULL,
  `ongemail` VARCHAR(100) NULL,
  PRIMARY KEY (`ongid`),
  UNIQUE INDEX `ongid_UNIQUE` (`ongid` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`pet_foto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`pet_foto` (
  `pftid` INT NOT NULL AUTO_INCREMENT,
  `pftlink` VARCHAR(100) NULL,
  `pftdados` BLOB NULL,
  `pet_petid` INT NOT NULL,
  PRIMARY KEY (`pftid`),
  UNIQUE INDEX `pftid_UNIQUE` (`pftid` ASC) VISIBLE,
  INDEX `fk_pet_foto_pet_idx` (`pet_petid` ASC) VISIBLE,
  CONSTRAINT `fk_pet_foto_pet`
    FOREIGN KEY (`pet_petid`)
    REFERENCES `mydb`.`pet` (`petid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`pet_adocao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`pet_adocao` (
  `pet_petid` INT NOT NULL,
  `pet_ong_ongid` INT NULL,
  `pet_pet_tipo_pttid` INT NOT NULL,
  `ong_ongid` INT NULL,
  PRIMARY KEY (`pet_petid`),
  INDEX `fk_pet_adocao_ong1_idx` (`ong_ongid` ASC) VISIBLE,
  CONSTRAINT `fk_pet_adocao_pet1`
    FOREIGN KEY (`pet_petid` , `pet_ong_ongid` , `pet_pet_tipo_pttid`)
    REFERENCES `mydb`.`pet` (`petid` , `ong_ongid` , `pet_tipo_pttid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_pet_adocao_ong1`
    FOREIGN KEY (`ong_ongid`)
    REFERENCES `mydb`.`ong` (`ongid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`formapagamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`formapagamento` (
  `fpgid` INT NOT NULL AUTO_INCREMENT,
  `fpgdescricao` VARCHAR(65) NULL,
  PRIMARY KEY (`fpgid`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`venda`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`venda` (
  `venid` INT NOT NULL AUTO_INCREMENT,
  `formapagamento_fpgid` INT NOT NULL,
  `pessoa_pesid` INT NOT NULL,
  PRIMARY KEY (`venid`),
  INDEX `fk_venda_formapagamento1_idx` (`formapagamento_fpgid` ASC) VISIBLE,
  INDEX `fk_venda_pessoa1_idx` (`pessoa_pesid` ASC) VISIBLE,
  CONSTRAINT `fk_venda_formapagamento1`
    FOREIGN KEY (`formapagamento_fpgid`)
    REFERENCES `mydb`.`formapagamento` (`fpgid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_venda_pessoa1`
    FOREIGN KEY (`pessoa_pesid`)
    REFERENCES `mydb`.`pessoa` (`pesid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`petshop`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`petshop` (
  `ptsid` INT NOT NULL AUTO_INCREMENT,
  `ptsnome` VARCHAR(65) NULL,
  `ptscnpj` VARCHAR(20) NOT NULL,
  `ptscidade` VARCHAR(65) NULL,
  `ptsbairro` VARCHAR(65) NULL,
  `ptsrua` VARCHAR(65) NULL,
  `ptsnumero` SMALLINT NULL,
  `ptstelefone` VARCHAR(15) NULL,
  `ptsemail` VARCHAR(65) NULL,
  `venda_venid` INT NULL,
  PRIMARY KEY (`ptsid`),
  INDEX `fk_petshop_venda1_idx` (`venda_venid` ASC) VISIBLE,
  CONSTRAINT `fk_petshop_venda1`
    FOREIGN KEY (`venda_venid`)
    REFERENCES `mydb`.`venda` (`venid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`produto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`produto` (
  `proid` INT NOT NULL AUTO_INCREMENT,
  `pronome` VARCHAR(65) NULL,
  `propreco` DOUBLE(6,2) NULL,
  `prosaldo` INT NULL,
  `petshop_ptsid` INT NOT NULL,
  PRIMARY KEY (`proid`),
  INDEX `fk_produto_petshop1_idx` (`petshop_ptsid` ASC) VISIBLE,
  CONSTRAINT `fk_produto_petshop1`
    FOREIGN KEY (`petshop_ptsid`)
    REFERENCES `mydb`.`petshop` (`ptsid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`banho`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`banho` (
  `banid` INT NOT NULL AUTO_INCREMENT,
  `banvalor` FLOAT NOT NULL,
  `pet_petid` INT NOT NULL,
  `bandatahora` DATETIME NOT NULL,
  `petshop_ptsid` INT NOT NULL,
  `pessoa_pesid` INT NOT NULL,
  `pessoa_venda_venid` INT NOT NULL,
  PRIMARY KEY (`banid`),
  INDEX `fk_banho_pet1_idx` (`pet_petid` ASC) VISIBLE,
  INDEX `fk_banho_petshop1_idx` (`petshop_ptsid` ASC) VISIBLE,
  INDEX `fk_banho_pessoa1_idx` (`pessoa_pesid` ASC, `pessoa_venda_venid` ASC) VISIBLE,
  CONSTRAINT `fk_banho_pet1`
    FOREIGN KEY (`pet_petid`)
    REFERENCES `mydb`.`pet` (`petid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_banho_petshop1`
    FOREIGN KEY (`petshop_ptsid`)
    REFERENCES `mydb`.`petshop` (`ptsid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_banho_pessoa1`
    FOREIGN KEY (`pessoa_pesid` , `pessoa_venda_venid`)
    REFERENCES `mydb`.`pessoa` (`pesid` , `venda_venid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`tosa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`tosa` (
  `tosid` INT NOT NULL AUTO_INCREMENT,
  `tosvalor` FLOAT NOT NULL,
  `tosdatahora` DATETIME NOT NULL,
  `pet_petid` INT NOT NULL,
  `pessoa_pesid` INT NOT NULL,
  `petshop_ptsid` INT NOT NULL,
  PRIMARY KEY (`tosid`),
  INDEX `fk_tosa_pet1_idx` (`pet_petid` ASC) VISIBLE,
  INDEX `fk_tosa_pessoa1_idx` (`pessoa_pesid` ASC) VISIBLE,
  INDEX `fk_tosa_petshop1_idx` (`petshop_ptsid` ASC) VISIBLE,
  CONSTRAINT `fk_tosa_pet1`
    FOREIGN KEY (`pet_petid`)
    REFERENCES `mydb`.`pet` (`petid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_tosa_pessoa1`
    FOREIGN KEY (`pessoa_pesid`)
    REFERENCES `mydb`.`pessoa` (`pesid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_tosa_petshop1`
    FOREIGN KEY (`petshop_ptsid`)
    REFERENCES `mydb`.`petshop` (`ptsid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`produto_foto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`produto_foto` (
  `prfid` INT NOT NULL AUTO_INCREMENT,
  `prflink` VARCHAR(65) NULL,
  `prffoto` BLOB NULL,
  `produto_proid` INT NOT NULL,
  PRIMARY KEY (`prfid`),
  INDEX `fk_produto_foto_produto1_idx` (`produto_proid` ASC) VISIBLE,
  CONSTRAINT `fk_produto_foto_produto1`
    FOREIGN KEY (`produto_proid`)
    REFERENCES `mydb`.`produto` (`proid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
