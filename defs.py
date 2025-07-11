import sqlite3

#Função que fica responsável por inserir os dados nas colunas correspondentes
def inserir_tarefa(titulo, descricao=""):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO database (titulo, descricao) VALUES(?, ?)", (titulo, descricao)
    )
    conn.commit()
    conn.close()