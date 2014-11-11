"""

File Name: morse_code.py
Developer: Justin A. Shores
Date Last Modified: Mon Nov 10 15:54:56 PST 2014
Description: Morse Code uses a series of short and long pulses called dots
    and dashes, respectively, to encode letters and digits. For example, 
    the letter A is “dot-dash,” B is “dash-dot-dot-dot.” Find a table of 
    Morse Code on the Internet to create a dictionary for mapping characters
    and digits to Morse Code. Use the dictionary to create a program that 
    can translate between Morse Code and characters and digits.

"""
# create the dictionary
def get_morse_code_dictionary():
    keys = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", 
                "M", "N", "O",  "P", "Q", "R", "S", "T", "U", "V", "W", "X", 
                "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
                "/", "+", "=", ".", ",", "?", "(", ")", "-", "\"", "_",
                "\'", ":", ";", "$"]
    values = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
                ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-",
                ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--",
                "--..", ".----", "..---", "...--", "....-", ".....",
                "-....", "--...", "---..", "----.", "-----", "-..-.",
                ".-.-.", "-...-", ".-.-.-", "--..--", "..--..", "-.--.", 
                "-.--.-", "-....-", ".-..-.", "..--.-", ".----.", "---...",
                "-.-.-.", "...-..-"]
    morse_code_dictionary = dict(zip(keys, values))
    return morse_code_dictionary

# create pretty output for conversion table
def pretty_output(original, converted):

    for i in range(0, len(original)):
        print("{:<12} {}".format(original[i], converted[i]))
    print("\n")

# convert from letters to morse code
def convert_to_code(dictionary, string):
    string = string.upper()
    words = string.split()
    code_string = []
    code_word = "["
    for word in words:
        for char in range(0, len(word)):
            try:
                code_word += dictionary[word[char]] + "]["
            except KeyError:
                code_word += char + " (is not a known char)]["
        code_string.append(code_word[:-1])
        code_word = "["
    print("\n{:<12} {}".format("Original:", "Converted (letters enclosed" \
             " by [] for clarity):"))
    pretty_output(words, code_string)

# convert from code to letters
def convert_from_code(dictionary, string):
    code_keys = string.split()
    string_value = []
    char_value = ""
    for key in code_keys:
        try:
            char_value = dictionary[key]
        except KeyError:
            char_value += value + " (is not a known code)]"
        string_value.append(char_value)
        char_value = ""
    print("\n{:<9} {}".format("Original:", " Converted:"))
    pretty_output(code_keys, string_value)

# evaluate which conversion should be used and use it
def get_conversion_type(string):
    dictionary = get_morse_code_dictionary()
    values = string.split()
    for value in values:
        for i in range(0, len(value)):
            if value[i] == "." or value[i] == "-":
                continue
            else:
                convert_to_code(dictionary, string)
                return
    dictionary = dict(zip(dictionary.values(), dictionary.keys()))
    convert_from_code(dictionary, string)
    return

# define the main
def main():
    users_string = input("Enter a string or morse code (if code, seperate each letter with space): ")
    get_conversion_type(users_string)

# run the program
main()
