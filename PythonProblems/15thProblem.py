def max_words_in_sentence(sentences):
    maximum = 0
    split = []
    for i in sentences:
        split = i.split()
        if len(split) > maximum:
            maximum = len(split)

    return maximum


sentences = ["alice and bob love leetcode", "i think so too"]
print(max_words_in_sentence(sentences))