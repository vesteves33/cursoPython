import pandas as pd
from selenium import webdriver
from time import sleep

#dtype object = texto, int = numero inteiro , float = numero com virgula
tabelaCliente = pd.read_excel("/home/vitor/Projetos/Python/Desafios/IntensivaoPython/Aula 4/Clientes Pagamento.xlsx", dtype={"Cliente": object})

#utilizando lib selenium para manipular navegador
navegador = webdriver.Firefox()
navegador.get("https://acesso.pagseguro.uol.com.br/")
navegador.find_element_by_id("user").send_keys("vesteves33@gmail.com")
navegador.find_element_by_id("password").send_keys("300694Vi.")
sleep(5)
navegador.find_element_by_xpath('/html/body/div[2]/div/div/main/div/div/div/form/div/div/div/div/div[3]/button').click()

#para não ficar exposto criar arquivo e importar para parametros do send_keys
#depois de passar o codigo captcha recomeçar script direcionando para pagina de cobrança

sleep(100)

navegador.get('https://pagseguro.uol.com.br/operations/charging.jhtml?_ga=2.157087227.1952588963.1613085144-1948505992.1612881079')

for linha in tabelaCliente.index:
    divida = tabelaCliente.loc[linha, "Valor Total Devido"] - tabelaCliente.loc[linha, "Valor Pago"]
    
    if divida > 0:
    
        nome = tabelaCliente.loc[linha, "Nome"]
        valor = divida
        email = tabelaCliente.loc[linha, "Email"]
        descricao = 'Cobrança pagamento'
        #adaptação para preenchimento do input do valor que é formatado com casas decimais.
        textoValor = f"{valor:.2f}"

        navegador.find_element_by_xpath('/html/body/div[1]/div[4]/section[2]/div/div/form/div[1]/section[1]/div/fieldset[1]/input').send_keys(email)
        navegador.find_element_by_xpath('/html/body/div[1]/div[4]/section[2]/div/div/form/div[1]/section[1]/div/fieldset[2]/input').send_keys(nome)
        navegador.find_element_by_xpath('/html/body/div[1]/div[4]/section[2]/div/div/form/div[1]/section[2]/div/fieldset[1]/input').send_keys(descricao)
        navegador.find_element_by_xpath('/html/body/div[1]/div[4]/section[2]/div/div/form/div[1]/section[2]/div/fieldset[2]/div/input').send_keys(textoValor)

        navegador.find_element_by_id("sendNewCharging").click()
        sleep(10)