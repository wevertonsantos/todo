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
    escolha = int(input("Opções: 1 - Mostrar lista, 2 - Adicionar tarefa, 3 - Marcar como feita, 4 - Remover tarefa, 5 - Sair da To-Do List. O que deseja da sua To-Do List? "))
    # início do if
    if escolha == 1:
        # verificando se lista está vazia
        if lista_tarefas == []: 
            print("Lista de tarefas vazia")
        else:
            print("Tarefas:")
            for tarefa in lista_tarefas:
                # mostrando cada tarefa
                print(f"{lista_tarefas.index(tarefa) + 1} - {tarefa}")
    elif escolha == 2:
        # perguntando qual tarefa deseja incluir
        nova_tarefa = input("Qual tarefa deseja colocar na lista? ") 
        # adicionando tarefa a lista de tarefas
        lista_tarefas.append(nova_tarefa) 
        print("Tarefa incluída com sucesso")
    elif escolha == 3:
        # perguntando qual tarefa deseja marcar como feita
        tarefa_feita = input("Qual tarefa deseja marcar como feita? ")
        # verificando se tarefa está na lista
        if tarefa_feita in lista_tarefas:
            # atribuindo concluído na tarefa feita
            lista_tarefas[lista_tarefas.index(tarefa_feita)] = f"[x] - {tarefa_feita} - concluído"
            print("Tarefa marcada como concluída")
    elif escolha == 4:
        # perguntando qual tarefa deseja excluir
        tarefa_para_excluir = input("Digite a tarefa que deseja excluir: ")
        # verificando se tarefa está na lista
        if tarefa_para_excluir in lista_tarefas:
            # removendo da lista a tarefa escolhida
            lista_tarefas.remove(tarefa_para_excluir)
            print("Tarefa removida com sucesso")
        else:
            print("Está tarefa não existe na lista")
    elif escolha == 5:
        print("Volte sempre! :)")
        break