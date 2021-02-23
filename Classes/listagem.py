#pequeno script pra preencher informação de empresas confraria Oloya's
print('-='*30)
print('Abaixo digite as informações da empresa parceira:')
print('-='*30)


arquivo = open('/home/vitor/Projetos/Python/Classes/listagemlojas', 'a')

while True:
    tipoNegocio = str(input('Setor do negócio: ')).strip()
    nome = str(input('Digite aqui o nome da empresa: ')).strip()
    endereco = str(input('Digite o endereço: ')).strip()
    telefone = str(input('Digite o telefone: ')).strip()
    facebook = str(input('Link do Facebook: ')).strip()
    instagram = str(input('Link do Instagram: ')).strip()
    site = str(input('Link do site: ')).strip()
    desconto = int(input('Digite o valor do desconto: '))
    desconto = str(desconto)
    resp = str(input('Deseja inserir novo parceiro [s/n]? ')).lower().strip()
    
    arquivo.write('Setor: ' + tipoNegocio + '\n')
    arquivo.write('Nome: ' + nome + '\n')
    arquivo.write('Endereço: ' + endereco + '\n')
    arquivo.write('Telefone: ' + telefone + '\n')
    arquivo.write('Facebook: ' + facebook + '\n')
    arquivo.write('Instagram: ' + instagram + '\n')
    arquivo.write('Site: ' + site + '\n')
    arquivo.write('Desconto: ' + desconto + '%' + '\n')
    arquivo.write('-='*30 + '\n')
    
    if resp == 'n':
        break
arquivo.close()







    

# Ramo do Negocio, Nome, endereço, telefone(s), social media, percentual desconto. 