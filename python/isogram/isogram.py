def is_isogram(string):
    for i in range (0, len(string)):
        for j in range(0, i):
            if string[j].lower() == string[i].lower() and string[i] != ' ' and string[i] != '-':
                return False
                break
    return True
