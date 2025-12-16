class Bank:
    def __init__(self, balance):
        self.__balance = balance  # private

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount > 0:
            self.__balance = amount
        else:
            print("Invalid amount")

b = Bank(5000)
print(b.get_balance())
b.set_balance(9000)
print(b.get_balance())
