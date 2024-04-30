# Faça um programa que:
# ○ Peça duas notas de 5 estudantes.
# ○ Calcule e armazene numa lista a média de cada estudante.
# ○ Imprima a lista de médias;
# ○ Imprima o número de estudantes com média >= 7.0.

nota1 = 0
nota2 = 0
i = 0
i2 = 0
media2 = []

for i in range(5):
    nota1 = int(input("Digite a nota 1: "))
    nota2 = int(input("Digite a nota 2: "))
    media = (nota1 + nota2)/2
    media2.append(media)
    if media2 [i] >= 7:
        i2 += 1


print(f"Medias: {media2}")
print(f"Número de estudantes com média >= 7: {i2}")
