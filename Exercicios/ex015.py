dias = int(input('Quantos dias foi alugado? '))
km = float(input('Quanto Km rodados? '))
total = (dias * 60) + (km * 0.15)
print('Valor total a ser pago é: R$ {:.2f}'.format(total))