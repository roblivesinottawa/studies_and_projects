# # first way 

# def get_factorial(n):
#     if n < 2:
#         return 1
#     return n * get_factorial(n - 1)

# print(get_factorial(3))
# print(get_factorial(4))
# print(get_factorial(5))


# # second way

# def factorial(n):
#     returned = 1
#     for i in range(n, 1, -1):
#         returned *= id
    
#     return returned

# print(get_factorial(3))
# print(get_factorial(4))
# print(get_factorial(5))

# third way

# def fact(num):
#     if num < 0:
#         return -1
#     fact = 1
#     for n in range(1, num + 1):
#         fact *= n
#     return fact

# print(fact(10))

# print(fact(4))
# print(fact(5))

# fourth way
def factorial(num):

    f = 1
    for x in range(1, num+1):
        f = f * x

    return f
    
n = 4
result = factorial(n)
print(result)