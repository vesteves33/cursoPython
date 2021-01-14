frase = str(input('Digite uma frase e veja se é palindromo: ')).strip().lower()
palavras = frase.split()
tudoJunto = ''.join(palavras)
inverso = ''
for letra in range(len(tudoJunto)-1, -1, -1):
    inverso += tudoJunto[letra]
if inverso == tudoJunto:
    print('A frase é um palíndromo')    
else:
    print('A frase não é um palindromo')