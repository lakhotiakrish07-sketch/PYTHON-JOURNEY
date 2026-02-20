Concepts Used
1. Inheritance

The Student class inherits from:

Person

Books

This shows how multiple inheritance works in Python.

2. Constructor Calling

Both parent constructors are called inside the Student class to initialize all attributes properly.

3. Methods

display() → Displays student and book details

tax() → Adds extra charge if book price is greater than 500

🏗 Project Structure
Person Class
    - name
    - rollnumber
    - year

Books Class
    - title
    - price
    - category

Student Class (inherits Person & Books)
    - display()
    - tax()

▶ Example Output

If book price is 550:

Name: krish
Roll Number: 98
Year: 2025
Title: elite codders
Price: 550
Category: skills
total price = 600

🎯 Purpose of This Project

Practice OOP concepts

Understand multiple inheritance

Learn how to call parent constructors

Build real-world structured code

🚀 Future Improvements

Add borrow limit system

Add return book feature

Use composition instead of inheritance

Add file handling for record storage

👨‍💻 Author

Krish Lakhotia
Python Learning Journey – Day 26