def str_str(word):
    if word.islower():
        return True

    elif word.isupper():
        return True

    elif (word[0].isupper() and word[1:].islower()):
        return True

    return False



word = "Usa"
print(str_str(word))