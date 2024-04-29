# 2) Uma loja online deseja criar um sistema de avaliação de produtos.
# O usuário deve inserir uma nota de 1 a 5 para um produto.
# Se uma nota inválida for digitada, o usuário deverá ser alertado.
# O programa deve calcular a média das notas.
# Continue coletando notas até que o usuário insira -1.

media = 0
soma = 0
i = 0
nota = 0

while nota != -1:
    nota = float(input("Digite uma nota para o produto: "))

    if nota == -1:
        break
    if 1 <= nota <= 5:
        i += 1
        soma = soma + nota
    else:
        print("Nota Inválida")
media = soma / i
print(f"Media das notas: {media}")
