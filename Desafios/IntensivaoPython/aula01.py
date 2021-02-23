import pandas as pd 

tbVendas = pd.read_excel('Desafios/IntensivaoPython/Vendas.xlsx')

#separação do ranking das lojas por faturamento
tbFaturamento = tbVendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
tbFaturamento = tbFaturamento.sort_values(by='Valor Final', ascending=False)

#sepração das lojas por quantidade de itens vendidos
tbQuantidade = tbVendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
tbQuantidade = tbQuantidade.sort_values(by='Quantidade', ascending=False)

#separação ticket médio de cada loja fórmula ticket médio = faturamento / quantidade..... to_frame ->dataFrame (python)
ticketMedio = tbFaturamento['Valor Final'] / tbQuantidade['Quantidade']
ticketMedio = ticketMedio.sort_values(ascending=False).to_frame()
ticketMedio = ticketMedio.rename(columns={0: 'Ticket Médio'})

#Criar função que dispara e-mails 
#Parametro se trata de nomeDaLoja = Destinatario do email tabela = Resultado da filtragem e agrupamento dos dados
def envioEmail(nomeDaLoja, tabela):
    import smtplib
    import email.message

    server = smtplib.SMTP('smtp.gmail.com:587')  
    #editar corpor de email
    corpoEmail = f"""
                    <p>Prezados</p>                 
                    <p>Segue o relatório de vendas</p>
                    {tabela.to_html()}
                    <p>Qualquer dúvida estou à disposição</p>
                    
                    <p><strong>Atenciosamente</strong></p>
                    <p><strong>Vitor Esteve</strong></p>
                 """
                 
    msg = email.message.Message()
    msg['Subject'] = f"Relatório de vendas - {nomeDaLoja}" #editar
    
    # Fazer antes (apenas na 1ª vez): Ativar Aplicativos não Seguros.
    # Gerenciar Conta Google -> Segurança -> Aplicativos não Seguros -> Habilitar
    # Caso mesmo assim dê o erro: smtplib.SMTPAuthenticationError: (534,
    # Você faz o login no seu e-mail e depois entra em: https://accounts.google.com/DisplayUnlockCaptcha
    msg['From'] = 'vesteves33@gmail.com' #editar
    msg['To'] = 'vesteves33@gmail.com' #editar
    password = "300694vitoR." #editar
    msg.add_header('Content-Type', 'text/html') 
    msg.set_payload(corpoEmail) 
    
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')   
    
    
#Utilização da função de disparo de emails como teste

tbCompleta = tbFaturamento.join(tbQuantidade).join(ticketMedio)

#envioEmail('Diretoria', tbCompleta)

#último passo da primeira aula, enviar email individual para cada loja

lojas = tbVendas['ID Loja'].unique()

for loja in lojas:
    tbLojas = tbVendas.loc[tbVendas['ID Loja'] == loja, ['ID Loja', 'Quantidade', 'Valor Final']]
    tbLojas = tbLojas.groupby('ID Loja').sum()
    tbLojas['Ticket Médio'] = tbLojas['Valor Final'] / tbLojas['Quantidade']
    #print(tbLojas)
    #envioEmail(loja, tbLojas)
