#  Uma loja deseja avaliar o desempenho de seus vendedores.
#  Crie um programa que:
# ○ Solicite ao usuário o número total de vendedores da loja.
# ○ Para cada vendedor, peça ao usuário o nome do vendedor e o total de vendas realizadas no ano.
# ○ Determine o vendedor com o maior volume de vendas e o vendedor com o menor volume.
# ○ Exiba o nome de todos os vendedores e suas vendas totais, destacando o vendedor com as vendas mais altas e o vendedor com as vendas mais baixas.

nomes = []
vendas = []

quantidade_vendedor = int(input("Digite o número total de vendedores da loja: "))

for i in range(quantidade_vendedor):
    nomes.append(input(f"Digite o nome do vendedor {i+1}: "))
    vendas.append(int(input(f"Digite o total de vendas do {nomes[i]} realizadas no ano: ")))

maior_venda = max(vendas)
menor_venda = min(vendas)

for i in range(quantidade_vendedor):
    if vendas[i] == maior_venda:
        print(f'{nomes[i]}: {vendas[i]} - Maior Volume de Vendas!')
    elif vendas[i] == menor_venda:
        print(f'{nomes[i]}: {vendas[i]} - Menor Volume de Vendas!')
    else:
        print(f"{nomes[i]}: {vendas[i]}")

