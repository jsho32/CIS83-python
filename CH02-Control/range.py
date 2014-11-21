"""
File Name: Ch2_Ex7.py
Developer: Justin A. Shores
Date Last Modified: 09/02/2014
Description: Consider range(a, b) are the following statements true or false
		     value of a is included in the range
		     value of b is included in the range
	   		 The answer should be a-true and b-false but here is a program that
		     proves it!
"""

# set range values
val_a = 1
val_b = 2

# boolean values for true false statements
bool_a = False
bool_b = False

# cycle range
for x in range(val_a, val_b):
	if x == val_a:
		bool_a = True

	if x == val_b:
		bool_b = True
		
# print statements as true or false
print("Statements and Answers:")
print("The value of 'a' is included in the range is: " + str(bool_a))
print("The value of 'b' is included in the range is: " + str(bool_b))
