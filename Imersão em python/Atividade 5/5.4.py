# 4) Faça um programa que:
# ○ Receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# ○ Calcule a média anual de temperaturas
# ○ Exiba todos os meses que têm as temperaturas acima da média anual (mostrar o mês por extenso: Janeiro, Fevereiro, . . . ).
# Dica: Crie uma lista de strings com todos os nomes dos meses.

temperaturas = []
temperaturas_acima_media = []
media_anual = 0
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

for i in (meses):
    temperaturas.append(float(input(f"Digite a temperatura do mês {i}: ")))
    media_anual = sum(temperaturas)/len(temperaturas)

meses_acima_media = [meses[i] for i in range(12) if temperaturas[i]> media_anual]

print(f"Média Anual de Temperaturas: {media_anual}")
print(f"Meses com temperaturas acima da média: \n{"\n".join(meses_acima_media)}",)
