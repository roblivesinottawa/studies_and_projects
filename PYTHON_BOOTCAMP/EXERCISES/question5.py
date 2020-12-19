user_input = int(input("please enter an integer between 1 and 20 >>> "))
user_input2 = int(input("please enter another integer between 1 and 20 >>> "))

if user_input > 15 and user_input2 > 15:
    print(user_input * user_input2)
elif user_input > 15 or user_input2 > 15:
    print(user_input + user_input2)
else:
    print(0)