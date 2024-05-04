# Uma pista de Kart permite 3 voltas para cada um dos 4 corredores.
# No programa principal, implemente um código que leia o nome do corredor e todos os tempos em segundos e os guarde em um dicionário, onde a chave é o nome do corredor.
# Implemente duas funções:
# 1. Uma função chamada calcular_media que recebe uma lista de tempos como parâmetro e retorna a média desses tempos.
# 2. Uma função chamada encontrar_campeao que recebe o dicionário de tempos como parâmetro e usa a função calcular_media para calcular a média de tempo de cada corredor.
# A função deve identificar o campeão (corredor com a menor média de tempo) e retornar o nome do campeão e sua média de tempo com duas casas decimais (use round(menor_media, 2).
# No final do programa principal, exiba o nome do campeão em maiúsculas e sua média de tempo com duas casas decimais.

def calcular_media(lista_tempos: list) -> float:
    """Função para calcular a media dos tempos.
    Arguments: 
    lista_tempos: {list} - Tempos em segundos
    Returns:
        float:Media dos Tempos - Média dos tempos
    """

    return sum(lista_tempos)/len(lista_tempos)

def encontrar_campeao(dic_tempos: dict) -> tuple[str, float]:
    """ Função para encontrar o campeão.
    
    Argumentos:
    dict_tempos: {dict} - Tempo dos corredores
    Returns:
    tuple[str, float]: Nome do campeão e sua média de tempo.
    """

    menor_media = float("inf")
    campeao = ""
    for corredor, tempos in dic_tempos.items():
        media = calcular_media(tempos)
        if media < menor_media:
            menor_media = media
            campeao = corredor
    return campeao, round(menor_media,2)

# Função Principal
def main() -> None:
    """"Função Principal."""""
tempos = {}

for i in range(4):
    corredor = input(f"Digite o nome do {i +1}º corredor: ")
    tempos[corredor] = [float(input(f'Digite o tempo de volta {j + 1}:')) for j in range(3)]

# vencedor, menor_media = encontrar_campeao(dic_corredores)

    campeao, media = encontrar_campeao(tempos)
print(f'O campeão é {campeao.upper()} com media de tempo de {media:.2f} segundos.')
