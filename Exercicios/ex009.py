dado = int(input('Digite um número de 1 a 9: '))
i = 1 
print('Tabuada de {}'.format(dado))
while(i <= 10):
    print("{} x {} = {}".format(dado, i, dado*i))
    i = i + 1