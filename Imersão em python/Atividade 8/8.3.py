# 3) Crie um programa que represente uma agenda de contatos.
# O programa deve oferecer as seguintes opções ao usuário:
# 1. Incluir contato: Permite ao usuário adicionar um nome e um número de telefone à agenda.
# 2. Excluir contato: Permite ao usuário remover um contato da agenda usando o nome como referência.
# 3. Buscar contato: Permite ao usuário buscar um contato na agenda pelo nome e exibir o número de telefone correspondente.
# 4. Finalizar programa.
# Crie três funções para realizar cada uma das opções acima: incluir_contato, excluir_contato e buscar_contato.
# ● incluir_contato recebe como parâmetro o nome e o telefone
# ● excluir_contato e buscar_contato recebe como parâmetro o nome
# No programa principal, um dicionário deve ser inicializado e o menu com as 4 opções deve ser exibido.
# Ao selecionar uma delas o usuário deve fornecer os parâmetros via input e a função equivalente à opção escolhida deve ser chamada.
# Ao finalizar o programa todo o dicionário deve ser exibido.

agenda = {}

def incluir_contato (nome, telefone):
    agenda[nome] = telefone
    print("Contato adicionado com sucesso!")
# def incluir_contato (agenda: dict, nome: str, telefone: int):
#     agenda[nome] = telefone
#     return agenda

def excluir_contato(nome):
    if nome in agenda:
        del agenda [nome]
        print("Contato excluido com sucesso!")
    else:
        print("Contato não encontrado na agenda.")
#ou:
# def excluir_contato(agenda: dict, nome: str):
#     agenda.pop(nome,)
#     return(agenda)
def buscar_contato(nome):
    agenda.get(nome, "contato não encontrado na agenda.")
    if nome in agenda:
        print(f"Número de telefone de {nome}: {agenda[nome]}")
    else:
        print("Contato não encontrado na agenda.")
#  ou:
# def buscar_contato (nome):
#     retorno = agenda.get(nome, "Contato não encontrado na agenda.")
#     return retorno

# def buscar_contato (agenda: dict, nome: str):
#     contato = agenda.get(nome, "")
#     if contato == ""
#         return "contato não encontrado"
#     else:
#         return contato

opcao = 0

while opcao != 4:
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        nome_contato =input("Digite um nome para ser adicionado: ")
        telefone_contato =input("Digite o telefone do contato: ")
        incluir_contato(nome_contato, telefone_contato)
        # agenda = incluir_contato(agenda, nome_contato, numero_contato)
    elif opcao == 2:
        nome_contato = input("Digite um nome para ser excluido: ")
        excluir_contato(nome_contato)
    elif opcao == 3:
        nome_contato = input("Digite o nome do contato: ")
        buscar_contato(nome_contato)

print(agenda)
print("programa finalizado.")
# print(f"agenda: {agenda}\nPrograma Finalizado.")


