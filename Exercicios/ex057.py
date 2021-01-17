sexo = ''
while sexo != 'm' and sexo != 'f':
    sexo = str(input('Diga qual seu sexo [M/F]: ')).strip().lower()
    if sexo.__len__() > 1:
        print('opção inválida tente novamente')
        sexo = str(input('Diga qual seu sexo [M/F]: ')).strip().lower()
            
print('Opção incluida com sucesso!')
        
            