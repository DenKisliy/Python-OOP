from Coin.Data import CoinSide
import random

class Coin:
    def __init__(self):
        pass

    def toss_result(self):
        return CoinSide(random.randint(1, 2))

    def toss(self, count):
        my_count = 0
        while my_count < count:
            print(self.toss_result())
            my_count +=1
