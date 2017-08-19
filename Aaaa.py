# Finds whether 3, 5 and 7 are the factors of the given number or not.

num = int(input("Enter a number: "))  # takes a number from user.

# compares multiplicity of all three numbers.
if (num % 3 == 0) and (num % 5 == 0) and (num % 7 == 0):
    print("The number is divisible by all 3 , 5 and 7")

# compares multiplicity of any of two of them.    
elif (num % 3 == 0) and (num % 5 == 0):
    print("The number is divisible by 3 and 5.")
elif (num % 3 == 0) and (num % 7 == 0):
    print("The number is divisible by 3 and 7.")
elif (num % 5 == 0) and (num % 7 == 0):
    print("The number is divisible by 5 and 7.")

# compares multiplicity of any one of them.
elif (num % 3 == 0):
    print("The number is divisible by 3.")
elif (num % 5 == 0):
    print("The number is divisible by 5.")
elif (num % 7 == 0):
    print("The number is divisible by 7.")

# if nothing matches displays message.
else:
    print("The number is not divisible by any of 3 , 5 and 7.")
    
