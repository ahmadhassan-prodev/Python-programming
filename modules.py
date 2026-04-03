# modules means libraries

import datetime
import time

today = datetime.date.today()
currentTime = time.time()

print(f'{today} and {currentTime}')

# we can also import custom module
from calculator import add

c = add(4,5)

print(c)