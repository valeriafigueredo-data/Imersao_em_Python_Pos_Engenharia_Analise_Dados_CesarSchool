# Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.). Exibir mensagem “Valor Inválido” caso um número inesperado for informado.

dia = int(input("Digite o código do dia da semana - 1 - domingo, 2 - segunda, 3 - terça, 4 - quarta, 5 - quinta, 6 - sexta, 7 - sábado: "))
if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda")
elif dia == 3:
    print("Terça-feira")
elif dia == 4:
     print("Quarta-feira")
elif dia == 5:
    print("Quinta-feira")
elif dia == 6:
    print("Sexta-feira")
elif dia == 7:
    print("sábado")
else:
    print("Valor inválido")

