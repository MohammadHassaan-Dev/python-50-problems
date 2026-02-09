def mergeAlternately(word1, word2):
    l = []
    for w1, w2 in zip(word1, word2):
        l.append(w1)
        l.append(w2)

    l.append(word1[len(word2):])
    l.append(word2[len(word1):])

    ans = "".join(l)
    return ans


word1 = "abcd"
word2 = "pq"
print(mergeAlternately(word1, word2))