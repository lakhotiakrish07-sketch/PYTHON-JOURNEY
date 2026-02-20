# Day 32 - Understanding dir(), __dict__ and help() in Python

##  Project Overview
In this project, I learned about:
- Attributes in Python
- dir() function
- __dict__ attribute
- help() function
- Basic OOP concepts

I created a simple Player class to understand how these built-in tools work with objects.

---

##  Concepts Covered

### 1️ Attributes
Attributes are variables that belong to an object.

### 2️ dir()
Used to see all attributes and methods of an object.

### 3️ __dict__
Shows only the data stored inside an object in dictionary format.

### 4️ help()
Displays documentation of a class or object.

---

##  Code

```python
class Player:
    def __init__(self, name, level, score):
        self.name = name
        self.score = score
        self.level = level

    def display(self):
        print(f"name:{self.name}\nlevel:{self.level}\nscore:{self.score}")

p1 = Player("krish", 199, 5000)

p1.display()
print(p1.__dict__)
print(dir(p1))
help(p1)
```

---

##  What I Learned

- Difference between attributes and methods
- How Python stores object data internally
- How to inspect objects using built-in functions
- Basic OOP structure in Python

---

##  Author
Krish Lakhotia  
100 Days of Code Challenge