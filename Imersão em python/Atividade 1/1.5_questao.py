# Escreva um programa que leia o valor total das vendas de um vendedor e a porcentagem de comissão que ele recebe.
# Calcule e mostre o valor da comissão.

v = float(input("Determine o valor das vendas: "))
c = float(input("Determine a porcentagem da comissão: "))
pc = c * 0.01
co = float(v * pc)
print(f"Valor da comissão: R$ {co}")
