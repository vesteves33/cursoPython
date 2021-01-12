from datetime import datetime

ano = int(input('Digite o ano de seu nascimento: '))
anoAtual = datetime.now()
tempo = anoAtual.year - ano
if tempo <= 17:
    faltaTempo = 18 - tempo
    print('Você ainda tem mais {} anos para aguardar seu momento.'.format(faltaTempo))  
elif tempo == 18:
    print('Não perca tempo se alista já! Seu pais conta com você')
else:
    faltaTempo = tempo - 18
    print('Seu tempo de alistamento já se passou em {} anos.'.format(faltaTempo))