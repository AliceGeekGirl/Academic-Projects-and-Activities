CREATE TABLE alunos (
  id_aluno INT,
  cpf INT UNIQUE,
  matricula INT UNIQUE,
  nome VARCHAR(50) NOT NULL,
  telefone INT,
  curso VARCHAR NOT NULL,
  email VARCHAR UNIQUE,
  PRIMARY KEY (id_aluno)
);
  
CREATE TABLE livro (
  codigo SERIAL,
  titulo VARCHAR NOT NULL,
  editora VARCHAR NOT NULL,
  nr_paginas INT NOT NULL,
  isbn VARCHAR UNIQUE,
  ano_publicacao INT NOT NULL, -- Corrigido de ano_publicao para ano_publicacao
  qtde_disponivel INT NOT NULL,
  PRIMARY KEY (codigo)
);
  
CREATE TABLE autor (
  id_autor INT,
  nome VARCHAR(50) NOT NULL,
  pais VARCHAR,
  PRIMARY KEY (id_autor)
);

CREATE TABLE livro_autor (
  codigo_livro INT,
  id_autor INT,
  PRIMARY KEY (codigo_livro, id_autor),
  FOREIGN KEY (codigo_livro) REFERENCES livro(codigo),
  FOREIGN KEY (id_autor) REFERENCES autor(id_autor)
);
  
CREATE TABLE emprestimo (
  id_emprestimo INT,
  data_emprestimo DATE NOT NULL,
  data_devolucao_prevista DATE,
  data_devolucao_real DATE,
  -- DECLARAÇÃO DAS COLUNAS QUE FALTAVAM AQUI:
  id_aluno INT,
  codigo_livro INT,
  PRIMARY KEY (id_emprestimo),
  -- Agora as Foreign Keys funcionam porque as colunas existem acima:
  FOREIGN KEY (id_aluno) REFERENCES alunos(id_aluno),
  FOREIGN KEY (codigo_livro) REFERENCES livro(codigo)
);






