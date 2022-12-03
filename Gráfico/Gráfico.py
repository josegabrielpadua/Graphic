import matplotlib.pyplot as plt
import pandas as pd

df1= pd.read_excel("Aracaju.xlsx")
df2 = pd.read_excel("Fortaleza.xlsx")
df3 = pd.read_excel("Natal.xlsx")
df4 = pd.read_excel("Recife.xlsx")
df5 = pd.read_excel("Salvador.xlsx")

df_todos = pd.concat([df1, df2, df3, df4, df5])
df_todos["Data"] = pd.to_datetime(df_todos["Data"])

#Criando uma coluna de receita gerada.

df_todos["LojaID"] = df_todos["LojaID"].astype("object")
df_todos["Receita"] = df_todos["Vendas"].mul(df_todos["Qtde"]) 

df_todos["Ano"] = df_todos["Data"].dt.year
df_todos["Mês"] = df_todos["Data"].dt.month
df_todos["Dia"] = df_todos["Data"].dt.day
df_todos["Trimestre"] = df_todos["Data"].dt.quarter


#Filtrando as vendas do dia 2 de março de 2019 na cidade de Fortaleza e Fazendo um gráfico (Relatório).
#Relação de LojaID x Receita gerada
#Podendo mudar o filtro à vontade.
#Se for inserido "0" na variável dia, será considerado apenas o mês e ano.
#Se for inserido "0" na variável mês, será considerado apenas o ano, independente do valor inserido na variável dia.

ano = 2019
mes = 3
dia = 2
cidade = "Fortaleza"

data: str
data2: str

if dia < 10:
    data = '0'
else:
    data = ""
if mes < 10:
    data2 = '0'
else:
    data2 = ""


df2_filtro = df_todos.loc[(df_todos["Data"].dt.year == ano) & (df_todos["Data"].dt.month == mes) & (df_todos["Data"].dt.day == dia)]
df2_filtro = df2_filtro.loc[df2_filtro["Cidade"] == f"{cidade}"]

msg_toda = f"Receita gerada em {data}{dia}/{data2}{mes}/{ano} em {cidade}"

if dia == 0:
    msg_toda = f"Receita gerada em {data2}{mes}/{ano} em {cidade}"
    df2_filtro = df_todos.loc[(df_todos["Data"].dt.year == ano) & (df_todos["Data"].dt.month == mes)]
    df2_filtro = df2_filtro.loc[df2_filtro["Cidade"] == f"{cidade}"]
    if mes == 0:
        msg_toda = f"Receita gerada em {ano} em {cidade}"
        df2_filtro = df_todos.loc[(df_todos["Data"].dt.year == ano)]
        df2_filtro = df2_filtro.loc[df2_filtro["Cidade"] == f"{cidade}"]

#Montando e personalizando o gráfico

df2_filtro.groupby("LojaID")["Receita"].sum().plot.bar(title=f"{msg_toda}", color="hotpink")
plt.style.use("ggplot")
plt.legend(loc='best')
plt.xlabel("LojaID", color="darkblue", fontsize='large')
plt.ylabel("Receita", color="darkblue", fontsize='large')
plt.show()
