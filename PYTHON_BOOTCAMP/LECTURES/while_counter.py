count = 0
class_names = []
name = input('enter name,type n to stop: ')

while name != 'n':
    count += 1
    class_names.append(name)
    print(f"{name} has been added.")
    name = input("next name: ")


print(f"there are {count} people in the class, they are {class_names}.")