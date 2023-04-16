try:
    x = int(input("Please enter a number: "))
    print("number", x)
except ValueError:
    print("Oops!  That was no valid number.  Try again...")