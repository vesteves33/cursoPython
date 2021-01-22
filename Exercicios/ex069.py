idade = 0
sexo = ''
resp = 's'
contadorMaioresIdade = 0
contadorHomem = 0
contadorMulher = 0
while resp == 's':
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [m/f] ')).strip().lower()
    
    if idade > 18:
        contadorMaioresIdade += 1
    if sexo == 'm':
        contadorHomem += 1
    if sexo == 'f' and idade < 20:
        contadorMulher += 1
    resp = str(input('Deseja continuar [s/n]? ')).strip().lower()
print(f'{contadorMaioresIdade} maiores de 18, {contadorHomem} são homens, {contadorMulher} são mulheres com menos de 20 anos')