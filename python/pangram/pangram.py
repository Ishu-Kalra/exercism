def is_pangram(sentence):
    s = 'abcdefghijklmnopqrstuvwxyz'
    for i in range (0, len(s)):
        if sentence.lower().find(s[i]) == -1:
            return False
    return True
