from cs50 import get_int
import re

# prompt user input
number = get_int("Number: ")
# clone number to calculate sum value
number0 = number
# set counter for each digit and sum value
digit = 0
sum = 0
while True:
    # take every 1st digit from the right
    number_le = number0 % 10
    # take every 2nd digit from the right x 2
    number_chan = (number0 / 10) % 10 * 2
    # add those products’ digits (i.e., not the products themselves) together
    number_chan = number_chan % 10 + (number_chan / 10) % 10
    # sum digits
    sum += number_le + number_chan
    digit += 1
    number0 /= 100
    if number0 <= 0:
        break

sum = sum % 10

# turn integer into string to use re module
number = str(number)
# American Express uses 15-digit numbers, MasterCard uses 16-digit numbers, and Visa uses 13- and 16-digit numbers.
# each digit is stored in a [], {} length of digits
if (re.search("^3[47][0-9]{13}$", number)):
    print("AMEX")
elif (re.search("^5[1-5][0-9]{14}$", number)):
    print("MASTERCARD")
elif (re.search("^4[0-9]{12,15}$", number)):
    print("VISA")
else:
    print("INVALID")
