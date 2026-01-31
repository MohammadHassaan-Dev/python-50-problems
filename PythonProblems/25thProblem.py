def final_value_after_operation(operations):
    x = 0 
    for operation in operations: 
        if operation == "++X" or operation == "X++":
            x += 1

        elif operation == "--X" or operation == "--X":
            x -= 1

    return x



operations = operations = ["--X","X++","X++"]
print(final_value_after_operation(operations))