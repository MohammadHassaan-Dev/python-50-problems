def Reverse_String(n):
    left = 0
    right = len(n) - 1 
    while left < right:
        n[left], n[right] = n[right], n[left]
        left += 1
        right -=1

n = ["o","l","l","e","h"]
Reverse_String(n)
print(n)