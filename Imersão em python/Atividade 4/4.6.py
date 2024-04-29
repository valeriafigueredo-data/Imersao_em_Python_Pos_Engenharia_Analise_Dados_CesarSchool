# 6) Faça um algoritmo que encontre qual o maior número par digitado pelo usuário.
# O usuário deve digitar 10 números e ao final o algoritmo deve imprimir o resultado.

maior_numero = 0
numero_digitado = 10

for i in range (numero_digitado):
    numero_atual = int(input(f"Digite um número, na posição {i+1}: "))
    if i == 0 and numero_atual % 2 == 0:
        maior_numero = numero_atual
    elif numero_atual > maior_numero and numero_atual % 2 ==0:
        maior_numero = numero_atual

print(f"Maior número par: {maior_numero}")
