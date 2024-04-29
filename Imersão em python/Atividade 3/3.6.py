# Uma rede de cinemas deseja criar um sistema para controlar a venda de ingressos. Eles
# Possuem três tipos de sessões: Matinê, Vespertina e Noturna.
# Cada sessão tem um preço diferente. As regras são:
# 1. Sessão Matinê: Custa R$ 20.
# 2. Sessão Vespertina: Custa R$ 25.
# 3. Sessão Noturna: Custa R$ 30.
# Crianças até 12 anos, estudantes e idosos (65+) têm direito a 50% de desconto em qualquer sessão.
# Escreva um programa que peça ao usuário para escolher o tipo de sessão e informar a idade.
# Caso o usuário não seja idoso ou criança, ele deverá informar se é estudante.
# O programa deve informar o valor total da compra.


PRECO_MATINE = 20.0
PRECO_VESPERTINO = 25.0
PRECO_NOTURNO = 30.0
IDADE_CRIANCA = 12
IDADE_IDOSO = 65
tipo = ""
matine_com_desconto = PRECO_MATINE * 0.5
vespertino_com_desconto = PRECO_VESPERTINO * 0.5
noturno_com_desconto = PRECO_NOTURNO * 0.5
idade = int(input("Determine a idade: "))

if IDADE_CRIANCA < idade and idade < IDADE_IDOSO:
    tipo = input("determine: estudante, não estudante: ")
sessao = input("Determine o tipo de sessão: matinê, vespertina, noturna: ")
if sessao == "matinê":
    if (IDADE_CRIANCA < idade and idade < IDADE_IDOSO) and tipo == "não estudante":
        print(f"Valor do ingresso: {PRECO_MATINE}")
    elif IDADE_CRIANCA >= idade or idade >= IDADE_IDOSO or tipo == "estudante":
        print(f"Valor do ingresso: {matine_com_desconto}")
elif sessao == "vespertina":
    if (IDADE_CRIANCA < idade and idade < IDADE_IDOSO) and tipo == "não estudante":
        print(f"Valor do ingresso: {PRECO_VESPERTINO}")
    elif IDADE_CRIANCA >= idade or idade >= IDADE_IDOSO or tipo == "estudante":
        print(f"Valor do ingresso: {vespertino_com_desconto}")
elif sessao == "noturna":
    if (IDADE_CRIANCA < idade and idade < IDADE_IDOSO) and tipo == "não estudante":
        print(f"Valor do ingresso: {PRECO_NOTURNO}")
    elif IDADE_CRIANCA >= idade or idade >= IDADE_IDOSO or tipo == "estudante":
        print(f"Valor do ingresso: {noturno_com_desconto}")
