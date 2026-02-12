def is_power_of_four(n):
    if n <= 0:
        return False

    while n%4 == 0:
        n //= 4 

    return n == 1


n = 16
print(is_power_of_four(n))

