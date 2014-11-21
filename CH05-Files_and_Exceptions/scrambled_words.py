"""

File Name: scrambled_words.py
Developer: Justin A. Shores
Date Last Modified: Sun Sep 21 08:31:46 PDT 2014
Description: Scrambled Words
The task will be to read in a paragraph from a file, scramble the internal letters of each
word, and then write the result to a file.
Handling punctuation is tricky. You are required to deal with punctuation that
comes at the end of a word (period, question mark, exclamation, etc.)—that is, punctu-
ation is left untouched and does not count as the final unscrambled letter. Optionally,
one can deal with the more difficult task of handling all punctuation, such as apostro-
phes for possessives or hyphenated words.
Truly randomizing the order of letters is a task for later in the text, but we can do
some reasonable approximations now.
Attacking this problem in a divide-and-conquer way should begin by writing code
to scramble the letters in a word. Here are three different approaches you might take,
in increasing order of difficulty:
    (a) Easiest: Rotate letters by 13 (known as ROT13). That is, ‘a’ becomes ‘n’, ‘b’ becomes
        ‘o’, . . . , ‘n’ becomes ‘a’, . . . . The chr and its inverse, ord , functions will be useful.
    (b) Harder: For each letter choose a random number and rotate that letter by the
        random amount. Import random and use the random.randint(a,b) function
        where ‘a’ and ‘b’ define the range of random numbers returned.
    (c) Hardest: Improve on the above techniques by scrambling the letters by a method
        of your choice.

"""
import random

# set input and output files
try:
    input_file = open("input.txt", "r")
    output_file = open("output.txt", "w")
except IOError:
    print("ERROR: The File", input_file, "could not be opened!")

# scramble words
def scramble(word):
    word_len = len(word)
    new_word = word[0] # first char remains same
    for x in range(1, word_len-1):
        new_position = random.randint(1, len(new_word))
        new_word = new_word[:new_position] + word[x] + new_word[new_position:]
        word = word[:x] + word[x:]
        word_len -= 1
    new_word += word[-1] # last char remains same
    return new_word

# handle words with punctuation
def de_punctuate_word(word):
    new_word = ""
    sub_words = ""
    if word.isalpha(): # just in case an alpha word got in
        new_word = scramble(word)
    else:
        for char in word:
            if not char.isalpha():
                 sub_words = word.split(char)
                 sub_words.insert(1, char) # insert punctuation in list after split
                 break
        for words in sub_words:
            if words.isalpha() and len(words) > 1:
                new_word += scramble(words)
            elif len(words) <= 1:
                new_word += words
            else:
                new_word += de_punctuate_word(words) # word has punctuation run de_puntuate_word again
            
    return new_word

# read scramble and write one line at a time
for line_str in input_file:
    line_str = line_str.strip()
    new_line = ""
    words = line_str.split(" ")
    for word in words:
        if word.isalpha():
            if len(word) > 3:
                new_line += scramble(word) + " "
            else:
                new_line += word + " "
        else:
            new_line += de_punctuate_word(word) + " "
            
    print(new_line, file = output_file)
