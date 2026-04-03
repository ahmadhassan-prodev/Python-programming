name = 'Ahmad Hassan'
dream = 'Become Successful'
goal_amount = 1000000

print(f'Name: {name}\nDream: {dream}\nGoal amount:{goal_amount}')


balance = 10000
if balance>5000:
    print(f'Enough to trade')
else:
    print(f'save more before trading')

candles =[
    [100, 120,  90, 110],
    [105, 115, 102, 107],
    [107, 112, 106, 106],
    [106, 120, 104, 119],
    [119, 121, 115, 116]
]

for candle in candles[-5]:
    open = candle[0],
    high = candle[1],
    low = candle[2],
    close = candle[3]

    print(f'Open:{open}\nHigh:{high}\nLow:{low}\nClose:{close}')

    if close>open:
        print('Bullish candle')
    elif close<open:
        print('Bearish candle')
    else:
        print('Doji')

