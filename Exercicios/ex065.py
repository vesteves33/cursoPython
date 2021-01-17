sequencia = []
somatorio = 0
contador = 1
maior = 0
menor = 0
resposta = ''
while resposta != 'n':
    if contador == 1:
        numeros = int(input('Digite os numeros e veja sua média: '))
        maior = numeros
        menor = numeros    
        sequencia.append(numeros)
        somatorio += numeros
        contador += contador
    else:
        numeros = int(input('Digite os numeros e veja sua média: '))
        somatorio += numeros
        sequencia.append(numeros)
        resposta = str(input('Deseja acrescentar mais números [s/n]? '))
        if numeros > maior:
            maior = numeros
        if numeros < menor:
            menor = numeros    
        media = somatorio / contador
        contador += 1
print(f'Os valores digitados foram {sequencia}')
print(f'A média obtida foi de {media}')
print(f'O maior valor foi {maior}')
print(f'O menor valor foi {menor}')