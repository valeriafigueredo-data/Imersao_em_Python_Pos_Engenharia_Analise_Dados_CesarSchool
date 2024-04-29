# Uma operadora de telefonia móvel deseja oferecer planos personalizados para seus clientes.
# Eles oferecem três tipos de planos com diferentes franquias de minutos e internet:
# ● Plano Básico: 100 minutos e 5GB de internet por R$ 50.
# ● Plano Intermediário: 300 minutos e 10GB de internet por R$ 80.
# ● Plano Avançado: 500 minutos e 20GB de internet por R$ 120.
# Caso o cliente ultrapasse a franquia de minutos, será cobrado R$ 1 por minuto adicional.
# Se ultrapassar a franquia de internet, será cobrado R$ 10 por GB adicional.
# Escreva um programa que peça ao usuário para escolher um plano,
# informar quantos minutos e quantos GB ele utilizou no mês.
# O programa deve calcular e mostrar o valor total da fatura.

MINUTO_BASICO = 100
GB_BASICO = 5
PRECO_BASICO = 50.0
MINUTO_INTERMEDIARIO = 300
GB_INTERMEDIARIO = 10
PRECO_INTERMEDIARIO = 80.0
MINUTO_AVANÇADO = 500
GB_AVANÇADO = 20
PRECO_AVANÇADO = 120.0
VALOR_AD_MINUTO = 1.0
VALOR_AD_GB = 10.0

plano = input("Determine o plano - básico, intermediário, avançado: ")
minutos_usados = int(input("Determine quantos minutos foram utilizados: "))
GB_usados = int(input("Determine quantos GB foram utilizados: "))

ad_gbb = GB_usados - GB_BASICO
ad_gbi = GB_usados - GB_INTERMEDIARIO
ad_gba = GB_usados - GB_AVANÇADO

ad_minutob = minutos_usados - MINUTO_BASICO
ad_minutoi = minutos_usados - MINUTO_INTERMEDIARIO
ad_minutoa = minutos_usados - MINUTO_AVANÇADO

preco_reajuste_basico = PRECO_BASICO + (ad_gbb * VALOR_AD_GB) + (ad_minutob * VALOR_AD_MINUTO)
preco_reajuste_intermediario = PRECO_INTERMEDIARIO + (ad_gbi * VALOR_AD_GB) + (ad_minutoi * VALOR_AD_MINUTO)
preco_reajuste_avançado = PRECO_AVANÇADO + (ad_gba * VALOR_AD_GB) + (ad_minutoa * VALOR_AD_MINUTO)

if plano == "básico":
    if minutos_usados <= MINUTO_BASICO  and GB_usados <= GB_BASICO:
        print(f"Valor da fatura: R${PRECO_BASICO}")
    elif minutos_usados > MINUTO_BASICO  or GB_usados > GB_BASICO:
        print(f"Valor da fatura: R${preco_reajuste_basico}")
elif plano == "intermediário":
    if minutos_usados <= MINUTO_INTERMEDIARIO and GB_usados <= GB_INTERMEDIARIO:
        print(f"Valor da fatura: R${PRECO_INTERMEDIARIO}")
    elif minutos_usados > MINUTO_INTERMEDIARIO or GB_usados > GB_INTERMEDIARIO:
        print(f"Valor da fatura: R${preco_reajuste_intermediario}")
elif plano == "avançado":
    if minutos_usados <= MINUTO_AVANÇADO and GB_usados <= GB_AVANÇADO:
        print(f"Valor da fatura: R${PRECO_AVANÇADO}")
    elif minutos_usados > MINUTO_AVANÇADO or GB_usados > GB_AVANÇADO:
        print(f"Valor da fatura: R${preco_reajuste_avançado}")

