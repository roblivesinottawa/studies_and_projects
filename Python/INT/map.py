# the map fumction is used to map through a sequence of objects
mylist = [0,1,2,3,4,5]

# convert all the elements to a float
mylist = list(map(float, mylist))
print(mylist)


# map with lambda
another_list = [0,1,2,3,4,5,6,7]
another_list = list(map(lambda x : x**2, another_list))
print(another_list)