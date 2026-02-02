def reverse_words(s, t):
    return sorted(s) == sorted(t)


s = "rat"
t = "car"

print(reverse_words(s, t))