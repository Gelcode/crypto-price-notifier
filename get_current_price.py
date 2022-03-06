import requests

URL = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd'
req = requests.get(url=URL)
data = req.json()

def get_current_price(symbol):
	for i in range(len(data)):
		if (data[i]['symbol']) == symbol:
			crypto = data[i]['id']
			price = data[i]['current_price']
			
			print(f'{crypto} = {price}')
			break

symbol = input()
get_current_price(symbol)
