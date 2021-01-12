r1 = float(input('digite o valor da reta 1'))
r2 = float(input('digite o valor da reta 2'))
r3 = float(input('digite o valor da reta 3'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('As retas podem formar um triangulo')
else:
    print('As retas não podem formar um triangulo')