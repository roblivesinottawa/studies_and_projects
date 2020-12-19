secret_number = 8
guess = int(input("guess the number between 1-10: "))

if guess == secret_number:
    print("you've guessed it right! Congratulations!!!")
elif guess > secret_number and guess <= 10:
    print("your guess was incorrect. try again.")
elif guess < secret_number and guess >= 1:
    print("your guess was incorrect. try again.")
else:
    print('out of range')