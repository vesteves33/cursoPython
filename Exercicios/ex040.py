nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua primeira nota: '))
media = (nota1 + nota2) / 2

if  media < 5.0:
    print('Reprovado, sua média foi {}'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('Recuperação, sua média foi {}'.format(media))
else:
    print('Aprovado, sua média foi {}'.format(media))