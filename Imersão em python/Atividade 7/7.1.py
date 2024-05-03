# 1) Crie um programa que contenha uma lista de tuplas, onde cada tupla contém o nome de uma cor e seus valores RGB (Red, Green, Blue), informadas pelo usuário.
# Para inserir os valores, o sistema deverá solicitar quantas cores ousuário deseja informar.
# Após a inserção, solicite ao usuário que digite o nome de uma cor e, se a cor estiver na lista, exiba seus valores RGB.
# Lista de Tupla = cores_rgb[(nome_da_cor, (r,g,b) ), (nome_da_cor, (r,g,b) )]


cores = []
cores_rgb = []

quantidade_cores = int(input("digite quantas cores deseja: "))
for i in range(quantidade_cores):
    cor = input("Digite uma cor: ")
    r = int(input("Informe o valor para vermelho: "))
    g = int(input("Informe o valor para verde: "))
    b = int(input("informe o valor para azul: "))
    cores_rgb.append((cor.lower(),(r,g,b)))

nome_cor = input("Digite o nome da cor: ")
for c in cores_rgb:
    if cor.lower() == c[0]:
        print(
            f'Valores RGB para a cor {c[0].title()}:Red ={c[1][0]}, Green ={c[1][1]}, Blue ={c[1][2]}',)
        break
else:
    print("Cor não encontrada.")

