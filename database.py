import sqlite3

conexao = sqlite3.connect("produtos.db")

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    preco REAL,
    quantidade INTEGER
)
""")

conexao.commit()