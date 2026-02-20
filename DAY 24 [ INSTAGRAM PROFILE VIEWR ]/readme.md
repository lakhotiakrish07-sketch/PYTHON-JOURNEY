# Instagram Profile Viewer (Getter Only)

This is a beginner-friendly Python mini project created to understand the concept of **getters** and **encapsulation** using Object-Oriented Programming.

The project simulates an Instagram profile where user data can be viewed but not modified.

## Features
- View username
- View followers count
- View following count
- View bio
- Read-only access (no setters used)

## Concepts Used
- Python classes and objects
- Constructors (`__init__`)
- Protected variables using underscore (`_`)
- Getter methods using `@property`
- Encapsulation

## Project Structure
- `Instaprofile` class stores profile data
- Internal variables are protected
- Getter methods provide controlled access to data

## Example Usage

```python
user = Instaprofile(190, 71, "krish lakhotia", "hi i am a coder")

print(user.followers)
print(user.following)
print(user.username)
print(user.bio)
