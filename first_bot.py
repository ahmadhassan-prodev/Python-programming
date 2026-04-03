from binance.client import Client
from datetime import datetime
import pandas as pd

api_key = '5a3Tq6sEdSYhw7rwOms6QTufF6C3COyOkb7ruy7DpqB7jLsJFdeUTUl2kIm9Id0E'
api_secret = 'wW4YMB0qXDCccGvqih3BjFF8SEPvwPjgHJ8IGphIZ1O0uZyPYWTzNS5V20UjbCGX'

client = Client(api_key,api_secret)

candles = client.get_klines(
    symbol='SOLUSDT',
    interval = Client.KLINE_INTERVAL_15MINUTE,
    limit = 5
    )

df = pd.DataFrame(candles)[[0,1,2,3,4,5,6]]
df.columns = ['Open Time','Open', 'High', 'Low', 'Close', 'Volume','Close Time']

df['Open Time'] = pd.to_datetime(df['Open Time'], unit='ms')
df['Open Time'] = df['Open Time'].dt.tz_localize('UTC').dt.tz_convert('Asia/Karachi')
df['Close Time'] = pd.to_datetime(df['Close Time'], unit='ms')
df['Close Time'] = df['Close Time'].dt.tz_localize('UTC').dt.tz_convert('Asia/Karachi')

for i in range(0,4):
    for data in df:
        print(df[data][i])
