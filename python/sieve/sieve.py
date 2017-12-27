def sieve(limit):
    master_lst = []
    iter_lst = [i for i in range(0, limit + 1)]

    for i in range(2, limit + 1):
        for j in range(i + 1, limit + 1):
            if j % i == 0:
                iter_lst[j] = 0

    for i in iter_lst:
        if i > 1:
            master_lst.append(i)
    return master_lst
