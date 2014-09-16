"""

File Name: Ch2_Ex22.py
Developer: Justin A. Shores
Date Last Modified: Tue Sep  2 20:35:55 PDT 2014
Description: Create a program that prompts for a positive number greater than 2 (check this
    condition) and then keeps taking the square root of this number until the square root
    is less than 2. Print the value each time the square root is taken, along with the number
    of times the operation has been completed

"""
import math

# prompt for number > 2 & check
while True:
    number_str = input("Enter a positive number bigger than 2: ")
    number_float = float(number_str)
    if number_float > 2:
        break
    else:
        continue

# take square roots as long as number is > 2 & print
count = 0
while number_float >= 2:
    number_float = math.sqrt(number_float)
    count += 1
    print(count, ": {0:.2f}".format(number_float))
