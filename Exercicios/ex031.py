viagem = int(input('Qual a distância da viagem? '))

if 0 <= viagem <= 200:
    viagem *= 0.5
    print('Sua passagem vai custar R${:.2f}'.format(viagem))
else:    
    viagem *= 0.45
    print('Sua passagem vai custar R${:.2f}'.format(viagem))