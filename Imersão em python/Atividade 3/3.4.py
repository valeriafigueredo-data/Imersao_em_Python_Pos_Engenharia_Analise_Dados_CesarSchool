# Em uma cidade, a prefeitura deseja classificar os motoristas com base em suas infrações de trânsito no último ano.
# O objetivo é criar um programa de reeducação para os motoristas que cometem infrações.
# Para isso, eles definiram as seguintes categorias:
# a) Motorista Exemplar: Não cometeu nenhuma infração.
# b) Motorista Atento: Cometeu até 3 infrações.
# c) Motorista Desatento: Cometeu entre 4 e 6 infrações.
# d) Motorista Perigoso: Cometeu mais de 6 infrações.
# Escreva um programa que peça ao usuário para inserir o número de infrações que cometeu no último ano e informe em qual categoria ele se encaixa.

infracoes = int(input("Digite o número de infrações que cometeu no último ano: "))
if infracoes == 0:
    print("Categoria: Motorista Exemplar")
elif 0 < infracoes <= 3:
    print("Categoria: Motorista Atento")
elif 4 < infracoes <= 6:
    print("Categoria: Motorista Desatento")
elif 4 < infracoes <= 6:
    print("Categoria: Motorista Desatento")
elif infracoes >6:
    print("Categoria: Motorista Perigoso")
else:
    print("categoria inválida")