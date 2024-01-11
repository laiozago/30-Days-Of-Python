import requests, pprint

cep = '25740220'
link = f'https://cep.awesomeapi.com.br/json/{cep}'
endereco = requests.get(link).json()

pprint.pprint(endereco)