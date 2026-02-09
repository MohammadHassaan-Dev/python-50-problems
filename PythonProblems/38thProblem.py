def balancedStringSplit(s):
    count = 0
    balanced = 0
    for i in s:
        if i == "R":
            balanced += 1

        else:
            balanced -= 1

        if balanced == 0:
            count += 1

    
    return count


        


s = "LLLLRRRR"
print(balancedStringSplit(s))
