valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))
resultado = 0
print('Diga qual operação deseja realizar')
menu = int(input('''
                    [ 1 ] Somar 
                    [ 2 ] Multiplicar
                    [ 3 ] Qual o maior
                    [ 4 ] Novos números
                    [ 5 ] Sair do programa    '''))
while menu != 5:
    if menu == 1:
        resultado = valor1 + valor2
    if menu == 2:
        resultado = valor1 * valor2
    if menu == 3:
        resultado = max(valor1, valor2)
    if menu == 4:
        ...
        
