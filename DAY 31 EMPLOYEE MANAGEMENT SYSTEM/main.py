# Day 31 Mini Project
# Employee Management System

class Employee:
    company_name = "SparkTech Pvt Ltd"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Company: {Employee.company_name}")
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print("-" * 30)

    # Alternative Constructor
    @classmethod
    def from_string(cls, data):
        name, salary = data.split("-")
        return cls(name, int(salary))


# Normal object creation
emp1 = Employee("Rahul", 40000)
emp1.display()

# Object creation using alternative constructor
emp2 = Employee.from_string("Krish-50000")
emp2.display()
