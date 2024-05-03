# 7) Crie um programa que represente uma agenda de contatos.
# O programa deve oferecer as seguintes opções ao usuário:
# 1. Incluir contato: Permite ao usuário adicionar um nome e um número de telefone à agenda.
# 2. Excluir contato: Permite ao usuário remover um contato da agenda usando o nome como referência.
# 3. Buscar contato: Permite ao usuário buscar um contato na agenda pelo nome e exibir o número de telefone correspondente.
# 4. Sair. Exibe todo o dicionário e a mensagem “Programa finalizado.”.
# Use um dicionário onde as chaves são os nomes dos contatos e os valores são os números de telefone.

agenda = {}
escolha= ''

while escolha != "sair":
    opçao = int(input(f"Digite uma opção (1-incluir contato, 2-Excluir contato, 3-Buscar contato, 4-Sair: "))

# 1. Incluir contato:
    if opçao == 1:
        contato = input("informe o nome do contato que será adicionado: ")
        numero = input("informe o número: ")
        agenda[contato] = numero
        print("Contato adicionado com sucesso!")

    elif opçao ==2:
        contato = input("informe o nome do contato que será deletado: ")
        if contato in agenda:
            del agenda[contato]
            print("Contato excluído com sucesso!")
        else:
           print("Contato não encontrado na agenda.")

    elif opçao ==3:
        contato = input("Informe o nome do contato que será procurado: ")
        agenda.get(f"{contato}, Contato não encontrado na agenda.")
        print(f"Número de telefone de {contato}: {numero}")

    elif opçao ==4:

        agenda[contato]:numero
        print(f"Agenda:{agenda}")
        print("Programa finalizado.")
        break

