# self keyword works in the same way as this in java

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')

# Inheritance
class student(person):
# constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.address = 'null'

    def set_address(self,address):
        self.address = address

    # Override display method
    def display(self):
        super().display()
        print(f'Address:{self.address}')

Ahmad = person('Ahmad Hassan',21)
Ahmad.display()

Ali = student('Ali',25)
Ali.address='Arifwala'
Ali.display()




class trade:
    def __init__(self,open_price,close_price):
        self.open_price = open_price
        self.close_price = close_price

    def is_bullish(self):
        if(self.close_price>self.open_price):
            return True
        
candle_info = trade(109,120)
print(candle_info.is_bullish())