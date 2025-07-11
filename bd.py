#Importa o SQLite
import sqlite3

#Função que cria o banco de dados e a tabela com suas colunas
def create_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   titulo TEXT NOT NULL,
                   descricao TEXT,
                   data_criacao TEXT DEFAULT CURRENT_TIMESTAMP,
                   status TEXT DEFAULT 'pendente'
                )
    ''')

