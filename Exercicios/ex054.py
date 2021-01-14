from datetime import date

anoAtual = date.today().year
menoresIdade = 0
maioresIdade = 0
for contador in range(0,7):
    anoNascimento = int(input('Digite seu o ano de nascimento: '))
    if anoAtual - anoNascimento < 18:
        menoresIdade += 1
    else:
        maioresIdade += 1
print('O numero de maiores de idade é: {} e de menores é: {}'.format(maioresIdade, menoresIdade))