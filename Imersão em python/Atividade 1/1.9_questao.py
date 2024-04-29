# Peça ao usuário para inserir o valor de um produto e a taxa de imposto aplicada sobre ele.
# Calcule e mostre o valor final do produto com o imposto.

vp = int(input("Determine o valor do produto: "))
ti = int(input("Determine a taxa de imposto: "))
i = ti * 0.01
vfi = vp + vp * i
print(f"Valor Final com Imposto: R$ {vfi}.")