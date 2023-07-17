# py -m pip install selenium
# chrome -> chromedriver
# firefox -> geckodriver

import pandas as pd
from selenium import webdriver # controlar o navegador
from selenium.webdriver.common.keys import Keys # usar o teclado
from selenium.webdriver.common.by import By # localizar os itens no navegador

navegador = webdriver.Chrome()
navegador.get("https://www.google.com/")

#pegaria a cotação do dólar
navegador.find_element(By.ID,"APjFqb").send_keys("cotação dolar")
navegador.find_element(By.ID,"APjFqb").send_keys(Keys.ENTER)
# ou
# navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dolar")
# navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)


cotacao_dolar = navegador. find_element(By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print("Dolar")
print(cotacao_dolar)

# entrarta no google e pesquisarta a cotação do euro
navegador.get("https://www.google.com/")
navegador.find_element(By.ID,"APjFqb").send_keys("cotação euro")
navegador.find_element(By.ID,"APjFqb").send_keys(Keys.ENTER)
# ou
# navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotaçao euro")
# navegador. find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

# pegarta a cotação do euro
cotacao_euro = navegador. find_element(By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print("Euro")
print(cotacao_euro)

#entrar no https://www.melhorcambio.com/ouro-hoje
navegador.get("https://www.melhorcambio.com/ouro-hoje")

cotacao_ouro = navegador. find_element(By.XPATH,'//*[@id="comercial"]').get_attribute('value')

cotacao_ouro = cotacao_ouro.replace(",",".")

# pegarta a cotação do ouro
print("Ouro")
print(cotacao_ouro)

navegador.quit()

tabela = pd.read_excel("Produtos.xlsx")
print(tabela)

# atual izar as cotações na base de dados
#cotacao do dolar
tabela.loc[tabela["Moeda"] == "Dólar" ,"Cotação"] = float(cotacao_dolar)
#cotacao do euro
tabela.loc[tabela["Moeda"] == "Euro" ,"Cotação"] = float(cotacao_euro)
#cotacao do ouro
tabela.loc[tabela["Moeda"] == "Ouro" ,"Cotação"] = float(cotacao_ouro)

# atualizar o preço de compra e de venda na base de dados
# preco de compra - preco original * cotacao
tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]
# preco de venda preco de compra * margem
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]

print(tabela)

# exportar essa base de dados para ter o resultado atualizado
tabela.to_excel("ProdutoNovo.xlsx",index= False)