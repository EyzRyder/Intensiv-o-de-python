import pandas as pd # py -m pip install pandas openpyxl numpy

# Passo 1 - Importar a base de dados para o Python
tabela = pd.read_csv("telecom_users.csv")

# Passo 2 - visualizar essa base de dados
# Entender as informações que você tem disponivel
# Descobrir as cagadas da base de dados
# axts - e -> Linha
# axis - 1 -> coluna
tabela = tabela.drop("Unnamed: 0", axis=1)
print(tabela)

# Passo 3 - Tratamento de Dados
# analisar se o python tá Lendo as informações no formato correto
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

# será que existe alguma coluna completamente vazia?
# axis = 0 -> Linha; axis = 1 -> coluna
tabela = tabela.dropna(how="all", axis=1)

# será que existe alguma informação em alguma Linha vazia?
tabela = tabela.dropna(how="any", axis=0)
print(tabela.info())

# Passo 4 - Análise INicial / Análise GLobal
# quantos clientes cancelaram e quantos não cancelLaram
print(tabela["Churn"].value_counts())

#o % de cleintes que cancelaram e que não cancelaram
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

# Passo 5 - Análise detalhada (buscar a causa/ a solução dos cancelamentos)
import plotly.express as px # py -m pip install plotly

# criar o grafico
# edições no gráfico: https://plotly.com/python/histograms/
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna,color="Churn")
    # exibir o grafico
    grafico.show()