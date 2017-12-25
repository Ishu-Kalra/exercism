def square_of_sum(number):
    summation = 0
    for i in range(1, number + 1):
        summation += i
    return summation * summation



def sum_of_squares(number):
    summation = 0
    for i in range(1, number + 1):
        summation += i*i
    return summation


def difference(n):
    return square_of_sum(n) - sum_of_squares(n)
