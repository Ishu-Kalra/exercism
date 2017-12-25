def rotate(text, key):
    lower_letter_count = dict([(i, chr(i)) for i in range(97,123)])
    upper_letter_count = dict([(i, chr(i)) for i in range(65, 91)])
    msg = ''
    new_char = ''
    for char in text:
        #flag = True
        if not char.isalpha():
            msg += char
            continue
        if char.islower():
            value = ord(char)
            value = value + key
            if value > 122: value = 97 + (value - 97) % 26
            new_char = lower_letter_count[value]
        if char.isupper():
            value = ord(char)
            value = value + key
            if value > 90: value = 65 + (value - 65) % 26
            new_char = upper_letter_count[value]
        msg += new_char
    return msg
