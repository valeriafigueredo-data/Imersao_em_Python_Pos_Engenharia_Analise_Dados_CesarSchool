# 3) Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário como String.
# Usando manipulação de Strings, altere a frase e exiba como no exemplo.

data_nascimento = ""
mes_atual = ""
meses = []

data_nascimento = input("informe a data de nascimento (dd/mm/aaaa): ")


dia,mes,ano = data_nascimento.split("/")
mes_extenso = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

print(f"Você nasceu em {dia} de {mes_extenso[int(mes)-1]} de {ano}.")

