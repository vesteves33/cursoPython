n1 = int(input('Digite o primeiro numero inteiro: '))
n2 = int(input('Digite o segundo numero inteiro: '))

if n1 > n2:
    print('O numero {} é maior'.format(n1))
elif n2 > n1:
    print('O numero {} é maior'.format(n2))
else:
    print('Não há número maior, os dois são iguais')