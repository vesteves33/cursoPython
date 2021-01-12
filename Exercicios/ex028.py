from random import randint 
from time import sleep

palpite = int(input('Digite um número entre 0 e 5: '))
computador = randint(0,5)
print('PROCESSANDO...')
sleep(3) 
if palpite == computador:
    print('Parabéns você acertou!')
else:
    print('Mais sorte na próxima, tente novamente!')