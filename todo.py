'''
Adicionar tarefa: você escreve o que precisa ser feito. Exemplo: "Estudar inglês".

Listar tarefas: todas aparecem na lista.

Marcar como feita: quando terminar é excluída

Remover tarefa (opcional): a tarefa pode ser apagada ou.

'''

def main():
    # criando lista
    lista_tarefas = []
    # fazendo loop while para não sair do programa assim que escolher alguma opção
    while True:
        try:
            # pedindo para o usuário que escolha alguma das opções
            escolha = int(input("Opções: 1 - Mostrar lista, 2 - Adicionar tarefa, 3 - Marcar como feita, 4 - Remover tarefa, 5 - Sair da To-Do List. O que deseja da sua To-Do List? "))
            # início do if
            if escolha == 1:
                mostrando_lista(lista_tarefas)
            elif escolha == 2:
                adicionando_tarefa(lista_tarefas)
            elif escolha == 3:
                marcando_feita(lista_tarefas)
            elif escolha == 4:
                excluindo_tarefa(lista_tarefas)
            elif escolha == 5:
                print("Volte sempre! :)")
                break
        except ValueError:
            print("Essa opção não é válida. Tente novamente!")

# função que mostra a lista de tarefas
def mostrando_lista(lista_tarefas):
    # verificando se lista está vazia
    if lista_tarefas == []: 
        print("Lista de tarefas vazia")
    else:
        print("Tarefas:")
        for tarefa in lista_tarefas:
            # mostrando cada tarefa
            print(f"{lista_tarefas.index(tarefa) + 1} - {tarefa}")

# função que adiciona tarefa
def adicionando_tarefa(lista_tarefas):
    # perguntando qual tarefa deseja incluir
    nova_tarefa = input("Qual tarefa deseja colocar na lista? ") 
    # adicionando tarefa a lista de tarefas
    lista_tarefas.append(nova_tarefa) 
    print("Tarefa incluída com sucesso")

# função que marca tarefa como feita
def marcando_feita(lista_tarefas):                
    # perguntando qual tarefa deseja marcar como feita
    tarefa_feita = input("Qual tarefa deseja marcar como feita? ")
    # verificando se tarefa está na lista
    if tarefa_feita in lista_tarefas:
    # atribuindo concluído na tarefa feita
        lista_tarefas.remove(tarefa_feita)
        print("Tarefa concluída")
    else:
        print("Está tarefa não existe na lista")

# função que exclui tarefa
def excluindo_tarefa(lista_tarefas):
    # perguntando qual tarefa deseja excluir
    tarefa_para_excluir = input("Digite a tarefa que deseja excluir: ")
    # verificando se tarefa está na lista
    if tarefa_para_excluir in lista_tarefas:
        # removendo da lista a tarefa escolhida
        lista_tarefas.remove(tarefa_para_excluir)
        print("Tarefa removida com sucesso")
    else:
        print("Está tarefa não existe na lista")

main()