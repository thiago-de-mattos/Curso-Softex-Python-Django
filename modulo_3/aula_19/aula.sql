-- Active: 1759755881379@@127.0.0.1@3306
create table alunos(
    id integer primary key,
    nome text not null,
    idade INTEGER
);

INSERT INTO alunos (nome, idade)
VALUES
('joâo', 20);

INSERT into alunos (nome, idade)
VALUES
('Maria', 31);

SELECT * FROM alunos;

UPDATE alunos 
SET idade = 21
WHERE nome = 'Maria';

DELETE FROM alunos
WHERE nome = 'joâo';

CREATE Table usuarios (
    id INTEGER PRIMARY KEY,
    primeiro_nome TEXT NOT NULL,
    sobrenome TEXT NOT NULL,
    email TEXT not NULL,
    senha TEXT NOT NULL
);

CREATE Table postagens (
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    postagem TEXT NOT NULL,
    id_autor INTEGER,
    Foreign Key (id_autor) REFERENCES usuarios(id)
);

INSERT into usuarios (primeiro_nome, sobrenome, email, senha)
VALUES
('Maria','Mattos', 'MariaMattos@gmail.com', '123dte@!');
INSERT into usuarios (primeiro_nome, sobrenome, email, senha)
VALUES
('Thiago','Mattos', 'ThiagoMattos@gmail.com', '3ehb28');

INSERT into usuarios (primeiro_nome, sobrenome, email, senha)
VALUES
('Geovana','Mattos', 'GeovanaMattos@gmail.com', '@nsgri4');

INSERT into usuarios (primeiro_nome, sobrenome, email, senha)
VALUES
('Ana','Cruz', 'AnaCruz@gmail.com', 'amsdhh$!');

INSERT into usuarios (primeiro_nome, sobrenome, email, senha)
VALUES
('Fernando','Souza', 'Fernando@gmail.com', '1J#Ydfagf');

SELECT * from usuarios;

INSERT INTO postagens(titulo, postagem, id_autor)
VALUES
('sei la', 'oi', 1);
INSERT INTO postagens(titulo, postagem, id_autor)
VALUES
('bonito', 'valeu', 2);

INSERT INTO postagens(titulo, postagem, id_autor)
VALUES
('sei la', 'tchau', 3);

INSERT INTO postagens(titulo, postagem, id_autor)
VALUES
('sei la', 'tudo bem', 4);

INSERT INTO postagens(titulo, postagem, id_autor)
VALUES
('sei la', 'oi', 5);

SELECT * FROM postagens;