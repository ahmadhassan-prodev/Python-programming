from binance.client import Client

api_key = '5a3Tq6sEdSYhw7rwOms6QTufF6C3COyOkb7ruy7DpqB7jLsJFdeUTUl2kIm9Id0E'
api_secret = 'wW4YMB0qXDCccGvqih3BjFF8SEPvwPjgHJ8IGphIZ1O0uZyPYWTzNS5V20UjbCGX'

client = Client(api_key,api_secret)
client.API_URL = 'https://testnet.binance.vision/api'

# account = client.get_account()
balance = client.get_asset_balance(asset='USDT')
print((balance['free']))