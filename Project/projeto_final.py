# PROJETO ESTOQUE DO COMÉRCIO FIG BEBIDAS

# Dicionário para armazenar os produtos
mercadoria = {}

# Funções intermas de inclusão, atualização, exclusão, consulta e listagem de mercadorias (Procedimento realizado pela equipe interna: estoque)

# Função para incluir um produto novo
def incluir_mercadoria():
    nome = input("Digite o nome da mercadoria: ")
    setor = input("Digite o setor da mercadoria: ")
    quantidade = int(input("Digite a quantidade: "))
    if quantidade < 0:
        print("quantidade não permitida")
        quantidade = int(input("Digite a quantidade: "))
    else:
        quantidade = quantidade
    preco = float(input("Digite o preço da mercadoria: R$"))
    total = quantidade * preco
    total2 = input(total)

    # Inclusão da mercadoria no dicionário
    mercadoria[nome] = {"setor": setor, "quantidade": quantidade, "preço": preco, "total": total}
    print(f"{nome} foi incluído com sucesso!")

# Função para editar uma mercadoria existente
def atualizar_mercadoria():
    nome = input("Digite o nome da mercadoria: ")
    if nome in mercadoria:
        setor = input("Atual setor: ")
        quantidade = int(input("Atual quantidade: "))
        preco = float(input("Digite o atual preço da mercadoria: R$ "))


        # Atualização da mercadoria no dicionário
        mercadoria[nome] = {"setor": setor, "quantidade": quantidade, "preço": preco}
        print(f"{nome} editado com sucesso!!")
    else:
        print("Mercadoria não encontrada")


# Função para excluir uma mercadoria do dicionário
def excluir_mercadoria():
    nome = input("Digite o nome da mercadoria: ")
    if nome in mercadoria:
        del mercadoria[nome]
        print(f"{nome} deletado com sucesso!!")
    else:
        print("Mercadoria não encontrada")

# Função para buscar uma mercadoria do dicionário
def consultar_mercadoria():
    nome = input("Digite o nome da mercadoria: ")
    if nome in mercadoria:
        mercadoria[nome]
        print(f"{nome} foi registrado(a) anteriormente")
    else:
        print("Mercadoria não encontrada")

# Função para listar todos os itens
def lista_mercadoria():
    print(f"Os itens listados são {mercadoria}")

def exibir_menu():
    print(" *=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*==*=*=*=*= ")
    print("1. Incluir mercadoria no estoque")
    print("2. Atualizar mercadoria no estoque")
    print("3. Consultar mercadoriano estoque")
    print("4. Listagem de itens no estoque")
    print("5. Finalizar")
    print(" *=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*==*=*=*=*= ")

# Boas vindas ao usuário
print("            BEM VINDO AO COMÉRCIO FIGUEREDO BEBIDAS               ")

# Programa Principal

while True:
    exibir_menu()
    opcao = input("Selecione uma opção: ")
    if opcao == '5':
        print("Programa finalizado ...")
        break
    elif opcao == '1':
        incluir_mercadoria()
    elif opcao == '2':
        atualizar_mercadoria()
    elif opcao == '3':
        consultar_mercadoria()
    elif opcao == '4':
        lista_mercadoria()
    else:
        print("Opção inválida")

