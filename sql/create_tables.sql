CREATE DATABASE DBAUTOCAR;
USE DBAUTOCAR;

select * from carros;

CREATE TABLE DBAUTOCAR.LOCACAO(
  ID INT AUTO_INCREMENT NOT NULL,
  ID_CARRO INT NOT NULL,
  ID_CLIENTE INT NOT NULL,
  DATA_LOCACAO DATE NOT NULL,
  DATA_RETORNO DATE NOT NULL,
  VALOR_DIARIA VARCHAR(10) NOT NULL,
  CONSTRAINT LOCACAO_PK PRIMARY KEY (ID)
);

CREATE TABLE DBAUTOCAR.CLIENTES(
  ID INT AUTO_INCREMENT NOT NULL,
  NOME VARCHAR(55) NOT NULL,
  NUMERO_CNH VARCHAR(11) NOT NULL,
  NUMERO_CARTAO_CREDITO VARCHAR(20) NOT NULL,
  TELEFONE VARCHAR(25) NOT NULL,
  EMAIL VARCHAR(100) NOT NULL,
  CONSTRAINT CLIENTES_PK PRIMARY KEY (ID)
);

CREATE TABLE DBAUTOCAR.CARROS(
  ID INT AUTO_INCREMENT NOT NULL,
  MODELO VARCHAR(20) NOT NULL,
  ANO NUMERIC NOT NULL,
  MARCA VARCHAR(20) NOT NULL,
  DISPONIBILIDADE BOOLEAN DEFAULT TRUE NOT NULL,
  CONSTRAINT CARROS_PK PRIMARY KEY (ID)
);

ALTER TABLE DBAUTOCAR.LOCACAO
ADD CONSTRAINT ID_CLIENTE_FK
    FOREIGN KEY (ID_CLIENTE)
    REFERENCES DBAUTOCAR.CLIENTES (ID);
    
ALTER TABLE DBAUTOCAR.LOCACAO
ADD CONSTRAINT ID_CARRO_FK
    FOREIGN KEY (ID_CARRO)
    REFERENCES DBAUTOCAR.CARROS (ID);
    
SELECT * FROM CARROS;
