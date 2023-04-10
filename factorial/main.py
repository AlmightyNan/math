def factorial(n):
    if n == 0:
        return 1                    # factorial of 0 is 1 so we return it manually
    else:
        return n * factorial(n-1)   # Calculate and return the factorial of n

n = int(input("Enter a number: "))  # get user input to pass in args for function
print(factorial(n))
