def interpret(command):
    command = command.replace("()", "o")  # Goooo(al)
    command = command.replace("(al)", "al") # Gooooal
    return command


command = "G()()()()(al)"
print(interpret(command))
