# Escreva um algoritmo que receba o código correspondente ao cargo de um funcionário de uma escola e seu salário atual. M
# Mostre o valor do novo salário, com aumento, conforme tabela.

cargo = int(input("Digite o Código do Cargo- 1 - Secretario, 2 - Tesoureiro, 3 - Professor, 4 - Coordenador, 5 - Diretor: "))
salario = float(input("Digite o salário atual: "))
salario1 = salario + (salario * 0.45)
salario2 = salario + (salario * 0.35)
salario3 = salario + (salario * 0.25)
salario4 = salario + (salario * 0.15)
salario5 = salario

if cargo == 1:
    print(f"Salário Atualizado: {salario1}")
if cargo == 2:
    print(f"Salário Atualizado: {salario2}")
if cargo == 3:
    print(f"Salário Atualizado: {salario3}")
if cargo == 4:
    print(f"Salário Atualizado: {salario4}")
if cargo == 5:
    print(f"Salário Atualizado: {salario5}")
