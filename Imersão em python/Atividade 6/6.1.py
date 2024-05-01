# 1) Faça um programa que receba um e-mail e verifique se ele é válido.
# Obs: Para um e-mail ser válido considerar se possui “@”.

email = ""

email = input("Digite o nome do e-mail: ")
if "@" in email:
    print("E-mail válido.")
else:
    print("E-mail inválido.")

# string.find(‘o que quer encontrar’)