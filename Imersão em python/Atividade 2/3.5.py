# Um hotel de luxo deseja automatizar seu sistema de reservas.
# Eles possuem três tipos de suítes: Standard, Luxo e Presidencial.
# Cada tipo de suíte tem uma quantidade limitada de noites que pode ser reservada a um preço diferente.
# O hotel definiu as seguintes regras:
# 1. Suíte Standard: Custa R$ 250 por noite, limite de 15 noites.
# 2. Suíte Luxo: Custa R$ 500 por noite, limite de 10 noites.
# 3. Suíte Presidencial: Custa R$ 1200 por noite, limite de 7 noites.
# Além disso, se o cliente desejar ficar 5 noites ou mais, ele recebe um desconto de 10% no valor total, independentemente do tipo de suíte escolhida.
# Escreva um programa que peça ao usuário para escolher o tipo de suíte, a quantidade de noites e informe o valor total da estadia.
# Se a quantidade de noites informada for maior que o limite disponível, informe ao usuário e finalize o sistema.

LIMITE_STANDARD = 15
LIMITE_LUXO = 10
LIMITE_PRESIDENCIAL = 7
DIARIA_STANDARD = 250.0
DIARIA_LUXO = 500.0
DIARIA_PRESIDENTE = 1200.00

tipo_suite = input("Escolha o tipo de suíte - standard, luxo, presidencial: ")
quantidade_noites = int(input("Determine a quantidade de noites: "))

valor_standard = DIARIA_STANDARD * quantidade_noites
desconto_standard = valor_standard - (valor_standard * 0.1)

valor_luxo = DIARIA_LUXO * quantidade_noites
desconto_luxo = valor_luxo - (valor_luxo * 0.1)

valor_presidencial = DIARIA_PRESIDENTE * quantidade_noites
desconto_presidencial = valor_presidencial - (valor_presidencial * 0.1)

if tipo_suite == "standard" and quantidade_noites < 5 and quantidade_noites <= LIMITE_STANDARD:
    print(f"Valor total da estadia: R$ {valor_standard}.")
elif tipo_suite == "standard" and quantidade_noites <= LIMITE_STANDARD and quantidade_noites >= 5:
    print(f"Valor total da estadia: R$ {desconto_standard}.")
elif tipo_suite == "standard" and quantidade_noites > LIMITE_STANDARD:
    print(" Limite de noites atingido.")
elif tipo_suite == "luxo" and quantidade_noites < 5 and quantidade_noites <= LIMITE_LUXO:
    print(f"Valor total da estadia: R$ {valor_luxo}.")
elif tipo_suite == "luxo" and quantidade_noites <= LIMITE_LUXO and quantidade_noites >= 5:
    print(f"Valor total da estadia: R$ {desconto_luxo}.")
elif tipo_suite == "luxo" and quantidade_noites > LIMITE_LUXO:
    print(" Limite de noites atingido.")
elif tipo_suite == "presidencial" and quantidade_noites < 5 and quantidade_noites <= LIMITE_PRESIDENCIAL:
    print(f"Valor total da estadia: R$ {valor_presidencial}.")
elif tipo_suite == "presidencial" and quantidade_noites <= LIMITE_PRESIDENCIAL and quantidade_noites >= 5:
    print(f"Valor total da estadia: R$ {desconto_presidencial}.")
elif tipo_suite == "presidencial" and quantidade_noites > LIMITE_PRESIDENCIAL:
    print("Limite de noites atingido.")
