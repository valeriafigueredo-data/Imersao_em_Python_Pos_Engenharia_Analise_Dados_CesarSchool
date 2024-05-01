# 6) Faça um programa que leia o nome e três notas de 3 estudantes.
# Os nomes e as médias devem ser armazenadas, cada um, em uma lista.
# Por fim, em outra estrutura de repetição, exiba o nome e a média, um a um,
# formatando o nome para ser exibido com a primeira letra maiúscula e o restante minúscula e a média para apenas duas casas decimais.
# Informe também se o estudante está aprovado ou reprovado.
# Obs: Para ser aprovado a média deve ser maior ou igual a 7.

nomes2 = []
media2 = []
situacao = ""
situacoes = []

for i in range(3):
    nome = input("Digite o seu nome: ")
    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    nota3 = float(input("Informe a terceira nota: "))
    media = (nota1 + nota2 + nota3)/3
    media2.append(media)
    nomes2.append(nome)
for media in media2:
    if media >= 7:
       situacao = "aprovado(a)"
    if media < 7:
        situacao = "reprovado(a)"
    situacoes.append(situacao)
for i in range(3):
    print(f"A média de {nomes2[i]} é {media2[i]:.2f} e ele(a) está {situacoes[i]}.")





