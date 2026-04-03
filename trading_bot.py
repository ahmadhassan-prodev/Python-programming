from binance.client import Client
import pandas as pd
import time
from datetime import datetime, timedelta
from ta.trend import EMAIndicator

api_key = '5a3Tq6sEdSYhw7rwOms6QTufF6C3COyOkb7ruy7DpqB7jLsJFdeUTUl2kIm9Id0E'
api_secret = 'wW4YMB0qXDCccGvqih3BjFF8SEPvwPjgHJ8IGphIZ1O0uZyPYWTzNS5V20UjbCGX'

# Connect Bot with Binance Api
client = Client(api_key,api_secret)
# client.API_URL = 'https://testnet.binance.vision/api'

# ------------------------------------------------------------------------------------------------------------------------

# Check Available USDT
def check_usdt():
    balance = client.get_asset_balance(asset='USDT')
    return(balance['free'])

# ------------------------------------------------------------------------------------------------------------------------

# Fetch candles data
def get_15min_candles():
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
    return df

# ------------------------------------------------------------------------------------------------------------------------
# Fetch candles data
def get_1hour_candles():
    candles = client.get_klines(
    symbol='SOLUSDT',
    interval = Client.KLINE_INTERVAL_1HOUR,
    limit = 200
    )
    df = pd.DataFrame(candles)[[0,1,2,3,4,5]]
    df.columns = ['Open Time','Open', 'High', 'Low', 'Close', 'Volume']
    df['Open Time'] = pd.to_datetime(df['Open Time'], unit='ms')
    df['Open Time'] = df['Open Time'].dt.tz_localize('UTC').dt.tz_convert('Asia/Karachi')
    df[['Open', 'High', 'Low', 'Close']] = df[['Open', 'High', 'Low', 'Close']].astype(float)
    return df

# ------------------------------------------------------------------------------------------------------------------------

def detect_candlestick_pattern(df):
    # Get details about last complete candle
    c = 1
    last_candle = df.iloc[-c]
    lo = last_candle['Open']
    lc = last_candle['Close']
    lh = last_candle['High']
    ll = last_candle['Low']

    # Second Last candle
    previous_candle = df.iloc[-(c+1)]
    po = previous_candle['Open']
    pc = previous_candle['Close']
    ph = previous_candle['High']
    pl = previous_candle['Low']

    print(previous_candle)
    print(last_candle)

    if (lc>lo):
        if (pc<po and lc>po and (lo<=pc or lo>=pc) and (lh>ph or ll<pl) and ((lc-lo)<((po-pc)*1.5)) and (((lo-ll)>=0.02 and (lh-lc)>=0.02 and ((pc-pl)>=0.02 or (ph-po)>=0.02)) or ((pc-pl)>=0.02 and (ph-po)>=0.02 and ((lo-ll)>=0.02 or (lh-lc)>=0.02)))):
            return('Bullish Engulfing')

        elif ((lc-lo)<=((lh-ll)/2.5) and (lc-lo)>=((lh-ll)/6) and lc>=(((lh+ll)/2)+((lh-ll)/4)) and (lo*1.05)>=((lh+ll)/2)):
            return("Right Hammer")

        elif ((lc-lo)<=((lh-ll)/2.5) and lc<=(((lh+ll)/2)*1.05) and lo<=(((lh+ll)/2)-((lh-ll)/4)) and (lc-lo)>=((lh-ll)/6)):
            return('Inverted hammer')

        elif((lc-lo)<((lh-ll)/2) and (lc-lo)>((lh-ll)/4) and lo>=(((lh+ll)/2)-((lh-ll)/4)) and lc<=(((lh+ll)/2)+((lh-ll)/4))):
            return('Spinning Top')

        elif ((lc-lo)<=((lh-ll)/4) and lc>=(((lh+ll)/2)+((lh-ll)/4.4)) and lo>((lh+ll)/2)):
            return('Dragonfly doji')

        elif ((lc-lo)<=((lh-ll)/4) and lo<=(((lh+ll)/2)-((lh-ll)/4.4))and lc<((lh+ll)/2)):
            return('Gravestone Doji')

        elif ((lc-lo)<=((lh-ll)/4) and lo>(((lh+ll)/2)-((lh-ll)/4.4)) and lc<(((lh+ll)/2)+((lh-ll)/4.4))):
            return('Simple Doji')
        
        elif(pc<po and lc>(((po+pc)/2)+((po-pc)/8)) and lc<(po-((po-pc)*0.15)) and pc!=pl and po!=ph and lo!=ll and lc!=lh):
            return('Bullish Marubuzu')

        elif(((lo-ll)<(((lh-lc)+((lh-lc)*0.02)))) and ((lo-ll) > ((lh-lc)-((lh-lc)*0.02))) and ((lh-lc)<(((lo-ll)+((lo-ll)*0.02)))) and ((lh-lc) > ((lo-ll)-((lo-ll)*0.02)))):
            return('Reversal')
        # Next candle is ki body ka half ko cut kar da to trade cut kar deni ha

        else:
            return 'None'

    elif(lc<lo):
        if (pc>po and lc<po and (lo<=pc or lo>=pc) and (lh>ph or ll<pl) and ((lo-lc)<((pc-po)*1.5)) and (((lc-ll)>=0.02 and (lh-lo)>=0.02 and ((po-pl)>=0.02 or (ph-pc)>=0.02)) or ((po-pl)>=0.02 and (ph-pc)>=0.02 and ((lc-ll)>=0.02 or (lh-lo)>=0.02)))):
            return('Bearish Engulfing')
        
        elif ((lo-lc)<=((lh-ll)/2.5) and (lo-lc)>=((lh-ll)/6) and (lc*1.05)>=((lh+ll)/2) and lo>=(((lh+ll)/2)+((lh-ll)/4))):
            return("Right Hammer")

        elif ((lo-lc)<=((lh-ll)/2.5) and (lo-lc)>=((lh-ll)/6) and lc<=(((lh+ll)/2)-((lh-ll)/4)) and lo<=(((lh+ll)/2)*1.05)):
            return('Inverted hammer')

        elif((lo-lc)<((lh-ll)/2) and (lo-lc)>((lh-ll)/4) and lc>=(((lh+ll)/2)-((lh-ll)/4)) and lo<=(((lh+ll)/2)+((lh-ll)/4))):
            return('Spinning Top')

        elif ((lo-lc)<=((lh-ll)/4) and lo>=(((lh+ll)/2)+((lh-ll)/4.4))and lc>((lh+ll)/2)):
            return('Dragonfly doji')

        elif ((lo-lc)<=((lh-ll)/4) and lc<=(((lh+ll)/2)-((lh-ll)/4.4))and lo<((lh+ll)/2)):
            return('Gravestone Doji')

        elif((lo-lc)<=((lh-ll)/4) and lc>(((lh+ll)/2)-((lh-ll)/4.4)) and lo<(((lh+ll)/2)+((lh-ll)/4.4))):
            return('Simple Doji')
        
        elif(pc>po and lc<(((po+pc)/2)-((po-pc)/8)) and lc>(po+((pc-po)*0.15)) and pc!=ph and po!=pl and lo!=lh and lc!=ll):
            return('Bearish Marubuzu')

        elif(((lc-ll)<(((lh-lo)+((lh-lo)*0.02)))) and ((lc-ll) > ((lh-lo)-((lh-lo)*0.02))) and ((lh-lo)<(((lc-ll)+((lc-ll)*0.02)))) and ((lh-lo) > ((lc-ll)-((lc-ll)*0.02)))):
            return('Reversal')
        
        else:
            return 'None'

    elif(lc==lo):
        if(lc>=(((lh+ll)/2)+((lh-ll)/4.4))):
            return('Dragonfly doji')

        elif(lc<=(((lh+ll)/2)-((lh-ll)/4.4))):
            return('Gravestone doji')

        else:
            return('Simple Doji')
        
# ------------------------------------------------------------------------------------------------------------------------
            
def candle_type(df):
    last_candle = df.iloc[-1]
    lo = last_candle['Open']
    lc = last_candle['Close']
    lh = last_candle['High']
    ll = last_candle['Low']

    if(lc>lo):
        return 'Bullish candle'
    elif(lc<lo):
        return 'Bearish candle'
    else:
        return 'Doji'
    
# ------------------------------------------------------------------------------------------------------------------------
def sleep_until_next_15min():
    now = datetime.now()
    next_15min = (now + timedelta(minutes=15 - now.minute % 15)).replace(second=0, microsecond=0)
    sleep_time = (next_15min - now).total_seconds()
    time.sleep(sleep_time)
    return next_15min
    
# ------------------------------------------------------------------------------------------------------------------------
def ema_check(df):
    ema_50 = EMAIndicator(close=df['Close'], window=50).ema_indicator()
    recent_ema = ema_50.dropna().iloc[-1]
    return recent_ema

# ------------------------------------------------------------------------------------------------------------------------
def ema_buy_check(df):
    ema_21 = EMAIndicator(close=df['Close'], window=21).ema_indicator()
    buy_ema = ema_21.dropna().iloc[-1]
    return buy_ema

# ------------------------------------------------------------------------------------------------------------------------
def ema_last(df):
    ema_l = EMAIndicator(close=df['Close'], window=95).ema_indicator()
    ema_la = ema_l.dropna().iloc[-1]
    return ema_la

# ------------------------------------------------------------------------------------------------------------------------
def trend_check(df):
    c = 1
    last_candle = df.iloc[-c]
    lo = last_candle['Open']
    lc = last_candle['Close']
    lh = last_candle['High']
    ll = last_candle['Low']

    # Second Last candle
    previous_candle_1 = df.iloc[-(c+1)]
    po1 = previous_candle_1['Open']
    pc1 = previous_candle_1['Close']
    ph1 = previous_candle_1['High']
    pl1 = previous_candle_1['Low']

    
    # 3rd Last candle
    previous_candle_2 = df.iloc[-(c+2)]
    po2 = previous_candle_2['Open']
    pc2 = previous_candle_2['Close']
    ph2 = previous_candle_2['High']
    pl2 = previous_candle_2['Low']

    # 4th Last candle
    previous_candle_3 = df.iloc[-(c+3)]
    po3 = previous_candle_3['Open']
    pc3 = previous_candle_3['Close']
    ph3 = previous_candle_3['High']
    pl3 = previous_candle_3['Low']
    
    # 5th Last candle
    previous_candle_4 = df.iloc[-(c+4)]
    po4 = previous_candle_4['Open']
    pc4 = previous_candle_4['Close']
    ph4 = previous_candle_4['High']
    pl4 = previous_candle_4['Low']
    
    # 6th Last candle
    previous_candle_5 = df.iloc[-(c+5)]
    po5 = previous_candle_5['Open']
    pc5 = previous_candle_5['Close']
    ph5 = previous_candle_5['High']
    pl5 = previous_candle_5['Low']

    count = 0
    if (pc5<po5):
        count = count + 1
    if (pc4<po4):
        count = count + 1
    if (pc3<po3):
        count = count + 1
    if (pc2<po2):
        count = count + 1
    if (pc1<po1):
        count = count + 1

    if((pc2<po2 and pc1<po1) or (count>3)):
        if(lc>lo and ll<pc1):
            return 'Down_trend'
        elif(lc<lo and ll<pl1):
            return 'Down_trend'
        elif(lc==lo and ll<pl1):
            return 'Down_trend'
        
    elif((pc2>po2 and pc1>po1) or (count<2)):
        if(lc>lo and lh>ph1):
            return 'Up_trend'
        elif(lc==lo and lh>ph1):
            return 'Up_trend'
        elif(lc<lo and lh>pc1): 
            return 'Up_trend'
        
    else:
        return 'No_trend'

# ------------------------------------------------------------------------------------------------------------------------
# Main Program
while (True):
    try:
        next_15min = sleep_until_next_15min()

        df = get_15min_candles()
        candle_Typ = candle_type(df)
        candle = detect_candlestick_pattern(df)
        ema = ema_check(df)
        ema_buy = ema_buy_check(df)
        ema_100 = ema_last(df)
        upper_ema_diff = ema_buy-ema
        lower_ema_diff = ema-ema_buy
        trend = trend_check(df)
        upper_ema = ema_check(df) + (ema_check(df) * 0.00075)
        lower_ema = ema_check(df) - (ema_check(df) * 0.00075)
        upper_exceed_ema = ema_check(df) + (ema_check(df) * 0.0015)
        lower_exceed_ema = ema_check(df) - (ema_check(df) * 0.0015)

        last_candle = df.iloc[-1]
        lo = last_candle['Open']
        lc = last_candle['Close']
        lh = last_candle['High']
        ll = last_candle['Low']

        previous_candle = df.iloc[-2]
        po = last_candle['Open']
        pc = last_candle['Close']
        ph = last_candle['High']
        pl = last_candle['Low']

        previous_candle = df.iloc[-3]
        po2 = last_candle['Open']
        pc2 = last_candle['Close']
        ph2 = last_candle['High']
        pl2 = last_candle['Low']

        print(candle_Typ)
        print(candle)
        print(ema_check(df))
        print(upper_ema)
        print(lower_ema)
        print(upper_exceed_ema)
        print(lower_exceed_ema)
        print(trend_check(df))

        # if(trade == 'now_buy'):
        # elif(trade == 'now_sell'):

        # For buy order
        if(candle == 'Bullish Engulfing' and candle_Typ == 'Bullish candle' and trend == 'Down_trend'):
            if(ema_buy<ema and lower_ema_diff>0.20):
                print('Buy Signal')
            elif(ema_buy>ema and upper_ema_diff>0.20):
                if((pl>lower_ema and pl<=upper_exceed_ema) or (ll>lower_ema and ll<=upper_exceed_ema)):
                    print('Buy Signal')
                elif((ema_buy>pl and ema_buy<ph) or (ema_buy>ll and ema_buy<lh)):
                    print('Buy signal')

        elif(candle == 'Right Hammer' and candle_Typ == 'Bullish candle' and trend == 'Down_trend'):
            if(ema_buy<ema and lower_ema_diff>0.20):
                print('Buy Signal')
            elif(ema_buy>ema and upper_ema_diff>0.20):
                if(ll>lower_ema and ll<=upper_exceed_ema):
                    print('Buy Signal')
                elif(ema_buy>ll and ema_buy<lh):
                    print('Buy Signal')

        elif(candle == 'Inverted hammer' and candle_Typ == 'Bullish candle' and trend == 'Down_trend'):
            if(ema_buy<ema and lower_ema_diff>0.20):
                print('Buy Signal')
            elif(ema_buy>ema and upper_ema_diff>0.20):
                if(ll>lower_ema and ll<=upper_exceed_ema):
                    print('Buy Signal')
                elif(ema_buy>ll and ema_buy<lh):
                    print('Buy Signal')

        elif(candle == 'Right Hammer' and candle_Typ == 'Bearish candle' and trend == 'Down_trend'):
            if(ema_buy<ema and lower_ema_diff>0.20):
                print('Buy Signal')
            elif(ema_buy>ema and upper_ema_diff>0.20):
                if(ll>lower_ema and ll<=upper_exceed_ema):
                    print('Buy Signal')
                elif(ema_buy>ll and ema_buy<lh):
                    print('Buy Signal')

        elif(candle == 'Inverted hammer' and candle_Typ == 'Bearish candle' and trend == 'Down_trend'):
            if(ema_buy<ema and lower_ema_diff>0.20):
                print('Buy Signal')
            elif(ema_buy>ema and upper_ema_diff>0.20):
                if(ll>lower_ema and ll<=upper_exceed_ema):
                    print('Buy Signal')
                elif(ema_buy>ll and ema_buy<lh):
                    print('Buy Signal')

        elif(candle == 'Spinning Top' and (candle_Typ == 'Bullish candle' or candle_Typ == 'Bearish candle') and trend == 'Down_trend'):
            if(ema_buy<ema and lower_ema_diff>0.20):
                print('Buy Signal')
            elif(ema_buy>ema and upper_ema_diff>0.20):
                if(ll>lower_ema and ll<=upper_exceed_ema):
                    print('Buy Signal')
                elif(ema_buy>ll and ema_buy<lh):
                    print('Buy Signal')

        elif(candle == 'Dragonfly doji' and (candle_Typ == 'Bullish candle' or candle_Typ == 'Bearish candle') and trend == 'Down_trend'):
            if(ema_buy<ema and lower_ema_diff>0.20):
                print('Buy Signal')
            elif(ema_buy>ema and upper_ema_diff>0.20):
                if(ll>lower_ema and ll<=upper_exceed_ema):
                    print('Buy Signal')
                elif(ema_buy>ll and ema_buy<lh):
                    print('Buy Signal')

        elif(candle == 'Gravestone Doji' and (candle_Typ == 'Bullish candle' or candle_Typ == 'Bearish candle') and trend == 'Down_trend'):
            if(ema_buy<ema and lower_ema_diff>0.20):
                print('Buy Signal')
            elif(ema_buy>ema and upper_ema_diff>0.20):
                if(ll>lower_ema and ll<=upper_exceed_ema):
                    print('Buy Signal')
                elif(ema_buy>ll and ema_buy<lh):
                    print('Buy Signal')

        elif(candle == 'Simple Doji' and (candle_Typ == 'Bullish candle' or candle_Typ == 'Bearish candle') and trend == 'Down_trend'):
            if(ema_buy<ema and lower_ema_diff>0.20):
                print('Buy Signal')
            elif(ema_buy>ema and upper_ema_diff>0.20):
                if(ll>lower_ema and ll<=upper_exceed_ema):
                    print('Buy Signal')
                elif(ema_buy>ll and ema_buy<lh):
                    print('Buy Signal')

        elif(candle == 'Dragonfly doji' and candle_Typ == 'Doji' and trend == 'Down_trend'):
            if(ema_buy<ema and lower_ema_diff>0.20):
                print('Buy Signal')
            elif(ema_buy>ema and upper_ema_diff>0.20):
                if(ll>lower_ema and ll<=upper_exceed_ema):
                    print('Buy Signal')
                elif(ema_buy>ll and ema_buy<lh):
                    print('Buy Signal')

        elif(candle == 'Gravestone Doji' and candle_Typ == 'Doji' and trend == 'Down_trend'):
            if(ema_buy<ema and lower_ema_diff>0.20):
                print('Buy Signal')
            elif(ema_buy>ema and upper_ema_diff>0.20):
                if(ll>lower_ema and ll<=upper_exceed_ema):
                    print('Buy Signal')
                elif(ema_buy>ll and ema_buy<lh):
                    print('Buy Signal')

        elif(candle == 'Simple Doji' and candle_Typ == 'Doji' and trend == 'Down_trend'):
            if(ema_buy<ema and lower_ema_diff>0.20):
                print('Buy Signal')
            elif(ema_buy>ema and upper_ema_diff>0.20):
                if(ll>lower_ema and ll<=upper_exceed_ema):
                    print('Buy Signal')
                elif(ema_buy>ll and ema_buy<lh):
                    print('Buy Signal')

        elif(candle == 'Reversal' and (candle_Typ == 'Bullish candle' or candle_Typ == 'Bearish candle') and trend == 'Down_trend'):
            if(ema_buy<ema and lower_ema_diff>0.20):
                print('Buy Signal')
            elif(ema_buy>ema and upper_ema_diff>0.20):
                if(ll>lower_ema and ll<=upper_exceed_ema):
                    print('Buy Signal')
                elif(ema_buy>ll and ema_buy<lh):
                    print('Buy Signal')

        elif(candle == 'Bullish Marubuzu' and candle_Typ == 'Bullish candle' and trend == 'Down_trend'):
            if(ema_buy<ema and lower_ema_diff>0.20):
                print('Buy Signal')
            elif(ema_buy>ema and upper_ema_diff>0.20):
                if((pl>lower_ema and pl<=upper_exceed_ema) or (ll>lower_ema and ll<=upper_exceed_ema)):
                    print('Buy Signal')
                elif((ema_buy>pl and ema_buy<ph) or (ema_buy>ll and ema_buy<lh)):
                    print('Buy signal')

        elif(ema_100<ema and trend == 'Down_trend' and ema_100<=lh and ema_100>=ll):
            if(candle == 'Bullish Engulfing' and candle_Typ == 'Bullish candle'):
                print('Buy Signal')
            elif(candle == 'Right Hammer' and candle_Typ == 'Bullish candle'):
                print('Buy Signal')
            elif(candle == 'Right Hammer' and candle_Typ == 'Bearish candle'):
                print('Buy Signal')
            elif(candle == 'Inverted hammer' and candle_Typ == 'Bullish candle'):
                print('Buy Signal')
            elif(candle == 'Inverted hammer' and candle_Typ == 'Bearish candle'):
                print('Buy Signal')
            elif(candle == 'Spinning Top' and (candle_Typ == 'Bullish candle' or candle_Typ == 'Bearish candle')):
                print('Buy Signal')
            elif(candle == 'Dragonfly doji' and (candle_Typ == 'Bullish candle' or candle_Typ == 'Bearish candle' or candle_Typ == 'Doji')):
                print('Buy Signal')
            elif(candle == 'Gravestone Doji' and (candle_Typ == 'Bullish candle' or candle_Typ == 'Bearish candle' or candle_Typ == 'Doji')):
                print('Buy Signal')
            elif(candle == 'Simple Doji' and (candle_Typ == 'Bullish candle' or candle_Typ == 'Bearish candle' or candle_Typ == 'Doji')):
                print('Buy Signal')
            elif(candle == 'Reversal' and (candle_Typ == 'Bullish candle' or candle_Typ == 'Bearish candle')):
                print('Buy Signal')
            elif(candle == 'Bullish Marubuzu' and candle_Typ == 'Bullish candle'):
                print('Buy Signal')


# ------------------------------------------------------------------------------------------------------------------------

        # For Selling
        if(candle == 'Bearish Engulfing' and candle_Typ == 'Bearish candle' and trend == 'Up_trend'):
            if(ema_buy>ema and upper_ema_diff>0.20):
                print('Sell Signal')
            elif(ema_buy<ema and lower_ema_diff>0.20):
                if((ph<upper_ema and ph>=lower_exceed_ema) or (lh<upper_ema and lh>=lower_exceed_ema)):
                    print('Sell Signal')

        # elif(candle == 'Right Hammer' and candle_Typ == 'Bullish candle' and trend == 'Up_trend'):
        #     if(ema_buy<ema and lower_ema_diff>0.20):
        #         print('Buy Signal')
        #     elif(ema_buy>ema and upper_ema_diff>0.20):
        #         if(ll>lower_ema and ll<=upper_exceed_ema):
        #             print('Buy Signal')

        # elif(candle == 'Inverted hammer' and candle_Typ == 'Bullish candle' and trend == 'Up_trend'):
        #     if(ema_buy<ema and lower_ema_diff>0.20):
        #         print('Buy Signal')
        #     elif(ema_buy>ema and upper_ema_diff>0.20):
        #         if(ll>lower_ema and ll<=upper_exceed_ema):
        #             print('Buy Signal')

        # elif(candle == 'Right Hammer' and candle_Typ == 'Bearish candle' and trend == 'Up_trend'):
        #     if(ema_buy<ema and lower_ema_diff>0.20):
        #         print('Buy Signal')
        #     elif(ema_buy>ema and upper_ema_diff>0.20):
        #         if(ll>lower_ema and ll<=upper_exceed_ema):
        #             print('Buy Signal')

        # elif(candle == 'Inverted hammer' and candle_Typ == 'Bearish candle' and trend == 'Up_trend'):
        #     if(ema_buy<ema and lower_ema_diff>0.20):
        #         print('Buy Signal')
        #     elif(ema_buy>ema and upper_ema_diff>0.20):
        #         if(ll>lower_ema and ll<=upper_exceed_ema):
        #             print('Buy Signal')

        # elif(candle == 'Spinning Top' and (candle_Typ == 'Bullish candle' or candle_Typ == 'Bearish candle') and trend == 'Up_trend'):
        #     if(ema_buy<ema and lower_ema_diff>0.20):
        #         print('Buy Signal')
        #     elif(ema_buy>ema and upper_ema_diff>0.20):
        #         if(ll>lower_ema and ll<=upper_exceed_ema):
        #             print('Buy Signal')

        # elif(candle == 'Dragonfly doji' and (candle_Typ == 'Bullish candle' or candle_Typ == 'Bearish candle') and trend == 'Up_trend'):
        #     if(ema_buy<ema and lower_ema_diff>0.20):
        #         print('Buy Signal')
        #     elif(ema_buy>ema and upper_ema_diff>0.20):
        #         if(ll>lower_ema and ll<=upper_exceed_ema):
        #             print('Buy Signal')

        # elif(candle == 'Gravestone Doji' and (candle_Typ == 'Bullish candle' or candle_Typ == 'Bearish candle') and trend == 'Up_trend'):
        #     if(ema_buy<ema and lower_ema_diff>0.20):
        #         print('Buy Signal')
        #     elif(ema_buy>ema and upper_ema_diff>0.20):
        #         if(ll>lower_ema and ll<=upper_exceed_ema):
        #             print('Buy Signal')

        # elif(candle == 'Simple Doji' and (candle_Typ == 'Bullish candle' or candle_Typ == 'Bearish candle') and trend == 'Up_trend'):
        #     if(ema_buy<ema and lower_ema_diff>0.20):
        #         print('Buy Signal')
        #     elif(ema_buy>ema and upper_ema_diff>0.20):
        #         if(ll>lower_ema and ll<=upper_exceed_ema):
        #             print('Buy Signal')

        # elif(candle == 'Dragonfly doji' and candle_Typ == 'Doji' and trend == 'Up_trend'):
        #     if(ema_buy<ema and lower_ema_diff>0.20):
        #         print('Buy Signal')
        #     elif(ema_buy>ema and upper_ema_diff>0.20):
        #         if(ll>lower_ema and ll<=upper_exceed_ema):
        #             print('Buy Signal')

        # elif(candle == 'Gravestone Doji' and candle_Typ == 'Doji' and trend == 'Up_trend'):
        #     if(ema_buy<ema and lower_ema_diff>0.20):
        #         print('Buy Signal')
        #     elif(ema_buy>ema and upper_ema_diff>0.20):
        #         if(ll>lower_ema and ll<=upper_exceed_ema):
        #             print('Buy Signal')

        # elif(candle == 'Simple Doji' and candle_Typ == 'Doji' and trend == 'Up_trend'):
        #     if(ema_buy<ema and lower_ema_diff>0.20):
        #         print('Buy Signal')
        #     elif(ema_buy>ema and upper_ema_diff>0.20):
        #         if(ll>lower_ema and ll<=upper_exceed_ema):
        #             print('Buy Signal')

        # elif(candle == 'Reversal' and (candle_Typ == 'Bullish candle' or candle_Typ == 'Bearish candle') and trend == 'Up_trend'):
        #     if(ema_buy<ema and lower_ema_diff>0.20):
        #         print('Buy Signal')
        #     elif(ema_buy>ema and upper_ema_diff>0.20):
        #         if(ll>lower_ema and ll<=upper_exceed_ema):
        #             print('Buy Signal')

        # elif(candle == 'Bearish Marubuzu' and candle_Typ == 'Bearish candle' and trend == 'Up_trend'):
        #     if(ema_buy<ema and lower_ema_diff>0.20):
        #         print('Buy Signal')
        #     elif(ema_buy>ema and upper_ema_diff>0.20):
        #         if((pl>lower_ema and pl<=upper_exceed_ema) or (ll>lower_ema and ll<=upper_exceed_ema)):
        #             print('Buy Signal')
    except Exception as e:
                print("Error occurred:", e)
                print("⏳ Waiting 30 seconds before retrying...")
                time.sleep(30)
# print(check_usdt())
# for i in range(195,199):
#     for data in df:
#         print(df[data][i])
# ------------------------------------------------------------------------------------------------------------------------
# Setup for 1 hour candle
# if (next_15min.minute == 0):
#     df2 = get_1hour_candles()
#     print('1 Hour')
#     print(detect_candlestick_pattern(df2))
#     print(candle_type(df2))
#     upper_ema = ema_check(df2) + (ema_check(df2) * 0.0007)
#     lower_ema = ema_check(df2) - (ema_check(df2) * 0.0007)
#     print(ema_check(df2))
#     print(upper_ema)
#     print(lower_ema)
#     print(trend_check(df2))