def celsius_kelvin_farhenheit(celsius):
    kelvin = celsius + 273.15
    fahrenheit = celsius * 1.80 + 32.00
    ans = []
    ans.append(kelvin)
    ans.append(fahrenheit)
    return ans

celsius = 122.11
print(celsius_kelvin_farhenheit(celsius))