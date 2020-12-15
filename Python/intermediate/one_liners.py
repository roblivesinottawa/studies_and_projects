# fib = lambda x:x if x <=1 else fib(x-1) + fib(x-2)

fact = lambda n:[1,0][n<1] or fact(n-1)*n
print(fact(100))