import requests



def get_listing():
    """This method for get data API from CMC"""
    api = "cc3b8a81-eff7-4a5a-9655-4003ac463d82"
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    response = requests.get(url, headers={
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': api,
      })

    data = response.json()['data']
    return data
