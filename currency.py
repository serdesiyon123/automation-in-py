import requests

API_KEY = 'fca_live_CVYuvK93BoTcCi9BYf0AKdVjc8M2Jyt13TWIU1Xv'
BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'

CURRENCIES = ["USD", "CAD",  "EUR", "CNY"]

def curreny_converter(base):
    currenies = ",".join(CURRENCIES)
    url = f'{BASE_URL}&base_currency={base}&currencies={currenies}'
    try:
        response = requests.get(url)
        data = response.json()
        print(data)
        return data
    except Exception as e:
        print(e)
        
curreny_converter("USD")