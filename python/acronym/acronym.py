def abbreviate(words):
    lst = words.replace('-', ' ').replace(',', ' ').replace(':', ' ').split()
    jargon = ''
    for item in lst:
        jargon += item[0].upper()
    return jargon
