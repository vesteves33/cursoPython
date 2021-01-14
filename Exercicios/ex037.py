num = int(input('Digite um número inteiro '))

print('''Escolha uma das bases de conversão:
[ 1 ] converter para Binário
[ 2 ] converter para Octal
[ 3 ] converter para Hexadecimal ''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para binario é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))    
else:
    print('Opção inválida')