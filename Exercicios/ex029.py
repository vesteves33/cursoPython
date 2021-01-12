velocidade = int(input('Qual a veloidade do carro? '))
multa = (velocidade - 80) * 7


if velocidade > 80:
    print('Você foi multado em R${}'.format(multa))