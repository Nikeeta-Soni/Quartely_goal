# A function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Get input from the user
num = int(input("Enter a number : "))

# Call the factorial function and print the result
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    fact = factorial(num)
    print(f"The factorial of {num} is {fact}")