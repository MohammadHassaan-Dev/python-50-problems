def reverse_words(s):
    reversed_words = []
    s = s.split()
    for i in s:
        reversed_words.append(i[::-1])    

    reversed_sentence = " ".join(reversed_words) 

    return reversed_sentence



s = "Let's take LeetCode contest"

print(reverse_words(s))