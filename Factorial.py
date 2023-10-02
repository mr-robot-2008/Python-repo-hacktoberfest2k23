def factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# user input
num = int(input("Enter a number: "))

result = factorial(num)
print(f"The factorial of {num} is {result}")
