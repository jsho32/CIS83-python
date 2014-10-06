"""

File Name: message_length.py
Developer: Justin A. Shores
Date Last Modified: Sun Oct  5 22:06:30 PDT 2014
Description: Chat:
(a) In certain chat programs or messaging applications, there is a limit on the number
of characters that you can send in a message. Write a function that takes as input
the message (a string) and checks whether the number of characters is less than
160 (or not). If the length of the message is less than 160, the message should be
returned. If the length of the message is greater than 160, a string consisting of only
the first 160 characters should be returned.
(b) How would you check if the restriction is on number of words rather than characters?
Write a function that allows a message with only 20 words.

"""

# define maximum character count
def maximum_char_length(message):
    if len(message) <= 160:
        return message
    else:
        return message[:160]

# define maximum word count
def maximum_word_count(message):
    words = message.split()
    if len(words) <= 20:
        return message
    else:
        new_message = ""
        for word in range(0, 20):
            new_message += words[word] + " "
        return new_message

# test program
message = input("Enter the message you want to send: ")
print("Here is the 160 char max:")
print(maximum_char_length(message))
print("Here is the 20 word max")
print(maximum_word_count(message))
