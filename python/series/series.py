def slices(series, length):
    s = 0
    l = length
    master_lst = []
    lst = []
    if length > len(series):
        raise ValueError('Length cannot be grater than the number of characters in the input string')
    if length == 0:
        raise ValueError('Length cannot be zero')
    for n in range(0, len(series) + 1 - length):
        l = length + n
        extracted_series = series[n: l]
        #print(extracted_series)
        for char in extracted_series:
            lst.append(int(char))
        master_lst.append(lst)
        lst = []
    return master_lst
