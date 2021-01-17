class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def mostrarInfo(self):
        print('Nome: {} \nIdade: {} \nSexo: {}'.format(self.nome, self.idade,self.sexo))