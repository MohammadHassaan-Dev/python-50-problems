def Running_Sum(l):
    l1 = [] 
    l2 = []
    for i in l:
        l1.append(i)
        sum_l = sum(l1)
        l2.append(sum_l)

    return l2

l = [3,1,2,10,1]
print(Running_Sum(l))




