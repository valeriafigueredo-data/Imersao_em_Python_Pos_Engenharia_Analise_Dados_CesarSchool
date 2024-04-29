# 4) Um petshop atende 10 cachorros por tarde.
# Faça um programa que solicite ao usuário o código do serviço efetuado: (1 - banho; 2 - tosa; 3 - banho e tosa; 4- outros).
# Por fim, exiba a quantidade de solicitações para cada um deles.

banho = 0
tosa = 0
banho_tosa = 0
outros = 0
quantidade = 0

while quantidade < 10:
    atendimento =int(input("Digite o código do serviço efetuado - 1 - banho; 2 - tosa; 3 - banho e tosa; 4- outros: "))
    if atendimento == 1:
       banho += 1
    elif atendimento == 2:
        tosa += 1
    elif atendimento == 3:
        banho_tosa += 1
    elif atendimento == 4:
        outros += 1

    quantidade += 1


print(f"Banho: {banho}")
print(f"Tosa: {tosa}")
print(f"Banho e tosa: {banho_tosa}")
print(f"Outros: {tosa}")

