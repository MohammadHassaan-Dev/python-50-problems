def count_digits(num):
    count = 0
    for i in str(num): #1, 2, 1 
        if num != 0 and num % int(i) == 0:
            count += 1

    return count


num = 121
print(count_digits(num))