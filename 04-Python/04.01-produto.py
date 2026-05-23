#criando as variaveis e solicitando os valores para o usuario
nome_produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o desconto do produto: "))

#calculando o desconto e o preço final
valor_do_desconto = preco * desconto / 100
preco_final = preco - valor_do_desconto

#apresentando os dados do produto para o usuario
print(f"Produto: {nome_produto}- Preço final: R$ {preco_final}")