temperature = int(input("enter temperature between 0 and 40: "))

if temperature > 30:
    print("it's hot out")
elif temperature > 15 and temperature < 30:
    print("it's nice out")
elif temperature < 15:
    print("it's chilly out")
else:
    print("it's freezing")