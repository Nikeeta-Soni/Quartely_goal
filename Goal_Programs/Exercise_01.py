# Program to print numbers from 1 to 10
# for number in range(1,11):
# print(number)


# Program to solve the fizzbuzz algorithm
def fizz_buzz(input):
    if (input%3==0) and (input%5==0):
      return "FizzBuzz"
    if input%3==0:
       return "Fizz"
    if input%5==0:
       return "Buzz"
    return input
print(fizz_buzz(45))