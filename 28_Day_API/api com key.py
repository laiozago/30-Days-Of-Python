#API KEY = PI6L41O2PCJBDZ4F
import requests, pprint
link = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=PI6L41O2PCJBDZ4F"

info = requests.get(link).json()
ticker = info['Meta Data']['2. Symbol']
data = '2024-01-05'
info_do_dia = info['Time Series (Daily)'][data]
pprint.pprint(ticker)
pprint.pprint(data)
pprint.pprint(info_do_dia)