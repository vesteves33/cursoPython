precoProduto = float(input('Diga o preço do produto: '))
metodoPagamento = int(input('Diga a forma de pagamento: 1-Dinheiro 2-Cheque 3-Cartão de Crédito: '))

if metodoPagamento == 1 or metodoPagamento == 2:
    precoProduto *= 0.9
    print('Preço do produto será R${:.2f}'.format(precoProduto))
elif metodoPagamento == 3:
    resposta = int(input('1-À vista 2-Parcelado '))
    if resposta == 1:
        precoProduto *= 0.95
        print('Preço do produto será R${:.2f}'.format(precoProduto))
    elif resposta == 2:
        parcelado = int(input('Quantas vezes 1-2x 2-3x '))
        if parcelado == 1:
            print('Preço do produto é R${:.2f}'.format(precoProduto))
        elif parcelado == 2:
            precoProduto *= 1.2
            print('Preço do produto é R${:.2f}'.format(precoProduto))
        else:
            print('Metodo não disponivel')
    else:
        print('Método não encontrado')
else:
    print('Para consultar as opções veja novamente nosso menu')            