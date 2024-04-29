# 1) Faça um algoritmo que leia idades até o usuário digitar -1.
# O programa deve exibir o total de idades válidas digitadas, a média das idades, quantas são maiores ou igual a 25 e quantas são menores que 25.

idade = 0
i = 0
i2 = 0
soma = 0

while idade != -1:
    idade = int(input("Digite uma idade ou -1 para finalizar: "))

    if idade == -1:
        break
    if idade >= 25:
        i += 1
    else:
        i2 += 1
    soma += idade

    total_idades = i + i2
    media = soma/total_idades

print(f"Total de idades: {total_idades}")
print(f"Media das idades: {media}")
print(f"Maiores de 25 anos: {i}")
print(f"Menores de 25 anos: {i2} ")
