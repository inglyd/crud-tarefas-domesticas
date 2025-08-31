from conexao import conectar 
conn = conectar()
cursor = conn.cursor()

# Criar tabelas (se não existirem)
cursor.executescript("""
CREATE TABLE IF NOT EXISTS Membro (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Email TEXT NOT NULL,
    DataNascimento DATE NOT NULL,
    DataCadastro DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS Tarefa (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Descricao TEXT NOT NULL,
    DataCriacao DATE NOT NULL,
    DataVencimento DATE NOT NULL,
    Status TEXT NOT NULL,
    PontuacaoTotal INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS Atribuicao (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_Membro INTEGER NOT NULL,
    ID_Tarefa INTEGER NOT NULL,
    DataAtribuicao DATE NOT NULL,
    DataConclusao DATE,
    Pontuacao INTEGER NOT NULL,
    FOREIGN KEY (ID_Membro) REFERENCES Membro(ID),
    FOREIGN KEY (ID_Tarefa) REFERENCES Tarefa(ID)
);
""")

conn.commit()
# Fechar a conexão ao terminar
def fechar_conexao():
    conn.close() 

# Funções de CRUD
# Create Membro
def inserir_membro(nome,email,data_nascimento,data_cadastro):
    cursor.execute("INSERT INTO Membro (Nome, Email, DataNascimento, DataCadastro) VALUES (?, ?, ?, ?)", (nome, email, data_nascimento, data_cadastro))
    conn.commit()
#Create Tarefa
def inserir_tabela(descricao, data_criacao, data_vencimento, status, pontuacao_total):
    cursor.execute("INSERT INTO Tarefa (Descricao, DataCriacao, DataVencimento, Status, PontuacaoTotal) VALUES (?, ?, ?, ?, ?)", (descricao, data_criacao, data_vencimento, status, pontuacao_total))
    conn.commit()
 # Create Atribuição
def inserir_atribuicao(id_membro, id_tarefa, data_atribuicao, pontuacao, data_conclusao=None):
    cursor.execute("INSERT INTO Atribuicao (ID_Membro, ID_Tarefa, DataAtribuicao, DataConclusao, Pontuacao) VALUES (?, ?, ?, ?, ?)", (id_membro, id_tarefa, data_atribuicao, data_conclusao, pontuacao))
    conn.commit()   

 # Read
def listar_membros():
    cursor.execute("SELECT * FROM Membro")
    # fetchall() para retornar todas as linhas resultantes.
    return cursor.fetchall()

def listar_tarefas():
    cursor.execute("SELECT * FROM Tarefa")
    return cursor.fetchall()

def listar_atribuicoes():
    cursor.execute("SELECT * FROM Atribuicao")
    return cursor.fetchall()

# Update
def atualizar_membro(id_membro, nome, email, data_nascimento):
    cursor.execute("UPDATE Membro SET Nome = ?, Email = ?, DataNascimento = ? WHERE ID = ?", (nome, email, data_nascimento, id_membro))
    conn.commit()

def atualizar_tarefa(id_tarefa, descricao, data_vencimento, status):
    cursor.execute("UPDATE Tarefa SET Descricao = ?, DataVencimento = ?, Status = ? WHERE ID = ?", (descricao, data_vencimento, status, id_tarefa))
    conn.commit()

def atualizar_atribuicao(id_atribuicao, data_conclusao, pontuacao):
    cursor.execute("UPDATE Atribuicao SET DataConclusao = ?, Pontuacao = ? WHERE ID = ?", (data_conclusao, pontuacao, id_atribuicao))
    conn.commit()

    # Delete
def deletar_membro(id_membro):
    cursor.execute("DELETE FROM Membro WHERE ID = ?", (id_membro,))
    conn.commit()

def deletar_tarefa(id_tarefa):
    cursor.execute("DELETE FROM Tarefa WHERE ID = ?", (id_tarefa,))
    conn.commit()

def deletar_atribuicao(id_atribuicao):
    cursor.execute("DELETE FROM Atribuicao WHERE ID = ?", (id_atribuicao,))
    conn.commit()

    