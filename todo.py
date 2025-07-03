'''
Adicionar tarefa: você escreve o que precisa ser feito. Exemplo: "Estudar inglês".

Listar tarefas: todas aparecem na lista, geralmente com uma checkbox (caixinha) ao lado.

Marcar como feita: quando terminar, marca a caixinha ou clica em “concluído”.

Remover tarefa (opcional): a tarefa pode ser apagada ou arquivada.

Editar ou reordenar tarefas (opcional): você pode mudar o texto ou a ordem de prioridade.
'''

# criando lista
lista_tarefas = []
# fazendo loop while para não sair do programa assim que escolher alguma opção
while True:
    # pedindo para o usuário que escolha alguma das opções
    escolha = int(input("Opções: 1 - Mostrar lista, 2 - Adicionar tarefa., 5 - Sair da To-Do List. O que deseja da sua To-Do List? "))
    # início do if
    if escolha == 1:
        # verificando se lista está vazia
        if lista_tarefas == []: 
            print("Lista de tarefas vazia")
        else:
            for tarefa in lista_tarefas:
                print("Tarefas:")
                print("Tarefas feitas: [x]. Tarefas não feitas: []")
                # mostrando cada tarefa
                print(f"[] - {tarefa}")
    elif escolha == 2:
        # perguntando qual tarefa deseja incluir
        nova_tarefa = input("Qual tarefa deseja colocar na lista? ") 
        # adicionando tarefa a lista de tarefas
        lista_tarefas.append(nova_tarefa) 
        print("Tarefa incluída com sucesso")
    elif escolha == 5:
        print("Volte sempre! :)")
        break