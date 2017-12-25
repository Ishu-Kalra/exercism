def hey(phrase):
    phrase = phrase.strip()
    if phrase.isupper():
        return "Whoa, chill out!"
    if phrase.endswith('?'):
        return "Sure."
    if phrase == '':
        return "Fine. Be that way!"

    return "Whatever."
