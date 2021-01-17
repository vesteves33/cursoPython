from Classes.Pessoa import Pessoa

#for dados in range(0, 3):
nome = str(input('Diga seu nome: ')).strip().capitalize()
idade = int(input('Diga sua idade: '))
sexo = str(input('Diga seu sexo [M/F]: ')).strip().lower()
    
pessoa = Pessoa(nome, idade, sexo)
print(pessoa.mostrarInfo())    