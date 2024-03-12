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
-- Table `mydb`.`ong`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`ong` (
  `ongid` INT NOT NULL,
  `ongnome` VARCHAR(65) NOT NULL,
  `ongcidade` VARCHAR(70) NULL,
  `ongbairro` VARCHAR(70) NOT NULL,
  `ongrua` VARCHAR(70) NOT NULL,
  `ongnum` SMALLINT NOT NULL,
  `ongcep` VARCHAR(15) NULL,
  `ongtelefone` VARCHAR(15) NULL,
  `ongemail` VARCHAR(100) NULL,
  PRIMARY KEY (`ongid`),
  UNIQUE INDEX `ongid_UNIQUE` (`ongid` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`pet_tipo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`pet_tipo` (
  `pttid` INT NOT NULL,
  `pttnome` VARCHAR(60) NOT NULL,
  UNIQUE INDEX `pttid_UNIQUE` (`pttid` ASC) VISIBLE,
  PRIMARY KEY (`pttid`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`pessoa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`pessoa` (
  `pesid` INT NOT NULL,
  `pescpf` CHAR(11) NOT NULL,
  `pesdtnascto` DATE NOT NULL,
  `pessexo` CHAR(1) NOT NULL,
  `pescidade` VARCHAR(65) NOT NULL,
  `pesbairro` VARCHAR(65) NOT NULL,
  `pesrua` VARCHAR(65) NOT NULL,
  `pesemail` VARCHAR(65) NOT NULL,
  `pesnumero` SMALLINT NOT NULL,
  `pestelefone` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`pesid`),
  UNIQUE INDEX `pesid_UNIQUE` (`pesid` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`pet_porte`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`pet_porte` (
  `ptpid` INT NOT NULL,
  `ptpnome` VARCHAR(65) NOT NULL,
  `ptpdescricao` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`ptpid`, `ptpnome`),
  UNIQUE INDEX `ptpid_UNIQUE` (`ptpid` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`pet`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`pet` (
  `petid` INT NOT NULL,
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
  INDEX `fk_pet_ong1_idx` (`ong_ongid` ASC) VISIBLE,
  INDEX `fk_pet_pet_tipo1_idx` (`pet_tipo_pttid` ASC) VISIBLE,
  INDEX `fk_pet_pessoa1_idx` (`pessoa_pesid` ASC) VISIBLE,
  INDEX `fk_pet_pet_porte1_idx` (`pet_porte_ptpid` ASC) VISIBLE,
  CONSTRAINT `fk_pet_ong1`
    FOREIGN KEY (`ong_ongid`)
    REFERENCES `mydb`.`ong` (`ongid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
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
  `ptrid` INT NOT NULL,
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
-- Table `mydb`.`pet_foto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`pet_foto` (
  `pftid` INT NOT NULL,
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


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
