num = 0
contador = 1
while True:
    print('-'*30)
    num = int(input('Qual tabuada deseja visualizar? '))
    print('-'*30)
    
    if num < 0:
        break
    
    for contador in range(1, 11):
        print(f'{num} x {contador} = {num*contador}')
print('Programa encerrado')