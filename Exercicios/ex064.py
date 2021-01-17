somatorio = 0
condicao = 0
contador = 0
while condicao != 999:
    condicao = int(input('Diga um número inteiro: '))
    if condicao == 999:
        somatorio = somatorio
    else:
        somatorio += condicao
    contador += 1
print(f'Foram digitados {contador-1} números diferentes e seu somatório é {somatorio}')