escolha = int(input('Escolha um numero de 1 a 9: '))
for tabuada in range(1,11):
    print('{} x {} = {}'.format(escolha, tabuada, escolha*tabuada))