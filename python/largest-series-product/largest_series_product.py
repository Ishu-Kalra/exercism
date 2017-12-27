def largest_product(series, size):
    i = 0
    l = size
    lst = []
    summ = 1
    if size < 0:
        raise ValueError("Negative number not allowed")
    for num in range(0, len(series) - size + 1):
        sub_str = series[i + num: l + num]
        for char in sub_str:
            summ *= int(char)
        lst.append(summ)
        summ = 1
    return max(lst)
