dado = input('Diga o nome da sua cidade: ')
dado.strip()
semEspaco = dado.lower().split()
print(semEspaco[0].find('santo') == 1)