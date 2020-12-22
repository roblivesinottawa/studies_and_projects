# create a unordered list and set it to a variable
data = [11,2,3,14,5,96,107,48,99]

# create a new list and make a copy of the original list
data_copy = data[:]
# the first for loop will iterate through the list and then will iterate through it again
for x in range(len(data_copy)):
# the -1 is added because we are comparing the index we are on with the one above it and without
# the decremantation, we will get a value error
# we have -x because as the list is iterated through, we want the highest value number to remain 
# where it is
    for y in range(0, len(data_copy)-x-1):
# if the value of the first one is greater than the values of the second one, switch the values
        if data_copy[y] > data_copy[y+1]:
# we swirch the values of the variables in one line
            data_copy[y], data_copy[y+1] = data_copy[y+1], data_copy[y]

print(data_copy)


# we can just use the built in method sorted()

data_one = [90,56,28,53,92,1,23,34]

sort = sorted(data_one)
print(sort)