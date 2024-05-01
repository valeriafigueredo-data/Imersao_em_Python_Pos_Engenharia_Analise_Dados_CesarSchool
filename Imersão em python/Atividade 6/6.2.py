# Faça um programa que peça ao usuário para inserir:
# ○ uma frase
# ○ uma palavra que está contida na frase
# ○ outra palavra que ele deseja substituir no lugar da primeira palavra inserida.
# Por fim, o programa exibe a frase modificada, toda em letra maiúscula.

frase = ""
palavra = ""
palavra2 = ""
frasecap = ""
frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra que está contida na frase: ")
palavra2 = input("Digite uma palavra para substituir a primeira: ")

nova_frase = frase.replace(palavra, palavra2)
print(nova_frase.upper())