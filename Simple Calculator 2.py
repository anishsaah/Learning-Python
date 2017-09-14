def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

while True:
    print("Option: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")

    z = input("Choose the option required: ")

    if z == "5":
        break

    elif z == "1":
        x = int(input("Enter first nunmber: "))
        y = int(input("Enter second number: "))
        print(x, "+", y,"=", add(x,y))
        

    elif z == "2":
        x = int(input("Enter first nunmber: "))
        y = int(input("Enter second number: "))
        print(x, "-", y, "=", subtract(x,y))
        


    elif z == "3":
        x = int(input("Enter first nunmber: "))
        y = int(input("Enter second number: "))
        print(x, "*", y, "=", multiply(x,y))
        


    elif z == "4":
        x = int(input("Enter first nunmber: "))
        y = int(input("Enter second number: "))
        print(x, "/", y, "=", divide(x,y))
        


    else:
        print("Unknown input.")

    print("-" * 80)
