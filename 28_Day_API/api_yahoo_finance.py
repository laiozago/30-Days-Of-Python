from IPython.display import display
import pandas as pd
import pandas_datareader.data as pdr
import yfinance

yfinance.pdr_override()

ativos = ["ITUB3.SA","VALE3.SA","PETR3.SA","^BVSP"]
data_inicial = "2023-01-01"
data_final = "2024-01-10"
tabela_cotacoes = pdr.get_data_yahoo(ativos, start=data_inicial, end=data_final)["Adj Close"]
display(tabela_cotacoes)