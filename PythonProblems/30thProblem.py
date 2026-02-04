def truncate_sentence(s,k):
    list_s = s.split()
    s = list_s[0 : k]
    return " ".join(s)
    

s = "chopper is not a tanuki"
k = 5

print(truncate_sentence(s,k))