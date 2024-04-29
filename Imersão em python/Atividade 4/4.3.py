# 3) Uma loja deseja criar um sistema de controle de estoque.
# O usuário deve inserir o nome do produto e a quantidade.
# Se a quantidade for negativa, o programa deve informar um erro e pedir novamente.
# Após cada inserção, o sistema solicitará um novo nome ou  o usuário informará “FIM” para encerrar o sistema.
# Por fim, o sistema deverá apresentar a quantidade de tipos de produtos inseridos.

nome_produto = ""
tipo_produto = 0
quantidade_produto =0
while nome_produto != "FIM":
    nome_produto = input("Digite o nome de um novo produto ou FIM para encerrar o sistema: ")
    if nome_produto =="FIM":
         break
    else:
        quantidade_produto = int(input("Digite a quantidade do produto: "))
        if quantidade_produto <= 0 :
            print ("Não é possível cadastro de estoque negativo.")
        elif quantidade_produto > 0 :
            tipo_produto +=1
print(f"Tipos de produtos cadastrados: {tipo_produto}")

