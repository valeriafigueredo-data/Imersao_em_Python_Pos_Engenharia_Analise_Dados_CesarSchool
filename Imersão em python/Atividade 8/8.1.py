# Crie uma função chamada quadrado que recebe um número x como parâmetro.
# A função deve retornar um dicionário onde as chaves são os números de 1 a x e os valores são o quadrado desses números.
# Teste a função no programa principal.

def quadrado(x):
    for i in range (1, x+1):
        numeros[i]= i*i
    return numeros

numeros = {}

#programa principal

qtd = int(input("Determine a quantidade de repetições: "))
resultado = quadrado(qtd)
print(resultado)