class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count_of_money = 0

    def can_add(self, v):
        return self.count_of_money + v <= self.capacity

    def add(self, v):
        if self.can_add(v):
            self.count_of_money += v
            return True
        else:
            return False