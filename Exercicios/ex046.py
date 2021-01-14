from time import sleep

for timer in range(10, 0, -1):
    print('{}!'.format(timer))
    print('*'*20)
    sleep(1)
    
print('Feliz Ano Novo!')