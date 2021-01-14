termoInicial = int(input('Digite o termo inicial: '))
razao = float(input('Digite o valor da razão da PA: '))
pa = []
for contador in range(1, 11):
    termoFinal = termoInicial + ((contador-1)*razao)  
    pa.append(termoFinal)
print('Os 10 primeiros termos da PA foram: {}'.format(pa)) 