# Desenvolva um programa que permita aos usuários avaliarem restaurantes com notas de 0 a 5.
# Cada restaurante só deve ser inserido uma vez na lista.
# Se um restaurante for avaliado mais de uma vez, o programa deve atualizar a nota média do restaurante considerando todas as avaliações fornecidas até o momento, mas o restaurante não deve ser adicionado novamente à lista.
# O programa deve:
# ● Solicitar o nome do restaurante ou digitar “PARE” para finalizar.
# ● Solicitar a nota dada pelo usuário (de 0 a 5).
# ● Se o restaurante já foi avaliado anteriormente, atualizar a nota média considerando todas as avaliações anteriores e a nova avaliação

restaurantes = []
avaliacoes = []
qtd_avaliacoes = []

restaurante = None

while restaurante != "PARE":
    restaurante = input("Digite o nome do restaurante ou digite PARE para finalizar: ")
    if restaurante.upper() == "PARE":
        break
    nota = float(input("Digite a nota do restaurante (de 0 a 5): "))

    index = (
        restaurantes.index(restaurante)
        if restaurante in restaurantes
        else -1)

    if index == -1:
        #inicializa a lista de restaurantes quando restaurante não existe
        restaurantes. append(restaurante)
        avaliacoes.append(nota)
        qtd_avaliacoes.append(1)

    else:
        #calcula a nova media
        avaliacoes[index] =(avaliacoes[index]*qtd_avaliacoes[index]+nota)/(qtd_avaliacoes[index]+1)

    #atualiza a quantidade de avaliações
        qtd_avaliacoes[index] += 1

    maior_avaliação = max(avaliacoes)
    menor_avaliação = min(avaliacoes)

    index_maior =avaliacoes.index(maior_avaliação)
    index_menor = avaliacoes.index(menor_avaliação)

print(f"Restaurante com a maior nota: {restaurantes [index_maior]} - Nota média: { avaliacoes [index_maior]}")
print(f"Restaurante com a menor nota: {restaurantes[index_menor]} - Nota média: {avaliacoes[index_menor]}")