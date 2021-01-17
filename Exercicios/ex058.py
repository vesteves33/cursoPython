from random import randint 
from time import sleep

palpite = -1
computador = randint(0,10)
contadorPalpites = 0

while palpite != computador:
    palpite = int(input('Digite um número entre 0 e 10: '))
    print('PROCESSANDO...')
    sleep(3) 
    if palpite == computador:
        print('Parabéns você acertou!')
        contadorPalpites += 1
    else:
        print('Mais sorte na próxima, tente novamente!')
        contadorPalpites += 1
        palpite = int(input('Digite um número entre 0 e 10: '))
print('Foram necessários {} palpites até acertar'.format(contadorPalpites))