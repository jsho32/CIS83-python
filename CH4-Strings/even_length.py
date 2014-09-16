"""

File Name: even_length.py
Developer: Justin A. Shores
Date Last Modified: Tue Sep 16 12:33:41 PDT 2014
Description: Given a variable S containing a string of even length:
        (a) Write an expression to print out the first half of the string.
        (b) Write an expression to print out the second half of the string.

"""
# set string
s = "1234567890"

# print first half part (a)
print("The firt half is: {}".format(s[:int(len(s)/2)]))

# print second half part (b)
print("The second half is: {}".format(s[int(len(s)/2):]))
