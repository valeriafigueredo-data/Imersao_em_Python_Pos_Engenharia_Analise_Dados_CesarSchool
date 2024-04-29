# Peça ao usuário para inserir o valor total de uma compra e o número de parcelas desejadas.
# Calcule e mostre o valor de cada parcela, considerando que não há juros.

vc = int(input("Determine o valor total da compra: "))
np = int(input("Determine o número de parcelas: "))
vp = (vc/np)
print(f"Valor de cada parcela R$ {vp}.")