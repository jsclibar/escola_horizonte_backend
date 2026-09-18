-- =====================================================
-- CRIAÇÃO DO BANCO DE DADOS
-- =====================================================

CREATE DATABASE IF NOT EXISTS escola_horizonte;

USE escola_horizonte;


-- =====================================================
-- LIMPEZA DAS TABELAS
-- =====================================================
-- Primeiro remove a tabela filha e depois a tabela pai,
-- pois TELEFONE possui uma chave estrangeira para ALUNO.

DROP TABLE IF EXISTS TELEFONE;
DROP TABLE IF EXISTS ALUNO;


-- =====================================================
-- CRIAÇÃO DA TABELA ALUNO
-- =====================================================

CREATE TABLE ALUNO (
    idaluno INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    data_nascimento DATE NOT NULL,
    logradouro VARCHAR(100),
    numero VARCHAR(10),
    complemento VARCHAR(30),
    bairro VARCHAR(50),
    cidade VARCHAR(50),
    estado CHAR(2),
    sexo CHAR(1)
);


-- =====================================================
-- CRIAÇÃO DA TABELA TELEFONE
-- =====================================================
-- Relacionamento 1:N
-- Um aluno pode possuir vários telefones.

CREATE TABLE TELEFONE (
    idtelefone INT AUTO_INCREMENT PRIMARY KEY,
    fk_idaluno INT NOT NULL,
    numero VARCHAR(25) NOT NULL,
    tipo VARCHAR(15),

    CONSTRAINT fk_aluno_telefone
        FOREIGN KEY (fk_idaluno)
        REFERENCES ALUNO(idaluno)
        ON DELETE CASCADE
);


-- =====================================================
-- INSERÇÃO DOS ALUNOS
-- =====================================================

INSERT INTO ALUNO (
    nome,
    email,
    data_nascimento,
    logradouro,
    numero,
    complemento,
    bairro,
    cidade,
    estado,
    sexo
)
VALUES
('Maria da Silva', 'maria.silva@email.com', '2008-03-15', 'Rua das Flores', '123', NULL, 'Vila Rezende', 'Piracicaba', 'SP', 'F'),

('Andre Santos', 'andre.santos@email.com', '2007-05-10', 'Av. Independência', '850', 'AP 73', 'Cidade Alta', 'Piracicaba', 'SP', 'M'),

('Juliana Costa', 'juliana.costa@email.com', '2006-07-22', 'Rua São José', '45', NULL, 'Centro', 'Limeira', 'SP', 'F'),

('Lucas Oliveira', 'lucas.oliveira@email.com', '2005-02-18', 'Av. Brasil', '1020', NULL, 'Centro', 'Americana', 'SP', 'M'),

('Camila Costa', 'camila.costa@email.com', '2008-09-05', 'Rua XV de Novembro', '300', 'AP 53', 'São Dimas', 'Piracicaba', 'SP', 'F'),

('Fabio Ferreira', 'fabio.ferreira@email.com', '2004-11-30', 'Rua dos Ipês', '890', 'CASA 1', 'Campestre', 'Piracicaba', 'SP', 'M'),

('Fernanda Almeida', 'fernanda.almeida@email.com', '2007-01-12', 'Av. Rio Claro', '510', NULL, 'Vila Rezende', 'Piracicaba', 'SP', 'F'),

('Pedro Souza', 'pedro.souza@email.com', '2005-04-23', 'Rua do Rosário', '430', 'AP 21', 'Centro', 'Piracicaba', 'SP', 'M'),

('Beatriz Rodrigues', 'beatriz.rodrigues@email.com', '2006-06-11', 'Rua Santa Cruz', '720', NULL, 'Alto', 'Piracicaba', 'SP', 'F'),

('Matheus Ribeiro', 'matheus.ribeiro@email.com', '2003-04-19', 'Av. Armando Salles', '980', NULL, 'Centro', 'Piracicaba', 'SP', 'M'),

('Camila Barbosa', 'camila.barbosa@email.com', '2005-08-25', 'Rua Treze de Maio', '340', NULL, 'Paulista', 'Piracicaba', 'SP', 'F'),

('Bruno Carvalho', 'bruno.carvalho@email.com', '2002-10-13', 'Rua Moraes Barros', '1120', 'AP 21', 'Centro', 'Piracicaba', 'SP', 'M'),

('Larissa Gomes', 'larissa.gomes@email.com', '2007-09-07', 'Rua Santa Cruz', '560', NULL, 'Alto', 'Piracicaba', 'SP', 'F'),

('Gustavo Rocha', 'gustavo.rocha@email.com', '2003-01-28', 'Av. Limeira', '2200', NULL, 'Areião', 'Piracicaba', 'SP', 'M'),

('Isabela Fernandes', 'isabela.fernandes@email.com', '2005-03-14', 'Rua Benjamin Constant', '670', 'AP 45', 'Centro', 'Piracicaba', 'SP', 'F'),

('Felipe Moreira', 'felipe.moreira@email.com', '2001-12-20', 'Rua Luiz de Queiroz', '420', NULL, 'Centro', 'Piracicaba', 'SP', 'M'),

('Amanda Lopes', 'amanda.lopes@email.com', '2006-07-03', 'Rua Voluntários de Piracicaba', '890', NULL, 'Centro', 'Piracicaba', 'SP', 'F'),

('Joao Pedro Lima', 'joao.lima@email.com', '2004-05-16', 'Rua Dona Eugênia', '225', NULL, 'Jardim Europa', 'Piracicaba', 'SP', 'M'),

('Leticia Nunes', 'leticia.nunes@email.com', '2007-02-09', 'Rua Tiradentes', '1330', 'AP 72', 'Centro', 'Piracicaba', 'SP', 'F'),

('Diego Correia', 'diego.correia@email.com', '2000-11-25', 'Rua Boa Morte', '840', NULL, 'Centro', 'Piracicaba', 'SP', 'M');


-- =====================================================
-- INSERÇÃO DOS TELEFONES
-- =====================================================
-- Alguns alunos possuem 1 telefone.
-- Outros possuem 2 ou 3 telefones.
-- Isso demonstra o relacionamento 1:N.

INSERT INTO TELEFONE (
    fk_idaluno,
    numero,
    tipo
)
VALUES

-- Maria
(1, '(19) 99999-1001', 'Celular'),

-- Andre
(2, '(19) 99999-1002', 'Celular'),
(2, '(19) 3433-1002', 'Residencial'),

-- Juliana
(3, '(19) 99999-1003', 'Celular'),

-- Lucas
(4, '(19) 99999-1004', 'Celular'),
(4, '(19) 3402-1004', 'Comercial'),

-- Camila Costa
(5, '(19) 99999-1005', 'Celular'),
(5, '(19) 3434-1005', 'Residencial'),

-- Fabio
(6, '(19) 99999-1006', 'Celular'),

-- Fernanda
(7, '(19) 99999-1007', 'Celular'),
(7, '(19) 3435-1007', 'Residencial'),
(7, '(19) 3422-1007', 'Comercial'),

-- Pedro
(8, '(19) 99999-1008', 'Celular'),

-- Beatriz
(9, '(19) 99999-1009', 'Celular'),
(9, '(19) 3433-1009', 'Residencial'),

-- Matheus
(10, '(19) 99999-1010', 'Celular'),

-- Camila Barbosa
(11, '(19) 99999-1011', 'Celular'),
(11, '(19) 3403-1011', 'Comercial'),

-- Bruno
(12, '(19) 99999-1012', 'Celular'),

-- Larissa
(13, '(19) 99999-1013', 'Celular'),
(13, '(19) 3434-1013', 'Residencial'),

-- Gustavo
(14, '(19) 99999-1014', 'Celular'),

-- Isabela
(15, '(19) 99999-1015', 'Celular'),
(15, '(19) 3435-1015', 'Residencial'),

-- Felipe
(16, '(19) 99999-1016', 'Celular'),
(16, '(19) 3402-1016', 'Comercial'),

-- Amanda
(17, '(19) 99999-1017', 'Celular'),

-- Joao
(18, '(19) 99999-1018', 'Celular'),
(18, '(19) 3433-1018', 'Residencial'),

-- Leticia
(19, '(19) 99999-1019', 'Celular'),

-- Diego
(20, '(19) 99999-1020', 'Celular'),
(20, '(19) 3434-1020', 'Residencial'),
(20, '(19) 3402-1020', 'Comercial');


-- =====================================================
-- CONSULTAS BÁSICAS
-- =====================================================

-- Exibe todos os alunos.
SELECT * FROM ALUNO;


-- Exibe todos os telefones.
SELECT * FROM TELEFONE;


-- =====================================================
-- CONSULTA COM INNER JOIN
-- =====================================================
-- Exibe os alunos e seus respectivos telefones,
-- relacionando ALUNO e TELEFONE pela chave estrangeira.

SELECT
    ALUNO.nome,
    TELEFONE.numero,
    TELEFONE.tipo
FROM ALUNO
INNER JOIN TELEFONE
    ON ALUNO.idaluno = TELEFONE.fk_idaluno;