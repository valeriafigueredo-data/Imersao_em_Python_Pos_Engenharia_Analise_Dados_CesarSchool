# ○ Parte 01: Ler 10 números inteiros e armazená-los em uma lista única.
# ○ Parte 02: Em uma nova estrutura de repetição, armazene os números pares na lista PARES e os números ímpares na lista ÍMPARES.
# ○ Imprima as três listas.

num = []
num_pares = []
num_impar = []

for i in range(10):
    num.append(int(input("Digite números inteiros: ")))
for numero in num:
    if numero % 2 == 0:
        num_pares.append(numero)
    if numero % 2 != 0:
        num_impar.append(numero)

print(f"Números: {num}")
print(f"Pares: {num_pares}")
print(f"Ímpares: {num_impar}")