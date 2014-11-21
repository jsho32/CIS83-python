"""

File Name: value_error
Developer: Justin A. Shores
Date Last Modified: Tue Sep 16 13:16:08 PDT 2014
Description: The following Python statement generates this error:
        “ValueError: too many values to unpack.” Why?
        first,second = input('two space-separated numbers:')

"""
# the space counts as an input the program expected two inputs but got 3

# resolved issue as long as nubers are < 10
first,space,second = input('two space-separated numbers(0-9):')

#check
print("The numbers are: {} and {}".format(first, second))
