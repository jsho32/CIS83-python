"""

File Name: scrambling_words.py
Developer: Justin A. Shores
Date Last Modified: Thu Oct 16 08:17:54 PDT 2014
Description: scramble words leaving first and last letters alone handle punctuation
Hints:
- Don’t bother trying to scramble words fewer than four characters long.
- The string split method is useful to create a list of words from a string of words.
- The string strip method is useful to remove end-of-line characters and other
whitespace.
- To scramble a string, convert it to a list, use random.shuffle from the random
module to scramble the string, and then use the join string method to convert 
back to a string ".join(list)
"""
import random

# get word string from file
def getWordString():
    try:
        dataFile = open("input.txt","r")
        print("\nProgress:\ninput.txt opened successfully\n")
    except IOError:
        print("ERROR: Could not open file")
    wordString = ''
    for line in dataFile:
        wordString += line
    wordString = wordString.strip()
    return wordString

# convert string to list of words
def getWordList(string):
    wordList = string.split()
    return wordList

# deal with punctuations
def scramblePunctuatedWords(word):
    new_word = ""
    sub_words = ""
    if word.isalpha(): # just in case an alpha word got in
        new_word = scrambleWord(word)
    else:
        for char in word:
            if not char.isalpha():
                 sub_words = word.split(char, 1) # only split once
                 sub_words.insert(1, char) # insert punctuation in list after split
                 break
        for words in sub_words:
            if words.isalpha() and len(words) > 1:
                new_word += scrambleWord(words)
            elif len(words) <= 1:
                new_word += words
            else:
                new_word += scramblePunctuatedWords(words) # word has punctuation run de_puntuate_word again
            
    return new_word

# scramble words leaving first and last letters alone
def scrambleWord(word):
    scrambled_word = ""
    if len(word) > 3:
        if word.isalpha():
            scrambled_word = word[0]
            x = list(word[1:len(word)-2])
            random.shuffle(x)
            scrambled_word += "".join(x)
            scrambled_word += word[-2:]
        else:
            scrambled_word = scramblePunctuatedWords(word)
    else:
        scrambled_word = word
    return scrambled_word

# get a the string of scrambled words
def getScrambledWords(word_list):
    scrambled_string = ""
    for word in word_list:
        scrambled_string += scrambleWord(word) + " "
    scrambled_string = scrambled_string.strip()
    return scrambled_string

# get word list from file
word_list = getWordList(getWordString())
print(getScrambledWords(word_list))
