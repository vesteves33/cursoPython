from random import randint

jogador = 0
computador = randint(0,10)
soma = 0
status = 'vitoria'
while True:
    jogador = int(input('Digite um número inteiro: '))
    
    print('-'*30)
    parImpar = str(input('Quer par ou impar [P/I]? ')).strip().lower()
    print('-'*30)
    soma = jogador + computador
    
    if soma % 2 == 0 and parImpar == 'p':
        print('O jogador venceu!')
    elif soma % 2 != 0 and parImpar == 'i':
        print('O jogador venceu!')
    else:
        break
print('O computador venceu')