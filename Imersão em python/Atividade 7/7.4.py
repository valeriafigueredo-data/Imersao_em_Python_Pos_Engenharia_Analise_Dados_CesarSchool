# Faça um programa que crie um dicionário onde as chaves serão os números de 1 a 15 e os valores serão o quadrado desses números.

# dicionario = {1:1*1, 2:2*2, 3:3*3, 4: 4*4, 5: 5*5, 6: 6*6, 7: 7*7, 8: 8*8, 9: 9*9, 10: 10*10, 11: 11*11, 12: 12*12, 13: 13*13, 14: 14*14, 15: 15*15}
# print(dicionario)


resultado = {}

for i in range(1,16):
    resultado[i] = i * i #(i**2)
    print(resultado)

