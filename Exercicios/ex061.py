termoInicial = int(input('Digite o termo inicial: '))
razao = float(input('Digite o valor da razão da PA: '))
pa = []
contador = 1

while contador < 11:
    termoFinal = termoInicial + ((contador-1)*razao)  
    pa.append(termoFinal)
    contador += 1
print('Os 10 primeiros termos da PA foram: {}'.format(pa)) 