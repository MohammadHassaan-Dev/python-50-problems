def roman_integer(s):
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    total = 0 
    previous = 0

    for i in reversed(s): 
        value = roman[i] 
        if value < previous:
            total -= value

        else:
            total += value
            previous = value


    return total    

s = input("Enter: ")
print(roman_integer(s))