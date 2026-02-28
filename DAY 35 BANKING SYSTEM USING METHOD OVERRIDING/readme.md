# Day 36 - Method Overriding in Python 🐍

Today I practiced **Method Overriding** using a simple Banking System example.

## 📌 Concept

Method Overriding allows a child class to provide its own implementation of a method that is already defined in the parent class.

It helps achieve:
- Runtime Polymorphism
- Flexible Code
- Clean OOP Structure

---

## 💻 Practice Task: Banking System

### Base Class:
- BankAccount → calculate_interest()

### Child Classes:
- SavingsAccount → 6% interest
- CurrentAccount → 3% interest

---

## 🔎 Code

```python
class BankAccount:
    def calculate_interest(self):
        print("Calculating generic bank interest")


class SavingsAccount(BankAccount):
    def calculate_interest(self):
        print("Savings account interest is 6%")


class CurrentAccount(BankAccount):
    def calculate_interest(self):
        print("Current account interest is 3%")


b = BankAccount()
s = SavingsAccount()
c = CurrentAccount()

b.calculate_interest()
s.calculate_interest()
c.calculate_interest()