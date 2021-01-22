resp = 's'
somaPreco = 0
contador = 0
menorPreco = 0
menorProduto = ''
while resp == 's':
    nome = str(input('Digite o nome do produto '))
    preco = float(input('Digite o preço do produto '))
    somaPreco += preco
    print('-='*20)
    resp = str(input('Deseja continuar [s/n]? ')).strip().lower()    
    print('-='*20)
    
    if preco > 1000.00:
        contador += 1
    
    if contador == 1 or preco < menorPreco:
        menorPreco = preco
        menorProduto = nome

print('*'*30)
print('Sumário da conta')
print(f'O total da compra é de R$ {somaPreco:.2f}')
print(f'{contador} produtos custam menos de R$ 1000.00')
print(f'O produto mais barato foi {menorProduto} custando R$ {menorPreco}')