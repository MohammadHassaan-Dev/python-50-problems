def maximum_wealth(accounts):
    maximum_wealth = 0
    maximum = 0 
    for account in accounts:
        maximum = 0
        for i in account:
            maximum += i
            if maximum > maximum_wealth:
                maximum_wealth = maximum

    return maximum_wealth

accounts = [[1,5],[7,3],[3,5]]

print(maximum_wealth(accounts))