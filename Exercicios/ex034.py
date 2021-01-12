salario = float(input('Digite o valor do salário: '))
if salario >= 1250.00:
    salario *= 1.1
    print('Seu salário atual é {}'.format(salario))
else:
    salario *= 1.15
    print('Seu salário atual é {}'.format(salario))
    