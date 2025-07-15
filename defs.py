import sqlite3

#Função que fica responsável por inserir os dados nas colunas correspondentes
def inserir_tarefa(titulo, descricao=""):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (titulo, descricao) VALUES(?, ?)", (titulo, descricao)
    )
    conn.commit()
    conn.close()
    print(f"Tarefa '{titulo}' criada com sucesso!")


#Criar Lógica de excluir
def excluir_tarefa(titulo):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    #Verifica se a tarefa existe
    cursor.execute("SELECT id FROM tasks WHERE titulo = ?", (titulo))
    if not cursor.fetchone():
        print(f"Tarefa '{titulo}' não encontrada ou não existe!")

    #Remove a tarefa
    cursor.execute(
        "DELETE FROM tasks WHERE titulo = ?",(titulo))
    conn.commit()
    conn.close()
    print(f"Tarefa '{titulo}' removida com sucesso!")