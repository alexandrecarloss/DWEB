USE clinica_medica;

CREATE TABLE IF NOT EXISTS clinica_medica.funcionarios(
	codigo_funcionario INT NOT NULL AUTO_INCREMENT,
    nome_completo VARCHAR(50)  NULL,
    numero_rg  VARCHAR(12)  NULL,
    orgao_emissor  VARCHAR(6)  NULL,
    numero_cpf  VARCHAR(14)  NULL,
    endereco  VARCHAR(50)  NULL,
    numero  VARCHAR(15)  NULL,
    complemento  VARCHAR(30)  NULL,
    bairro  VARCHAR(40)  NULL,
    cidade  VARCHAR(40)  NULL,
    estado  VARCHAR(2)  NULL,
    telefone  VARCHAR(20)  NULL,
    celular  VARCHAR(20)  NULL,
    numero_ctps  VARCHAR(20)  NULL,
    numero_pis  VARCHAR(20)  NULL,
    data_nascimento DATE NULL,
    PRIMARY KEY(codigo_funcionario),
    INDEX Idx_Nome(nome_completo ASC),
    INDEX Idx_RG(numero_rg ASC),
    INDEX Idx_CPF(numero_cpf ASC)) 
ENGINE = InnoDB;

USE clinica_medica;

CREATE TABLE IF NOT EXISTS clinica_medica.usuarios(
	registro_usuario INT NOT NULL AUTO_INCREMENT,
    identificacao_usuario VARCHAR(20)  NULL,
    senha_acesso  VARCHAR(12)  NULL,
    cadastro_funcionario VARCHAR(1) NULL DEFAULT 'N',
    cadastro_usuario VARCHAR(1) NULL DEFAULT 'N',
    cadastro_paciente VARCHAR(1) NULL DEFAULT 'N',
    cadastro_especialidade VARCHAR(1) NULL DEFAULT 'N',
    cadastro_medico VARCHAR(1) NULL DEFAULT 'N',
    cadastro_convenio VARCHAR(1) NULL DEFAULT 'N',
    agendamento_consulta VARCHAR(1) NULL DEFAULT 'N',
    cancelamento_consulta VARCHAR(1) NULL DEFAULT 'N',
    modulo_administrativo VARCHAR(1) NULL DEFAULT 'N',
    modulo_agendamento VARCHAR(1) NULL DEFAULT 'N',
    modulo_atendimento VARCHAR(1) NULL DEFAULT 'N',
	PRIMARY KEY(registro_usuario)) 
ENGINE = InnoDB;

USE clinica_medica;
CREATE TABLE IF NOT EXISTS clinica_medica.especialidades(
	codigo_especialidade INT NOT NULL AUTO_INCREMENT,
    descricao_especialidade VARCHAR(45) NULL,
	PRIMARY KEY(codigo_especialidade)) 
ENGINE = InnoDB;

USE clinica_medica;

CREATE TABLE IF NOT EXISTS clinica_medica.medicos(
	codigo_medico INT NOT NULL AUTO_INCREMENT,
    nome_medico VARCHAR(50) NULL,
    codigo_especialidade INT NOT NULL,
    CRM VARCHAR(20) NULL,
	PRIMARY KEY(codigo_medico, codigo_especialidade),
    INDEX fk_medicos_especialidade1_idx(codigo_especialidade ASC),
    CONSTRAINT fk_medicos_especialidades1
		FOREIGN KEY (codigo_especialidade)
        REFERENCES clinica_medica.especialidades(codigo_especialidade)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE clinica_medica;
CREATE TABLE IF NOT EXISTS clinica_medica.convenios(
	codigo_convenio INT NOT NULL AUTO_INCREMENT,
    empresa_convenio VARCHAR(45) NULL,
    CNPJ VARCHAR(19) NULL,
    telefone VARCHAR(20) NULL,
	PRIMARY KEY(codigo_convenio)) 
ENGINE = InnoDB;

USE clinica_medica;

CREATE TABLE IF NOT EXISTS clinica_medica.pacientes(
	codigo_paciente INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(50)  NULL,
    numero_rg  VARCHAR(12)  NULL,
    orgao_emissor  VARCHAR(6)  NULL,
    numero_cpf  VARCHAR(14)  NULL,
    endereco  VARCHAR(50)  NULL,
    numero  VARCHAR(15)  NULL,
    complemento  VARCHAR(30)  NULL,
    bairro  VARCHAR(40)  NULL,
    cidade  VARCHAR(40)  NULL,
    estado  VARCHAR(2)  NULL,
    telefone  VARCHAR(20)  NULL,
    celular  VARCHAR(20)  NULL,
    data_nascimento DATE NULL,
    sexo VARCHAR(1)  NULL,
    tem_convenio VARCHAR(1)  NULL,
    codigo_convenio INT NOT NULL,
    senha_acesso VARCHAR(12),
    PRIMARY KEY(codigo_paciente, codigo_convenio),
    INDEX fk_pacientes_convenio1_idx(codigo_convenio ASC),
    CONSTRAINT fk_pacientes_convenios1
    FOREIGN KEY (codigo_convenio)
        REFERENCES clinica_medica.convenios(codigo_convenio)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE clinica_medica;

CREATE TABLE IF NOT EXISTS clinica_medica.agenda_consulta(
	registro_agenda INT NOT NULL AUTO_INCREMENT,
    codigo_usuario INT NOT NULL,
    codigo_paciente INT NOT NULL,
    codigo_medico INT NOT NULL,
    data DATE NULL,
    hora VARCHAR(5)  NULL,
    retorno VARCHAR(1)  NULL DEFAULT 'N',
    cancelado VARCHAR(1)  NULL DEFAULT 'N',
    motivo_cancelamento TEXT NULL,
    PRIMARY KEY(registro_agenda, codigo_usuario, codigo_medico, codigo_paciente),
    INDEX fk_agenda_consulta_pacientes1_idx(codigo_paciente ASC),
    INDEX fk_agenda_consulta_medicos1_idx(codigo_medico ASC),
    INDEX fk_agenda_consulta_usuarios1_idx(codigo_usuario ASC),
    CONSTRAINT fk_agenda_consulta_pacientes1
		FOREIGN KEY (codigo_paciente)
        REFERENCES clinica_medica.pacientes(codigo_paciente)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION,
	CONSTRAINT fk_agenda_consulta_medicos1
		FOREIGN KEY (codigo_medico)
        REFERENCES clinica_medica.medicos(codigo_medico)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION,
	CONSTRAINT fk_agenda_consulta_usuarios1
		FOREIGN KEY (codigo_usuario)
        REFERENCES clinica_medica.usuarios(registro_usuario)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE clinica_medica;

CREATE TABLE IF NOT EXISTS clinica_medica.prontuario_paciente(
	registro INT NOT NULL AUTO_INCREMENT,
    registro_agenda INT NOT NULL,
    historico TEXT NULL,
    receituario TEXT NULL,
    exames TEXT NULL,
    PRIMARY KEY(registro, registro_agenda),
    INDEX fk_prontuario_paciente_agenda_consulta1_idx(registro_agenda ASC),  
    CONSTRAINT fk_prontuario_paciente_agenda_consulta1
		FOREIGN KEY (registro_agenda)
        REFERENCES clinica_medica.agenda_consulta(registro_agenda)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION)
ENGINE = InnoDB;

