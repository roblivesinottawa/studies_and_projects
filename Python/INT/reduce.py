# the reduce function is used to perform some type of computation in a given sequence

from functools import reduce

_list = [1,2,3,4,5]

# find the product
prod = reduce((lambda x,y: x*y), _list)
print(prod)

# find the greatest element in the list
greatest = reduce((lambda x,y : y if y>x else x), _list)
print(greatest)

# using a regular function
def greater(x,y):
    if y > x:
        return y
    return x

result = reduce(greater, _list)
print(result)