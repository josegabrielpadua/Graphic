Esse é um projeto no qual foi utilizado arquivos excel para poder gerar uma coluna de receita
gerada. Com isso, também pode ser gerado um gráfico com uma relação entre LojaID x Receita gerada.

- O sistema automatiza a geração da coluna receita gerada, na qual é uma relação de multiplicidade de Vendas x Quantidade.
- O sistema gera um gráfico com base na entrada de dados. 

No arquivo .py, a partir da linha 30, é notado as seguintes linhas:

30 - ano = 2019
31 - mes = 3
32 - dia = 2
33 - cidade = "Fortaleza"

Caso for alterado, filtrando o ano, mês, dia e cidade, poderá gerar um gráfico. Algumas instruções caso for alterado:

#Se for inserido "0" na variável dia, será considerado apenas o mês e ano.
#Se for inserido "0" na variável mês, será considerado apenas o ano, independente do valor inserido na variável dia.

Autor: José Pádua.
