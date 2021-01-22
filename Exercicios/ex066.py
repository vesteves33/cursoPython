num = 0
contador = 0 
soma = 0
while True:
    num = int(input('Digite um número inteiro: ')) 
    
    if num == 999:
        break
    contador += 1
    soma += num
print(f'O numero de repetições foi de {contador} e a soma foi {soma}')