termoInicial = int(input('Digite o termo inicial: '))
razao = int(input('Digite o valor da razão da PA: '))
pa = []
contador = 1
contador2 = 1

while contador < 11:
    termoFinal = termoInicial + ((contador-1)*razao)  
    pa.append(termoFinal)
    contador += 1        
    
resposta = str(input('Deseja acrescentar mais termos da PA? [S/N]')).strip().lower()
if len(resposta) == 1:
    if resposta == 'n':
        print('Os 10 primeiros termos da PA foram: {}'.format(pa)) 
    else:    
        maisTermos = int(input('Quantos termos deseja acrescentar? '))
        termoInicial = termoFinal
        while contador2 <= maisTermos:
            termoFinal = termoInicial + (contador2 * razao)
            pa.append(termoFinal)
            contador2 += 1
        print(f'A sequencia da PA é {pa}')        