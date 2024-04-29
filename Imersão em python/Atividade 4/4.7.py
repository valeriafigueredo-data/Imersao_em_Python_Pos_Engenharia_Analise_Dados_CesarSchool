# Uma academia deseja fazer um censo entre seus clientes para descobrir o mais alto, o mais baixo, o mais pesado e o mais leve.
# Antes de iniciar é necessário perguntar ao usuário quantos clientes há na academia.
# Após isto, o sistema irá receber, de cada um dos clientes da academia:
# ● seu código;
# ● sua altura;
# ● e seu peso.
# Ao encerrar o programa devem ser informados:
# ● o código, altura e peso do cliente mais alto
# ● o código, altura e peso do cliente mais baixo
# ● o código, altura e peso do cliente mais pesado
# ● o código, altura e peso do cliente mais leve
# ● a média das alturas de todos os clientes
# ● a média dos pesos de todos os clientes

cod_maior = 0
alt_do_maior = 0.0
peso_do_maior = 0.0

cod_menor = 0
alt_do_menor = 0.0
peso_do_menor = 0.0

cod_mais_pesado = 0
alt_mais_pesado = 0.0
peso_mais_pesado = 0.0

cod_mais_leve = 0
alt_do_mais_leve = 0.0
peso_do_mais_leve = 0.0

soma_altura = 0.0
soma_peso = 0.0

qtd_clientes = int(input("Digite a quantidade de clientes na academia: "))

for i in range(qtd_clientes):
    cod = int(input(f"Determine o código do cliente {i + 1}: "))
    altura = float(input(f"Determine a altura do cliente {i+1}: "))
    peso = float(input(f"Determine o peso do cliente {i+1}: "))

    if i == 0:
        cod_maior = cod
        altura_do_maior = altura
        peso_do_maior = peso

        cod_menor = cod
        altura_do_menor = altura
        peso_do_menor = peso

        cod_mais_pesado = cod
        altura_mais_pesado = altura
        peso_mais_pesado = peso

        cod_mais_leve = cod
        altura_do_mais_leve = altura
        peso_do_mais_leve = peso

    if altura > altura_do_maior:
        cod_maior = cod
        altura_do_maior = altura
        peso_do_maior = peso

    if altura < altura_do_menor:
        cod_menor = cod
        altura_do_menor = altura
        peso_do_menor = peso

    if peso > peso_mais_pesado:
        cod_mais_pesado = cod
        altura_mais_pesado = altura
        peso_mais_pesado = peso

    if peso < peso_do_mais_leve:
        cod_mais_leve = cod
        altura_do_mais_leve = altura
        peso_do_mais_leve = peso

    soma_altura += altura
    soma_peso += peso

media_altura = soma_altura/qtd_clientes
media_peso = soma_peso/qtd_clientes

print(f"O cliente mais alto tem: código {cod_maior}, altura {altura_do_maior}m e peso {peso_do_maior}kg.")
print(f"O cliente mais baixo tem: código {cod_menor}, altura { altura_do_menor}m e peso {peso_do_menor}kg.")
print(f"O cliente mais leve tem: código {cod_mais_leve}, altura {altura_do_mais_leve}m e peso {peso_do_mais_leve}kg.")
print(f"O cliente mais pesado tem: código {cod_mais_pesado}, altura {altura_mais_pesado}m e peso {peso_mais_pesado}kg.")
print(f"A média das alturas é: {media_altura}")
print (f"A média dos pesos é: {media_peso}")






