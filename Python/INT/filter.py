# filter is used to filter some elements in a given sequence of objects

# Create a list and find the odds
_list = [-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9]

odds = list(filter((lambda x: x%2), _list))
print(odds)

# Say you want to find only the positive elements from a list
pos = list(filter((lambda x: x>0), _list))
print(pos)

# all the negative integers
neg = list(filter((lambda x: x<0), _list))
print(neg)