#!/usr/bin/env python3
"""
Exercise 1: Personal Profile Builder

Create an interactive program that collects user information 
and displays a formatted profile.
"""

# Write your code here
# 1. Print a welcome message
# 2. Ask for name, age, height, and hobby using input()
# 3. Convert age to int and height to float
# 4. Calculate birth year (2024 - age)
# 5. Display formatted profile using f-strings
import time
import sys
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def skrivmaskin(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

name = input("Vad är ditt namn? ")
clear()
age = int(input("Hur gammal är du? "))
clear()
height = input ("Hur lång är du? ")
clear()
hobby = input ("Vad gillar du att göra? ")
clear()

skrivmaskin("Här är din information:\n", 0.09)
time.sleep(0.5)

skrivmaskin(f"Namn: {name} \n", 0.01)
skrivmaskin(f"Födelse år: {2025 - age} \n", 0.01)
skrivmaskin(f"Längd: {height} \n", 0.01)
skrivmaskin(f"Hobby: {hobby} \n", 0.01)