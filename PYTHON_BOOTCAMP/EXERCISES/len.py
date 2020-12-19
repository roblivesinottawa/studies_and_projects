name = input("enter name >>> ")
length = len(name)
if length > 3:
    print(f"your name contains {length} characters")
else:
    print("your name is too short.")