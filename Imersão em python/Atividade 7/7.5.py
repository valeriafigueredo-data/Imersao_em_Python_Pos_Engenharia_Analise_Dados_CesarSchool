# 5) Uma pista de Kart permite 3 voltas para cada um dos 4 corredores. Escreva um
# programa que leia todos os tempos em segundos e os guarde em um dicionário,
# onde a chave é o nome do corredor. Ao final diga quem foi o campeão,
# apresentando o nome (com a todas as letras maiúsculas) e sua média de tempo
# (com duas casas decimais). Lembre-se: o campeão tem a menor média.

tempos = {}
corredores = 4
medias = []

for i in range(corredores):
    nome = input(f"Digite o nome do {i+1}º corredor: ")
    tempos[nome.upper()] = []
    for v in range(3):
        tempo = float(input(f"Tempo de volta {v+1} (s): "))
        tempos[nome.upper()].append(tempo)
campeao = ""
menor_media = 0
for nome, tempos in tempos.items():
    media = sum(tempos)/len(tempos)
    if not menor_media or media < menor_media:
        menor_media = media
        campeao = nome

print(f"O campeão é {campeao} com média de tempo de {menor_media:.2f} segundos.")

