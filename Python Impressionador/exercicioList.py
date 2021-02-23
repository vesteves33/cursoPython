meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas1Sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas2Sem = [19850, 20120, 17540, 15555, 49051, 9650]

vendas1Sem.extend(vendas2Sem)

melhorMes = max(vendas1Sem)
piorMes = min(vendas1Sem)

indiceMelhorMes = vendas1Sem.index(melhorMes)
indicePiorMes = vendas1Sem.index(piorMes)

m = meses[indiceMelhorMes]
p = meses[indicePiorMes]
#Primeira parte, printar na tela o melhor/pior mes e qual valor ele teve 
print(f'O melhor mês foi {m} e o valor de vendas foi R$ {melhorMes}')
print(f'O pior mês foi {p} e o valor de vendas foi R$ {piorMes}')

#Segunda parte, faturamento anual
faturamentoAnual = sum(vendas1Sem)
print('O faturamento do ano foi de R$ {:,.2f}'.format(faturamentoAnual))

percentual = melhorMes / faturamentoAnual

print('O melhor mês representou {:.2%} do meu faturamento anual'.format(percentual))

#Criando top 3 de vendas.
vendasTotal = vendas1Sem.copy()
top3 = []
top3Mes = []
for ranking in range(3):
    top1 = max(vendasTotal)
    top3.append(top1)
    indicetop3 = vendasTotal.index(top1)
    top3Mes.append(meses[indicetop3])
    vendasTotal.remove(top1)
    

print('Os meu top 3 meses do ano foram {}, {}, {} com valores de {:,.2f}, {:,.2f}, {:,.2f}'.format(top3Mes[0], top3Mes[1], top3Mes[2], top3[0], top3[1], top3[2]))