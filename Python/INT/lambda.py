# lambda functions are also known as anonymous functons, they don't need to be named.
# they are usually one line functions
# lambda + arguments + expression

pwr = lambda a, b : a**b
rslt = pwr(10, 10)
print(rslt)


# regular way of defining a function
def power(a,b):
    return a**b

print(power(10,10))

# here is a list
mylist = [0,1,2,3,4,5]
# find the average
average = lambda L : sum(L) / len(L)
print(average(mylist))


# fibonacci in lambda
fib = lambda x : x if x <= 1 else fib(x - 1) + (x - 2)
print(fib(5))

# regular function fibonacci
def fib1(x):
    if x <= 1:
        return 1
    return (x -1) + (x - 2)

print(fib1(40))
    