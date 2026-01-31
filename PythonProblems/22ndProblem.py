def subtract_product_and_sum(n):
    sum_n = 0 #9
    for i in str(n):
        sum_n += int(i)



    product_n = 1
    for i in str(n):
        product_n *= int(i)

    
    return product_n - sum_n



n = 4421  #2, 3, 4
print(subtract_product_and_sum(n))