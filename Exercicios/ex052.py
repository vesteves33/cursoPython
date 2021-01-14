num = int(input('Digite um número inteiro: '))
totalContagem = 0
for contador in range(1, num+1):
    if num % contador == 0:
        totalContagem += 1
    
if totalContagem == 2:
    print('Número {} é primo'.format(num))
else:
    print('Número {} não é primo'.format(num))