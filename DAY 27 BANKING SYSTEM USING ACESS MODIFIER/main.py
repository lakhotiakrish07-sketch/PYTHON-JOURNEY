class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name              # Public
        self._account_number = account_number   # Protected
        self.__balance = balance      # Private

    def deposit(self, amount):
        self.__balance += amount
        print("Amount Deposited Successfully")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance

acc1 = BankAccount("Krish", 12345, 5000)

acc1.deposit(1000)
acc1.withdraw(2000)

print("Current Balance:", acc1.get_balance())

print("Name:", acc1.name)  # Public works
print("Account Number:", acc1._account_number)  # Possible but not recommended
# print(acc1.__balance)Should give error
