programa {
  funcao inicio() {
    // criando as variaveis
    real preco_original, porcentagem_desconto, preco_final, valor_desconto
    
    // solicitando os valores ao usuario
    escreva("digite o valor do produto: ")
    leia(preco_original)
    escreva("digite o percentual de desconto: ")
    leia(porcentagem_desconto)

    // calculando o percentual de desconto e o preço final
    valor_desconto = preco_original * (porcentagem_desconto / 100)
    preco_final = preco_original - valor_desconto

    // apresentar o preco final ao usuario
    escreva("valor do desconto: R$",valor_desconto)
    escreva("\nPreço final do produto: R$", preco_final)

  }
}
