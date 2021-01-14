soma = 0
listaNumeros = []
for contador in range(0,6):
    numero = int(input('Digite um número inteiro: '))
    if numero % 2 == 0:
        listaNumeros.append(numero)
        soma += numero
print('Numeros pares escolhidos: {}'.format(listaNumeros))        
print('A soma dos números pares escolhidos foi de {}'.format(soma))