'''
Adicionar tarefa: você escreve o que precisa ser feito. Exemplo: "Estudar inglês".

Listar tarefas: todas aparecem na lista, geralmente com uma checkbox (caixinha) ao lado.

Marcar como feita: quando terminar, marca a caixinha ou clica em “concluído”.

Remover tarefa (opcional): a tarefa pode ser apagada ou arquivada.

Editar ou reordenar tarefas (opcional): você pode mudar o texto ou a ordem de prioridade.
'''

# criando lista
lista_tarefas = []
# pedindo para o usuário que escolha alguma das opções
escolha = input("O que deseja fazer na sua To-Do List? Opções: 1 - Mostrar lista, 2 - Adicionar tarefa")

if escolha == 1:
    print(lista_tarefas) # mostrando a lista de tarefas
elif escolha == 2:
    nova_tarefa = input("Qual tarefa deseja colocar na lista?") # perguntando qual tarefa deseja incluir
    lista_tarefas.append(nova_tarefa) # adicionando tarefa a lista de tarefas