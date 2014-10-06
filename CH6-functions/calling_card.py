"""

File Name: calling_card.py
Developer: Justin A. Shores
Date Last Modified: Sun Oct  5 21:29:04 PDT 2014
Description: You buy an international calling card to India. The calling card company has some
special offers.
(a)If you charge your card with $ 5 or $ 10, you don’t get anything extra.
(b)For a $ 25 charge, you get $ 3 of extra phone time.
(c)For a $ 50 charge, you get $ 8 of extra phone time.
(d)For a $ 100 charge, you get $ 20 of extra phone time.
Write a function that asks the user for the amount he/she wants on the card and returns
the total charge that the user gets. Note: Values other than those mentioned above are
not allowed.

"""

# define amount on calling card
def calling_card():
    while True:
        credit = int(input("How much would you like to put on your calling card? "))
        if credit == 5 or credit == 10:
            break
        elif credit == 25:
            credit += 3
            break
        elif credit == 50:
            credit += 8
            break
        elif credit == 100:
            credit += 20
            break
        else:
            print("Invalid entry! options include $5, $10, $25, $50, $100")
            continue
    return credit

# test program
test = calling_card()
print("Your card is now credited ${}".format(test))
