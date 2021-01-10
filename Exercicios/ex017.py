from math import pow, sqrt

catetoOposto = float(input('Diga o valor do cateto oposto: '))
catetoAdj = float(input('Diga o valor do cateto adjacente: '))
hipotenusa = sqrt(pow(catetoOposto, 2) + pow(catetoAdj, 2))
print('Comprimento da Hipotenus do triângulo é: {}'.format(hipotenusa))