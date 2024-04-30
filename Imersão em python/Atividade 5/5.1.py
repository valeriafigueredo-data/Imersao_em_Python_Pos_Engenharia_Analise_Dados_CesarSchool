# Faça um programa que leia um número indeterminado de valores, correspondentes a idades, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
# Após esta entrada de dados, faça:

# ○ Mostre a quantidade de idades válidas;
# ○ Exiba as idades armazenadas;
# ○ Calcule e mostre a média das idades;
# ○ Calcule e mostre a quantidade de idades acima da média calculada;
# ○ Exiba a maior e menor idade;
# ○ Calcule e mostre a quantidade de valores abaixo de 18.


idades = []
idades2 = []
DEZOITO = 18
i = 0
i2 = 0
i3 = 0

while idades != -1:
    idades.append(int(input("Digite uma idade ou -1 para finalizar: ")))
    if idades [i] == -1:
        break
    else:
        i += 1
        media = sum(idades)/len(idades)

idades2 = idades
idades2.remove(-1)
for idade in idades2:
    if idade > media:
        i2 += 1
    if idade < DEZOITO:
        i3 += 1

print(f"Quantidade de idades válidas: {i}")
print(f"Idades armazenadas: {idades2}")
print(f"Média das idades: {media}")
print(f"Quant. de idades acima da média: {i2}")
print(f"Maior idade:", max(idades))
print(f"Menor idade:", min(idades))
print(f"Quant. de idades abaixo de 18: {i3} ")
