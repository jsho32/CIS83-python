"""
File Name: Ch1_Ex9.py
Developer: Justin A. Shores
Date Last Modified: 08/27/2014
Description: Prompt for a number
 	     Take the number, add 2, multiply by 3, subtract 6, and divide by 3.
 	     Should end up with the number you started with
"""
# Get number from user
number_str = input("Enter any number: ")
number_int = int(number_str)

# specs arithmatic
number_int = ((number_int + 2) * 3 - 6) / 3
print(number_int)
