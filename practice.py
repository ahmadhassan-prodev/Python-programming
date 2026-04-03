fake_candles = [
    [100, 110, 95, 105],   # Bullish
    [105, 108, 100, 104],  # Bearish
    [104, 106, 104, 104],  # Doji
    [104, 114, 106, 110],   # Bullish
    [110, 113, 105, 112],  # Bullish
    [112, 115, 107, 109],  # Bearish
    [109, 111, 103, 104],  # Bearish
    [104, 108, 107, 107],  # Bullish
    [107, 110, 104, 108]
]
bullish_candles = 0
bearish_candles = 0
for candle in fake_candles:
    if candle[0]<candle[3]:
        bullish_candles +=1
    elif candle[0]>candle[3]:
        bearish_candles +=1

print(f'Bullish candles = {bullish_candles}')
print(f'Bearish candles = {bearish_candles}')


for i in range(1,len(fake_candles)):
    pre_close = fake_candles[i-1][3]
    curr_close = fake_candles[i][3]

    if curr_close>pre_close and fake_candles[i-1][3]>fake_candles[i-1][0] and fake_candles[i][3]>fake_candles[i][0]:
        print(f'Strong uptrend found at candle {i-1} and candle {i}')


def is_support(a):
    for i in range(2,len(a)-2):
        if a[i][2]<a[i-1][2] and a[i][2]<a[i-2][2] and a[i][2]<a[i+1][2] and a[i][2]<a[i+2][2]:
            return i
    
print(f'Support found at candle {is_support(fake_candles)}')