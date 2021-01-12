from math import pow

peso = float(input('Diga seu peso atual: '))
altura = float(input('Diga sua altura em metros: '))

imc = peso/pow(altura, 2)

if imc >=0 and imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')    
elif imc >= 30 and imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')