class Bank:
    def __init__(self, balance):
        self.balance = balance

    def is_have_money(self, money):
        return self.balance >= money

    def push(self, money):
        self.balance += money
        print("Funds deposited  into the account")

    def pop(self, money):
        if self.is_have_money(money):
            self.balance -= money
            print("Funds withdrawn")
        else:
            print("Not enough money")

    def print_info(self):
        print(f"On the account: {self.balance}")

    def update_information(self):
        self.print_info()
        self.pop(12000)
        self.print_info()
        self.push(200000)
        self.print_info()
        self.pop(201000)
        self.print_info()

