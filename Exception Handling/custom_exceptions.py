class InsufficientBalanceError(Exception):
    pass

class ATMAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient funds!")
        self.balance -= amount
        print(f"{amount} withdrawn, remaining balance {self.balance}")

try:
    account = ATMAccount(5000)
    account.withdraw(6000)
except Exception as e:
    print("Error:", e)
