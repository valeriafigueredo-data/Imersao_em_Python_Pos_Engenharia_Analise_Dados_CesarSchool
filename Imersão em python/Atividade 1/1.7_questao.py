# Escreva um programa que leia o custo de produção de um produto e seu preço de venda.
# Calcule e mostre o lucro bruto obtido na venda do produto.

cp = float(input("Determine o custo da produção: "))
pv = float(input("Determine o preço de venda: "))
lb = pv - cp
print(f"Lucro Bruto: R$ {lb}")