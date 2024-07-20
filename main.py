import time
from cehcker import Checker
from config import address_in, address_out, amount, profit

while True:
    value = Checker(address_in, address_out, amount)
    time.sleep(1.1)
    value_2 = Checker(address_out, address_in, value)

    diff = value_2 - value

    if diff > profit:
        #arbitrage(address_in, address_out, value_2)
        print(f'Можно было бы заработать {diff}')
    else:
        pass

    

    time.sleep(1.1)
