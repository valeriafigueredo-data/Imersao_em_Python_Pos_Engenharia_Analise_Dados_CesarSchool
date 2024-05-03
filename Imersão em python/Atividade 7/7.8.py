# 8) Desenvolva um programa para o controle de estoque de uma loja.
# O programa deve permitir as seguintes operações:
# 1. Incluir produto: Permite ao usuário adicionar um produto ao estoque.
# O  usuário deve fornecer o nome do produto, a quantidade em estoque e o preço unitário.
# 2. Excluir produto: Permite ao usuário remover um produto do estoque usando o nome como referência.
# 3. Atualizar estoque: Permite ao usuário atualizar a quantidade em estoque de um produto já existente.
# 4. Exibir todo o estoque: Exibe a lista de todos os produtos no estoque, incluindo seus nomes, quantidades em estoque e preços unitários.
# 5. Calcular valor total do estoque: Calcula e exibe o valor total do estoque com base nos preços dos produtos.
# 6. Sair: Encerra o programa.
# Use um dicionário onde as chaves são os nomes dos produtos e os valores são listas contendo a quantidade em estoque e o preço unitário.

estoque = {}
escolha = ""
soma = 0
valor_total = 0

while escolha != "6":
    opçao = int(input(f"Digite uma opção (1-incluir produto, 2-Excluir produto, 3-Atualizar estoque, 4-Exibir, 5-Valor total do estoque, 6-Sair: "))

# 1. Incluir produto:
    if opçao == 1:
        produto = input("informe o nome do produto que será adicionado: ")
        quantidade = int(input("informe a quantidade em estoque: "))
        preco = float(input("Informe o preço unitário: "))
        estoque[produto] = [quantidade, preco]
        print(f"Produto {produto} adicionado ao estoque.")

# 2. Excluir produto:
    elif opçao ==2:
        produto = input("informe o nome do produto que será deletado: ")
        if produto in estoque:
            del estoque[produto] #excluido = estoque.pop(nome, None)
            print("Produto excluído com sucesso!")
        else:
           print("Produto não encontrado no estoque.")

#3. Atualizar produto:
    elif opçao ==3:
        produto = input("informe o nome do produto que será adicionado: ")
        quantidade = input("informe a quantidade em estoque: ")
        estoque[produto] = quantidade
        print(f"Estoque de {produto} atualizado para {quantidade} unidades.")

#4 Exibir:
    elif opçao == 4:
        print("Lista de Produtos em Estoque: ")
        for produto, dados in estoque.items():
            print(f"Nome: {produto}")
            print(f"Quantidade em estoque: {dados[0]} unidades")
            print(f"Preço Unitário: R$ {dados[1]}")

#5 Valor Total do estoque:
    elif opçao == 5:
        for dados in estoque.values():
            valor_total = sum([dados[0] * dados[1]])
            print(f"Valor total do estoque: R$ {valor_total:.2f}")

# Finalizar processo:
    elif opçao == 6:
        print("Programa finalizado.")
        break

    else:
        print("Opção Inválida")

#Match opcao:
#case 1 case 2...
