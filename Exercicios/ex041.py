from datetime import datetime

idade = int(input('Ano de nascimento do atleta: '))
anoAtual = datetime.now()
faixaEtaria = anoAtual.year - idade

if  faixaEtaria >= 0 and faixaEtaria <= 9:
    print('Mirim ')
elif faixaEtaria >= 10 and faixaEtaria <= 14:
    print('Infatil')
elif faixaEtaria >= 15 and faixaEtaria <= 19:
    print('Junior')
elif faixaEtaria > 19 and faixaEtaria == 20:
    print('Senior')
else:
    print('Master')