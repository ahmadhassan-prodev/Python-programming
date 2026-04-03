
def is_bullish(candle):
    if(candle[3]>candle[0]):
        return True
    else:
        return False



name ='Ahmad Hassan'
age = 21
starting_capital = 34
currently_trading = True

btc_prices = [57000, 57300, 56900, 57500, 56800]

recent = 0
for i in range(len(btc_prices)):
    print(btc_prices[i])
    if(btc_prices[i]>recent):
        print('Price is higher than previous price')
    else:
        print("Price is lower than previous price")
    recent = btc_prices[i]

candle = [104, 108, 101, 107] 
print(is_bullish(candle))

