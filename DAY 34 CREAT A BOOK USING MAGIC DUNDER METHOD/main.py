class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title}, Pages: {self.pages}"

    def __len__(self):
        return self.pages

    def __add__(self, other):
        return self.pages + other.pages


# Creating objects
book1 = Book("Python Basics", 200)
book2 = Book("OOP Mastery", 150)

# Using magic methods
print(book1)           # Calls __str__
print(len(book1))      # Calls __len__
print(book1 + book2)   # Calls __add__