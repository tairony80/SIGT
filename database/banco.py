import sqlite3

BANCO = "database.db"


def conectar():
    conexao = sqlite3.connect(BANCO)
    return conexao
