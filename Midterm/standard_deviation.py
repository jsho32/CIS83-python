"""

File Name: standard_deviation.py
Developer: Justin A. Shores
Date Last Modified: Wed Oct 15 17:39:26 PDT 2014
Description: implement the average, squarelist, and delta list to find 
    the standard deviation of the list that is included in the program

"""
# included list of numbers: 1, 3, 4, 6, 9, 19

import math
def average(the_list):
    list_sum = 0
    list_count = 0
    for number in the_list:
        list_sum += number
        list_count += 1
    list_average = list_sum / list_count
    return list_average

# return a list of numbers that equal : (each list item - the mean)
def deltalist(the_list,a):
    delta_list = []
    for number in the_list:
        delta_list.append(number-a)
    return delta_list

# return a list of numbers that equal : (each list item squared)
def squarelist(the_list):
    squared_list = []
    for number in the_list:
        squared_list.append(number ** 2)
    return squared_list

# return a list of numbers that equal : ((each list item - mean) squared)
def variance(the_list,mean):
    return squarelist(deltalist(the_list,mean))

# return the standard deviation of a list
def stddev(l):
    a = average(l)
    l3 = variance(l,a)
    return math.sqrt(sum(l3)/(len(l3) - 1))

lst = [1,3,4,6,9,19]
print("This is the given list:", str(lst))
print("The standard deviation of the list is:", stddev(lst))
#the answer should be roughly 6.48
