class BankAccount:
    def __init__(self, holder_name, balance=0):
        self.holder_name = holder_name
        self.__balance = balance

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):
    def deposit(self):
        amount = float(input(f"{self.holder_name} deposit: "))
        self._BankAccount__balance += amount
        print(f"New balance: ${self.get_balance()}")


class BusinessAccount(SavingsAccount):
    pass


acc1 = SavingsAccount("Alice", 100)
acc2 = BusinessAccount("Bob", 500)

acc1.deposit()
acc2.deposit()
