def Palindrome_number(n):
    if n==n[::-1]:
        return "true"

    else:
        return "false"

n = input("Enter number: ")
print(Palindrome_number(n))