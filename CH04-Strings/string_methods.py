"""

File Name: string_methods.py
Developer: Justin A. Shores
Date Last Modified: Tue Sep 16 13:41:56 PDT 2014
Description: Five string methods manipulate case: capitalize , title ,
        swapcase , upper , and lower . Consider the strings: 
        s1 = "concord" , s2 = "souix city" , s3 ="HONOLULU" , and 
        s4 = "TopHat".
        (a)Describe what capitalize does.
        (b)Describe what swapcase does.
        (c)Describe what upper does.
        (d)Describe what lower does.
        (e)Describe what title does.

"""
# set strings
s1, s2, s3, s4 = "concord", "souix city", "HONOLULU", "TopHat"

# (a) capitalize will make the first char of the string uppercase
print("capitalize: {}".format(s2.capitalize()))

# (b) swapcase will turn existing uppercase into lowercase and visa versa
print("swapcase: {}".format(s4.swapcase()))

# (c) upper makes all chars in the string uppercase
print("upper: {}".format(s1.upper()))

# (d) lower makes all chars in the string lowercase
print("lower: {}".format(s3.lower()))

# (e) title will make the first char of each word in the string uppercase
print("title: {}".format(s2.title()))
