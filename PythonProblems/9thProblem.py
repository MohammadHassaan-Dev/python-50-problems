def Palindrome(n):
    clean = ""
    for characters in n:
        if characters.isalpha():
            clean += characters

    return clean == clean[::-1] 

n = "A man, a plan, a canal: Panama".lower()
print(Palindrome(n))

