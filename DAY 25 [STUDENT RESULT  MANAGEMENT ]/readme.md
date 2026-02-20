# Student Result Management System

This is a beginner-friendly Python mini project created to understand the concepts of:

- Getters
- Setters
- Encapsulation
- Data validation using properties
- Object-Oriented Programming (OOP)

## Project Overview

The project simulates a simple student record system where:

- Student name and roll number can be viewed.
- Marks can be accessed using a getter.
- Marks can be updated using a setter.
- Validation ensures that marks remain between 0 and 100.

The system prevents invalid data assignment and demonstrates how to protect internal variables using `_` and `@property`.

## Concepts Used

- Python classes and objects
- Constructor (`__init__`)
- Protected variables using underscore (`_variable`)
- Getter methods using `@property`
- Setter methods using `@property_name.setter`
- Input validation logic

## How It Works

- Internal data is stored in protected variables such as `_marks`.
- Public access is provided through property methods like `marks`.
- The setter ensures marks are only assigned if they are within the valid range (0–100).
- Invalid assignments are rejected with an error message.

## Example Usage

```python
s1 = Student("krish", 200, 0)

print(s1.name)
print(s1.rollnumber)
print(s1.marks)

s1.marks = 95
print(s1.marks)

s1.marks = 105   # Invalid
print(s1.marks)
