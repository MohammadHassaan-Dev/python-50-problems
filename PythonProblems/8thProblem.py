def add_one(number):
    for i in range(len(number)-1,-1,-1):
        if number[i] < 9:
            number[i] += 1
            return number
        
        number[i] = 0

    return [1] + number

number = [2,2,9] 
print(add_one(number))