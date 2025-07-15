import sqlite3
from defs import inserir_tarefa, excluir_tarefa
print("""
     _______________________________________________
    |                                              |                        
    | Seja bem vindo ao listador de Tarefas        |
    |                                              |
    | Neste listador você pode Criar um título     |
    | para a tarefa e uma descrição, e para as     |
    | tarefas já criada, pode-se alterar o status. |
    |                                              |
    | DEV: João Henrique                           |
    |______________________________________________|    
""")


question_1 = input("\nSe deseja adicionar, digite 'A', se deseja remover, digite 'R': ")

if question_1 == "a":
    title = input("Digite o título da tarefa: ")
    description = input("Digite a descrição da tarefa: ")

    if title == "" and description == "":
        print("O título e a descrição não podem ser vazios.")
    else:
        inserir_tarefa(title, description)

elif question_1 == "r":
    tarefa_remover = input("Digite o título da tarefa a remover: ")
    excluir_tarefa(tarefa_remover)


elif question_1 != "a" and "r":
    print("Digite uma das opções válidas")







#Criar lógica que verifica se existe ou tarefa no inicio ou não
