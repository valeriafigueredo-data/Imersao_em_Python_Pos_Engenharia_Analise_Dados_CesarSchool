# Faça um programa que leia o nome, idade e altura de 5 pessoas.
# O sistema deverá apresentar o nome, idade e altura da pessoa mais alta.

maior_nome = ""
maior_altura = 0.0
maior_idade = 0

for i in range (5):
    nome_atual = input(f"Digite o nome da posição {i+1}: ")
    idade_atual = int(input(f"Digite a idade atual da posição {i+1}: "))
    altura_atual = float(input(f"Digite a altura atual da posição {i+1}: "))

    if i== 0:

        maior_altura = altura_atual
        maior_idade = idade_atual
        maior_nome = nome_atual

    elif altura_atual > maior_altura:
        maior_altura = altura_atual
        maior_nome = nome_atual
        maior_idade = idade_atual

print(f"{maior_nome}, com {maior_idade} anos e {maior_altura}m, é a pesoa mais alta do grupo.")
