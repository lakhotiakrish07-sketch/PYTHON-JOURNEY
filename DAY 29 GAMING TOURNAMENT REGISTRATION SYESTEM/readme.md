# Day 29 - Tournament Registration System

This project is a simple Python program built using Object-Oriented Programming (OOP) concepts.

It simulates a gaming tournament where players can join based on their rank.

## Concepts Used

- Class Variables
- Instance Variables
- Constructor (__init__)
- Conditional Logic
- Object Creation
- Preventing Double Registration

## Project Explanation

The `tournament` class represents a gaming tournament.

### Class Variables:
- tournament_name
- tournament_price
- membernumber (counts total joined players)

### Instance Variables:
- name
- gameid
- rank
- join (tracks if player has joined)

## Rules

- Players with rank less than 20 cannot join.
- A player cannot join twice.
- Member count increases only when a player successfully joins.

## Example Output Flow

1. Create player object
2. Call `jointournament()` method
3. Call `result()` method to display information

## Author

Krish  
Daily Python Practice Project
