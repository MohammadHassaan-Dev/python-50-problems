def FizzBuzz(n):
    output = []
    for i in range(1,n+1):
        if i%5 == 0 and i%3 ==0:
            output.append("FizzBuzz")

        elif i%3==0:
            output.append("Fizz")
            
        elif i%5==0:
            output.append("Buzz")
            
        else:
            output.append(i)

    return output

n = int(input("Enter a number: "))
print(FizzBuzz(n))
        