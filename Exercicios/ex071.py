print('='*30)
print('{:^30}'.format('BANCO VEC'))
print('='*30)

valor = int(input('Quanto quer sacar? '))
total = valor
cedula = 50
totalCedula = 0 
while True:
    if total >= cedula:
        total -= cedula
        totalCedula += 1
    else:
        if totalCedula > 0:
            print(f'Total de {totalCedula} cedulas de R${cedula}')
        if cedula == 50:
             cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedula = 0
        
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO VEC. Tenha um Bom dia!')