# create a variable that will ask the user for input. 
# user needs to enter different ages - use int() and input()
user = int(input("enter ages of members. type -1 to quit: "))

# initialize an empty list that will store the age values
ages = []
# do the check using a while loop
while user > 0:
# create a variable that will append the values to the empty list
    ages.append(user)
    user = int(input('the next age: '))
print(f"the ages are {ages}")