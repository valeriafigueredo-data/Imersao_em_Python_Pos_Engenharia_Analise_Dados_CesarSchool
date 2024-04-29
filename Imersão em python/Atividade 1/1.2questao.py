# 2. Peça ao usuário para inserir o valor original de um produto e a porcentagem de desconto.
# Calcule e mostre o valor do produto após o desconto.

valor = float(input("Digite um valor: "))
desconto = float(input ("Digite um valor para o desconto: "))
valor_final = float(valor - (valor * (desconto * 0.01)))

print (f"Valor com desconto: R$ {valor_final}.")
