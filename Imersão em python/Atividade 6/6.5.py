# 5) Faça um programa que leia um número de celular, e corrija o número no caso deste conter somente 8 dígitos, adicionando o '9' na frente.
# O usuário pode informar o número com ou sem o traço separador.

novo_num = ""
numero = input("Digite o número do celular: ")
legal_size = 10 if "-" in numero else 9

if len(numero) < legal_size:
    novo_numero = f'9{numero}'
    print(novo_numero)
elif len(numero)== legal_size:
    print(numero)
