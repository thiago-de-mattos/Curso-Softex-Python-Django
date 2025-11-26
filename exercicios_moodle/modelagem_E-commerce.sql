use commerce;

CREATE TABLE if not exists clientes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(150) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE if not exists produtos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(200) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    estoque INT NOT NULL
);

CREATE TABLE if not exists pedidos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    data_compra DATETIME DEFAULT NOW(),
    total DECIMAL(10,2) NOT NULL,
    id_cliente INT NOT NULL,
    CONSTRAINT fk_pedidos_clientes
	FOREIGN KEY (id_cliente) REFERENCES clientes(id)
);

CREATE TABLE if not exists itens_pedido(
	id  INT PRIMARY KEY AUTO_INCREMENT,
    id_pedido INT NOT NULL,
    id_produto INT NOT NULL,
    CONSTRAINT	foreign key (id_pedido) REFERENCES pedidos(id),
	CONSTRAINT fk_itens_pedidos_produto
		FOREIGN KEY (id_produto) REFERENCES produtos(id)
);

INSERT INTO clientes (nome, email)
VALUES 
('João', 'joao@email.com'),
('Maria', 'maria@email.com'),
('Ana', 'ana@email.com');

INSERT INTO produtos (nome, preco, estoque)
VALUES
('Teclado', 200.00, 50),
('Mouse', 100.00, 100),
('Monitor', 850.00, 20);

INSERT INTO pedidos (total, id_cliente)
VALUES (400.00, 2);

INSERT INTO itens_pedido (id_pedido, id_produto)
VALUES
(1, 1),  
(1, 2),  
(1, 2);  

SELECT nome, preco
FROM produtos
WHERE preco > 100;

SELECT c.nome AS nome_cliente, 
	   P.id AS "id do pedido",
       p.data_compra AS "data de compra"
FROM pedidos p
JOIN clientes c ON p.id_cliente = c.id
WHERE c.nome = 'Maria';

UPDATE produtos
SET preco = preco * 1.10
WHERE nome = 'Mouse';

UPDATE produtos
SET estoque = estoque - 2
WHERE nome = 'Mouse';

delete FROM clientes
WHERE nome ="Joâo";

DELETE FROM itens_pedido
WHERE id_pedido = 1
  AND id_produto = 1 LIMIT 1;


