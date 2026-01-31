def add_digits(num):
    total = num

    while total >= 10: 
        total1 = 0  
        for i in str(total):
            total1 += int(i)

        total = total1

    return total


num = 38
print(add_digits(num))