"""

File Name: Ch2_Ex25.py
Developer: Justin A. Shores
Date Last Modified: Tue Sep  2 21:04:32 PDT 2014
Description: Find the two-digit number such that when you square it,
     the resulting three-digit number has its rightmost two digits the same as
     the original two-digit number. That is, for a number in the 
     form AB, AB*AB = CAB for some C.
     (Note to developer: check for 25 * 25 = 625)

"""
# get squares of two digit numbers
for x in range(10, 99):
    squared = x ** 2
    if (squared % 100) == x and squared < 1000:
        print("Solution:", x, "*", x, "=", squared)
