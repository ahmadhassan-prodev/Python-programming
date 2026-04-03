# Function is same like java but syntax is different

def sayHello(name):
    print('Hello',name)

def add(a,b):
    c = a + b
    return c


sayHello('Ahmad')
print(add(5,10))

# * is used to enter list and ** is used to enter dictionary

def Value(*a,**b):
    print(a)
    print(b)

names = ['Ahmad','Hassan']
details = {'Name':'Ahmad','Age':21}

Value(*names,**details)