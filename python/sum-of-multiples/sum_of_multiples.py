def sum_of_multiples(limit, multiples):
    lst = []
    for i in range(0, limit):
        for divisor in multiples:
            if i % divisor == 0 and i not in lst:
                lst.append(i)
    return sum(lst)

#print(sum_of_multiples(10, [3, 5]))
