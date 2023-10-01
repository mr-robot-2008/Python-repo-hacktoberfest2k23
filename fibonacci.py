def fibonacci(num: int) -> int:
    if num < 0:
        print("Wrong input")
        return
 
    # check if number is between 1, 0 and return that number
    elif num < 2:
        return num
 
    # return the fibonacci of num - 1 & num - 2
    return fibonacci(num - 1) + fibonacci(num - 2)
 
 
#input 
n=int(input("Enter a number : "))
print(fibonacci(n)) #calling fibonacci function
