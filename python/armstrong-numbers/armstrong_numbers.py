import math

def is_armstrong(number):
    length = len(str(number))
    summation = 0
    for char in str(number):
        summation += math.pow(int(char), length)
    if number == summation:
        return True
    return False
print(is_armstrong(154))
