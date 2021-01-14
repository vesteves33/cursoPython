from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''' )
jogador = int(input('Sua escolha: '))

print('-='*20)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO....')
print('-='*20)

if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador Venceu')
    elif jogador == 2:
        print('Computador Venceu')
    else:
        print('Jogada inválida')
elif computador == 1:
    if jogador == 0:
        print('Computador Venceu')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador Venceu')
    else:
        print('Jogada inválida')   
elif computador == 2:
    if jogador == 0:
        print('Jogador Venceu')
    elif jogador == 1:
        print('Computador Venceu')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada inválida')    
else:
    print('Tente novamente')