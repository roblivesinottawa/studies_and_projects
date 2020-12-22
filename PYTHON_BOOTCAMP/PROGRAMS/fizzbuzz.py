
# with a for loop
# num = 100

# for x in range(1, num+1):
#     if x % 3 == 0 and x % 5 == 0:
#         print(x, "fizzbuzz")
#     elif x % 3 == 0:
#         print(x, "fizz")
#     elif x % 5 == 0:
#         print(x, "buzz")
#     else:
#         print(x)

# function
def fizz_buzz(input):
    if (input % 3 == 0 )and (input % 5 == 0):
        return "FizzBuzz"
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"
    return input

result = (fizz_buzz(15))
print(result)