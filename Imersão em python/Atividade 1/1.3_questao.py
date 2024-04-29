# Dados os lados a, b, e c de um triângulo, calcule sua área.
# Utilize a fórmula de Heron: Área = s (s − a) (s − b) (s − c), onde s é o semiperímetro do triângulo, dado por s = a +b+c/2

a = int(input("Digite um valor: "))
b = int(input("Digite um valor: "))
c = int(input("Digite um valor: "))
s = (a + b + c)/2
ar = s * (s - a) * (s - b) * (s - c)
rq = ar ** 0.5

print(f"Área do triângulo: {rq}.")