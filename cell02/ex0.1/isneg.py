#!/usr/bin/env python3
number = input("Enter a number: ").strip()
if number.startswith('-'):
    print("this number is negative.") 
elif number == "0":
    print("This number i-'both positive and negative.")
else:
    print ("This number is positive.")
