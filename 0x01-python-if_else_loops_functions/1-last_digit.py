#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
digit = abs(num) % 10
if digit > 5:
    result_string = "Last digit of 98 and is greater than 5"
elif digit == 0:
    result_string = "Lat digit of 0 is and is 0"
else:
    result_string = "and is less than 6 and not 0"
    print("The string Last digit of", number, "is", digit, result_string)
