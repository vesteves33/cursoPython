numero = int(input('Diga um número e veja seu fatorial: '))
fatorial = 1

print(f'Calculando {numero}! = ', end='')
while numero > 0:
    fatorial *= numero
    print(f'{numero}',end='')
    print(' x ' if numero > 1 else ' = ', end='')    
    numero -=1
print(f'{fatorial} ')