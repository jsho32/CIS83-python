"""

File Name: monty_python.py
Developer: Justin A. Shores
Date Last Modified: Tue Sep 16 12:05:51 PDT 2014
Description: Given the string "Monty Python " :
        (a) Write an expression to print the first character.
        (b) Write an expression to print the last character.
        (c) Write an expression inculding len to print the last character.
        (d) Write an expression that prints " Monty ".

"""
# set string
monty_str = "Monty Python"
print("The String is: ", monty_str)

# first char part (a)
print("The first character is: ", monty_str[0])

# last char part (b)
print("The last character is: ", monty_str[-1])

# include len to print last char part (c)
print("The last character is: ",monty_str[len(monty_str) - 1])

# prints 'Monty' part (d)
print("The first word is: ", monty_str[0:5])

