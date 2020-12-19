user_input = input("select a string between one and five: ")
user_input = user_input.lower()

if user_input == "one":
    print(1)
elif user_input == "two":
    print(2)
elif user_input == "three":
    print(3)
elif user_input == "four":
    print(4)
elif user_input == "five":
    print(5)
else:
    print("out of range")