word = "python"

guess = input("guess the word. hint: it's a programming language: ")
guess = guess.lower()

if guess == "javascript":
    print("No, it's not javascript.")
elif guess == "c plus plus":
    print("No, it's not c plus plus")
elif guess == "python":
    print("Yes! You got it!!")
else:
    print(guess.capitalize(), "is not in the list. try again.")