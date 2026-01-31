def func(words, allowed):
    for i in range(len(words)):
        if allowed in words[i]:
            return i
allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]

print(func(words, allowed))