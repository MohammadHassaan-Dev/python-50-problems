def findWordsContaining(words, x):
    l = []
    for i in range(len(words)):
        if x in words[i]:
            l.append(i)

    return l

words = ["abc","bcd","aaaa","cbc"]
x = "z"
print(findWordsContaining(words, x))