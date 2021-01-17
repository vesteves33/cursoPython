quantosTermos = int(input('Quantos termos da sequencia de Fibonachi deseja ver? '))
termos = 0
seqFibo = []
contador = 0
termoFinal = 0

while contador < quantosTermos:
    if contador == 0:
        seqFibo.append(termos)
        contador += 1
    if contador == 1:
        termos +=1
        seqFibo.append(termos)
        contador += 1       
    termoFinal += termos
    seqFibo.append(termoFinal)  
    contador +=1  
print(f'Sequencia de Fibonachi: {seqFibo}')