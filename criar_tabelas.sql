--Criação da tabela Membro

CREATE TABLE Membro (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Email TEXT NOT NULL,
    DataNascimento DATE NOT NULL,
    DataCadastro DATE NOT NULL
);

--Criação da tabela Tarefa 

CREATE TABLE Tarefa (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Descricao TEXT NOT NULL,
    DataCriacao DATE NOT NULL,
    DataVencimento DATE NOT NULL,
    PontuacaoTotal INTEGER NOT NULL
);

-- Criação da tabela Atribuicao

CREATE TABLE Atribuicao (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_Membro INTEGER NOT NULL,
    ID_Tarefa INTEGER NOT NULL,
    DataAtribuicao DATE NOT NULL,
    DataConclusao DATE,
    Pontuacao INTEGER NOT NULL,
    FOREIGN KEY (ID_Membro) REFERENCES Membro(ID),
    FOREIGN KEY (ID_Tarefa) REFERENCES Tarefa(ID)
);
