#!/usr/bin/env python3
"""
Exercise 1: BMI Calculator

Calculate BMI and determine health category using operators.
"""

# Write your code here
# 1. Store weight (kg) and height (m) in variables
# 2. Calculate BMI using: weight / (height ** 2)
# 3. Determine category using comparison operators
# 4. Print weight, height, BMI, and category

weight = 60
height = 1.73

bmi = (weight / (height**2))

print(bmi)

if (bmi <= 18.5):
    print("Underweight")
elif ( bmi <= 25):
    print("normalvikt")
elif (bmi <= 30 ):
    print("overweiht")
else:
    print("obese")
