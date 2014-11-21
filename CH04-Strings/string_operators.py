"""

File Name: string_operators.py
Developer: Justin A. Shores
Date Last Modified: Tue Sep 16 14:08:17 PDT 2014
Description: (String operators)
(a) Suppose you want to print a line full of '#' characters. For simplicity, let’s say that a
line can have only 80 characters. One way is to create a long string to be printed. How
would you do it more elegantly in Python using the plus operation (+) of strings?
(b) Suppose you want to print a column full of '#' characters. For simplicity, let’s
say that a column could have only 30 characters. Similar to (a), how would you do
it more elegantly in Python using the mulitply operation (*) of strings? Hint: Use
the newline character (‘\n’).

"""

# (a) you could use a loop that iterates 80 times adding (+) "#" each time
my_str = ""
for x in range(0,80):
    my_str += "#"
    
print("80 # string: \n{}".format(my_str))

# (b) use (*) to replicate the string + \n 30 times
col_str = "#"
print("Here's a ridiculous column:\n{}".format((col_str + "\n") * 30))
