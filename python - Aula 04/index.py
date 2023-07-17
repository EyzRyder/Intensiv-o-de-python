import pandas as pd

tabela = pd.read_csv("advertising.csv")
print(tabela)


import matplotlib.pyplot as plt # py -m pip install matplotlib
import seaborn as sns # py -m pip install seaborn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression # py -m pip install scikit-learn
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

# Análise Exploratória
# Vamos tentar visualizar como as informações de cada item estão distribuídas
# Vamos ver a correlação entre cada um dos itens

# cria o grafica
sns.heatmap(tabela.corr(), cmap="Wistia", annot=True)
# exibe o grafico
plt.show()

# Com isso, podemos partir para a preparação dos dados para treinarmos o Modelo de Machine Learning
# Separando em dados de treino e dados de teste
y = tabela["Vendas"]
x = tabela[["TV","Radio","Jornal"]]

x_treino, x_test, y_treino, y_test = train_test_split(x,y, test_size=0.3)

# Temos um problema de regressão - Vamos escolher os modelos que vamos usar:
# Regressão Linear
# RandomForest (Árvore de Decisão)

# criar os modelos
modelo_regressaolinear = LinearRegression()
modelo_arvoredecisao = RandomForestRegressor()

# treinar os modelos
modelo_regressaolinear.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)


# Teste da AI e Avaliação do Melhor Modelo
# Vamos usar o R² -> diz o % que o nosso modelo consegue explicar o que acontece

previsao_regressaolinear = modelo_regressaolinear.predict(x_test)
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_test)

print(metrics.r2_score(y_test, previsao_regressaolinear))
print(metrics.r2_score(y_test, previsao_arvoredecisao))

# Visualização Gráfica das Previsões
# arvore de decisao é o melhor modelo, vamos usar ele para fazer os nossas previsoes
tabela_auxiliar = pd.DataFrame()
tabela_auxiliar["y_test"] = y_test
tabela_auxiliar["Previsao Regressao Linear"] = previsao_regressaolinear
tabela_auxiliar["Previsao ArvoreDecisao"] = previsao_arvoredecisao

plt.figure(figsize=(15,6))
sns.lineplot(data=tabela_auxiliar)
plt.show()
# Como fazer uma nova previsão?
# importar a tabela com as novas informações que voce quer prever

nova_tabela = pd.read_csv("novos.csv")
print(nova_tabela)

#usar o modelo_arvoredecisao e fazer um predict com ele
previsao = modelo_arvoredecisao.predict(nova_tabela)
print(previsao)

# Qual a importância de cada variável para as vendas?
sns.barplot(x=x_treino.columns, y=modelo_arvoredecisao.feature_importances_)
plt.show()

# Caso queira comparar Radio com Jornal
# print(df[["Radio", "Jornal"]].sum())