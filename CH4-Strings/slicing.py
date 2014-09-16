"""

File Name: slicing.py
Developer: Justin A. Shores
Date Last Modified: Tue Sep 16 14:38:10 PDT 2014
Description: Given the string 'abcdefghij' , write a single line of code that will print the
following (Hint: Slicing is your friend):
        (a) 'jihgfedcba'
        (b) 'adgj'
        (c) 'igeca'

"""

# given string
my_str = "abcdefghij"

# single line to print all that
print("(a) '{}'\n(b) '{}'\n(c) '{}'".format(my_str[::-1],my_str[::3],my_str[-2::-2]))
