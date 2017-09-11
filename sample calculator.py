while True:
    print("Options:")
    print("Enter 'add' to add two numbers.")
    print("Enter 'subtract' to subtract two numbers.")
    print("Enter 'multiply' to multiply two numbers.")
    print("Enter 'divide' to divide two numbers.")
    print("Enter 'quit' to end the program.")

    a = input(": ")

    if a == "quit":
        break

    elif a == "add":
        x = int(input("Enter a number; "))
        y = int(input("Enter another number; "))
        z = x + y
        print("The sum of two numbers is; " + str(z))

    elif a == "subtract":
        x = int(input("Enter a number; "))
        y = int(input("Enter another number; "))
        z = x - y
        print("The subtraction of two numbers is; " + str(z))

    elif a == "multiply":
        x = int(input("Enter a number; "))
        y = int(input("Enter another number; "))
        z = x * y
        print("The multiplication of two numbers is; " + str(z))

    elif a == "divide":
        x = int(input("Enter a number; "))
        y = int(input("Enter another number; "))
        z = x / y
        print("The division of two numbers is; " + str(z))

    else:
        print("Unknown input.")
