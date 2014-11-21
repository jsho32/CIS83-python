"""

File Name: count_method.py
Developer: Justin A. Shores
Date Last Modified: Tue Sep 16 13:57:26 PDT 2014
Description: Experiment with the count method. What does it count?
        For example,
        some string = "Hello world!"
        some string.count("o")

"""
# count() iterates through the string and records how many times it finds a defined sequence
my_str = "How many letter 'e's does this sentence have?"
print("The sentence has {} letter 'e's.".format(my_str.count("e")))
print("It also has {} 'er's.".format(my_str.count("er")))
