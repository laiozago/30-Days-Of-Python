import requests
import json

#pegar as cotações
cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
#info vem em json, tem que passar para um formato dicionario do py
cotacoes = cotacoes.json()
cotacao_dolar = cotacoes['USDBRL']['bid']
cotacao_euro = cotacoes['EURBRL']['bid']
cotacao_btc = cotacoes['BTCBRL']['bid']
print(f'Dolar: {cotacao_dolar} Euro: {cotacao_euro} Bitcoin: {cotacao_btc}')