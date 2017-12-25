def decode(string):
    counter = 0
    init = 0
    msg = ''
    number = 0

    for i in range(0, len(string)):
        init = i
        if string[i].isnumeric():
            counter += 1
        else:
            if counter != 0:
                number = int(string[init - counter: init])
            else:
                number = 1
            counter = 0
            for k in range(0, number):
                msg += string[i]
    return msg
#    initial = 0
#    counter = 1
#    msg =''
#       if string[i].isnumeric():
#            counter += 1
#            initial = i
#        else:
#            number = int(string[initial-counter:initial])
#                for k in range(0, number)
#                msg += string[i]
#            counter = 1
#    return msg





def encode(string):
    counter = 0
    prev = 0
    crypt =''
    string = string + '*'
    print('lenght of string', len(string))
    for j in range(0, len(string)):
        if string[prev] == string[j]:
            counter += 1
            continue
        else:
            if counter != 1:
                crypt += str(counter) + string[prev]
            else:
                crypt += string[prev]
            counter = 1
            prev = j
    return crypt

#    crypt = ''
#    var = 0
#    i = 0
#    j = 0
#    while i < len(string):
#        j = i
#        while j < len(string):
#            if string[j] == string[var]:
#                j = + 1
#                if j == len(string)-1:
#                    i = j + 1
#                    crypt = crypt + str(j) + string[var]
#                    break
#
#                continue
#            else:
#                crypt = crypt + str(j) + string[var]
#                var = j
#                j = j + 1
#                break
#        i = j
#    return crypt
