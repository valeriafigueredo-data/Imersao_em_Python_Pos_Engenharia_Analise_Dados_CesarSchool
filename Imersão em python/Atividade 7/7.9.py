# 9) Crie um dicionário chamado contas para armazenar informações das contas bancárias.
# As chaves serão os números das contas (por exemplo, "001", "002") e os valores serão outros dicionários contendo as informações da conta: nome do
# titular e saldo.
# Implemente um menu com as seguintes opções:
# ● Digite 1 para criar uma nova conta. Solicite ao usuário o número da
# conta, nome do titular e saldo inicial.
# ● Digite 2 para consultar o saldo de uma conta específica. Solicite ao
# usuário o número da conta e exiba o saldo.
# ● Digite 3 para realizar um saque em uma conta. Solicite ao usuário o
# número da conta e o valor a ser sacado. Certifique-se de que a conta
# exista e que o saldo seja suficiente.
# ● Digite 4 para realizar um depósito em uma conta. Solicite ao usuário o
# número da conta e o valor a ser depositado.
# ● Digite 5 para sair do programa.
# Após cada operação, exiba uma mensagem apropriada informando o resultado da operação (por exemplo, "Conta criada com sucesso", "Saldo da conta: x.x", "Saque realizado com sucesso", "Depósito realizado com sucesso").
# Garanta que o programa seja executado em um loop até que o usuário escolha a opção 5 para sair.
# Certifique-se de que o programa lide adequadamente com casos em que o usuário consulta, saca ou deposita em uma conta que não existe.

conta = {}
escolha = ""

while escolha != 5:
    opcao = int(input(f"Digite uma opção (1-incluir produto, 2-Excluir produto, 3-Atualizar estoque, 4-Exibir, 5-Valor total do estoque, 6-Sair: "))

# 1. Incluir produto:
    if opcao == 1:
        numero = input("informe o número da conta: ")
        nome = input("informe o nome do titular: ")
        saldo= float(input("Informe o saldo inicial: "))
        conta[numero] = nome, saldo
        print(f"Conta criada com sucesso.")

# 2.consultar o saldo de uma conta específica. Solicite ao usuário o número da conta e exiba o saldo.
    elif opcao ==2:
        numero2 = input(f"Informe o número da conta: ")
        if numero2 in conta:
            print(f"Saldo da conta: {saldo}")
        else:
            print(f"Conta não encontrada.")
# ● 3 para realizar um saque em uma conta. Solicite ao usuário o número da conta e o valor a ser sacado. Certifique-se de que a conta exista e que o saldo seja suficiente.
    elif opcao == 3:
        numero3 = input(f"Informe o número da conta: ")
        saque = float(input("Informe o valor a ser sacado: "))
        if numero3 in conta and saque < saldo:
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente.")
        saldo = (saldo - saque)
# ● Digite 4 para realizar um depósito em uma conta. Solicite ao usuário o número da conta e o valor a ser depositado.
    elif opcao == 4:
        numero = input(f"Informe o número da conta: ")
        deposito = float(input("Informe o valor a depositado: "))
        print("Depósito realizado com sucesso.")
        saldo = saldo + deposito
# ● Digite 5 para sair do programa.
    elif opcao == 5:
        print("Programa finalizado.")
        break

