nome = str(input('Digite seu nome completo: ')).strip()
nomeSeparado = nome.split()
print('Primeiro nome: {}'.format(nomeSeparado[0]))
print('Ultimo nome: {}'.format(nomeSeparado[len(nomeSeparado)-1]))