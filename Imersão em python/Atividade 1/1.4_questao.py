# Peça ao usuário para inserir um valor inicial, a taxa de juro e o tempo. Calcule e
# mostre o valor futuro após o período especificado com juros simples.

v = float(input("Diga o valor inicial: "))
j = float(input("Diga a taxa de juros: "))
ju = j * 0.01
t = float(input("Diga o tempo: "))

vf = float(v + (v * ju * t))
print(f"valor futuro: {vf}")
