def sqrt(x):
    c = 0
    for i in range(1,x+1): #4
        if i*i <= x:
            c += 1

    return c

print(sqrt(2))