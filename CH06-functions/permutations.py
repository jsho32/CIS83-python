"""

File Name: permutations.py
Developer: Justin A. Shores
Date Last Modified: Tue Oct  7 06:36:46 PDT 2014
Description: Given a string of length three representing a set 
(i.e., surrounded by curly braces) such as " {ABC} " , write a function 
that takes the string as an argument and returns a string of its
permutations in comma-separated form, such as " {ABC, ACB, BAC, BCA, CAB,
CBA} " . Hint: use multiple for loops.

"""

# find and and permutations to string
def permutations(char_set):
    permutation = char_set[char_set.index("{")+1:char_set.index("}")]
    final_set = "{"
    for x in range(0, 3):
       # final_set += permutation + ", "
        first = permutation[x]
        if x < 2:
            temp = permutation[:x] + permutation[x+1:]
        else:
            temp = permutation[:x]
        for y in range(0, 1):
            final_set += first + temp[::-1] + ", "
        permutation = first + temp        
        final_set += permutation + ", "
    final_set = final_set[:-2]
    final_set += "}"
    return final_set

# test program
test = "{ABC}"
print(permutations(test))
