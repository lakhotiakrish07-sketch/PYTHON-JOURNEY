# Day 33 - super() Keyword Example

class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
        print("Vehicle constructor called")

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Speed: {self.speed} km/h")


class Car(Vehicle):
    def __init__(self, brand, speed, model):
        super().__init__(brand, speed)   # Calling parent constructor
        self.model = model
        print("Car constructor called")

    def display_car(self):
        self.display_info()
        print(f"Model: {self.model}")


# Creating object
obj = Car("Toyota", 180, "Fortuner")
obj.display_car()