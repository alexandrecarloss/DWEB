-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema artemis
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema artemis
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS artemis DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema bd_artemis
-- -----------------------------------------------------
USE artemis ;

-- -----------------------------------------------------
-- Table artemis.pessoa
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS artemis.pessoa (
  pesid INT NOT NULL AUTO_INCREMENT,
  pescpf CHAR(11) NOT NULL,
  pesdtnascto DATE NOT NULL,
  pessexo CHAR(1) NOT NULL,
  pescidade VARCHAR(65) NOT NULL,
  pesbairro VARCHAR(65) NOT NULL,
  pesrua VARCHAR(65) NOT NULL,
  pesemail VARCHAR(65) NOT NULL,
  pesnumero SMALLINT NOT NULL,
  pestelefone VARCHAR(15) NOT NULL,
  pesnome VARCHAR(100) NOT NULL,
  pesestado VARCHAR(60) NOT NULL,
  PRIMARY KEY (pesid),
  UNIQUE INDEX pesid_UNIQUE (pesid ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table artemis.pet_porte
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS artemis.pet_porte (
  ptpid INT NOT NULL AUTO_INCREMENT,
  ptpnome VARCHAR(65) NOT NULL,
  ptpdescricao VARCHAR(100) NOT NULL,
  PRIMARY KEY (ptpid),
  UNIQUE INDEX ptpid_UNIQUE (ptpid ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table artemis.pet_tipo
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS artemis.pet_tipo (
  pttid INT NOT NULL AUTO_INCREMENT,
  pttnome VARCHAR(60) NOT NULL,
  UNIQUE INDEX pttid_UNIQUE (pttid ASC) VISIBLE,
  PRIMARY KEY (pttid))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table artemis.pet_raca
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS artemis.pet_raca (
  ptrid INT NOT NULL AUTO_INCREMENT,
  ptrnome VARCHAR(65) NULL,
  pet_tipo_pttid INT NOT NULL,
  PRIMARY KEY (ptrid),
  UNIQUE INDEX racaid_UNIQUE (ptrid ASC) VISIBLE,
  INDEX fk_pet_raca_pet_tipo1_idx (pet_tipo_pttid ASC) VISIBLE,
  CONSTRAINT fk_pet_raca_pet_tipo1
    FOREIGN KEY (pet_tipo_pttid)
    REFERENCES artemis.pet_tipo (pttid)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table artemis.pet
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS artemis.pet (
  petid INT NOT NULL AUTO_INCREMENT,
  petnome VARCHAR(65) NOT NULL,
  petsexo CHAR(1) NOT NULL,
  petcastrado ENUM('Castrado', 'Não Castrado', 'Não sei') NOT NULL,
  petdtnascto DATE NOT NULL,
  petpeso FLOAT NOT NULL,
  pessoa_pesid INT NULL,
  pet_porte_ptpid INT NOT NULL,
  pet_raca_ptrid INT NOT NULL,
  pet_tipo_pttid INT NOT NULL,
  PRIMARY KEY (petid),
  UNIQUE INDEX petid_UNIQUE (petid ASC) VISIBLE,
  INDEX fk_pet_pessoa1_idx (pessoa_pesid ASC) VISIBLE,
  INDEX fk_pet_pet_porte1_idx (pet_porte_ptpid ASC) VISIBLE,
  INDEX fk_pet_pet_raca1_idx (pet_raca_ptrid ASC) VISIBLE,
  INDEX fk_pet_pet_tipo1_idx (pet_tipo_pttid ASC) VISIBLE,
  CONSTRAINT fk_pet_pessoa1
    FOREIGN KEY (pessoa_pesid)
    REFERENCES artemis.pessoa (pesid)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_pet_pet_porte1
    FOREIGN KEY (pet_porte_ptpid)
    REFERENCES artemis.pet_porte (ptpid)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_pet_pet_raca1
    FOREIGN KEY (pet_raca_ptrid)
    REFERENCES artemis.pet_raca (ptrid)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_pet_pet_tipo1
    FOREIGN KEY (pet_tipo_pttid)
    REFERENCES artemis.pet_tipo (pttid)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table artemis.ong
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS artemis.ong (
  ongid INT NOT NULL AUTO_INCREMENT,
  ongnome VARCHAR(65) NOT NULL,
  ongcidade VARCHAR(70) NULL,
  ongbairro VARCHAR(70) NOT NULL,
  ongrua VARCHAR(70) NOT NULL,
  ongnum SMALLINT NOT NULL,
  ongtelefone VARCHAR(15) NULL,
  ongemail VARCHAR(100) NULL,
  PRIMARY KEY (ongid),
  UNIQUE INDEX ongid_UNIQUE (ongid ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table artemis.pet_foto
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS artemis.pet_foto (
  pftid INT NOT NULL AUTO_INCREMENT,
  pftfoto VARCHAR(100) NOT NULL,
  pet_petid INT NOT NULL,
  PRIMARY KEY (pftid),
  UNIQUE INDEX pftid_UNIQUE (pftid ASC) VISIBLE,
  INDEX fk_pet_foto_pet_idx (pet_petid ASC) VISIBLE,
  CONSTRAINT fk_pet_foto_pet
    FOREIGN KEY (pet_petid)
    REFERENCES artemis.pet (petid)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table artemis.pet_adocao
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS artemis.pet_adocao (
  ong_ongid INT NULL,
  pet_petid INT NOT NULL,
  INDEX fk_pet_adocao_ong1_idx (ong_ongid ASC) VISIBLE,
  PRIMARY KEY (pet_petid),
  CONSTRAINT fk_pet_adocao_ong1
    FOREIGN KEY (ong_ongid)
    REFERENCES artemis.ong (ongid)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_pet_adocao_pet1
    FOREIGN KEY (pet_petid)
    REFERENCES artemis.pet (petid)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table artemis.petshop
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS artemis.petshop (
  ptsid INT NOT NULL AUTO_INCREMENT,
  ptsnome VARCHAR(65) NULL,
  ptscnpj VARCHAR(20) NOT NULL,
  ptscidade VARCHAR(65) NULL,
  ptsbairro VARCHAR(65) NULL,
  ptsrua VARCHAR(65) NULL,
  ptsnumero SMALLINT NULL,
  ptstelefone VARCHAR(15) NULL,
  ptsemail VARCHAR(65) NULL,
  PRIMARY KEY (ptsid))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table artemis.produto
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS artemis.produto (
  proid INT NOT NULL AUTO_INCREMENT,
  pronome VARCHAR(65) NOT NULL,
  propreco DOUBLE(6,2) NOT NULL,
  prosaldo INT NULL,
  propetshop_ptsid INT NOT NULL,
  prodtvalidade DATE NULL,
  PRIMARY KEY (proid),
  INDEX fk_produto_petshop1_idx (propetshop_ptsid ASC) VISIBLE,
  CONSTRAINT fk_produto_petshop1
    FOREIGN KEY (propetshop_ptsid)
    REFERENCES artemis.petshop (ptsid)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table artemis.formapagamento
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS artemis.formapagamento (
  fpgid INT NOT NULL AUTO_INCREMENT,
  fpgdescricao VARCHAR(65) NULL,
  PRIMARY KEY (fpgid))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table artemis.venda
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS artemis.venda (
  venid INT NOT NULL AUTO_INCREMENT,
  venformapagamento_fpgid INT NOT NULL,
  venpessoa_pesid INT NOT NULL,
  venpetshop_ptsid INT NOT NULL,
  venvalor FLOAT NOT NULL,
  PRIMARY KEY (venid),
  INDEX fk_venda_formapagamento1_idx (venformapagamento_fpgid ASC) VISIBLE,
  INDEX fk_venda_pessoa1_idx (venpessoa_pesid ASC) VISIBLE,
  INDEX fk_venda_petshop1_idx (venpetshop_ptsid ASC) VISIBLE,
  CONSTRAINT fk_venda_formapagamento1
    FOREIGN KEY (venformapagamento_fpgid)
    REFERENCES artemis.formapagamento (fpgid)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_venda_pessoa1
    FOREIGN KEY (venpessoa_pesid)
    REFERENCES artemis.pessoa (pesid)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_venda_petshop1
    FOREIGN KEY (venpetshop_ptsid)
    REFERENCES artemis.petshop (ptsid)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table artemis.tiposervico
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS artemis.tiposervico (
  tpsid INT NOT NULL AUTO_INCREMENT,
  tpsnome VARCHAR(70) NOT NULL,
  tpsdescricao VARCHAR(45) NOT NULL,
  PRIMARY KEY (tpsid))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table artemis.servico
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS artemis.servico (
  serid INT NOT NULL AUTO_INCREMENT,
  servalor FLOAT NOT NULL,
  tosdatahora DATETIME NOT NULL,
  pet_petid INT NOT NULL,
  pessoa_pesid INT NOT NULL,
  petshop_ptsid INT NOT NULL,
  tiposervico_tpsid INT NOT NULL,
  PRIMARY KEY (serid),
  INDEX fk_tosa_pet1_idx (pet_petid ASC) VISIBLE,
  INDEX fk_tosa_pessoa1_idx (pessoa_pesid ASC) VISIBLE,
  INDEX fk_tosa_petshop1_idx (petshop_ptsid ASC) VISIBLE,
  INDEX fk_servico_tiposervico1_idx (tiposervico_tpsid ASC) VISIBLE,
  CONSTRAINT fk_tosa_pet1
    FOREIGN KEY (pet_petid)
    REFERENCES artemis.pet (petid)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_tosa_pessoa1
    FOREIGN KEY (pessoa_pesid)
    REFERENCES artemis.pessoa (pesid)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_tosa_petshop1
    FOREIGN KEY (petshop_ptsid)
    REFERENCES artemis.petshop (ptsid)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_servico_tiposervico1
    FOREIGN KEY (tiposervico_tpsid)
    REFERENCES artemis.tiposervico (tpsid)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table artemis.produto_foto
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS artemis.produto_foto (
  prfid INT NOT NULL AUTO_INCREMENT,
  prffoto VARCHAR(100) NOT NULL,
  produto_proid INT NOT NULL,
  PRIMARY KEY (prfid),
  INDEX fk_produto_foto_produto1_idx (produto_proid ASC) VISIBLE,
  UNIQUE INDEX prfid_UNIQUE (prfid ASC) VISIBLE,
  CONSTRAINT fk_produto_foto_produto1
    FOREIGN KEY (produto_proid)
    REFERENCES artemis.produto (proid)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table artemis.itemvenda
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS artemis.itemvenda (
  produto_proid INT NOT NULL,
  venda_venid INT NOT NULL,
  itvqtde INT NOT NULL,
  PRIMARY KEY (produto_proid, venda_venid),
  INDEX fk_produto_has_venda_venda1_idx (venda_venid ASC) VISIBLE,
  INDEX fk_produto_has_venda_produto1_idx (produto_proid ASC) VISIBLE,
  CONSTRAINT fk_produto_has_venda_produto1
    FOREIGN KEY (produto_proid)
    REFERENCES artemis.produto (proid)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_produto_has_venda_venda1
    FOREIGN KEY (venda_venid)
    REFERENCES artemis.venda (venid)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

INSERT INTO `artemis`.`pet_porte` (`ptpnome`, `ptpdescricao`) VALUES ('Pequeno', 'circunferência de 31 a 43 cm');
INSERT INTO `artemis`.`pet_porte` (`ptpnome`, `ptpdescricao`) VALUES ('Médio', 'circunferência de 43 a 66 cm');
INSERT INTO `artemis`.`pet_porte` (`ptpnome`, `ptpdescricao`) VALUES ('Grande', 'circunferência de 63 a 80 cm');

INSERT INTO `artemis`.`pet_tipo` (`pttnome`) VALUES ('Cachorro');
INSERT INTO `artemis`.`pet_tipo` (`pttnome`) VALUES ('Gato');
INSERT INTO `artemis`.`pet_tipo` (`pttnome`) VALUES ('Coelho');

select * from pet_porte;
select * from pet_raca;
select * from pet_tipo;

delimiter ##
create procedure sp_inserepet(nome varchar(65), sexo char(1), castrado enum('castrado','não castrado','não sei'), dtnascto date, peso float, pessoa int, porte int, raca int, tipo int)
begin
if(pessoa in (select pesid from pessoa)) then
	if(porte in (select ptpid from pet_porte)) then
		if (raca in (select ptrid from pet_raca)) then
			if (tipo in (select pttid from pet_tipo)) then
				insert into pet (petnome, petsexo, petcastrado, petdtnascto, petpeso, pessoa_pesid, pet_porte_ptpid, pet_raca_ptrid, pet_tipo_pttid)
				values (nome, sexo, castrado, dtnascto, peso, pessoa, porte, raca, tipo);
			else
				select "Tipo de pet não registrado";
			end if;
		else
			select "Tipo de reça não registrado";
		end if;
	else
		select "Porte não registrado";
	end if;
else
	select "Pessoa não existe";
end if;

end##
delimiter ;

delimiter ##
create procedure sp_alterapet(nome varchar(65), sexo char(1), castrado enum('castrado','não castrado','não sei'), dtnascto date, peso float, pessoa int, porte int, raca int, tipo int, cod int)
begin
if(pessoa in (select pesid from pessoa)) then
	if(porte in (select ptpid from pet_porte)) then
		if (raca in (select ptrid from pet_raca)) then
			if (tipo in (select pttid from pet_tipo)) then
				update pet 
                set petnome=nome,
                petsexo=sexo, 
                petcastrado= castrado, 
                petdtnascto=dtnascto, 
                petpeso=peso, 
                pessoa_pesid=pessoa,
                pet_porte_ptpid=porte, 
                pet_raca_ptrid=raca, 
                pet_tipo_pttid = tipo
                where cod= petid;
			else
				select "Tipo de pet não registrado";
			end if;
		else
			select "Tipo de reça não registrado";
		end if;
	else
		select "Porte não registrado";
	end if;
else
	select "Pessoa não existe";
end if;

end##
delimiter ;


delimiter ##
create procedure sp_excluipet(cod int)
begin

if (cod in (select petid from pet)) then
	delete from pet
	where petid = cod;
else
	select "Pet não existe";
end if;

end##
delimiter ;


delimiter ##
create procedure sp_inserepessoa(cpf varchar(12), dtnascto date, sexo char(1), cidade varchar(70), bairro varchar(70), rua varchar(70), email varchar(70), numero int, telefone varchar(12), nome varchar(70), estado varchar(70))
begin

insert into pessoa (pescpf,pesdtnascto,pessexo,pescidade,pesbairro,pesrua,pesemail,pesnumero,pestelefone,pesnome,pesestado)
values (cpf, dtnascto, sexo, cidade, bairro, rua, email, numero, telefone, nome, estado);

end##
delimiter ;



delimiter ##
create procedure sp_excluipessoa(cod int)
begin

if (cod in (select pesid from pessoa)) then
	delete from pessoa
	where pesid = cod;
else
	select "Pessoa não existe";
end if;

end##
delimiter ;




delimiter ##
create procedure sp_alterapessoa(cpf varchar(12), dtnascto date, sexo char(1), cidade varchar(70), bairro varchar(70), rua varchar(70), email varchar(70), numero int, telefone varchar(12), nome varchar(70), estado varchar(70), cod int)
begin

update pessoa 
set pescpf=cpf,
pesdtnascto=dtnascto,
pessexo=sexo,
pescidade=cidade,
pesbairro=bairro,
pesrua=rua,
pesemail=email,
pesnumero=numero,
pestelefone=telefone,
pesnome=nome,
pesestado=estado
where cod=pesid;

end##
delimiter ;





