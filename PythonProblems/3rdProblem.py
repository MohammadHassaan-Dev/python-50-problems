def length_of_last_word(s):
    list_s = s.split()
    lenght = len(list_s)
    last_word = list_s[lenght-1]
    return len(last_word)

s = input("Enter a string: ")
print(length_of_last_word(s))