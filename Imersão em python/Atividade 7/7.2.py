# 2) Crie um programa que leia as coordenadas x, y e z de dois pontos no espaço 3D, representados como tuplas.
# Calcule a distância entre esses dois pontos usando a fórmula da distância Euclidiana:

import math


x1 = float(input("digite uma coordenada: "))
y1 = float(input("digite uma coordenada: "))
z1 = float(input("digite uma coordenada: "))
x2 = float(input("digite uma coordenada: "))
y2 = float(input("digite uma coordenada: "))
z2 = float(input("digite uma coordenada: "))

# d = ((x2 * x2) - (x1 * x1)) + ((y2 * y2) - (y1 * y1)) + ((z2 * z2) - (z1 * z1))
# raiz_quadrada = math.sqrt(d)
d = ((x2 - x1) **2) + ((y2 - y1) **2) + ((z2 - z1)**2)
raiz_quadrada = math.sqrt(d)
raiz_quadrada2 = format(raiz_quadrada, ".2f")
print(f"A distância entre os dois pontos é: {raiz_quadrada2}")