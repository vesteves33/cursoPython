numero = int(input('Diga um número e veja seu fatorial: '))
fatorial = 1
contador = numero
while numero > 0:
    fatorial *= numero
    numero -=1

print('O resultado de {}! é = {}'.format(contador, fatorial))