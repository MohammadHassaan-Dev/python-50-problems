def jewels_stones(jewels, stones):
    count = 0
    for i in stones:
        if i in jewels:
            count += 1

    return count

jewels = "aA"
stones = "aAAbbbb"
print(jewels_stones(jewels, stones))
