"""

File Name: find_in_strings.py
Developer: Justin A. Shores
Date Last Modified: Wed Oct 15 15:01:22 PDT 2014
Description: Python Midterm:
1. Write a program that will take a string as input and will perform 
    the following functions:
        Print the number(count) of spaces in the string
        Print the number(count) of lower case letters
        Print number of punctuation marks
The program should use a function that you write. As a hint, look at the
in operator, you should then only need 1 function.

"""
# define the finding function
def find_chars(string):
    space_count = 0
    lower_count = 0
    punctuaution_count = 0
    for char in string:
        if char == " ":
            space_count += 1
        elif not char.isalpha() and not char.isdigit():
            punctuaution_count += 1
        elif char.islower():
            lower_count += 1

    print("Space count =", space_count)
    print("Punctuation count =", punctuaution_count)
    print("Lower case count =", lower_count)

# test the function
my_str = "This is... a punctuated string! It also has numbers, like 10 and 11."
print(my_str)
find_chars(my_str)
