casa = float(input('Qual o preço do imóvel? '))
salario = float(input('Qual o valor do salário? '))
anos = float(input('Quantos anos você quer pagar? '))

mensal = anos*12
prestacao = casa/mensal

if prestacao <= 0.3*salario:
    print('Empréstimo autorizado, o valor da mensalidade é {:.2f}'.format(prestacao))
else:
    print('Empréstimo negado!')