# Faça um algoritmo que leia a primeira letra do estado civil de uma pessoa e mostre uma mensagem com a sua descrição (Solteiro, Casado, Viúvo, Divorciado).
# Mostre uma mensagem de erro, se necessário.

estado_civil = input("Digite o seu estado civil- S - Solteiro , C - Casado, V - Viúvo, D - Divorciado: ")
if estado_civil == "S":
    print("Solteiro")
elif estado_civil == "C":
    print("Casado")
elif estado_civil =="V":
    print("Viúvo")
elif estado_civil == "D":
    print("Divorciado")
else:
    print("Entrada inválida")

