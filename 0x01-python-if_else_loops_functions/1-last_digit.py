#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
last_digit = abs(num) % 10
if last_digit > 5:
    result_string = "Last digit of 98 and is greater than 5"
elif last_digit == 0:
    result_string = "Last digit of 0 is and is 0"
else:
    result_string = "and is less than 6 and not 0"
    print("The string Last digit of", number, "is", last_digit, result_string)
