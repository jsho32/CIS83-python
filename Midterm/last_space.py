"""

File Name: last_space.py
Developer: Justin A. Shores
Date Last Modified: Wed Oct 15 16:54:24 PDT 2014
Description: Demonstrate how you would find the last space in a string.

"""

# Assuming that space literally means " ", we can do this in many ways
my_str = "This is a string that I have written."
print(my_str)

# We could use a loop and find " "'s while they exist
new_str = my_str
index = -1
while " " in new_str:
    # find index of each space adding it to index
    index += new_str.find(" ") + 1
    # cut string from space to end
    new_str = new_str[new_str.find(" ")+1:]

print("\nUsing loops to find spaces: ")
print("The index of the last space in the string is:", index)
print("Everything after the last space is:", new_str)

# we could also use the rsplit() function to split the string at the last " "
split_str = my_str.rsplit(" ", 1)
print("\nUsing right split function to find last space: ")
print("Everything before the last space is:", split_str[0])
print("Everything after the last space is:", split_str[1])
print("The index of the last space in the string is:", len(split_str[0]))
