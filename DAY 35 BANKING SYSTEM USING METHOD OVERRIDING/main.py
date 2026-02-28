class BankAccount:
    def calculate_interest(self):
        print("Calculating generic bank interest")


class SavingsAccount(BankAccount):
    def calculate_interest(self):
        print("Savings account interest is 6%")


class CurrentAccount(BankAccount):
    def calculate_interest(self):
        print("Current account interest is 3%")


# Creating objects
b = BankAccount()
s = SavingsAccount()
c = CurrentAccount()

b.calculate_interest()
s.calculate_interest()
c.calculate_interest()