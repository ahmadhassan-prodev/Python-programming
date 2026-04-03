from binance.client import Client
from datetime import datetime
import pandas as pd
from ta.trend import EMAIndicator

api_key = '5a3Tq6sEdSYhw7rwOms6QTufF6C3COyOkb7ruy7DpqB7jLsJFdeUTUl2kIm9Id0E'
api_secret = 'wW4YMB0qXDCccGvqih3BjFF8SEPvwPjgHJ8IGphIZ1O0uZyPYWTzNS5V20UjbCGX'

client = Client(api_key,api_secret)
candles = client.get_klines(
    symbol='SOLUSDT',
    interval = Client.KLINE_INTERVAL_15MINUTE,
    limit = 200
    )
df = pd.DataFrame(candles)[[0,1,2,3,4,5]]
df.columns = ['Open Time','Open', 'High', 'Low', 'Close', 'Volume']
df['Open Time'] = pd.to_datetime(df['Open Time'], unit='ms')
df['Open Time'] = df['Open Time'].dt.tz_localize('UTC').dt.tz_convert('Asia/Karachi')
df[['Open', 'High', 'Low', 'Close']] = df[['Open', 'High', 'Low', 'Close']].astype(float)

c = 9
last_candle = df.iloc[-c]
lo = last_candle['Open']
lc = last_candle['Close']
lh = last_candle['High']
ll = last_candle['Low']

previous_candle = df.iloc[-(c+1)]
po = previous_candle['Open']
pc = previous_candle['Close']
ph = previous_candle['High']
pl = previous_candle['Low']

print(previous_candle)
print(last_candle)
print('--------------------------------------')

if (lc>lo):
    print('Bullish candle')
    if (pc<po and lc>po and (lo<=pc or lo>=pc) and (lh>ph or ll<pl) and ((lc-lo)<((po-pc)*1.5)) and (((lo-ll)>=0.02 and (lh-lc)>=0.02 and ((pc-pl)>=0.02 or (ph-po)>=0.02)) or ((pc-pl)>=0.02 and (ph-po)>=0.02 and ((lo-ll)>=0.02 or (lh-lc)>=0.02)))):
        print('Bullish Engulfing')

    elif ((lc-lo)<=((lh-ll)/2.5) and (lc-lo)>=((lh-ll)/6) and lc>=(((lh+ll)/2)+((lh-ll)/4)) and (lo*1.05)>=((lh+ll)/2)):
        print("Right Hammer")

    elif ((lc-lo)<=((lh-ll)/2.5) and lc<=(((lh+ll)/2)*1.05) and lo<=(((lh+ll)/2)-((lh-ll)/4)) and (lc-lo)>=((lh-ll)/6)):
        print('Inverted hammer')

    elif((lc-lo)<((lh-ll)/2) and (lc-lo)>((lh-ll)/4) and lo>=(((lh+ll)/2)-((lh-ll)/4)) and lc<=(((lh+ll)/2)+((lh-ll)/4))):
        print('Spinning Top')

    elif ((lc-lo)<=((lh-ll)/4) and lc>=(((lh+ll)/2)+((lh-ll)/4.4)) and lo>((lh+ll)/2)):
        print('Dragonfly doji')

    elif ((lc-lo)<=((lh-ll)/4) and lo<=(((lh+ll)/2)-((lh-ll)/4.4))and lc<((lh+ll)/2)):
        print('Gravestone Doji')

    elif ((lc-lo)<=((lh-ll)/4) and lo>(((lh+ll)/2)-((lh-ll)/4.4)) and lc<(((lh+ll)/2)+((lh-ll)/4.4))):
        print('Simple Doji')

    elif(((lo-ll)<(((lh-lc)+((lh-lc)*0.02)))) and ((lo-ll) > ((lh-lc)-((lh-lc)*0.02))) and ((lh-lc)<(((lo-ll)+((lo-ll)*0.02)))) and ((lh-lc) > ((lo-ll)-((lo-ll)*0.02)))):
        print('Reversal')
    # Next candle is ki body ka half ko cut kar da to trade cut kar deni ha

    # Try karna ha k kisi bhi trade ko moving average ka nazdeeq cut krein

    elif(pc<po and lc>(((po+pc)/2)+((po-pc)/8)) and lc<(po-((po-pc)*0.10)) and pc!=pl and po!=ph and lo!=ll and lc!=lh):
        print('Bullish Marubuzu')

elif(lc<lo):
    print('Bearish candle')
    if (pc>po and lc<po and (lo<=pc or lo>=pc) and (lh>ph or ll<pl) and ((lo-lc)<((pc-po)*1.5)) and (((lc-ll)>=0.02 and (lh-lo)>=0.02 and ((po-pl)>=0.02 or (ph-pc)>=0.02)) or ((po-pl)>=0.02 and (ph-pc)>=0.02 and ((lc-ll)>=0.02 or (lh-lo)>=0.02)))):
        print('Bearish Engulfing')
    
    elif ((lo-lc)<=((lh-ll)/2.5) and (lo-lc)>=((lh-ll)/6) and (lc*1.05)>=((lh+ll)/2) and lo>=(((lh+ll)/2)+((lh-ll)/4))):
        print("Right Hammer")

    elif ((lo-lc)<=((lh-ll)/2.5) and (lo-lc)>=((lh-ll)/6) and lc<=(((lh+ll)/2)-((lh-ll)/4)) and lo<=(((lh+ll)/2)*1.05)):
        print('Inverted hammer')

    elif((lo-lc)<((lh-ll)/2) and (lo-lc)>((lh-ll)/4) and lc>=(((lh+ll)/2)-((lh-ll)/4)) and lo<=(((lh+ll)/2)+((lh-ll)/4))):
        print('Spinning Top')

    elif ((lo-lc)<=((lh-ll)/4) and lo>=(((lh+ll)/2)+((lh-ll)/4.4))and lc>((lh+ll)/2)):
        print('Dragonfly doji')

    elif ((lo-lc)<=((lh-ll)/4) and lc<=(((lh+ll)/2)-((lh-ll)/4.4))and lo<((lh+ll)/2)):
        print('Gravestone Doji')

    elif((lo-lc)<=((lh-ll)/4) and lc>(((lh+ll)/2)-((lh-ll)/4.4)) and lo<(((lh+ll)/2)+((lh-ll)/4.4))):
        print('Simple Doji')

    elif(((lc-ll)<(((lh-lo)+((lh-lo)*0.02)))) and ((lc-ll) > ((lh-lo)-((lh-lo)*0.02))) and ((lh-lo)<(((lc-ll)+((lc-ll)*0.02)))) and ((lh-lo) > ((lc-ll)-((lc-ll)*0.02)))):
        print('Reversal')

    elif(pc>po and lc<((pc+po)/2) and lc>(po+((pc-po)*0.15))):
        print('Bearish Marubuzu')

elif(lc==lo):
    print('Doji')
    if(lc>=(((lh+ll)/2)+((lh-ll)/4.4))):
        print('Dragonfly doji')

    elif(lc<=(((lh+ll)/2)-((lh-ll)/4.4))):
        print('Gravestone doji')

    else:
        print('Simple Doji')


ema_50 = EMAIndicator(close=df['Close'], window=50).ema_indicator()
recent_ema = ema_50.dropna().iloc[-1]
print(recent_ema)

ema_21 = EMAIndicator(close=df['Close'], window=21).ema_indicator()
buy_ema = ema_21.dropna().iloc[-1]
print(buy_ema)

print(buy_ema-recent_ema)


upper_ema = recent_ema + (recent_ema * 0.00075)
lower_ema = recent_ema - (recent_ema * 0.00075)
print(upper_ema)
print(lower_ema)

print(lo-ll)
print(lh-lc)
        