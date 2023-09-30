create table dimensao_municipio (
	id integer primary key identity(1,1),
	codigo_ibge varchar(50),
	nome_munic varchar(100)
);

create table dimensao_drs (
	id integer primary key identity(1,1),
	nome_drs varchar(100),
	id_municipio integer,
	FOREIGN KEY (id_municipio) REFERENCES dimensao_municipio (id)
);

create table dimensao_raca_cor (
	id integer primary key identity(1,1),
	raca_cor varchar(20)
);

create table dimensao_sexo (
	id integer primary key identity(1,1),
	sexo varchar(20)
);

create table dimensao_paciente (
	id integer primary key identity(1,1),
	idade integer,
	id_sexo integer,
	id_raca_cor integer,
	id_drs integer,
	FOREIGN KEY (id_sexo) REFERENCES dimensao_sexo (id),
	FOREIGN KEY (id_raca_cor) REFERENCES dimensao_raca_cor (id),
	FOREIGN KEY (id_drs) REFERENCES dimensao_drs (id)
);

create table dimensao_condicao_saude (
	id integer primary key identity(1,1),
	tipo varchar(20)
);

create table dimensao_paciente_condicao_saude(
	id_paciente integer,
	id_condicao_saude integer,
	grau varchar(10),
	PRIMARY KEY (id_paciente, id_condicao_saude),
	FOREIGN KEY (id_paciente) REFERENCES dimensao_paciente (id),
	FOREIGN KEY (id_condicao_saude) REFERENCES dimensao_condicao_saude (id)
);

create table fato_casos (
	id integer primary key identity(1,1),
	id_paciente integer,

	FOREIGN KEY (id_paciente) REFERENCES dimensao_paciente (id)
);
