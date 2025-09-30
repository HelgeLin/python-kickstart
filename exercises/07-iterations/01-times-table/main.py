#!/usr/bin/env python3
"""
Exercise 1: Times Table Generator

Generate multiplication tables using for loops.
"""

# Write your code here
# 1. Ask user for a number
# 2. Print a header for the times table
# 3. Use a for loop with range(1, 11) to generate table
# 4. Calculate and print each multiplication result

number = int(input("Skrive ett number mellan 1-10: "))

if number < 1 or number > 10:
    print("Det är inte ett number mellan 1-10")
else:
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

