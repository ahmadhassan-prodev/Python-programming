import json
import requests
import time
# request = '{"symbol": "ETHUSDT", "price": "2950.00", "volume": "120.5"}'

# data = json.loads(request)

# for key,value in data.items():
#     print(f'{key}:{value}')



# person = '{"name":"Ahmad", "Age":21, "Phone#":"03028890247"}'

# data2 = json.loads(person)

# for key,value in data2.items():
#     print(f'{key}:{value}')

# People = {
#     "Name":"Ahmad",
#     "Age":21,
#     "Address":"Arifwala"
# }

# json_people = json.dumps(People)
# print(type(json_people))

# print(type(data2))

# while(True):
#     url = "https://api.binance.com/api/v3/klines"
#     params = {
#         "symbol": "SOLUSDT",
#         "interval": "1s",
#         "limit": 1
#     }

#     response = requests.get(url, params=params)
#     data = response.json()

#     for canlde in data:
#         print(canlde[3])


url = "https://api.binance.com/api/v3/klines"
params = {
    "symbol": "SOLUSDT",
    "interval":"5m",
    "limit":1
}

response = requests.get(url, params=params)
data = response.json()

print(data)
# for candle in data:
#     for i in range(0,len(candle)):
#         print(candle[i])
time.sleep(10)

