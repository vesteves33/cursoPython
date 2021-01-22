quantosTermos = int(input('Quantos termos da sequencia de Fibonachi deseja ver? '))
termo1 = 0
termo2 = 1
termo3 = termo1 + termo2
contador = 3
print('-'*30)
print('Sequencia de Fibonachi'.upper())
print('-'*30)

print(f'{termo1} -> {termo2} -> ',end='')
while contador <= quantosTermos:
    termo3 = termo1 + termo2
    print(f'{termo3} -> ', end='')
    termo1 = termo2
    termo2 = termo3
    contador += 1
print('FIM')
    