def isPerfectSquare(num):
    if num < 0:
        return False

    if num == 1:
        return True

    for i in range(1, num+1): 
        if i*i == num:
            return True

        elif i*i > num:
            return False


num = 5
print(isPerfectSquare(num))
