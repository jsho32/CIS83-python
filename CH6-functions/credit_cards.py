"""

File Name: credit_cards.py
Developer: Justin A. Shores
Date Last Modified: Sun Oct  5 19:05:09 PDT 2014
Description: Error checking with meaningful error messages is an important
part of programming. Consider the following scenario: A customer has to pay
his monthly credit card bill. The credit limit on the card is $ 1000. The 
minimum payment due is always $ 20. Let the payment on the credit card be 
$ P. Write a function called make payment(P) that takes as an argument the 
total payment on the credit card ( $ P) and prints “Success” or “Retry.” 
Try to think of all the errors that should be taken care of and implement 
those in the function. One example would be that if the payment is less 
than $ 20, the program should remind the user that it’s less than the 
minimum payment due.

"""

# define acceptable payments
def make_payment(p):
    minimum = 20
    maximum = 1000
    if not p.replace(".", "").isdigit():
        print("Invalid Entry\nRetry")
        return False
    elif float(p) > maximum:
        print("That is too much you can't pay more than the limit of ${} \nRetry".format(maximum))
        return False
    elif float(p) < minimum:
        print("The amount of ${} is less than the minimum allowed payment of ${}\nRetry".format(p, minimum))
        return False
    else:
        print("Payment Successful")
        return True

payment = input("Enter your card's payment amount: $")
while not make_payment(payment):
    payment = input("Enter amount: $")
    continue
print("Thank You!")
