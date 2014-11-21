"""
File Name: Ch2_Ex1.py
Developer: Justin A. Shores
Date Last Modified: 09/02/2014
Description: Write a program that prints all 3 digit numbers divisible by 17
"""

# Program
print("Here are all the 3 digit numbers that are divisible by 17")

# count numbers
int_count = 0

# cycle through 3 digit numbers checking divisibility (print and add count)
for x in range(100, 1000):
	if ((x % 17) == 0):
		print(x)
		int_count = int_count + 1

# format and print total amount of numbers divisible by 3
str_count = "There are " + str(int_count) + " three digit numbers divisible by 17"
print(str_count)
