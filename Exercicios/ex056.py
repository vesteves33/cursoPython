mediaIdade = 0
homemVelho = ''
idadeHomem = 0
mulheres20 = 0
for pessoa in range(1,5):
    nome = str(input('Nome da {}ª pessoa: '.format(pessoa))).strip().lower()
    idade = int(input('Idade da {}ª pessoa: '.format(pessoa)))
    sexo = str(input('Sexo [M/F]')).strip().lower()
    
    mediaIdade = (mediaIdade + idade) /pessoa
    
    if pessoa == 1 and sexo == 'm':
        homemVelho = nome
        idadeHomem = idade
    if sexo == 'm' and idade > idadeHomem:
        idadeHomem = idade
        homemVelho = nome
    if sexo == 'f' and idade < 20:
        mulheres20 += 1
    
print('A media de idade do grupo é: {:.2f}'.format(mediaIdade))
print('O homem mais velho é {} e sua idade é {}'.format(homemVelho, idadeHomem))
print('O número de mulheres com menos de 20 anos é {}'.format(mulheres20))