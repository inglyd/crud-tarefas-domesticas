import sqlite3
def conectar():
    conn = sqlite3.connect("tarefas_domesticas.db")
    return conn


