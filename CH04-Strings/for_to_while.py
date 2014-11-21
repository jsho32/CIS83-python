"""

File Name: for_to_while.py
Developer: Justin A. Shores
Date Last Modified: Tue Sep 16 13:02:06 PDT 2014
Description: In the following program, replace the for with a while loop.
S="I had a cat named amanda when I was little"
count = 0
for i in S:
    if i == "a":
        count += 1
        print(count)

"""
# altered code:
S="I had a cat named amanda when I was little"
count, i = 0, 0
while i < len(S):
    if S[i] == "a":
        count += 1
        print(count)
    i += 1

