import requests, pprint

link = 'https://cep.awesomeapi.com.br/json/25740220'

endereco = requests.get(link).json()

pprint.pprint(endereco)