# 8) Uma loja deseja oferecer um bônus de natal para seus clientes.
# O algoritmo deverá perguntar quantos clientes há na loja, e para cada um deles ler o nome e o valor total das compras no ano.
# Se o valor for igual ou maior que R$2.000,00, calcular um bônus de 15% e exibir “Cliente apto para receber o bônus”.
# Informar ao final quantos clientes ganharam o bônus e o total em reais.

VALOR_BONUS = 2000.00
v= 0
bonus = 0
soma =0

quantidade_clientes = int(input("Quantos clientes há na loja: "))
for i in range(quantidade_clientes):
    nome = input("Informe o seu nome:" )
    valor_total = float(input("Determine o valor total das compras: "))
    if valor_total >= VALOR_BONUS:
            print("Cliente apto para receber o bônus")
            v += 1
            soma += valor_total
            bonus = soma * 0.15
print(f"Clientes: {v}")
print (f"Total: R$ {bonus}")
