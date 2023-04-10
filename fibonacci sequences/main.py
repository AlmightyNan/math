def fibonacci(n):
    if n == 0:      # return 0 as it is
        return 0
    elif n == 1:    # return 1 as it is
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)  # Calculate and return the nth number in the Fibonacci sequence

n = int(input("Enter a number: "))
for i in range(n):
    print(fibonacci(i), end=' ')
print()
