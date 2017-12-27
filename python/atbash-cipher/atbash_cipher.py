def encode(plain_text):
    master_string = ' abcdefghijklmnopqrstuvwxyz'
    cipher = ''
    for char in plain_text:
        char = char.lower()
        if char.isalpha():
            cipher += master_string[-1 * master_string.find(char)]
        if char.isnumeric():
            cipher += char
    lst = []
    for i in range(0, int(len(cipher) / 5)):
        if (i + 1) * 5 <= len(cipher):
            sub_str = cipher[i * 5: (i + 1) * 5]
            lst.append(sub_str)
    lst.append(cipher[int(len(cipher) / 5) * 5: len(cipher)])
    cipher = ''
    for item in lst:
        cipher += ' ' + item
    return cipher.strip()


def decode(cipher):
    lst = cipher.split()
    master_string = ' abcdefghijklmnopqrstuvwxyz'
    decipher = ''
    for item in lst:
        for char in item:
            if char.isalpha():
                decipher += master_string[-1 * master_string.find(char)]
            if char.isnumeric():
                decipher += char
    return decipher
