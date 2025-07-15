
CREATE TABLE Pedidos (
    IdPedido INTEGER PRIMARY KEY,
    Status VARCHAR(30) NOT NULL,
    Delivery BOOLEAN,
    Endereco VARCHAR(100),
    Data DATE,
    ValorTotal REAL NOT NULL
);

CREATE TABLE Itens (
    IdItens INTEGER PRIMARY KEY,
    Nome VARCHAR(30),
    Preco REAL,
    Tipo VARCHAR(30),
    Descricao VARCHAR(255),
    CONSTRAINT Produto_Unico UNIQUE (Nome)
);

CREATE TABLE ItensPedidos (
    Id INTEGER PRIMARY KEY,
    IdPedido INTEGER NOT NULL,
    IdItem INTEGER NOT NULL,
    FOREIGN KEY (IdPedido) REFERENCES Pedidos(IdPedido),
    FOREIGN KEY (IdItem) REFERENCES Itens(IdItens)
);
