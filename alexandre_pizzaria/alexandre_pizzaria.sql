-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema alexandre_pizzaria
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema alexandre_pizzaria
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `alexandre_pizzaria` DEFAULT CHARACTER SET utf8 ;
USE `alexandre_pizzaria` ;

-- -----------------------------------------------------
-- Table `alexandre_pizzaria`.`pizza`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `alexandre_pizzaria`.`pizza` (
  `pizid` INT NOT NULL,
  `piznome` VARCHAR(45) NOT NULL,
  `pizdescricao` VARCHAR(500) NOT NULL,
  `pizpreco` DOUBLE(4,2) NOT NULL,
  PRIMARY KEY (`pizid`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alexandre_pizzaria`.`pedido`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `alexandre_pizzaria`.`pedido` (
  `pedid` INT NOT NULL,
  `cli_nome` VARCHAR(45) NOT NULL,
  `cli_endereco` VARCHAR(200) NOT NULL,
  `cli_telefone` VARCHAR(15) NOT NULL,
  `total` DOUBLE(5,2) NULL,
  `status` VARCHAR(45) NULL,
  `pizid` INT NOT NULL,
  PRIMARY KEY (`pedid`),
  INDEX `fk_pedido_pizza_idx` (`pizid` ASC) VISIBLE,
  CONSTRAINT `fk_pedido_pizza`
    FOREIGN KEY (`pizid`)
    REFERENCES `alexandre_pizzaria`.`pizza` (`pizid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
