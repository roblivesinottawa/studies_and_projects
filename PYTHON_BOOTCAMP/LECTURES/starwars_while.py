count = 0
characters = []
name = input("enter character name, type q to quit: ")

while name != 'q':
    count +=1
    characters.append(name)
    print(f"{name} has been added.")
    name = input('next character or type q to quit: ')


print(f"there are {count} characters in this Star Wars list, they are {characters}")