def distance(strand_a, strand_b):
    distance = 0
    if len(strand_a) != len(strand_b):
        raise ValueError('Not equal length')
    for a, b in zip(strand_a, strand_b):
        if a != b:
            distance += 1
    return distance
